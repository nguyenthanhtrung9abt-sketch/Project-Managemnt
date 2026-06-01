# cong_viec.py
from structures import CongViec, MyArray
from utils import sinh_ma_cong_viec, nhap_chuoi_bat_buoc, nhap_ngay, nhap_so_thuc_duong, chon_tu_danh_sach, tim_vi_tri_nhan_vien, sap_xep_noi_bot_cong_viec_theo_gio
from storage import ghi_file_cong_viec

def ghi_nhan_cong_viec(ds_cv, ds_da, ds_nv):
    print("\n--- GHI NHAN CONG VIEC (TIMESHEET) ---")
    if ds_da.kich_thuoc() == 0 or ds_nv.kich_thuoc() == 0: return
    vt_da = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da} | {da.ten_da}", "Chon du an")
    if vt_da == -1: return
    da = ds_da[vt_da]
    vt_nv = chon_tu_danh_sach(ds_nv, lambda nv: f"{nv.ma_nv} | {nv.ten_nv}", "Chon nhan vien")
    if vt_nv == -1: return
    nv = ds_nv[vt_nv]
    
    la_thanh_vien = False
    for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
        if da.ds_ma_thanh_vien[i] == nv.ma_nv: la_thanh_vien = True
    if not la_thanh_vien and input("   [!] NV chua co trong DA. Tiep tuc? (y/n): ").strip().lower() != 'y': return

    ma_cv = sinh_ma_cong_viec()
    ten_cv = nhap_chuoi_bat_buoc("Nhap ten cong viec: ")
    print("  Loai hinh: 1.BA | 2.Design | 3.Code | 4.Test")
    while True:
        chon_lh = input("  Lua chon (1-4): ").strip()
        if   chon_lh == '1': loai_hinh = 'BA';     break
        elif chon_lh == '2': loai_hinh = 'Design'; break
        elif chon_lh == '3': loai_hinh = 'Code';   break
        elif chon_lh == '4': loai_hinh = 'Test';   break
    tg_bd = nhap_ngay("  Ngay bat dau (dd/mm/yyyy): ")
    tg_kt = nhap_ngay("  Ngay ket thuc (dd/mm/yyyy): ")
    gio_cong = nhap_so_thuc_duong("  So gio lam viec: ")
    chon_tt = input("  Trang thai (1.In Progress | 2.Done): ").strip()
    trang_thai = 'Done' if chon_tt == '2' else 'In Progress'

    ds_cv.them(CongViec(ma_cv, ten_cv, da.ma_da, nv.ma_nv, loai_hinh, tg_bd, tg_kt, gio_cong, trang_thai))
    ghi_file_cong_viec("CongViec.txt", ds_cv)
    print(f"=> Ghi nhan cong viec thanh cong! Ma: {ma_cv}")

def hien_thi_danh_sach_cong_viec(ds_cv, ds_da):
    if ds_cv.kich_thuoc() == 0: return
    loc_ma_da = ""
    vt_loc = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da} | {da.ten_da}", "Chon DA de loc (0 = xem tat ca)")
    if vt_loc != -1: loc_ma_da = ds_da[vt_loc].ma_da
    ds_sorted = sap_xep_noi_bot_cong_viec_theo_gio(ds_cv)
    tieu_de = (f"  {'Ma CV':<10} | {'Ten Cong Viec':<28} | {'Ma DA':<8} | {'Ma NV':<8} | {'Gio':>5} | {'Trang Thai':<13}")
    print("\n" + tieu_de + "\n  " + "-" * (len(tieu_de) - 2))
    for cv in ds_sorted:
        if loc_ma_da != "" and cv.ma_da != loc_ma_da: continue
        print(f"  {cv.ma_cv:<10} | {cv.ten_cv:<28} | {cv.ma_da:<8} | {cv.ma_nv:<8} | {cv.gio_cong:>5.1f} | {cv.trang_thai:<13}")

def sua_cong_viec(ds_cv):
    if ds_cv.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_cv, lambda cv: f"{cv.ma_cv} | {cv.ten_cv}", "Chon task can sua")
    if vi_tri == -1: return
    cv = ds_cv[vi_tri]
    ten_moi = input(f"  Ten moi [{cv.ten_cv}]: ").strip()
    if ten_moi != "": cv.ten_cv = ten_moi
    gio_input = input(f"  Gio cong [{cv.gio_cong}]: ").strip()
    if gio_input != "":
        try:
            val = float(gio_input)
            if val > 0: cv.gio_cong = val
        except ValueError: pass
    chon_tt = input("  Trang thai (1.In Progress | 2.Done | Enter bo qua): ").strip()
    if   chon_tt == '1': cv.trang_thai = 'In Progress'
    elif chon_tt == '2': cv.trang_thai = 'Done'
    ghi_file_cong_viec("CongViec.txt", ds_cv)
    print("=> Cap nhat cong viec thanh cong!")

def xoa_cong_viec(ds_cv):
    if ds_cv.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_cv, lambda cv: f"{cv.ma_cv} | {cv.ten_cv}", "Chon task can xoa")
    if vi_tri == -1: return
    if input(f"Xoa task '{ds_cv[vi_tri].ten_cv}'? (y/n): ").strip().lower() == 'y':
        ds_cv.xoa_tai(vi_tri)
        ghi_file_cong_viec("CongViec.txt", ds_cv)
        print("=> Da xoa task thanh cong!")

def bao_cao_tien_do_va_chi_phi(ds_da, ds_nv, ds_cv):
    if ds_da.kich_thuoc() == 0: return
    vt_da = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da} | {da.ten_da}", "Chon du an xem bao cao")
    if vt_da == -1: return
    du_an = ds_da[vt_da]
    tong_so_task, so_task_done, tong_chi_phi = 0, 0, 0.0
    chi_phi_nv_ma, chi_phi_nv_ten, chi_phi_nv_gio, chi_phi_nv_cp = MyArray(), MyArray(), MyArray(), MyArray()

    for cv in ds_cv:
        if cv.ma_da != du_an.ma_da: continue
        tong_so_task += 1
        if cv.trang_thai == 'Done': so_task_done += 1
        vt_nv = tim_vi_tri_nhan_vien(cv.ma_nv, ds_nv)
        if vt_nv == -1: continue
        nv = ds_nv[vt_nv]
        cp_task = cv.gio_cong * nv.don_gia
        tong_chi_phi += cp_task
        
        vi_tri_cp = -1
        for k in range(chi_phi_nv_ma.kich_thuoc()):
            if chi_phi_nv_ma[k] == cv.ma_nv: vi_tri_cp = k
        if vi_tri_cp == -1:
            chi_phi_nv_ma.them(nv.ma_nv)
            chi_phi_nv_ten.them(nv.ten_nv)
            chi_phi_nv_gio.them(cv.gio_cong)
            chi_phi_nv_cp.them(cp_task)
        else:
            chi_phi_nv_gio[vi_tri_cp] += cv.gio_cong
            chi_phi_nv_cp[vi_tri_cp] += cp_task

    phan_tram = (so_task_done / tong_so_task * 100) if tong_so_task > 0 else 0
    thanh = "[" + "#" * int(phan_tram/100*40) + "-" * (40 - int(phan_tram/100*40)) + "]"
    
    print("\n" + "=" * 62 + f"\n  BAO CAO: {du_an.ten_da.upper()}\n" + "=" * 62)
    print(f"\n  [TIEN DO] Task: {so_task_done}/{tong_so_task} \n  {thanh} {phan_tram:.1f}%")
    print(f"\n  [CHI PHI THEO NHAN VIEN]")
    for k in range(chi_phi_nv_ma.kich_thuoc()):
        print(f"  {chi_phi_nv_ten[k]:<25} | {chi_phi_nv_gio[k]:>9.1f}h | {chi_phi_nv_cp[k]:>16,.0f} VND")
    print("-" * 62)
    print(f"  Ngan sach : {du_an.ngan_sach:>22,.0f} VND")
    print(f"  Thuc te   : {tong_chi_phi:>22,.0f} VND")
    if tong_chi_phi > du_an.ngan_sach:
        print(f"  *** CANH BAO: VUOT {tong_chi_phi - du_an.ngan_sach:,.0f} VND! ***")
    else:
        print(f"  >> AN TOAN: Con lai {du_an.ngan_sach - tong_chi_phi:,.0f} VND.")

def menu_cong_viec_va_bao_cao(ds_cv, ds_da, ds_nv):
    while True:
        print("\n" + "=" * 42 + "\n    QUAN LY TIMESHEET & BAO CAO    \n" + "=" * 42)
        print("  1. Cham cong\n  2. Hien thi danh sach\n  3. Sua task\n  4. Xoa task\n  5. Bao cao Tien do & Chi phi\n  0. Tro ve")
        chon = input("  Moi chon (0-5): ").strip()
        if   chon == '1': ghi_nhan_cong_viec(ds_cv, ds_da, ds_nv)
        elif chon == '2': hien_thi_danh_sach_cong_viec(ds_cv, ds_da)
        elif chon == '3': sua_cong_viec(ds_cv)
        elif chon == '4': xoa_cong_viec(ds_cv)
        elif chon == '5': bao_cao_tien_do_va_chi_phi(ds_da, ds_nv, ds_cv)
        elif chon == '0': break
        else: print("=> LOI: Lua chon khong hop le!")
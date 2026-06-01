# nhan_vien.py
from structures import NhanVien
from utils import sinh_ma_nhan_vien, nhap_chuoi_bat_buoc, nhap_so_thuc_duong, chon_tu_danh_sach, sap_xep_noi_bot_nhan_vien_theo_ten
from storage import ghi_file_nhan_vien, ghi_file_cong_viec, ghi_file_du_an

def them_nhan_vien(ds_nv):
    print("\n--- THEM NHAN VIEN MOI ---")
    ma_nv = sinh_ma_nhan_vien()
    ten_nv = nhap_chuoi_bat_buoc("Nhap ho ten nhan vien: ")
    print("  Chon vai tro: 1. BA  |  2. Dev  |  3. Test")
    while True:
        chon = input("  Lua chon (1-3): ").strip()
        if   chon == '1': vai_tro = 'BA';   break
        elif chon == '2': vai_tro = 'Dev';  break
        elif chon == '3': vai_tro = 'Test'; break
    don_gia = nhap_so_thuc_duong(f"  Don gia gio cong {vai_tro} (VND/gio): ")
    ds_nv.them(NhanVien(ma_nv, ten_nv, vai_tro, don_gia))
    ghi_file_nhan_vien("NhanVien.txt", ds_nv)
    print(f"=> Them nhan vien thanh cong! Ma: {ma_nv}")

def hien_thi_danh_sach_nhan_vien(ds_nv):
    if ds_nv.kich_thuoc() == 0: return
    ds_sorted = sap_xep_noi_bot_nhan_vien_theo_ten(ds_nv)
    tieu_de = (f"  {'STT':<5} | {'Ma NV':<8} | {'Ho Ten':<28} | {'Vai Tro':<8} | {'Don Gia':>18}")
    print("\n" + tieu_de + "\n  " + "-" * (len(tieu_de) - 2))
    for i in range(ds_sorted.kich_thuoc()):
        nv = ds_sorted[i]
        print(f"  {i+1:<5} | {nv.ma_nv:<8} | {nv.ten_nv:<28} | {nv.vai_tro:<8} | {nv.don_gia:>18,.0f}")

def sua_nhan_vien(ds_nv):
    if ds_nv.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_nv, lambda nv: f"{nv.ma_nv} | {nv.ten_nv}", "Chon nhan vien can sua")
    if vi_tri == -1: return
    nv = ds_nv[vi_tri]
    ten_moi = input(f"  Ten moi [{nv.ten_nv}]: ").strip()
    if ten_moi != "": nv.ten_nv = ten_moi
    chon_vai = input("  Vai tro (1.BA | 2.Dev | 3.Test | Enter bo qua): ").strip()
    if   chon_vai == '1': nv.vai_tro = 'BA'
    elif chon_vai == '2': nv.vai_tro = 'Dev'
    elif chon_vai == '3': nv.vai_tro = 'Test'
    gia_input = input(f"  Don gia [{nv.don_gia:,.0f}]: ").strip()
    if gia_input != "":
        try:
            val = float(gia_input)
            if val > 0: nv.don_gia = val
        except ValueError: pass
    ghi_file_nhan_vien("NhanVien.txt", ds_nv)
    print("=> Cap nhat nhan vien thanh cong!")

def xoa_nhan_vien(ds_nv, ds_cv, ds_da):
    if ds_nv.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_nv, lambda nv: f"{nv.ma_nv} | {nv.ten_nv}", "Chon nhan vien can xoa")
    if vi_tri == -1: return
    nv = ds_nv[vi_tri]
    if input(f"Xoa '{nv.ten_nv}' va TAT CA task? (y/n): ").strip().lower() == 'y':
        ma_nv = nv.ma_nv
        ds_nv.xoa_tai(vi_tri)
        for i in range(ds_cv.kich_thuoc() - 1, -1, -1):
            if ds_cv[i].ma_nv == ma_nv: ds_cv.xoa_tai(i)
        for da in ds_da:
            for j in range(da.ds_ma_thanh_vien.kich_thuoc() - 1, -1, -1):
                if da.ds_ma_thanh_vien[j] == ma_nv: da.ds_ma_thanh_vien.xoa_tai(j)
        ghi_file_nhan_vien("NhanVien.txt", ds_nv)
        ghi_file_cong_viec("CongViec.txt", ds_cv)
        ghi_file_du_an("DuAn.txt", ds_da)
        print(f"=> Da xoa nhan vien '{nv.ten_nv}'!")

def menu_nhan_vien(ds_nv, ds_cv, ds_da):
    while True:
        print("\n" + "=" * 38 + "\n       QUAN LY NHAN VIEN        \n" + "=" * 38)
        print("  1. Them Nhan vien\n  2. Hien thi danh sach (A-Z)\n  3. Sua thong tin\n  4. Xoa Nhan vien\n  0. Tro ve")
        chon = input("  Moi chon (0-4): ").strip()
        if   chon == '1': them_nhan_vien(ds_nv)
        elif chon == '2': hien_thi_danh_sach_nhan_vien(ds_nv)
        elif chon == '3': sua_nhan_vien(ds_nv)
        elif chon == '4': xoa_nhan_vien(ds_nv, ds_cv, ds_da)
        elif chon == '0': break
        else: print("=> LOI: Lua chon khong hop le!")
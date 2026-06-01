# du_an.py
from structures import DuAn, MyArray
from utils import sinh_ma_du_an, nhap_chuoi_bat_buoc, nhap_so_thuc_duong, nhap_ngay, chon_tu_danh_sach, tim_vi_tri_nhan_vien
from storage import ghi_file_du_an, ghi_file_cong_viec

def them_du_an(ds_da):
    print("\n--- THEM DU AN MOI ---")
    ma_da = sinh_ma_du_an()
    print(f"  Ma du an duoc cap tu dong: [{ma_da}]")
    ten_da     = nhap_chuoi_bat_buoc("Nhap ten du an       : ")
    khach_hang = nhap_chuoi_bat_buoc("Nhap ten khach hang  : ")
    ngan_sach  = nhap_so_thuc_duong ("Nhap ngan sach (VND) : ")
    ngay_bd    = nhap_ngay           ("Ngay bat dau (dd/mm/yyyy): ")
    ngay_kt    = nhap_ngay           ("Ngay ket thuc (dd/mm/yyyy): ")
    ds_da.them(DuAn(ma_da, ten_da, khach_hang, ngan_sach, ngay_bd, ngay_kt))
    ghi_file_du_an("DuAn.txt", ds_da)
    print(f"=> Them du an thanh cong! Ma: {ma_da}")

def hien_thi_danh_sach_du_an(ds_da):
    print("\n--- DANH SACH DU AN ---")
    if ds_da.kich_thuoc() == 0:
        print("Chua co du an nao trong he thong.")
        return
    tieu_de = (f"{'Ma DA':<8} | {'Ten Du An':<28} | {'Khach Hang':<20} | {'Ngan Sach (VND)':>18} | {'Ngay BD':<12} | {'Ngay KT':<12}")
    print(tieu_de)
    print("-" * len(tieu_de))
    for da in ds_da:
        print(f"{da.ma_da:<8} | {da.ten_da:<28} | {da.khach_hang:<20} | {da.ngan_sach:>18,.0f} | {da.ngay_bd:<12} | {da.ngay_kt:<12}")

def sua_du_an(ds_da):
    print("\n--- SUA THONG TIN DU AN ---")
    if ds_da.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da}  |  {da.ten_da}  |  {da.khach_hang}", "Chon du an can sua")
    if vi_tri == -1: return
    da = ds_da[vi_tri]
    print(f"\nDang sua: [{da.ma_da}] {da.ten_da}   (Enter de giu nguyen)")
    ten_moi = input(f"  Ten moi [{da.ten_da}]: ").strip()
    if ten_moi != "": da.ten_da = ten_moi
    khach_moi = input(f"  Khach hang moi [{da.khach_hang}]: ").strip()
    if khach_moi != "": da.khach_hang = khach_moi
    ns_input = input(f"  Ngan sach moi [{da.ngan_sach:,.0f}]: ").strip()
    if ns_input != "":
        try:
            val = float(ns_input)
            if val > 0: da.ngan_sach = val
        except ValueError: pass
    ghi_file_du_an("DuAn.txt", ds_da)
    print("=> Cap nhat du an thanh cong!")

def xoa_du_an(ds_da, ds_cv):
    print("\n--- XOA DU AN ---")
    if ds_da.kich_thuoc() == 0: return
    vi_tri = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da}  |  {da.ten_da}  |  {da.khach_hang}", "Chon du an can xoa")
    if vi_tri == -1: return
    da = ds_da[vi_tri]
    if input(f"Xoa '{da.ten_da}' va TAT CA cong viec? (y/n): ").strip().lower() == 'y':
        ma_da = da.ma_da
        ds_da.xoa_tai(vi_tri)
        for i in range(ds_cv.kich_thuoc() - 1, -1, -1):
            if ds_cv[i].ma_da == ma_da: ds_cv.xoa_tai(i)
        ghi_file_du_an("DuAn.txt", ds_da)
        ghi_file_cong_viec("CongViec.txt", ds_cv)
        print(f"=> Da xoa du an '{da.ten_da}'!")

def them_thanh_vien_du_an(ds_da, ds_nv):
    print("\n--- THEM THANH VIEN VAO DU AN ---")
    if ds_da.kich_thuoc() == 0 or ds_nv.kich_thuoc() == 0: return
    vt_da = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da}  |  {da.ten_da}", "Chon du an")
    if vt_da == -1: return
    vt_nv = chon_tu_danh_sach(ds_nv, lambda nv: f"{nv.ma_nv}  |  {nv.ten_nv}", "Chon nhan vien")
    if vt_nv == -1: return
    da, nv = ds_da[vt_da], ds_nv[vt_nv]
    for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
        if da.ds_ma_thanh_vien[i] == nv.ma_nv:
            print(f"=> LOI: '{nv.ten_nv}' da la thanh vien!")
            return
    da.ds_ma_thanh_vien.them(nv.ma_nv)
    ghi_file_du_an("DuAn.txt", ds_da)
    print(f"=> Da them '{nv.ten_nv}' vao du an '{da.ten_da}'!")

def xoa_thanh_vien_du_an(ds_da, ds_nv):
    if ds_da.kich_thuoc() == 0: return
    vt_da = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da}  |  {da.ten_da}", "Chon du an")
    if vt_da == -1: return
    da = ds_da[vt_da]
    if da.ds_ma_thanh_vien.kich_thuoc() == 0: return
    ds_tv_tam = MyArray()
    for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
        vt = tim_vi_tri_nhan_vien(da.ds_ma_thanh_vien[i], ds_nv)
        if vt != -1: ds_tv_tam.them(ds_nv[vt])
    vt_chon = chon_tu_danh_sach(ds_tv_tam, lambda nv: f"{nv.ma_nv}  |  {nv.ten_nv}", "Chon thanh vien can xoa")
    if vt_chon == -1: return
    ma_nv_xoa = ds_tv_tam[vt_chon].ma_nv
    for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
        if da.ds_ma_thanh_vien[i] == ma_nv_xoa:
            da.ds_ma_thanh_vien.xoa_tai(i)
            break
    ghi_file_du_an("DuAn.txt", ds_da)
    print(f"=> Da xoa '{ds_tv_tam[vt_chon].ten_nv}'!")

def hien_thi_thanh_vien_du_an(ds_da, ds_nv):
    if ds_da.kich_thuoc() == 0: return
    vt_da = chon_tu_danh_sach(ds_da, lambda da: f"{da.ma_da}  |  {da.ten_da}", "Chon du an can xem")
    if vt_da == -1: return
    da = ds_da[vt_da]
    print(f"\n  Du an    : [{da.ma_da}] {da.ten_da}")
    print("-" * 65)
    for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
        ma = da.ds_ma_thanh_vien[i]
        vt = tim_vi_tri_nhan_vien(ma, ds_nv)
        if vt != -1:
            print(f"  {i+1:<5} | {ds_nv[vt].ma_nv:<8} | {ds_nv[vt].ten_nv:<25} | {ds_nv[vt].vai_tro:<8}")

def menu_du_an(ds_da, ds_cv, ds_nv):
    while True:
        print("\n" + "=" * 38 + "\n         QUAN LY DU AN          \n" + "=" * 38)
        print("  1. Them Du an moi\n  2. Hien thi danh sach Du an\n  3. Sua thong tin Du an\n  4. Xoa Du an\n  5. Them Thanh vien\n  6. Xoa Thanh vien\n  7. Xem DS Thanh vien\n  0. Tro ve")
        chon = input("  Moi chon (0-7): ").strip()
        if   chon == '1': them_du_an(ds_da)
        elif chon == '2': hien_thi_danh_sach_du_an(ds_da)
        elif chon == '3': sua_du_an(ds_da)
        elif chon == '4': xoa_du_an(ds_da, ds_cv)
        elif chon == '5': them_thanh_vien_du_an(ds_da, ds_nv)
        elif chon == '6': xoa_thanh_vien_du_an(ds_da, ds_nv)
        elif chon == '7': hien_thi_thanh_vien_du_an(ds_da, ds_nv)
        elif chon == '0': break
        else: print("=> LOI: Lua chon khong hop le!")
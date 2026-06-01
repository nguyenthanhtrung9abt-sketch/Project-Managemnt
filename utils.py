# utils.py
from structures import MyArray

_dem_da = 0
_dem_nv = 0
_dem_cv = 0

def _cap_nhat_bo_dem(ds_da, ds_nv, ds_cv):
    global _dem_da, _dem_nv, _dem_cv
    for da in ds_da:
        if da.ma_da.startswith("DA") and da.ma_da[2:].isdigit():
            so = int(da.ma_da[2:])
            if so > _dem_da: _dem_da = so
    for nv in ds_nv:
        if nv.ma_nv.startswith("NV") and nv.ma_nv[2:].isdigit():
            so = int(nv.ma_nv[2:])
            if so > _dem_nv: _dem_nv = so
    for cv in ds_cv:
        if cv.ma_cv.startswith("TASK-") and cv.ma_cv[5:].isdigit():
            so = int(cv.ma_cv[5:])
            if so > _dem_cv: _dem_cv = so

def sinh_ma_du_an():
    global _dem_da
    _dem_da += 1
    return f"DA{_dem_da:03d}"

def sinh_ma_nhan_vien():
    global _dem_nv
    _dem_nv += 1
    return f"NV{_dem_nv:03d}"

def sinh_ma_cong_viec():
    global _dem_cv
    _dem_cv += 1
    return f"TASK-{_dem_cv:03d}"

def nhap_so_thuc_duong(prompt):
    while True:
        try:
            val = float(input(prompt).strip())
            if val > 0: return val
            print("   [!] Gia tri phai lon hon 0. Vui long nhap lai.")
        except ValueError:
            print("   [!] Vui long nhap mot so hop le.")

def nhap_ngay(prompt):
    while True:
        s = input(prompt).strip()
        phan = s.split('/')
        if len(phan) == 3:
            try:
                d, m, y = int(phan[0]), int(phan[1]), int(phan[2])
                if 1 <= d <= 31 and 1 <= m <= 12 and 1000 <= y <= 9999:
                    return s
            except ValueError: pass
        print("   [!] Ngay khong hop le. Dinh dang: dd/mm/yyyy")

def nhap_chuoi_bat_buoc(prompt):
    while True:
        s = input(prompt).strip()
        if s != "": return s
        print("   [!] Truong nay khong duoc de trong.")

def chon_tu_danh_sach(ds, lay_nhan, tieu_de="Chon STT"):
    if ds.kich_thuoc() == 0:
        print("   (Danh sach trong)")
        return -1
    print(f"\n   {tieu_de}:")
    for i in range(ds.kich_thuoc()):
        print(f"   {i+1:>3}. {lay_nhan(ds[i])}")
    print("     0. Huy")
    while True:
        try:
            chon = int(input("   Nhap so thu tu: ").strip())
            if chon == 0: return -1
            if 1 <= chon <= ds.kich_thuoc(): return chon - 1
            print(f"   [!] Vui long chon tu 1 den {ds.kich_thuoc()}, hoac 0 de huy.")
        except ValueError:
            print("   [!] Vui long nhap so nguyen.")

def tim_vi_tri_du_an(ma_da, danh_sach):
    for i in range(danh_sach.kich_thuoc()):
        if danh_sach[i].ma_da == ma_da: return i
    return -1

def tim_vi_tri_nhan_vien(ma_nv, danh_sach):
    for i in range(danh_sach.kich_thuoc()):
        if danh_sach[i].ma_nv == ma_nv: return i
    return -1

def tim_vi_tri_cong_viec(ma_cv, danh_sach):
    for i in range(danh_sach.kich_thuoc()):
        if danh_sach[i].ma_cv == ma_cv: return i
    return -1

def sap_xep_noi_bot_nhan_vien_theo_ten(danh_sach):
    n = danh_sach.kich_thuoc()
    tam = MyArray()
    for i in range(n): tam.them(danh_sach[i])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tam[j].ten_nv.lower() > tam[j + 1].ten_nv.lower():
                tam[j], tam[j + 1] = tam[j + 1], tam[j]
    return tam

def sap_xep_noi_bot_cong_viec_theo_gio(danh_sach):
    n = danh_sach.kich_thuoc()
    tam = MyArray()
    for i in range(n): tam.them(danh_sach[i])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tam[j].gio_cong < tam[j + 1].gio_cong:
                tam[j], tam[j + 1] = tam[j + 1], tam[j]
    return tam
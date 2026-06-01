# storage.py
from structures import DuAn, NhanVien, CongViec

def doc_file_du_an(ten_file, danh_sach):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == "": continue
                parts = line.split(',')
                if len(parts) >= 6:
                    da = DuAn(parts[0].strip(), parts[1].strip(), parts[2].strip(), 
                              parts[3].strip(), parts[4].strip(), parts[5].strip())
                    if len(parts) == 7 and parts[6].strip() != "":
                        for ma_nv in parts[6].strip().split('|'):
                            ma_nv = ma_nv.strip()
                            if ma_nv != "": da.ds_ma_thanh_vien.them(ma_nv)
                    danh_sach.them(da)
    except FileNotFoundError: pass

def ghi_file_du_an(ten_file, danh_sach):
    with open(ten_file, 'w', encoding='utf-8') as f:
        for da in danh_sach:
            tv_str = ""
            for i in range(da.ds_ma_thanh_vien.kich_thuoc()):
                if i > 0: tv_str += "|"
                tv_str += da.ds_ma_thanh_vien[i]
            f.write(f"{da.ma_da},{da.ten_da},{da.khach_hang},{da.ngan_sach},{da.ngay_bd},{da.ngay_kt},{tv_str}\n")

def doc_file_nhan_vien(ten_file, danh_sach):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == "": continue
                parts = line.split(',')
                if len(parts) == 4:
                    nv = NhanVien(parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip())
                    danh_sach.them(nv)
    except FileNotFoundError: pass

def ghi_file_nhan_vien(ten_file, danh_sach):
    with open(ten_file, 'w', encoding='utf-8') as f:
        for nv in danh_sach:
            f.write(f"{nv.ma_nv},{nv.ten_nv},{nv.vai_tro},{nv.don_gia}\n")

def doc_file_cong_viec(ten_file, danh_sach):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == "": continue
                parts = line.split(',')
                if len(parts) == 9:
                    cv = CongViec(parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip(),
                                  parts[4].strip(), parts[5].strip(), parts[6].strip(), parts[7].strip(), parts[8].strip())
                    danh_sach.them(cv)
    except FileNotFoundError: pass

def ghi_file_cong_viec(ten_file, danh_sach):
    with open(ten_file, 'w', encoding='utf-8') as f:
        for cv in danh_sach:
            f.write(f"{cv.ma_cv},{cv.ten_cv},{cv.ma_da},{cv.ma_nv},{cv.loai_hinh},{cv.thoi_gian_bd},{cv.thoi_gian_kt},{cv.gio_cong},{cv.trang_thai}\n")
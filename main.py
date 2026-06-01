# main.py
from structures import MyArray
from utils import _cap_nhat_bo_dem
from storage import (doc_file_du_an, doc_file_nhan_vien, doc_file_cong_viec,
                     ghi_file_du_an, ghi_file_nhan_vien, ghi_file_cong_viec)

from du_an import menu_du_an
from nhan_vien import menu_nhan_vien
from cong_viec import menu_cong_viec_va_bao_cao

# Khởi tạo 3 mảng toàn cục
danh_sach_du_an     = MyArray()
danh_sach_nhan_vien = MyArray()
danh_sach_cong_viec = MyArray()

def main():
    doc_file_du_an("DuAn.txt", danh_sach_du_an)
    doc_file_nhan_vien("NhanVien.txt", danh_sach_nhan_vien)
    doc_file_cong_viec("CongViec.txt", danh_sach_cong_viec)
    
    _cap_nhat_bo_dem(danh_sach_du_an, danh_sach_nhan_vien, danh_sach_cong_viec)

    print("\n" + "=" * 52 + "\n   CHAO MUNG DEN VOI HE THONG QUAN LY CONG VIEC\n" + "=" * 52)

    while True:
        print("\n" + "=" * 52 + "\n              MENU CHINH               \n" + "=" * 52)
        print("  1. Quan ly Du an")
        print("  2. Quan ly Nhan vien")
        print("  3. Quan ly Timesheet & Bao cao")
        print("  0. Thoat chuong trinh")
        chon = input("  Moi chon (0-3): ").strip()

        if chon == '1':
            menu_du_an(danh_sach_du_an, danh_sach_cong_viec, danh_sach_nhan_vien)
        elif chon == '2':
            menu_nhan_vien(danh_sach_nhan_vien, danh_sach_cong_viec, danh_sach_du_an)
        elif chon == '3':
            menu_cong_viec_va_bao_cao(danh_sach_cong_viec, danh_sach_du_an, danh_sach_nhan_vien)
        elif chon == '0':
            print("\nDang luu du lieu...")
            ghi_file_du_an("DuAn.txt", danh_sach_du_an)
            ghi_file_nhan_vien("NhanVien.txt", danh_sach_nhan_vien)
            ghi_file_cong_viec("CongViec.txt", danh_sach_cong_viec)
            print("Luu thanh cong. Tam biet!")
            break
        else:
            print("=> LOI: Lua chon khong hop le, vui long chon lai!")

if __name__ == "__main__":
    main()


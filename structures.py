# structures.py
class MyArray:
    _CAPACITY_DEFAULT = 8

    def __init__(self):
        self._capacity = MyArray._CAPACITY_DEFAULT
        self._data = [None] * self._capacity
        self._size = 0

    def _mo_rong(self):
        cap_moi = self._capacity * 2
        data_moi = [None] * cap_moi
        for i in range(self._size):
            data_moi[i] = self._data[i]
        self._data = data_moi
        self._capacity = cap_moi

    def them(self, phan_tu):
        if self._size == self._capacity:
            self._mo_rong()
        self._data[self._size] = phan_tu
        self._size += 1

    def xoa_tai(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Chi so ngoai pham vi mang")
        phan_tu_bi_xoa = self._data[i]
        for j in range(i, self._size - 1):
            self._data[j] = self._data[j + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return phan_tu_bi_xoa

    def lay(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("Chi so ngoai pham vi mang")
        return self._data[i]

    def dat(self, i, gia_tri):
        if i < 0 or i >= self._size:
            raise IndexError("Chi so ngoai pham vi mang")
        self._data[i] = gia_tri

    def kich_thuoc(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            yield self._data[i]

    def __getitem__(self, i):
        return self.lay(i)

    def __setitem__(self, i, val):
        self.dat(i, val)

    def __len__(self):
        return self._size

class DuAn:
    def __init__(self, ma_da, ten_da, khach_hang, ngan_sach, ngay_bd, ngay_kt):
        self.ma_da       = ma_da
        self.ten_da      = ten_da
        self.khach_hang  = khach_hang
        self.ngan_sach   = float(ngan_sach)
        self.ngay_bd     = ngay_bd
        self.ngay_kt     = ngay_kt
        self.ds_ma_thanh_vien = MyArray()

class NhanVien:
    def __init__(self, ma_nv, ten_nv, vai_tro, don_gia):
        self.ma_nv   = ma_nv
        self.ten_nv  = ten_nv
        self.vai_tro = vai_tro
        self.don_gia = float(don_gia)

class CongViec:
    def __init__(self, ma_cv, ten_cv, ma_da, ma_nv, loai_hinh, thoi_gian_bd, thoi_gian_kt, gio_cong, trang_thai):
        self.ma_cv        = ma_cv
        self.ten_cv       = ten_cv
        self.ma_da        = ma_da
        self.ma_nv        = ma_nv
        self.loai_hinh    = loai_hinh
        self.thoi_gian_bd = thoi_gian_bd
        self.thoi_gian_kt = thoi_gian_kt
        self.gio_cong     = float(gio_cong)
        self.trang_thai   = trang_thai
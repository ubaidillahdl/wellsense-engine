import numpy as np

# ============================================
# 1. DATA KALIBRASI (6 ORANG)
# ============================================
calib_sbp = [
    (118, 130),  # (prediksi, target)
    (117, 124),
    (115, 129),
    (102, 100),
    (102, 110),
    (104, 127),
]

calib_dbp = [
    (63, 86),
    (60, 61),
    (60, 64),
    (57, 61),
    (56, 60),
    (59, 77),
]

calib_hb = [
    (155, 156),
    (153, 153),
    (153, 174),
    (129, 137),
    (129, 89),
    (130, 130),
]

# ============================================
# 2. DATA VALIDASI (SUDAH KALIBRASI)
# ============================================
data_validasi = [
    {
        "nama": "Anisa",
        "SBP": 110.515409236726,
        "DBP": 61.8179872972973,
        "HB": 119.199918190316,
    },
    {
        "nama": "Rosmiya",
        "SBP": 111.180581415929,
        "DBP": 61.8854610810811,
        "HB": 119.148570573939,
    },
    {
        "nama": "Maisaroh",
        "SBP": 111.001082190265,
        "DBP": 63.8471691891892,
        "HB": 119.654067040568,
    },
]


# ============================================
# 3. FUNGSI REGRESI LINEAR
# ============================================
def regresi_linear(data):
    """
    Menghitung koefisien regresi linear: y = a*x + b
    Input: list of tuple (x, y)
    Output: a, b
    """
    if len(data) < 2:
        if data:
            x1, y1 = data[0]
            return 1, y1 - x1
        return 1, 0

    x = np.array([d[0] for d in data])
    y = np.array([d[1] for d in data])
    a, b = np.polyfit(x, y, 1)
    return a, b


# ============================================
# 4. FUNGSI REVERSE KALIBRASI
# ============================================
def reverse_kalibrasi(y_cal, a, b):
    """Mengembalikan nilai kalibrasi ke raw: y_raw = (y_cal - b) / a"""
    return (y_cal - b) / a


# ============================================
# 5. HITUNG KOEFISIEN
# ============================================
a_sbp, b_sbp = regresi_linear(calib_sbp)
a_dbp, b_dbp = regresi_linear(calib_dbp)
a_hb, b_hb = regresi_linear(calib_hb)

print("=" * 55)
print("  KOEFISIEN KALIBRASI")
print("=" * 55)
print(f"  SBP : a = {a_sbp:.6f}, b = {b_sbp:.6f}")
print(f"  DBP : a = {a_dbp:.6f}, b = {b_dbp:.6f}")
print(f"  HB  : a = {a_hb:.6f},  b = {b_hb:.6f}")
print("=" * 55)
print()

# ============================================
# 6. REVERSE KALIBRASI
# ============================================
print("=" * 55)
print("  DATA VALIDASI (RAW / SEBELUM KALIBRASI)")
print("=" * 55)
print(f"{'Nama':<12} {'SBP Raw':<12} {'DBP Raw':<12} {'HB Raw':<12}")
print("-" * 55)

for d in data_validasi:
    sbp_raw = reverse_kalibrasi(d["SBP"], a_sbp, b_sbp)
    dbp_raw = reverse_kalibrasi(d["DBP"], a_dbp, b_dbp)
    hb_raw = reverse_kalibrasi(d["HB"], a_hb, b_hb)
    print(f"{d['nama']:<12} {sbp_raw:<12.2f} {dbp_raw:<12.2f} {hb_raw:<12.2f}")

print("=" * 55)
print()

# ============================================
# 7. UNTUK DITULIS DI LAPORAN
# ============================================
print("📝 UNTUK LAPORAN:")
print("-" * 55)
print("Tabel 4.x. Hasil Reverse Kalibrasi (Data Tanpa Kalibrasi)")
print(
    f"{'Nama':<12} {'SBP Raw (mmHg)':<18} {'DBP Raw (mmHg)':<18} {'Hb Raw (g/L)':<15}"
)
print("-" * 65)
for d in data_validasi:
    sbp_raw = reverse_kalibrasi(d["SBP"], a_sbp, b_sbp)
    dbp_raw = reverse_kalibrasi(d["DBP"], a_dbp, b_dbp)
    hb_raw = reverse_kalibrasi(d["HB"], a_hb, b_hb)
    print(f"{d['nama']:<12} {sbp_raw:<18.2f} {dbp_raw:<18.2f} {hb_raw:<15.2f}")

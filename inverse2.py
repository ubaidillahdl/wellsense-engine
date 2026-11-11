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
    # {
    #     "nama": "Anisa",
    #     "SBP": 110.515409236726,
    #     "DBP": 61.8179872972973,
    #     "HB": 119.199918190316,
    # },
    # {
    #     "nama": "Rosmiya",
    #     "SBP": 111.180581415929,
    #     "DBP": 61.8854610810811,
    #     "HB": 119.148570573939,
    # },
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
    return (y_cal - b) / a


# ============================================
# 5. HITUNG KOEFISIEN (PRESISI PENUH)
# ============================================
a_sbp, b_sbp = regresi_linear(calib_sbp)
a_dbp, b_dbp = regresi_linear(calib_dbp)
a_hb, b_hb = regresi_linear(calib_hb)

print("=" * 70)
print("  KOEFISIEN KALIBRASI (PRESISI PENUH)")
print("=" * 70)
print(f"  SBP : a = {a_sbp:.12f}, b = {b_sbp:.12f}")
print(f"  DBP : a = {a_dbp:.12f}, b = {b_dbp:.12f}")
print(f"  HB  : a = {a_hb:.12f},  b = {b_hb:.12f}")
print("=" * 70)
print()

# ============================================
# 6. REVERSE KALIBRASI (TANPA PEMBATASAN)
# ============================================
print("=" * 70)
print("  DATA VALIDASI (RAW / SEBELUM KALIBRASI) — PRESISI PENUH")
print("=" * 70)
print(f"{'Nama':<12} {'SBP Raw':<25} {'DBP Raw':<25} {'HB Raw':<25}")
print("-" * 90)

results = []
for d in data_validasi:
    sbp_raw = reverse_kalibrasi(d["SBP"], a_sbp, b_sbp)
    dbp_raw = reverse_kalibrasi(d["DBP"], a_dbp, b_dbp)
    hb_raw = reverse_kalibrasi(d["HB"], a_hb, b_hb)

    results.append(
        {"nama": d["nama"], "SBP_raw": sbp_raw, "DBP_raw": dbp_raw, "HB_raw": hb_raw}
    )

    print(f"{d['nama']:<12} {sbp_raw:<25.12f} {dbp_raw:<25.12f} {hb_raw:<25.12f}")

print("=" * 70)
print()

# ============================================
# 7. UNTUK LAPORAN (TANPA PEMBATASAN)
# ============================================
print("📝 UNTUK LAPORAN (TANPA PEMBATASAN):")
print("-" * 90)
print("Tabel 4.x. Hasil Reverse Kalibrasi (Data Tanpa Kalibrasi) — Presisi Penuh")
print(
    f"{'Nama':<12} {'SBP Raw (mmHg)':<30} {'DBP Raw (mmHg)':<30} {'Hb Raw (g/L)':<25}"
)
print("-" * 100)

for r in results:
    print(
        f"{r['nama']:<12} {r['SBP_raw']:<30.12f} {r['DBP_raw']:<30.12f} {r['HB_raw']:<25.12f}"
    )

print("-" * 100)
print()

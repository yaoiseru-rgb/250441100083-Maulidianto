tugas = 85
uts =75
uas = 90

btugas = 0.3
buts = 0.3
buas = 0.4

nilaiakhirtugas = tugas * btugas
nilaiakhiruts = uts * buts
nilaiakhiruas = uas * buas

totalnilai = nilaiakhirtugas + nilaiakhiruts + nilaiakhiruas

print("--- Nilai yang Andi Peroleh ---")
print("Nilai Tugas:", tugas)
print("Nilai UTS:", uts)
print("Nilai UAS:", uas)
print("Nilai akhir dari Tugas (30%):", round(nilaiakhirtugas, 2))
print("Nilai akhir dari UTS (30%):", round(nilaiakhiruts, 2))
print("Nilai akhir dari UAS (40%):", round(nilaiakhiruas, 2))
print("-------------------------------")
print("Total Nilai Yang Andi peroleh:", round(totalnilai, 2))
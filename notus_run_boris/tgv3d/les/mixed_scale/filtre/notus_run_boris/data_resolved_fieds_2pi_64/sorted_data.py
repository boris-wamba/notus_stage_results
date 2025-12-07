# Tri d'un fichier de données "time  MeanKEDR" par ordre croissant

in_file = "nu_int.dat"
out_file = "nu.dat"

rows = []

with open(in_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        time = float(parts[0])
        value = float(parts[1])
        rows.append((time, value))

rows.sort(key=lambda x: x[0])

with open(out_file, "w", encoding="utf-8") as f:
    f.write("# time   MeanKEDR\n")
    for t, v in rows:
        f.write(f"{t:.4f}    {v:.7f}\n")

print("Fichier trié créé :", out_file)


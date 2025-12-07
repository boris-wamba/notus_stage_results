# Remplace les virgules par des points dans tout le fichier

in_file = "van_rees"
out_file = "van_rees.dat"

with open(in_file, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace(",", ".")

with open(out_file, "w", encoding="utf-8") as f:
    f.write(content)

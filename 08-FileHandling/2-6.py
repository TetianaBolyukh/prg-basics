# Otwórz plik i przeczytaj zawartość
with open("plik.txt", "r") as f:
    zawartosc = f.read()

# Załóżmy, że dzielimy tekst na części na podstawie jakiegoś separatora, np. nowa linia
czesci = zawartosc.split("\n")

# Zapisz każdą część do osobnego pliku
for i, czesc in enumerate(czesci, start=1):
    with open(f"plik{i}.txt", "w") as f_out:
        f_out.write(czesc)

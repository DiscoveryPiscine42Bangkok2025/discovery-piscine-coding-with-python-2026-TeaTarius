tuaprae = 0
while tuaprae <= 10:
    print(f"Table de {tuaprae}:", end="")
    rol = 0
    while rol <= 10:
        print(f" {rol * tuaprae}", end="")
        rol += 1
    tuaprae += 1
    print()
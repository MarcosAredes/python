# -------------------------------------------------------------------

frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]

frutas2 = [iten for iten in frutas1 if "b" in iten]

print(frutas2)


# --------------------------------------------------------------------


frutas1 = ["abacate", "banana", "morango", "kiwi", "abacaxi"]

frutas2 = []

for itens in frutas1:
    if "b" in itens:
        frutas2.append(itens)

print(frutas2)

# ------------------------------------------------------------------------

# Criando lista com códigos dos caracteres da string
symbols = "$&@*]}=§"

codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print("Construção de uma lista a partir de uma string\n")

print("(for): ", codes)

codes = [ord(symbol) for symbol in symbols]
print("(listcomp): ", codes)

# Comparação entre listcomps e map/filter
codes_ascii_listcomp = [ord(s) for s in symbols if ord(s) > 127]

codes_ascii_map = list(filter(lambda c: c > 127, map(ord, symbols)))

print("\n(ord) > 127")
print("(listcomp): ", codes_ascii_listcomp)
print("(map/filter): ", codes_ascii_map)

print("\nProduto cartesiano usando uma list comprehension\n")

colors = ["black", "white"]
sizes = ["S", "M", "L"]

tshirts = [(color, size) for color in colors for size in sizes]

print("Colors: ", colors)
print("Sizes: ", sizes)
print("(C X S): ", tshirts)

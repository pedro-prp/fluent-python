# Criando lista com códigos dos caracteres da string
import array

symbols = "$&@*]}=§"

gen_list_tuple = tuple(ord(symbol) for symbol in symbols)


gen_list_array = array.array("I", (ord(symbol) for symbol in symbols))

print("Genexps\n")
print("(Tuple): ", gen_list_tuple)
print("(Array): ", gen_list_array)


# Exemplo com camisetas e tamanhos usando Gen Expression
colors = ["black", "white"]
sizes = ["S", "M", "L"]

for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)

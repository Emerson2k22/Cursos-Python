familia = ["Roger", "Cris", "Manu", "Vini", "Celine"]
#             0        1       2       3       4
#            -5       -4      -3      -2      -1

print(familia[3])  # retona um indice
print(familia[-3]) # retorna um indice de traz pra frente
print(familia[2:]) # retorna a partir do indice 2
print(familia[2:4]) # retorna a partir do indice até o 4, excluindo o 4 

print(familia)
familia[3] = "Roger"
print(familia)

familia.extend(["Fernando", "Rosania"])

familia.append("Spock")
familia.insert(1, "Emerson")
familia.pop() # remove o último indice
familia.remove("Emerson")
#familia.clear - limpa a lista
print(familia)
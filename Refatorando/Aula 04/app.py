minha_string = "qualquer texto"
print(f"Concatenar {minha_string} em string.")

print(minha_string.upper) # deixa tudo em maiusculo

print(minha_string.lower) # deixa tudo em minusculo

print(minha_string.isupper) # verifica se o texto está em maiusculo

print(minha_string.islower) # verifica se o texto está em minusculo

print(minha_string.strip()) # remove todos os espaços do texto

print(minha_string.replace("qualquer", "meu")) # faz a substituição de palavras ou letras da frase/string
print(len(minha_string)) # conta quantos caracteres existe
#0123456789 de trás pra frente não tem 0 é do -1 em diante
print(minha_string[2])

print(minha_string.index("u")) # retorna em qual indice a letra se encontra

x = "texto" in minha_string
print(x)

texto_meu = """Linha 1,
Linha 2,
Linha 3
"""
# para pular linhas e tbm pode se usar o \n e pra escrever aspas no texto se usa as barras \"texto\"

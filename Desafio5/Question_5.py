# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(s):
    lista_caracteres = list(s)
    inicio = 0
    fim = len(lista_caracteres) - 1

    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[inicio]
        inicio +=1
        fim -= 1
    return ''.join(lista_caracteres)

inserir_string = input("Digite a string para inverter: ")
resutaldo = inserir_string(inserir_string)
print("Sua String invertida:", resutaldo)

# Resultado de exemplo:
# String : exemplo
# Resultado : olpmexe
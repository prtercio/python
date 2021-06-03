#poicion-123456789
"""
texto = 'Abc Def Ghij'
buscar = 'Santos'
tamanho = len(buscar)
indice = texto.find(buscar)

print(texto[indice:indice+tamanho])

for letra in buscar:
    print(letra)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
"""
"""
x = 0
#y = 0

while x < 10:
    y = 0
    
    while y < 5:
        print(f'({x}, {y})')
        y += 1

    x += 1

print('Acabou!')
"""

#calculadora
while True:
    print()
    num1 = input('Digite um número: ')
    if num1 == 'x':
        break
    num2 = input('Digite otro número: ')
    operador = input('Digite um operador: ')
   

    if not num1.isnumeric() or not num2.isnumeric():
        print('Um dos dígitos nao é um Número!!!')
        continue

    # aqui buscamos em una lista
    operadoresAceitados = ['+', '-', '*', '/']

    if operadoresAceitados.count(operador) == 0:
        print('Digite um operador válido (+, -, * ou /)')
        continue

    """    
    # aqui buscamos em um string
    operadoresAceitados = '+ - * /'
    if operadoresAceitados.find(operador) == -1:
        print('Digite um operador válido (+, -, * ou /)')
        continue
    """

    num1 = int(num1)
    num2 = int(num2)    

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)

print("nova linea de prova alterando terceiro commit")
print("nova linea de prova alterando terceiro commit 2")
print("nova linea de prova alterando terceiro commit 3 master")

def prueba1():
    return True

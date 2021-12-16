print("************Calculadora Python*************\n")

print('Selecione o número da operação desejada:\n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

cal = input("Digite sua opção (1/2/3/4/5):\n")

if cal == "1":
    print("soma")
    num1 = int(input("Digite primeiro número:\n"))
    num2 = int(input("Digite Segundo  número:\n"))
    print( num1 + num2)
elif cal == "2":
    print("Subtração")
    num1 = int(input("Digite primeiro número:\n"))
    num2 = int(input("Digite Segundo  número:\n"))
    print(num1 - num2)
elif cal == "3":
    print("Divisão")
    num1 = int(input("Digite primeiro número:\n"))
    num2 = int(input("Digite Segundo  número:\n"))
    print(num1 / num2)
elif cal == "4":
    print("Multiplicação")
    num1 = int(input("Digite primeiro número:\n"))
    num2 = int(input("Digite Segundo  número:\n"))
    print(num1 * num2)
else:
    print('não encontrado')

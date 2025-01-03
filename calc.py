import math

def calculadora_cientifica():
    print("Selecione a operação:")
    print("1 - Seno")
    print("2 - Cosseno")
    print("3 - Logaritmo")
    print("4 - Potência")

    escolha = input("Digite o número da operação desejada: ")

    if escolha in ['1', '2', '3']:
        num = float(input("Digite o número: "))
    elif escolha == '4':
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))

    if escolha == '1':
        print(f"Resultado: {math.sin(math.radians(num))}")
    elif escolha == '2':
        print(f"Resultado: {math.cos(math.radians(num))}")
    elif escolha == '3':
        print(f"Resultado: {math.log(num)}")
    elif escolha == '4':
        print(f"Resultado: {math.pow(base, expoente)}")
    else:
        print("Operação inválida!")

calculadora_cientifica()

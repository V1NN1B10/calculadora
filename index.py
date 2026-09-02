#calculadora simples

while True:
    try:
        num1 = float(input('Digite um numero: '))
        op = input('Digite o operador que deseja executar: ')
        num2 = float(input('Digite outro numero: '))
    except ValueError:
        continue
    
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '/':
        resultado = num1 / num2
    else:
        print('Operação invalida!')
       

    print(f'{num1} {op} {num2} = {resultado}')

    continuar = input('Deseja continuar ? responda com (s/n): ').upper()
    if continuar == 'N':
     print('Encerrando calculadora, Volte sempre!')
     break
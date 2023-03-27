cont = True
while cont != 'Sair':
    primeiro_numero = int(input('digite o primeiro numero: '))
    operacao = input('Digite a operação que você vai utilizar (+, -, *, /): ')
    segundo_numero = int(input('digite o segundo numero: '))

    if operacao == '+':
        resultado = primeiro_numero + segundo_numero
    elif operacao == '-':
        resultado - primeiro_numero - segundo_numero
    elif operacao == '/':
        resultado = primeiro_numero / segundo_numero
    elif operacao == '*':
        resultado = primeiro_numero * segundo_numero

    print
    print(f'RESULTADO: {resultado}')
    print

    cont = input('Para finalizar digite (Sair), caso não digite qualquer outra coisa: ')
    cont.title()
#criando função para calcular o imc
def calculo_imc(peso, altura):
    imc = (int(peso) / float(altura) ** 2)
    return imc

#criando função para verificar a tabela de imc e imprimir o resultado 
def mostra_resultado(imc):

    str_result = ''
    if imc <= 16.9:
        str_result = 'Muito abaixo do peso'
    elif imc >= 17 and imc <= 18.4:
        str_result = 'Abaixo do Peso'  
    elif imc >= 18.5 and imc <= 24.9:
        str_result = 'Peso normal' 
    elif imc >= 25 and imc <= 29.9:
        str_result = 'Acima do peso' 
    elif  imc >= 30 and imc <= 34.9:
        str_result = 'Obesidade Grau I'  
    elif  imc >= 35 and imc <= 40: 
        str_result and 'Obesidade Grau II'   
    elif  imc > 40 :
        str_result = 'Obesidade Grau III'   

    print('seu imc é :', str_result) 

#definindo as variaveis peso e altura de acordo com a entrada do usuário 
str_peso = input('informe seu peso: ')
str_altura = input('informe sua altura: ')

#resgatando o caulo do imc com base no peso e altura
result_imc = calculo_imc(str_peso, str_altura)

#executando a função que faz a verificação da tabela do IMC e mostra o resultado na tela
mostra_resultado(result_imc)



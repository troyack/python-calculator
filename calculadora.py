#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
#render template: passando o nome do modelo e a variáveis ele vai renderizar o template
#request: faz as requisições da nosa aplicação
#redirect: redireciona pra outras páginas
#url_for: vai para aonde o redirect indica

app = Flask(__name__)
app.secret_key = 'flask'
#Chave secreta da sessão


#Função que executa o cálculo e retorna o resultado
def calc(string):
    input = list(string)
    operands = []
    operators = []
    num = ""
    if input[0] == '-':
        negative = True
        input.pop(0)
    else:
        negative = False
    for i in input:
        if i.isdigit() or i == ".":
            num = num + i
        else:
            operands.append(num)
            num = ""
            operators.append(i)
    
    operands.append(num)
    if negative == True:
        operands[0] = str((float(operands[0]) * -1))
    #Até aqui a função separou números de operadores em dois arrays.

    for i in operands:
        if i.count('.') > 1:
            return 'Erro: Entrada inválida'
    result = float(operands[0])
    for i in range(len(operators)):
        if operators[i] == '+':
            result = result + float(operands[i+1])

        if operators[i] == '-':
            result = result - float(operands[i+1])

        if operators[i] == '*':
            result = result * float(operands[i+1])

        if operators[i] == '/':
            if float(operands[i+1]) == 0:
                return 'Erro: Divisão por zero'
            else:
                result = result / float(operands[i+1])
                
    #Formatando a resposta
    result = round(result, 2)
    if result.is_integer():
        result = int(result)

    return result

#Configuração da rota index
@app.route('/',  methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        leno = 1
    else:
        leno = 0

    if request.method == 'POST':
        string = request.form['string']
        result = calc(string)
    else:
        result = 0
    return render_template('calc.html', title='Calculadora Python', leno=leno, result=result)

app.run(debug=True)
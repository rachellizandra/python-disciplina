# Implementar uma solução com Flask que faça

# a. Exiba a mensagem: "Olá, programadores!" no endereço raiz de uma página web e apareça o link "/user/Usuario"
# b. Exiba a mensagem: "Olá, Usuário!" no endereço "/user/" e exiba a mensagem "Altere os endereços do browser e recarregue a página"
# c. Exiba a mensagem: "Olá, nome_usuario!" no endereço "/user/nome_usuario" de uma página web

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def cumprimento():
    boas_vindas = '<h1>Olá, programadores!</h1>'
    link = '<p><a href="user/Usuario">Clique aqui</a></p>'
    return boas_vindas + link

@app.route('/user/')
@app.route('/user/<nome>')
def user(nome="Usuario"):
    personalizar = f'<h1>Olá, {nome}!</h1>'
    instrucao = '<p>Altere o nome no <em> endereço do browser</em> e recarregue a página.</p>'
    return personalizar + instrucao

if __name__ == '__main__':
    app.run(debug=True)
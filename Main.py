from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main.htm')


@app.route('/advice')
def get_advice():
    ''' Objetivo: Criar site em Flask que mostre os conselho da API. '''

    # Método que encontrei para consumir a API
    # API : Advice Slip

    site_request = requests.get('https://api.adviceslip.com/advice')
    response = str(site_request.content)

    #print(response) --> Reposta da API 

    a = len(response)


    a1 = a-3
    advice = response[33:a1]
    ''' a1 e b são um "Algoritmo" que criei só para
    pegar a mensagem e retirar informações extras.'''

    #print(a) --> Tamanho da resposta da API  

    # Mensagem a ser mostrada ao usuário

    return render_template('advice.htm', advice=advice)
    
if __name__ == "__main__": # Just to set Debug mode on
    app.run(debug=True)
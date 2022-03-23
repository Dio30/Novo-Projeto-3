import requests
from tkinter import *

API_KEY = "d7c5eb336a9f9bea2f44c4e2cc117f48"
cidade = "Biguaçu"
link = f"https://api.openweathermap.org/data/2.5/weather?q={'biguaçu'}&appid={'d7c5eb336a9f9bea2f44c4e2cc117f48'}&lang=pt_br"

def pegar_temperatura():
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15

    texto = f'''
    Biguaçu: {temperatura}'''
    texto_previsoes["text"] = texto

janela = Tk()
janela.title("Previsão do Tempo em Biguaçu")

texto_orientacao = Label(janela, text="Clique no botão para ver a previsão do tempo")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar previsão do tempo", command=pegar_temperatura)
botao.grid(column=0, row=1)

texto_previsoes = Label(janela, text="")
texto_previsoes.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
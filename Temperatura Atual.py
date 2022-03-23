import requests
from tkinter import *

#para conseguir a API_Key voce tem que se inscrever no site https://api.openweathermap.org
API_KEY = "Coloque sua api key aqui"
cidade = "rio de janeiro"
link = f"https://api.openweathermap.org/data/2.5/weather?q={'rio de janeiro'}&appid={'api_key'}&lang=pt_br"

def pegar_temperatura():
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15

    texto = f'''
    Rio de Janeiro: {temperatura}'''
    texto_previsoes["text"] = texto

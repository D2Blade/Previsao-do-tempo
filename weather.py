import requests

def traduzir_clima(descricao):
    traducoes = {
        "clear sky": "céu limpo",
        "few clouds": "poucas nuvens",
        "scattered clouds": "nuvens dispersas",
        "broken clouds": "nuvens quebradas",
        "overcast clouds": "nuvens nubladas",
        "mist": "névoa",
        "haze": "névoa seca",
        "light rain": "chuva fraca",
        "moderate rain": "chuva moderada",
        "heavy intensity rain": "chuva forte",
        "very heavy rain": "chuva muito forte",
        "thunderstorm": "tempestade",
        "snow": "neve",
        "mist": "névoa",
        "fog": "nevoeiro"
    }

    return traducoes.get(descricao, descricao)

def obter_previsao_tempo(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        clima = data['weather'][0]['description']
        clima_traduzido = traduzir_clima(clima)

        temperatura = data['main']['temp']
        umidade = data['main']['humidity']
        vento = data['wind']['speed']

        print(f"Previsão do tempo para {cidade}:")
        print(f"Condição do clima: {clima_traduzido}")
        print(f"Temperatura: {temperatura}°C")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do vento: {vento} m/s")
    else:
        print(f"Erro ao obter previsão do tempo. Código de erro: {response.status_code}")

if __name__ == "__main__":
    chave_api = "dee4e735ec0ec7985b3aa71185be5658"
    cidade = input("Digite o nome da cidade: ")
    obter_previsao_tempo(cidade, chave_api)

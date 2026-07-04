import requests



Key = 'acafc1eda3db81af6ed497887b59aad9'

inputcitta = input("Inserisci la tua città: ")

info = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={inputcitta}&units=metric&APPID={Key}")


if info.json()['cod'] == '404':
    print("Città insesistente")
else :
    situazione = info.json()['weather'] [0] ['main']
    temp = round(info.json()['main']['temp'])
    match situazione:
        case "Clouds":
            print("Nuvoloso")
            print("possibile pioggia")
        case "Rain":
            print("Pioggia")
            print("consigliato un ombrello")
        case "Sun":
            print("Soleggiato")
        case "Haze":
            print("Foschia")
        case "Clear":
            print("Sereno")
    print(f"temperatura: {temp}°C")

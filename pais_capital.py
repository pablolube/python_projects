paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Bolivia": "La Paz",
    "Perú": "Lima",
    "Ecuador": "Quito",
    "Colombia": "Bogotá",
    "Venezuela": "Caracas",
    "Estados Unidos": "Washington D.C.",
    "Canadá": "Ottawa",
    "México": "Ciudad de México",
    "España": "Madrid",
    "Francia": "París",
    "Alemania": "Berlín",
    "Italia": "Roma",
    "Reino Unido": "Londres",
    "Portugal": "Lisboa",
    "China": "Pekín",
    "Japón": "Tokio",
    "India": "Nueva Delhi",
    "Rusia": "Moscú",
    "Australia": "Canberra",
    "Egipto": "El Cairo",
    "Sudáfrica": "Pretoria"
}

def quiz_capital():
    print('Bienvenido al Quiz de Capitales')
    score = 0

    for country,capital in paises_capitales.items():
        print(f"Cual es la capital de {country}")
        user_answer=input('Tu respuesta es: ')

        if user_answer.lower()==capital.lower():
            print('Respuesta correcta, ganaste 1 punto')
            score+=1
        else:
            print(f'Respuesta incorrecta. La capital de {country} es {capital}.')
    print(f'Tu puntuacion final es: {score}/{len(paises_capitales)}')

quiz_capital()

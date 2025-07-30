from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = 'Positivo'
    elif polarity < 0:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutro'

    print(f'Texto: {text}')
    print(f'Polaridad: {polarity}')
    print(f'Sentimiento: {sentiment}')

text_example = input('Ingrese texto aquí: ')
analyze_sentiment(text_example)

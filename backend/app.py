from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

# Cargar el tokenizador y el modelo
tokenizer = AutoTokenizer.from_pretrained('openai-community/gpt2')
model = AutoModelForCausalLM.from_pretrained('openai-community/gpt2')

# Lista de canciones con sus emociones asociadas
songs = [
    {'title': 'Happy Song', 'emotion': 'happy'},
    {'title': 'Sad Song', 'emotion': 'sad'},
    {'title': 'Relaxing Tune', 'emotion': 'relaxed'},
    {'title': 'Energetic Beat', 'emotion': 'energetic'},
]

# Función para recomendar una canción basada en la emoción
def recommend_song(emotion):
    for song in songs:
        if song['emotion'] == emotion:
            return song['title']
    return 'No recommendation available.'

# Endpoint para obtener una recomendación de canción basada en un prompt
@app.route('/recommend', methods=['POST'])
def get_emotion_based_song():
    data = request.json
    prompt = data.get('prompt', '')
    
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(**inputs, max_length=50)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Aquí, simplemente vamos a buscar una emoción en el texto generado
    if 'happy' in generated_text:
        song = recommend_song('happy')
    elif 'sad' in generated_text:
        song = recommend_song('sad')
    elif 'relaxed' in generated_text:
        song = recommend_song('relaxed')
    elif 'energetic' in generated_text:
        song = recommend_song('energetic')
    else:
        song = 'I\'m not sure how you feel. Can you tell me more?'
    
    return jsonify({'recommended_song': song})

# Ejecutar la aplicación de Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
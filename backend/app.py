from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import cohere
from flask_cors import CORS
import json
# Reemplaza 'tu_api_key_aqui' con tu clave API de Cohere
co = cohere.Client('QZNxmmynbPhVHvtlEZRQMWn8JYqKOM26EUi3g8fL')

app = Flask(__name__)
CORS(app)

def get_albums_by_singer(singer_name, file_path):
    # Abre el archivo JSON y carga su contenido
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Busca el cantante especificado y devuelve la lista de álbumes
    for singer in data:
        if singer['name'].lower() == singer_name.lower():
            return [album['title'] for album in singer['albums']]
    
    # Si no se encuentra el cantante, devuelve una lista vacía
    return []

def es_json_valido(s):
    try:
        json.loads(s)
    except ValueError as e:
        return False
    return True

def obtener_descripcion_album(album_title, data):
    print(album_title)
    with open(data, 'r') as file:
        data = json.load(file)
        for artist in data:
            for album in artist["albums"]:
                if album["title"] == album_title:
                    return {
                        "Description": album["description"].strip()
                    }
    return None

# Endpoint para obtener una recomendación de canción basada en un prompt
@app.route('/recommendAlbum', methods=['POST'])
def get_based_album(): 
    try:
        data = request.get_json()  

        # Verificar que los parámetros necesarios están presentes
        if 'prompt' not in data or 'singer' not in data:
            return jsonify({"error": "Missed parameters 'prompt' o 'singer'"}), 400

        singer = data['singer']
        album_list = get_albums_by_singer(singer, "data.json")

        prompt = data['prompt']
        album_list = str(album_list)

        response = co.chat(
            message='Do not write dots. Recommend only the name of the album from the following list considering that the result goes in a json, so result can not have special characters like this: {"Name": "response", "Reason": "response"} and '+prompt +'. List= '+album_list
        )
        response_text = response.text.strip()
        final_response = {"recommended_album": response_text}
        if es_json_valido(response_text):
            response_json = json.loads(response_text)
            name = response_json["Name"]
            description = obtener_descripcion_album(name,"data.json")
            final_response.update(description)

        return jsonify(final_response)


        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ejecutar la aplicación de Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
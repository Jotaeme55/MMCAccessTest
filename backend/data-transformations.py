import json

# Abre el archivo JSON y carga su contenido
with open("data.json", "r") as file:
    json_file = json.load(file)

# Imprime el contenido del archivo JSON
print(json_file)

# Extrae los nombres usando una comprensión de listas
artist_list = [artist["name"] for artist in json_file]

# Imprime la lista de nombres
print(artist_list)

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

print(get_albums_by_singer("Taylor Swift", "data.json") )
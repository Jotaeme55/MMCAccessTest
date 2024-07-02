import cohere

# Reemplaza 'tu_api_key_aqui' con tu clave API de Cohere
co = cohere.Client('QZNxmmynbPhVHvtlEZRQMWn8JYqKOM26EUi3g8fL')

# Crear un prompt para recomendar el álbum más corto de la lista
prompt_duracion = (

    "Recommend only the name of the album from the following list considering, que sea el album mas corto:\n"
    ['The King of Limbs de Radiohead',
    'OK Computer de Radiohead',
    'Dummy de Portishead',
    'Third de Portishead',
    'Herzeleid de Rammstein',
    'Mutter de Rammstein',
    'Fearless de Taylor Swift',
    '1989 de Taylor Swift']
    "que el resultado sea asi: Nombre: respuesta, motivo: respuesta"

)


response = co.chat(

    message=prompt_duracion,
    # perform web search before answering the question. You can also use your own custom connector.
    # connectors=[{"id": "web-search"}],
)

print(response.text)

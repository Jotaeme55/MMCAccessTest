require('dotenv').config();

export default class ApiService {

    async getBasedAlbum(singer, prompt) {
        const data = {
            singer: singer,
            prompt: prompt
        };

        // Configuración de la petición
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        };

        try {
            const response = await fetch('http://localhost:3000/recommendAlbum', requestOptions);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const responseData = await response.json();
            console.log('Success:', responseData);
            return responseData;
        } catch (error) {
            console.error('Error:', error);
            throw error; // Lanzar el error para que pueda ser manejado por quien llama a la función
        }
    }
}
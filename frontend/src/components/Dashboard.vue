<template> 
    <!-- intro -->
    <section class="intro" :style="fondoIntro" >
        <Toast />
        <div class="card-intro">
            <div class="title">
                <h1 class="h1-title">GenieTunes: Magic Search with Autocomplete</h1>
            </div>
            <div class="content">
                <div class="left-content" >
                    <div class="cloud">
                        <p style="font-size:larger">{{displayedText}}</p>
                    </div>
                </div>
                <div class="right-content">
                    <transition v-if="!loadingData && !LoadedData" name="fade">
                        <div v-if="!loadingData && !LoadedData" class="genius-block">
                            <img class="genius" src="images/genio-ready.png" alt="genius-start">
                        </div>
                    </transition>
                    <!-- Div para la imagen genio pensando -->
                    <transition v-if="loadingData" name="fade">
                        <div v-if="loadingData" class="genius-block">
                            <img class="genius" src="images/genio-pensando.png" alt="genius-pensando">
                        </div>
                    </transition>
                    <transition v-if="!loadingData && LoadedData" name="fade">
                        <div v-if="!loadingData && LoadedData" class="genius-block">
                            <img class="genius" src="images/genio-rock.png" alt="genius-pensando">
                        </div>
                    </transition>
                </div>
            </div>
            <div class="searchBar">
                <div class="searchBar-funcionality">
                    <h4 style="margin-right: 20px;" class="title-feature first-title">Select a singer or group</h4>
                    <div class="autocomplete-container" style="margin-right: 20px; position: relative;">
                        <input type="text" v-model="query" @input="updateSuggestions" placeholder="Type to search..." class="autocomplete-input"/>
                        <ul v-if="filteredSuggestions.length" class="suggestions-list">
                            <li v-for="(suggestion, index) in filteredSuggestions" :key="index" @click="selectSuggestion(suggestion)">
                                {{ suggestion }}
                            </li>
                        </ul>
                        <Button @click="toggleSuggestions" class="autocomplete-button"><i class="pi pi-arrow-down"></i></Button>
                    </div>
                </div>
                
                <div class="searchBar-funcionality">
                    <h4 style="margin-right: 20px;" class="title-feature">Tell me anything relevant</h4>
                    <textarea style="margin-right: 20px;" v-model="textAreaValue" rows="5" cols="30"></textarea>
                </div>


                <Button class="submit" label="Submit" @click="searchAlbum" />
            </div>
        </div>
    </section>
    <!-- intro -->

    <!-- cuerpo -->
    
    <!-- formulario -->
   
</template>

<script>
import apiService from "../service/apiService";
export default {
	data() {
        return {
            
            imageredes: { backgroundImage: "url(./images/fotoredes.png)" },
            fondoIntro: {backgroundImage: "url(./images/fondo-mmc.jpg)"},
            fondoNube: {backgroundImage: "url(./images/nube.PNG)"},
            fondoCamera: {backgroundImage: "url(./images/camera.png)"},
            fondoDesign: {backgroundImage: "url(./images/design.png)"},
            fondoClients: { backgroundImage: "url(./images/clients.png)" },
            fullText: "Hello, I’m the music genie! Tell me a band or artist and something relevant about you or them, and I’ll reveal one of their albums that matches it!",
            displayedText: "",
            index: 0,
            typingSpeed: 30, // Ajusta la velocidad de escritura aquí,
            textAreaValue: '',
            suggestions: ['Radiohead', 'Portishead', 'Rammstein', 'Taylor Swift'],
            query: "",
            filteredSuggestions: [],
            loadingData:false,
            LoadedData:false
        }
        
    },
    apiService: null,
    async created() {
        this.apiService =  new apiService;
	},
	mounted() {
        this.index=0
        this.displayedText = ""
        this.typeText();
    },
    methods: {
        typeText() {

            if (this.index < this.fullText.length) {
                this.displayedText += this.fullText.charAt(this.index);
                this.index++;
                setTimeout(this.typeText, this.typingSpeed);
            }
        },
        updateSuggestions() {
            this.filteredSuggestions = this.suggestions.filter(suggestion =>
                suggestion.toLowerCase().includes(this.query.toLowerCase())
            );
        },
        selectSuggestion(suggestion) {
            this.query = suggestion;
            this.filteredSuggestions = [];
        },
        toggleSuggestions() {
            if (this.filteredSuggestions.length === 0) {
                this.filteredSuggestions = this.suggestions;
            } else {
                this.filteredSuggestions = [];
            }
        },
        async searchAlbum() {
            if (this.query.length === 0 || !this.suggestions.includes(this.query)) {
                this.$toast.add({severity: 'error', summary: 'Please select a group or singer', life: 3000});
                return;
            }

            this.loadingData = true; // Establecer loadingData en true antes de la llamada a la API
            this.index = 0;
            this.displayedText = "";
            this.fullText = "Jummmm...";
            this.typeText();

            try {
                const apiCall = this.apiService.getBasedAlbum(this.query, this.textAreaValue);
                const delay = new Promise(resolve => setTimeout(resolve, 3000));
                const response = await Promise.all([apiCall, delay]);

                console.log(response[0]); // La respuesta de la API está en response[0]

                let recommendedAlbum = JSON.parse(response[0]["recommended_album"]);

                if (response[0] && typeof response[0] === 'object' && Object.prototype.hasOwnProperty.call(response[0], 'Description')) {
                    this.fullText = `I recommend you the album ${recommendedAlbum["Name"]} because ${recommendedAlbum["Reason"]}\nFurthermore, ${response[0]["Description"]}`;
                } else {
                    this.fullText = `I recommend you the album ${recommendedAlbum["Name"]} because ${recommendedAlbum["Reason"]}`;
                }

                this.index = 0;
                this.displayedText = "";
                this.typeText();
            } catch (error) {
                console.error('Error fetching album data:', error);
            } finally {
                this.loadingData = false; // Establecer loadingData en false después de que se completen la llamada a la API y el temporizador
                this.LoadedData = true;
            }
        }

    },
	computed: {
	},
    components: {
    }
}
</script>
<style>
     /*  layout main container controla el padding del topbar y el footbar */
     /*intro ----------------------------------------------------------intro*/
    .intro{
        width: 100%;
        background-size: 100% 100%;
        height:calc(100vh);
        /* background: linear-gradient(to right, #ffffff, #31A76B); */
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
        flex-direction: column;

    }

    .card-intro{
        width: 80%;
        height: 80%;
        background-color: white;
        border-radius: 20px;
        box-shadow: 0 16px 8px rgba(0, 0, 0.4, 0.4);
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }


    .title{
        width: 100%;
        height: 20%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .content{
        width: 80%;
        height: 50%;
        display: flex;
    }

    .left-content{
        width: 60%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center
    }

    .cloud{
        width: 80%;
        height: 80%;
        border: 1px solid black;
        border-radius: 10px;
        padding: 10px;
        overflow-y: auto;
    }

    .right-content{
        width: 40%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .genius-block{
        width: 80%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .genius {
        width: 100%;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
    }

    /* Transiciones de opacidad */
    .fade-enter-active, .fade-leave-active {
        transition: opacity 1s;
    }

    .fade-enter, .fade-leave-to {
        opacity: 0;
    }

    .searchBar{
        width: 100%;
        height: 30%;
        border-top: 1px solid black;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .intro .overlay{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.65); /* Oscurece la imagen de fondo */
        border-radius: 10px; /* Mantiene los bordes redondeados */
        z-index: 1; /* Coloca la capa por encima de la imagen de fondo */
    }

    .intro .principal{
        width: 50%;
        height: 40%;
        z-index: 2;
    }

    .intro-bottom{
        width: 70%;
        height: 50%;
        z-index: 2;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .cta-button {
        width: 17rem;
        height: 5rem;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 1rem 2rem;
        background-color: #31A76B;
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: bold;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
    }

    .cta-button:hover {
        background-color: #288a58;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
    }

    .imagen-intro {
        width: 40%;
        max-width: 500px;
        margin-left: 3rem;
        z-index: 2;
    }

    .imagen-intro img {
        width: 100%;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .autocomplete{
        width: 25%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: row;
    }



    .autocomplete-container {
        width: 100%;
        display: flex;
        flex-direction: row;
        position: relative;
    }

    .searchBar-funcionality{
        width: 30%;
        height: 95%;
        margin-right: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .autocomplete-input {
        width: 100%;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    .autocomplete-button {
        margin-left: 10px;
    }

    .suggestions-list {
        list-style-type: none;
        margin: 0;
        padding: 0;
        border: 1px solid #ccc;
        max-height: 150px;
        overflow-y: auto;
        position: absolute;
        top: 100%;
        left: 0;
        width: 100%;
        background: white;
        z-index: 1;
    }

    .suggestions-list li {
        padding: 5px;
        cursor: pointer;
    }

    .suggestions-list li:hover {
        background-color: #f0f0f0;
    }

    /*intro ----------------------------------------------------------intro*/
    
    @media (max-width: 768px) {
    /* Estilos específicos para teléfonos y dispositivos móviles medianos */

        .card-intro{
            width: 90%;
            height: 90%;
        }

        .title{
            height: 5%;
        }

        .h1-title{
            font-size: larger;
            text-align: center;
        }

        .content{
            width: 100%;
        }

        .left-content{
            width: 60%;
        }

        .cloud{
            width: 85%;
        }

        .right-content{
            width: 40%;

        }

        .genius-block{
            width: 100%
        }

        .genius{
            height: 50%; 
        }

        .searchBar{
            height: 40%;
            flex-direction: column;
        }

        .searchBar-funcionality{
            width: 70%;
            margin-right: 0px;
        }

        .autocomplete-container{
            width: 80%;
            height: 40%;
        }

        .first-title{
            margin-top: 15px!important;
        }

        .title-feature{
            font-size: medium;
            
        }

        .submit{
            margin-top: 10px
        }
    }
</style>
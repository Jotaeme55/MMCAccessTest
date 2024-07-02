<template> 
    <Toast />
    <!-- intro -->
    <section class="intro" :style="fondoIntro" >
        <div class="card-intro">
            <div class="title">
                <h1>GenieTunes: Magic Search with Autocomplete</h1>
            </div>
            <div class="content">
                <div class="left-content" :style="fondoNube">

                </div>
                <div class="right-content">
                    <div class="genius-block">
                        <img class="genius" src="images/genio-ready.png" alt="genius-start">
                    </div>
                </div>
            </div>
            <div class="searchBar">
                <h4 style="margin-right: 20px;">Search for a song</h4>
                <Textarea v-model="value" rows="5" cols="30" />
            </div>
        </div>
    </section>
    <!-- intro -->

    <!-- cuerpo -->
    
    <!-- formulario -->
   
</template>

<script>
import UserService from "../service/UserService";
export default {
	data() {
        return {
            
            imageredes: { backgroundImage: "url(./images/fotoredes.png)" },
            fondoIntro: {backgroundImage: "url(./images/fondo-mmc.jpg)"},
            fondoNube: {backgroundImage: "url(./images/nube.PNG)"},
            fondoCamera: {backgroundImage: "url(./images/camera.png)"},
            fondoDesign: {backgroundImage: "url(./images/design.png)"},
            fondoClients: { backgroundImage: "url(./images/clients.png)" },
            fondoContactUs: {backgroundImage: "url(./images/contact-us.png)"},
            currentSlide: 0,
            textos: [
                "No me aclaraba con mi proyecto, tenia muchas ideas pero no canseguía avanzar. Gracias a BeeLasy en minutos tenia todo el desarrollo.",
                "Como vi q costaba tan poco pensé que no perdía mucho. Aprobé con notaza.",
                "Me la recomendó un compañero de clase y se quedó cortísimo, rapidísimo.",
                "Estaba super agobiada con montones de exámenes y ya no me daba tiempo para nada, un sobre super guay.",
                "Entre la casa, el trabajo, la familia y los estudios estaba pensando en tirar la toalla, y me hablaron de BeeLasy. El mejor consejo de mi vida.",
            ],
            autores: [
                "Marcos de León- Empresariales",
                "Álvaro Sevilla - Psicología",
                "Gorka Sevilla - Psicología",
                "Esther - Bachillerato Segovia",
                "Ana - Filología",
            ],
            nombre:"",
            message:"",
            email:"",
        }
        
    },
    userService: null,
    async created() {
        this.userService = new UserService;
	},
	mounted() {

        setInterval(this.nextSlide, 5000);
    },
    methods: {
        nextSlide() {
            if (this.currentSlide === this.textos.length - 1) {
                this.currentSlide = 0;
            } else {
                this.currentSlide++;
            }
        },
        async enviarEmail(){

            if (this.email=="" || this.name=="" || this.message=="") {
                this.$toast.add({severity:'error', summary: 'El nombre, el mensaje o el email están vacíos',  life: 3000});
            }else{
                try{
                    await this.userService.sendUserQuestionToBeelasy(this.nombre,this.message,this.email);
                    this.$toast.add({severity:'success', summary: 'Successful', detail: 'Se ha enviado corréctamente', life: 3000});
                }catch{
                    this.$toast.add({severity:'error', summary: 'Ha habido un error en el mensaje',  life: 3000});
                }
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
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;

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

    .genius{
        width: 100%;
        height: 100%;
        background-size: cover;
        background-repeat: no-repeat;
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

    /*intro ----------------------------------------------------------intro*/
    
     
</style>
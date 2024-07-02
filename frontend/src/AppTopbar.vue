<template>
    <div class="layout-topbar ">
        <div class="logo">

            <img id="logo-connectify" @load="cargarLogoConnectify" class="bloque-logo" style="display: none;" src="images/logo-connectify.png" alt="Description of image">
            <Skeleton :style="{ display: mostrarLogo ? 'block' : 'none' }" width="3rem" height="3rem"></Skeleton>
            <p style="font-size:2rem;color: #00344D;">Connectify</p>
        </div>
        <div class="routes">

            <div style="font-size:1.5rem;color: #00344D;" class="mr-5">
                <p >Home</p>
            </div>
            <div style="font-size:1.5rem;color: #00344D;" class="mr-5">
                <p >How this works?</p>
            </div>
            <div style="font-size:1.5rem;color: #00344D;" class="mr-5" >
                <p >Contact us</p>
            </div>
        </div>
    </div>  
</template>


<script>
export default {
    data() {
        return {
            visibleLeft:false,
            displayConfirmationTopBar: false,
            overlayMenuItems: [],
            mostrarLogo: true,
            mostrarSkeletonAbeja: true,
        }
    },
    mounted(){
    },
    methods: {
        cargarLogoConnectify(){
            this.mostrarLogo = false;
            const imagen = document.getElementById('logo-connectify');
            imagen.style.display = 'block';
        },
    },
    computed: {
        
        darkTheme() {
            return this.$appState.darkTheme;
        }
    },

}
</script>
<style>
    .layout-topbar .logo{
        width: 30%;
        height: 100%;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        
    }

    .logo .bloque-logo{
        width: 5rem;
        height: 4rem;
        margin-left: 3rem;
    }

    .layout-topbar .routes{
        width: 70%;
        height: 100%;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        flex-direction: row;
    }


    /* RESPONSIVE------------------------------------------------ */
</style>
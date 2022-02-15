// EVENTOS PARA EL SIDEBAR DEL MENU DE CITADINE
window.addEventListener("DOMContentLoaded", () => {
    document.getElementById("logo").addEventListener("click", () => toggleMenu()), 
    // document.getElementById("menuIcono").addEventListener("click", () => toggleMenu())
    document.getElementById("close-sideBar").addEventListener("click", () => toggleMenu())
    document.getElementById("close-sideBar").addEventListener("keydown", (e) => onkey_tab(e))
    // agregar manejador en evento press
    // let lista = document.getElementsByClassName("sidebar-body-ul")[0].children;
    // for (let i = 0; i < lista.length; i++) {   lista[i].addEventListener("onkeydown", () => onkey_tab())  }


    // enfoque para la carga de secciones
    if (document.getElementById("covid")){
        document.getElementById("covid").focus();
    }

    if (document.getElementById("anounce")){
        document.getElementById("anounce").focus();
    }

    if (document.getElementById("about")){
        document.getElementById("about").focus();
    }

    if (document.getElementById("languaje")){
        document.getElementById("languaje").focus();
    }

    if (document.getElementById("header")){
        document.getElementById("header").focus();
    }

    // ###########
    // LIGHT GALLERY
    // ###########
    var imagPop = document.getElementById("lightgallery");
    console.log(imagPop);
    if (imagPop != null){
        lightGallery(imagPop, { 
            download:false,
            speed: 500,
            addClass: 'lg-custom-thumbnails',
            plugins: [lgZoom, lgThumbnail, lgVideo],      
            mobileSettings:{ 
                showCloseIcon: true,
            }
        });
    }

    let listimgPop = document.getElementsByClassName("gallery__libro");
    console.log(listimgPop);
    if(listimgPop != null){
        for (let i = 0; i < listimgPop.length; i++) {
            lightGallery(listimgPop[i], { 
                download:false,
                speed: 500,
                addClass: 'lg-custom-thumbnails',
                plugins: [lgThumbnail, lgVideo],
                mobileSettings:{ 
                    showCloseIcon: true,
                }
            });
        }
    }


});
const onkey_tab = (e)=>{
    switch (e.keyCode) {
        case 13:
        case 27:
            document.getElementsByClassName("sidebar-body-ul")[0].setAttribute("tabindex",-1);
            document.getElementsByClassName("sidebar-body-ul")[0].blur();
            toggleMenu();
            break;
        case 9:
            document.getElementById("close-sideBar").blur();
            document.getElementsByClassName("sidebar-body-ul")[0].setAttribute("tabindex",1);
            document.getElementsByClassName("sidebar-body-ul")[0].focus();
        default:
            break;
    }
}

const toggleMenu = () => {
    document.getElementById("menuIcono").classList.toggle("active")
    document.getElementById("logo").classList.toggle("boton-active")
    
    // let menu_deslizante=document.getElementsByClassName("sidebar-body-ul");
    // // console.log(menu_deslizante[0].children[0])
    // menu_deslizante[0].children.setAttribute('tabindex', 0)
    // document.getElementById('tab-secciones').focus();


    let lista=document.getElementsByClassName("sidebar-body-ul")[0].children;

    for (let i = 0; i < lista.length; i++) {
        aux = i+1;
        if (lista[i].getAttribute("tabindex") == -1){
            lista[i].setAttribute("tabindex", aux);
        } else {
            lista[i].setAttribute("tabindex",-1);
        }
    }

    if(lista[0].getAttribute('tabindex') != -1){
        lista[0].focus();
        document.getElementById("close-sideBar").setAttribute("tabindex",lista.length + 1);
    } else{
        document.getElementById("close-sideBar").setAttribute("tabindex", -1 );
        document.getElementById("close-sideBar").blur();
    }
    


};


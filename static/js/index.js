// titulos para los alert de diario y citadine
const title_mapa = 'El sitio del <strong>Mapa de entrevistados</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';

const title_dia = 'El sitio del diario <strong>El Día</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_hoy = 'El sitio del diario <strong>Hoy</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_clarin = 'El sitio del diario <strong>Clarín</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_nacion = ' El sitio del diario <strong>La Nación</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_citadineVERDE = ' El sitio de Citadine <strong>Soluciones basadas en la naturaleza</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_citadineAZUL = ' El sitio de Citadine <strong>Catástrofes naturales</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
// enlaces para redireccionar en caso de confirmaicon en el alert
const MAPA = "https://entrevistas-inundacion.netlify.app/index.html";
const CITADINE_VERDE = "http://ifw-raspi.projekt.jade-hs.de/wordpress/nbs/";
const CITADINE_AZUL = "http://ifw-raspi.projekt.jade-hs.de/wordpress/";
const NACION = "https://es.kiosko.net/ar/2013-04-03/np/nacion.html";
const CLARIN =
  "https://www.clarin.com/ciudades/critica-situacion-plata-cientos-evacuados_0_S19zAYFiDXg.html";
const HOY = "https://diariohoy.net/adjuntos/archivos/000/024/0000024100.pdf";
const ELDIA =
  "https://www.eldia.com/nota/2013-4-3--el-agua-ya-esta-en-un-metro-y-medio-por-favor-que-alguien-nos-mande-botes";
// una vez que el DOM esté cargado...
  window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("logo").addEventListener("click", () => toggleMenu()),
    document
      .getElementById("close-sideBar")
      .addEventListener("click", () => toggleMenu()),
    document
      .getElementById("close-sideBar")
      .addEventListener("keydown", (e) => onkey_tab(e)),
    document.getElementById("covid") &&
      document.getElementById("covid").focus(),
    document.getElementById("anounce") &&
      document.getElementById("anounce").focus(),
    document.getElementById("about") &&
      document.getElementById("about").focus(),
    document.getElementById("languaje") &&
      document.getElementById("languaje").focus(),
    document.getElementById("header") &&
      document.getElementById("header").focus();
      // llamada de los 5 albumnes
  var e = document.getElementById("lightgallery");

  // fotos impactantes
  null != e &&
  e.addEventListener("lgAfterOpen", (e) => {
      document.getElementById("lg-prev-1").focus();
    }), null != e &&
          lightGallery(e, {
            download: !1,
            speed: 500,
            addClass: "lg-custom-thumbnails",
            plugins: [lgZoom, lgThumbnail, lgVideo],
            mobileSettings: { showCloseIcon: !0 },
          });
          let t = document.getElementsByClassName("gallery__libro");
          if (
          (null != t &&
          0 != t.length &&
          t[0].addEventListener("lgAfterOpen", (e) => {
              document.getElementById("lg-prev-1").focus();
          }),
          null != t)
          )
          for (let e = 0; e < t.length; e++)
          lightGallery(t[e], {
            download: !1,
            speed: 500,
            addClass: "lg-custom-thumbnails",
            plugins: [lgThumbnail, lgVideo],
            mobileSettings: { showCloseIcon: !0 },
          });
          });


const onkey_tab = (e) => {
    switch (e.keyCode) {
      case 13:
      case 27:
        document
          .getElementsByClassName("sidebar-body-ul")[0]
          .setAttribute("tabindex", -1),
          document.getElementsByClassName("sidebar-body-ul")[0].blur(),
          toggleMenu();
        break;
      case 9:
        document.getElementById("close-sideBar").blur(),
          document
            .getElementsByClassName("sidebar-body-ul")[0]
            .setAttribute("tabindex", 1),
          document.getElementsByClassName("sidebar-body-ul")[0].focus();
    }
  },
  toggleMenu = () => {
    document.getElementById("menuIcono").classList.toggle("active"),
      document.getElementById("logo").classList.toggle("boton-active");
    let e = document.getElementsByClassName("sidebar-body-ul")[0].children;
    for (let t = 0; t < e.length; t++) {
      aux = t + 1;
      if (-1 == e[t].children[0].getAttribute("tabindex")) {
        e[t].children[0].setAttribute("tabindex", aux),
          e[t].setAttribute("tabindex", aux);
      } else
        e[t].children[0].setAttribute("tabindex", -1),
          e[t].setAttribute("tabindex", -1);
    }
    if (-1 != e[0].children[0].getAttribute("tabindex")) {
      e[0].focus(),
        document
          .getElementById("close-sideBar")
          .setAttribute("tabindex", e.length + 1);
    } else
      document.getElementById("close-sideBar").setAttribute("tabindex", -1),
        document.getElementById("close-sideBar").blur();
  };
//  busqueda y asignacion de eventos...
var e = document.getElementById("diario-1-1");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_dia, abri_website, ELDIA);
  });
  e = document.getElementById("mapa");
  null != e &&
    e.addEventListener("click", (e) => {
      custom_popup(title_mapa, abri_website, MAPA);
    });
  
  e = document.getElementById("diario-2-2");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_hoy, abri_website, HOY);
  });
e = document.getElementById("diario-3-3");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_clarin, abri_website, CLARIN);
  });
e = document.getElementById("diario-4-4");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_nacion, abri_website, NACION);
  });
e = document.getElementsByClassName("citadineAzul");
if (null != e)
  for (let i = 0; i < e.length; i++) {
    e[i].addEventListener("click", (e) => {
      custom_popup(title_citadineAZUL, abri_website, CITADINE_AZUL);
    });
  }
e = document.getElementsByClassName("citadineVerde");
if (null != e)
  for (let i = 0; i < e.length; i++) {
    e[i].addEventListener("click", (e) => {
      custom_popup(title_citadineVERDE, abri_website, CITADINE_VERDE);
    });
  }
function custom_popup(titulo, comportamiento, parametro) {
  Swal.fire({
    customClass: {
      confirmButton: 'alert-btn confirm-btn',
      denyButton: 'alert-btn cancel-btn',
      closeButton: 'cancel-btn',
      popup: 'swal2-pop-style',
    },
    buttonsStyling: false,

    title: titulo,
    icon: "warning",
    iconColor:"#E10000",
    showCloseButton: !0,
    showDenyButton: !0,
    focusConfirm: !1,
    confirmButtonText: "Si.",
    denyButtonText: "No.",
    confirmButtonAriaLabel: "Si.",
    denyButtonAriaLabel: "No.",
    // width: "70rem",
    // height: "35rem",
    width: "auto",
    height: "auto",
    color: '#000',
    background: '#FBFFF0 url(./static/images/greeb.jpg) no-repeat left center/contain' ,
    
    backdrop: `
      rgba(0,0,123,0.4)
      url("./static/images/demo-256x256.gif")
      left top
      no-repeat
    `
  }).then((result) => {
    if (result.isConfirmed) {
      comportamiento(parametro);
    }
  });
}
function abri_website(url) {
  window.open(url, "_blank");
}
//service worker

if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register("/sw.js", { scope: '/' })
    .then(function(registration) {
      // Registration was successful
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
      // registration failed :(
      console.log('ServiceWorker registration failed: ', err);
    });
  });
} 

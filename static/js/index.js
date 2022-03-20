// titulos para los alert de diario y citadine
const title_juego1 = 'El sitio web del <strong>Disaster cross</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_juego2 = 'El sitio web de <strong>Limpiar la ciudad</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_juego3 = 'El sitio web del <strong>Rompecabezas NBS</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_juego4 = 'El sitio web de <strong>Inundados (Flooded)</strong> no se encuentra disponible por el momento pero si estás presente en el evento, podrás encontrarlo en el escritorio o en la barra de tareas.';
const title_juego5 = 'El sitio web del <strong>Juego de la memoria</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_juego6 = 'El sitio web del <strong>Quiz Aprendiendo a prepararme</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_juego7 = 'El sitio web del <strong>Quiz Mochila de emergencia (Quiz emergency backpack)</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';

const title_dondeir1 = 'El sitio web de <strong>¿Dónde ir?-Centros de evacuación</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir2 = 'El sitio web de <strong>Caminos a refugios</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir3 = 'El sitio web de <strong>EvacuAR</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir4 = 'El sitio web de <strong>Servicios</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir5 = 'El sitio web de <strong>Zonas inundadas</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir6 = 'El sitio web de <strong>Municipalidad de La Plata</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir7 = 'El sitio web de <strong>Inundaciones La Plata</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_dondeir8 = 'El sitio web de <strong>Ayud-AR</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';

const title_mapa = 'El sitio web del <strong>Mapa de entrevistados</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';

const title_dia = 'El sitio web del diario <strong>El Día</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_hoy = 'El sitio web del diario <strong>Hoy</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_clarin = 'El sitio web del diario <strong>Clarín</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_nacion = ' El sitio web del diario <strong>La Nación</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_citadineVERDE = ' El sitio web de Citadine <strong>Soluciones basadas en la naturaleza</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
const title_citadineAZUL = ' El sitio web de Citadine <strong>Catástrofes naturales</strong> se abrirá en una pestaña nueva. ¿Desea continuar?';
// enlaces para redireccionar en caso de confirmaicon en el alert
const JUEGO1="https://disaster-cross.vercel.app/";
const JUEGO2="https://ecarletti.github.io/deu/dist/";
const JUEGO3="https://deu-2021.vercel.app/";
// const JUEGO4="C:\Users\Juego\Desktop\juegos-compilados\Inundados.exe";
const JUEGO5="https://juego-de-memoria-inundaciones.herokuapp.com";
const JUEGO6="https://barbicorro.github.io/DEU_2021_Corro_Torres/index.html";
const JUEGO7="https://dux2021.herokuapp.com/";

const DONDEIR1="https://hidden-taiga-68681.herokuapp.com/"
const DONDEIR3="https://grupo8.proyecto2021.linti.unlp.edu.ar/"
const DONDEIR4="https://grupo28.proyecto2021.linti.unlp.edu.ar/"
const DONDEIR5="https://grupo30.proyecto2021.linti.unlp.edu.ar/"
const DONDEIR6="https://grupo19.proyecto2021.linti.unlp.edu.ar/"
const DONDEIR7="https://grupo7.proyecto2021.linti.unlp.edu.ar/"
const DONDEIR8="https://grupo12.proyecto2021.linti.unlp.edu.ar/"

const MAPA = "https://mapa-de-entrevistas.netlify.app/index.html";
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

var e = document.getElementById("dondeircamino");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir2, abri_website, DONDEIR1);
});

var e = document.getElementById("dondeir1");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir1, abri_website, DONDEIR1);
});

var e = document.getElementById("dondeir2");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir3, abri_website, DONDEIR3);
});

var e = document.getElementById("dondeir3");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir4, abri_website, DONDEIR4);
});

var e = document.getElementById("dondeir4");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir5, abri_website, DONDEIR5);
});

var e = document.getElementById("dondeir5");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir6, abri_website, DONDEIR6);
});

var e = document.getElementById("dondeir6");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir7, abri_website, DONDEIR7);
});

var e = document.getElementById("dondeir7");
null != e &&
e.addEventListener("click", (e) => {
  custom_popup(title_dondeir8, abri_website, DONDEIR8);
});

var e = document.getElementById("juego1");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego1, abri_website, JUEGO1);
  });
var e = document.getElementById("juego2");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego2, abri_website, JUEGO2);
  });
var e = document.getElementById("juego3");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego3, abri_website, JUEGO3);
  });


var e = document.getElementById("juego5");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego5, abri_website, JUEGO5);
  }); 

var e = document.getElementById("juego6");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego6, abri_website, JUEGO6);
  }); 
  
var e = document.getElementById("juego7");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_juego7, abri_website, JUEGO7);
  });   
var e = document.getElementById("mapa");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_mapa, abri_website, MAPA);
  });

e = document.getElementById("diario-1-1");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_dia, abri_website, ELDIA);
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


  e = document.getElementById("1-1-1");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_dia, abri_website, ELDIA);
  });
  e = document.getElementById("2-2-2");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_hoy, abri_website, HOY);
  });
e = document.getElementById("3-3-3");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_clarin, abri_website, CLARIN);
  });
e = document.getElementById("4-4-4");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(title_nacion, abri_website, NACION);
  });

// inundados
e = document.getElementById("juego4");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup_2("Oh no! \n"+title_juego4 )
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
      url("./static/images/demo-142x170.gif")
      left top
      no-repeat
    `
  }).then((result) => {
    if (result.isConfirmed) {
      comportamiento(parametro);
    }
  });
}

function custom_popup_2(titulo1) {
  Swal.fire({
    title: titulo1,
    imageUrl: './static/images/ansiedad.png',
    imageWidth: 512,
    imageHeight: 256,
    imageAlt: 'oh no',
    
    backdrop: `
      rgba(0,0,123,0.4)
      url("./static/images/demo-142x170.gif")
      left top
      no-repeat
    `
  })
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

const TITULO =
  " Estas saliendo de la página <strong>Generar Conciencia</strong> hacia la página de <strong>Citadine</strong>. ¿Desea continuar?";
const CITADINE_VERDE = "http://ifw-raspi.projekt.jade-hs.de/wordpress/nbs/";
const CITADINE_AZUL = "http://ifw-raspi.projekt.jade-hs.de/wordpress/";
const NACION = "https://es.kiosko.net/ar/2013-04-03/np/nacion.html";
const CLARIN =
  "https://www.clarin.com/ciudades/critica-situacion-plata-cientos-evacuados_0_S19zAYFiDXg.html";
const HOY = "https://diariohoy.net/adjuntos/archivos/000/024/0000024100.pdf";
const ELDIA =
  "https://www.eldia.com/nota/2013-4-3--el-agua-ya-esta-en-un-metro-y-medio-por-favor-que-alguien-nos-mande-botes";
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
  var e = document.getElementById("lightgallery");
  null != e &&
    e.addEventListener("lgAfterOpen", (e) => {
      document.getElementById("lg-prev-1").focus();
    }),
    null != e &&
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
var e = document.getElementById("diario-1-1");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(TITULO, abri_website, ELDIA);
  });
e = document.getElementById("diario-2-2");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(TITULO, abri_website, HOY);
  });
e = document.getElementById("diario-3-3");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(TITULO, abri_website, CLARIN);
  });
e = document.getElementById("diario-4-4");
null != e &&
  e.addEventListener("click", (e) => {
    custom_popup(TITULO, abri_website, NACION);
  });
e = document.getElementsByClassName("citadineAzul");
if (null != e)
  for (let i = 0; i < e.length; i++) {
    e[i].addEventListener("click", (e) => {
      custom_popup(TITULO, abri_website, CITADINE_AZUL);
    });
  }
e = document.getElementsByClassName("citadineVerde");
if (null != e)
  for (let i = 0; i < e.length; i++) {
    e[i].addEventListener("click", (e) => {
      custom_popup(TITULO, abri_website, CITADINE_VERDE);
    });
  }
function custom_popup(titulo, comportamiento, parametro) {
  Swal.fire({
    title: titulo,
    icon: "warning",
    iconColor:"rgb(255 247 1 / 93%)",
    showCloseButton: !0,
    showDenyButton: !0,
    focusConfirm: !1,
    confirmButtonText: "Aceptar",
    denyButtonText: "Cancelar",
    confirmButtonAriaLabel: "Aceptar.",
    denyButtonAriaLabel: "Cancelar.",
    width: "70rem",
    height: "35rem",
    color: 'rgb(0 0 0);',
    background: '#fff url(./static/images/greeb.jpg)' ,
    backdrop: `
        rgba(0,0,123,0.4)
        url("./static/images/cat.gif")
        
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

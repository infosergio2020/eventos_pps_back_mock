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
    for (let t = 0; t < e.length; t++){
        aux = t + 1;
        if (-1 == e[t].children[0].getAttribute("tabindex") )
           { e[t].children[0].setAttribute("tabindex", aux), e[t].setAttribute("tabindex", aux)}
        else e[t].children[0].setAttribute("tabindex", -1),e[t].setAttribute("tabindex", -1);
    }
    if (-1 != e[0].children[0].getAttribute("tabindex"))
      { (e[0].focus(),
        document
          .getElementById("close-sideBar")
          .setAttribute("tabindex", e.length + 1)) }
    else (document.getElementById("close-sideBar").setAttribute("tabindex", -1),
        document.getElementById("close-sideBar").blur());
  };
/**
 * Se utiliza sweetalert2 para mostrar advertencias antes de salir de diarios
 */
  var e = document.getElementById('diario-1-1');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: 'Estas saliendo de la página <strong>Generar Conciencia</strong> hacia un enlace del diario <strong>El Día</strong>. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Aceptar.',
      denyButtonAriaLabel: 'Cancelar.'
    }).then((result) => {
        if (result.isConfirmed) {window.open('https://www.eldia.com/nota/2013-4-3--el-agua-ya-esta-en-un-metro-y-medio-por-favor-que-alguien-nos-mande-botes','_blank');}
    })
  });

  e = document.getElementById('diario-2-2');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: 'Estas saliendo de la página <strong>Generar Conciencia</strong> hacia un enlace del diario <strong>Hoy</strong>. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Aceptar.',
      denyButtonAriaLabel: 'Cancelar.'
    }).then((result) => {
        if (result.isConfirmed) {window.open('https://diariohoy.net/adjuntos/archivos/000/024/0000024100.pdf', '_blank');}
    })
  });

  e = document.getElementById('diario-3-3');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: 'Estas saliendo de la página <strong>Generar Conciencia</strong> hacia un enlace del diario <strong>Clarín</strong>. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Aceptar.',
      denyButtonAriaLabel: 'Cancelar.'
    }).then((result) => {
        if (result.isConfirmed) {window.open('https://www.clarin.com/ciudades/critica-situacion-plata-cientos-evacuados_0_S19zAYFiDXg.html','_blank')}
    })
  });

  e = document.getElementById('diario-4-4');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: ' Estas saliendo de la página <strong>Generar Conciencia</strong> hacia un enlace del diario <strong>La Nación</strong>. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      // cancelButtonText:'funciona',
      // cancelButtonAriaLabel: 'lool',
      confirmButtonAriaLabel: 'Aceptar.',
      denyButtonAriaLabel: 'Cancelar.'
    }).then((result) => {
        if (result.isConfirmed) {window.open('https://es.kiosko.net/ar/2013-04-03/np/nacion.html','_blank')}
    })
  });

  /**
 * Se utiliza sweetalert2 para mostrar advertencias antes de salir a links de citadine
 */
   e = document.getElementsByClassName('citadineAzul');
   if (null != e)
   for(let i=0;i<e.length;i++){
   e[i].addEventListener("click", (e) => {
     Swal.fire({
       title: ' Estas saliendo de la página <strong>Generar Conciencia</strong> hacia la página de <strong>Citadine</strong>. ¿Desea continuar?',
       icon: 'warning',
       showCloseButton: true,
       showDenyButton: true,
       focusConfirm: false,
       confirmButtonText: 'Aceptar',
       denyButtonText: 'Cancelar',
       confirmButtonAriaLabel: 'Aceptar.',
       denyButtonAriaLabel: 'Cancelar.'
     }).then((result) => {
         if (result.isConfirmed) {window.open('http://ifw-raspi.projekt.jade-hs.de/wordpress/','_blank')}
     })
   });
  }
   e = document.getElementsByClassName('citadineVerde');
   if (null != e)
   for(let i=0;i<e.length;i++){
   e[i].addEventListener("click", (e) => {
     Swal.fire({
       title: ' Estas saliendo de la página <strong>Generar Conciencia</strong> hacia la página de <strong>Citadine</strong>. ¿Desea continuar?',
       icon: 'warning',
       showCloseButton: true,
       showDenyButton: true,
       focusConfirm: false,
       confirmButtonText: 'Aceptar',
       denyButtonText: 'Cancelar',
       confirmButtonAriaLabel: 'Aceptar.',
       denyButtonAriaLabel: 'Cancelar.'
     }).then((result) => {
         if (result.isConfirmed) {window.open('http://ifw-raspi.projekt.jade-hs.de/wordpress/nbs/','_blank')}
     })
   });
  }
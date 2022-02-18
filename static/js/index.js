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
 * A partir de acá se utiliza sweetalert2 para mostrar advertencias antes de salir de diarios
 */
  var e = document.getElementById('diario-1-1');
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: '<strong>Atención. </strong>Estas saliendo de la página de Citadine hacia un enlace del diario El Día. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Saliendo de la página.',
      denyButtonAriaLabel: 'Cancelado.'
    }).then((result) => {
        if (result.isConfirmed) window.location.href='https://www.eldia.com/nota/2013-4-3--el-agua-ya-esta-en-un-metro-y-medio-por-favor-que-alguien-nos-mande-botes'
    })
  });

  e = document.getElementById('diario-2-2');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: '<strong>Atención.</strong>Estas saliendo de la página de Citadine hacia un enlace del diario Hoy. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Saliendo de la página.',
      denyButtonAriaLabel: 'Cancelado.'
    }).then((result) => {
        if (result.isConfirmed) window.location.href='https://diariohoy.net/adjuntos/archivos/000/024/0000024100.pdf'
    })
  });

  e = document.getElementById('diario-3-3');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: '<strong>Atención.</strong>Estas saliendo de la página de Citadine hacia un enlace del diario Clarín. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Saliendo de la página.',
      denyButtonAriaLabel: 'Cancelado.'
    }).then((result) => {
        if (result.isConfirmed) window.location.href='https://www.clarin.com/ciudades/critica-situacion-plata-cientos-evacuados_0_S19zAYFiDXg.html'
    })
  });

  e = document.getElementById('diario-4-4');
  null != e &&
  e.addEventListener("click", (e) => {
    Swal.fire({
      title: '<strong>Atención.</strong> Estas saliendo de la página de Citadine hacia un enlace del diario La Nación. ¿Desea continuar?',
      icon: 'warning',
      showCloseButton: true,
      showDenyButton: true,
      focusConfirm: false,
      confirmButtonText: 'Aceptar',
      denyButtonText: 'Cancelar',
      confirmButtonAriaLabel: 'Saliendo de la página.',
      denyButtonAriaLabel: 'Cancelado.'
    }).then((result) => {
        if (result.isConfirmed) window.location.href='https://es.kiosko.net/ar/2013-04-03/np/nacion.html'
    })
  });
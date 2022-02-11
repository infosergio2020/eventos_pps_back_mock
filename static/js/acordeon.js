/*
 *   This content is licensed according to the W3C Software License at
 *   https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
 *
 *   Simple accordion pattern example
 */

'use strict';
// document.getElementsByClassName("accordion-trigger").addEventListener("click", () => openAcordeon());

// const openAcordeon = (e)=>{
//   let boton_acordeon=document.getElementById("amina-mas");
//   boton_acordeon.focus()
//   boton_acordeon.setAttribute("tabindex",0)

// }

class Accordion {
  constructor(domNode) {
    this.rootEl = domNode;
    this.buttonEl = this.rootEl.querySelector('button[aria-expanded]');

    const controlsId = this.buttonEl.getAttribute('aria-controls');
    this.contentEl = document.getElementById(controlsId);

    this.open = this.buttonEl.getAttribute('aria-expanded') === 'true';

    // add event listeners
    this.buttonEl.addEventListener('click', this.onButtonClick.bind(this));
}

  onButtonClick() {
    this.toggle(!this.open);
  }

  toggle(open) {
    // don't do anything if the open state doesn't change
    if (open === this.open) {
      return;
    }

    // update the internal state
    this.open = open;

    // handle DOM updates
    this.buttonEl.setAttribute('aria-expanded', `${open}`);

    if (open) {
      this.contentEl.removeAttribute('hidden');
      console.log(this.contentEl.children[0].children[0].children);
      // forzando el foco al parrafo
      this.contentEl.children[0].children[0].children[0].focus();
    } else {
      this.contentEl.setAttribute('hidden', '');
    }
  }

  // Add public open and close methods for convenience
  open() {
    this.toggle(true);


  }

  close() {
    this.toggle(false);
  }
}

// init accordions
const accordions = document.querySelectorAll('.accordion');
accordions.forEach((accordionEl) => {
  new Accordion(accordionEl);
});



// script para detectar si es o no visible
// window.addEventListener("DOMContentLoaded", () => {
//   function callback(entries,observer){
//      if(entries[0].isIntersecting){//verificamos si actualmente es visible
//        console.log("El elemento ya está visible...");
//      }else{
//        console.log("El elemento no es visible.");
//        console.log(entries[0].target.setAttribute('hidden', ''));
//      }
//    }
//    var observer = new IntersectionObserver(callback, {});
   
//    const element = document.querySelector('#sect1');
//    observer.observe(element);
//  })
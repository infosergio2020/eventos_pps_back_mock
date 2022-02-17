'use strict';class Accordion{constructor(domNode){this.rootEl=domNode;this.buttonEl=this.rootEl.querySelector('button[aria-expanded]');const controlsId=this.buttonEl.getAttribute('aria-controls');this.contentEl=document.getElementById(controlsId);this.open=this.buttonEl.getAttribute('aria-expanded')==='true';this.buttonEl.addEventListener('click',this.onButtonClick.bind(this))}
onButtonClick(){this.toggle(!this.open)}
toggle(open){if(open===this.open){return}
this.open=open;this.buttonEl.setAttribute('aria-expanded',`${open}`);if(open){this.contentEl.removeAttribute('hidden');console.log(this.contentEl.children[0].children[0].children);this.contentEl.children[0].children[0].children[0].focus()}else{this.contentEl.setAttribute('hidden','')}}
open(){this.toggle(!0)}
close(){this.toggle(!1)}}
const accordions=document.querySelectorAll('.accordion');accordions.forEach((accordionEl)=>{new Accordion(accordionEl)})
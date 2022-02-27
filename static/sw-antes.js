// self.addEventListener("install", e => {
//    console.log("Install!");
// })
// guardar en cache
const cacheName = 'cache-v1';
const resourceToPrecache = [
  './',
  './templates/conclusion-del-evento/la-ayuda-de-la-radio.html',
  './templates/conclusion-del-evento/la-importancia-de-la-solidaridad.html',
  './templates/conclusion-del-evento/legado-memoria.html',
  './templates/conclusion-del-evento/reflexiones-de-los-entrevistados.html',

  './templates/inundacion-exterior/alemania.html',
  './templates/inundacion-exterior/chile.html',
  './templates/inundacion-exterior/polonia.html',

  './templates/sections/section-1.html',
  './templates/sections/section-2.html',
  './templates/sections/section-3.html',
  './templates/sections/section-4.html',
  './templates/sections/section-5.html',
  './templates/sections/section-6.html',

  './templates/sidebar/about.html',
  './templates/sidebar/anounce.html',
  './templates/sidebar/covid.html',
  './templates/sidebar/languaje.html',
  './templates/sidebar/objetivo.html',
  './templates/sidebar/recorrido.html',
  './templates/sidebar/sections.html',

  './templates/Conclusiones-del-evento.html',
  './templates/diarios.html',
  './templates/dondeir.html',
  './templates/index.html',
  './templates/inundaciones-en-el-exterior.html',
  './templates/juegos.html',
  './templates/mochila-inteligente.html',
  './templates/photo-album.html',
  './templates/recomendacion-como-actuar.html',
  './templates/sandbox.html',
  './templates/shocking-photos.html',
  './templates/testimonio1.html',
  './templates/testimonio2.html',
  './templates/testimonio3.html',
  './templates/the-news-of-the-day.html',
  './templates/water-level-simulator.html',
  './templates/Why-do-we-flood.html',

  
  './static/css/chat.css',
  './static/css/contenidoPrincipal.css',
  './static/css/diario.css',
  './static/css/libro.css',
  './static/css/lightgallery-bundle.min.css',
  './static/css/lixtbox.css',
  './static/css/main.css',
  './static/css/minAcordeon.css',
  './static/css/normalize.css',
  './static/css/photoAlbum-1.css',
  './static/css/photoAlbum-2.css',
  './static/css/portada.css',
  './static/css/style.css',
  './static/css/testimonios.css',


  './static/js/acordeon.js',
  './static/js/index.js',
  './static/js/jquery-3.2.1.min.js',
  './static/js/lg-thumbnail.min.js',
  './static/js/lg-video.min.js',
  './static/js/lg-zoom.min.js',
  './static/js/lightgallery.min.js',
  './static/js/lixtbox.js',
  './static/js/sweetalert2@11.js'
];

self.addEventListener('install', async e => {
  const cache = await caches.open(cacheName);
  await cache.addAll(resourceToPrecache);
  return self.skipWaiting();
});

self.addEventListener('activate', e => {
  self.clients.claim();
});

self.addEventListener('fetch', async e => {
  const req = e.request;
  const url = new URL(req.url);

  if (url.origin === location.origin) {
    e.respondWith(cacheFirst(req));
  } else {
    e.respondWith(networkAndCache(req));
  }
});

async function cacheFirst(req) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(req);
  return cached || fetch(req);
}

async function networkAndCache(req) {
  const cache = await caches.open(cacheName);
  try {
    const fresh = await fetch(req);
    await cache.put(req, fresh.clone());
    return fresh;
  } catch (e) {
    const cached = await cache.match(req);
    return cached;
  }
}
// listen for beforeinstallprompt

let deferredPrompt;

document.addEventListener('DOMContentLoaded',()=>{

  window.addEventListener('beforeinstallprompt', (e)=>{
    // prevent chrome 67 and earlier from automatically
    // showing the prompt
    e.preventDefault();
    // stash the event so it can be triggered later.
    deferredPrompt=w;
  });
  // Notify the user to install
  
  window.addEventListener('beforeinstallprompt', (e)=>{
    e.preventDefault();
    deferredPrompt=e;
    //update ui notify the user they can
    // add to home screen
    btnAdd.style.display='block';
  });
  
  // show the prompt
  btnAdd.addEventListener('click', (e)=>{
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult)=>{
      if(choiceResult.outcome==='accepted'){
        console.log('user accepted the A2hs prompt');
      }
      deferredPrompt=null;
    });
  });
  // confirming installations
  window.addEventListener('appinstalled', (evt)=>{
    app.logEvent('a2hs','installed');
  });

});


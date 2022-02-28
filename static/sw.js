const CACHE_VERSION = "cache_v1";

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
  './static/js/sweetalert2@11.js',

  './static/img/',
  './static/images/',
];

// acciones a realizar durante la intalacion...
self.addEventListener('install', event => {
    // esperar hasta que el pre cache se complete
    event.waitUntil(precache());
});

// acciones a realizar cuando se haga una peticion
self.addEventListener('fetch', event => {
    // 1ro extraemos la peticion
    const request = event.request;
    // solo procesamos peticiones GET
    if (request.method != "GET"){ return; }
    // buscar en cache
    event.respondWith(cachedResponse(request));//respondemos con una respuesta cacheada
    // actualizar el cache
    event.waitUntil(updateCache(request));
});


// 
// FUNCION ENCARGADA DE SUBIR ALGUNOS RECURSOS ESTATICOS A LA CACHE PARA OPTIMIZAR LA CARGA DE RECURSOS
// 
async function precache() {
    // tenemos que trabajar con una api del DOM
    const cache = await caches.open(CACHE_VERSION)
    // waitUntil espera una promesa asi que debemos regresarla
    return cache.addAll(resourceToPrecache)
    .catch(error => {console.log(error.message);})
}


// 
// FUNCION ENCARGADA DE BUSCAR EN CACHE LA PETICION SOLICITADA EN CASO DE NO EXISTIR HACE LA PETICION A LA RED Y LA RETORNA
// 
async function cachedResponse(request) {
    // buscamos la cache
    const cache = await caches.open(CACHE_VERSION);
    // verificamos que la peticion enviada este contenida en la cache
    const response = await cache.match(request);
    // devolvemos la respuesta, si la respuesta es undefined por que no esta en cache devolvemos los que nos de ña red
    return response || fetch(request)
}


// 
// FUNCION ENCARGADA DE ACTUALIZAR LA CACHE PARA USO DEL SERVICEWORKER
// 
async function updateCache(request) {
    // buscamos la cache
    const cache = await caches.open(CACHE_VERSION);
    // buscamos la peticion en la red
    const response = await fetch(request);
    // con la guia de request vamos a guardar el response
    return cache.put(request, response);
    
}
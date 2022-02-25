// self.addEventListener("install", e => {
//    console.log("Install!");
// })

const cacheName = 'news-v1';
const staticAssets = [
  './',
  './templates/index.html',
  './static/css/styles.css',
  './static/js/index.js'
];

self.addEventListener('install', async e => {
  const cache = await caches.open(cacheName);
  await cache.addAll(staticAssets);
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
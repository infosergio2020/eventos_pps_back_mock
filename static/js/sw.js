self.addEventListener('fetch', event =>{
   console.log( event.respondWith( fetch(event.request.includes(".css")) ) );
});
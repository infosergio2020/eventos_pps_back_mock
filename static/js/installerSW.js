if("serviceWorker" in navigator){
    navigator.serviceWorker.register('./static/sw.js').then(registration => {
        console.log("Sw Registered!");
        console.log(registration);
    }).catch(error => {
        console.log("SW Registration Failed!");
        console.log(error);
    });
}
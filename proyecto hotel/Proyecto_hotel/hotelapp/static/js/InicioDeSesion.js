const formulario = document.getElementById("formulario_inicio_sesion");
var mensaje4 = document.getElementById("mail-ini");
var mensaje5 = document.getElementById("pass-ini");



formulario.addEventListener('submit', e => {
    console.log('summit')
    let mjsMostrar = "";
    let enviar = true;



    //comienzo validaciones

    //mail
    var email = document.getElementById("correo-inicio");
    if (email.value === "") {
        mjsMostrar = "Debe agregar un email";
        enviar = false;
    } else { //retornar el estado sin aviso, enviar = false
        mjsMostrar = "";
        enviar = true;
    }
    mensaje4.innerHTML = mjsMostrar;
    // //contraseña
    let enviar2 = true;
    var pass = document.getElementById("pass-inicio");
    if (pass.value === "") {
        mjsMostrar = "Debe agregar una contraseña";
        enviar2 = false;
    } else { //retornar el estado sin aviso, enviar = false
        mjsMostrar = "";
        enviar2 = true;
    }
    
        mensaje5.innerHTML = mjsMostrar;

    if (!enviar||!enviar2) { e.preventDefault(); }

});
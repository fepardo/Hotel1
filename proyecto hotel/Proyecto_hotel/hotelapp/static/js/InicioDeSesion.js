const formulario = document.getElementById("formulario_inicio_sesion");
var mensaje4 = document.getElementById("mail-ini");
var mensaje5 = document.getElementById("pass-ini");



formulario.addEventListener('submit',e=>{
console.log('summit')
    let mjsMostrar = "";
    let enviar = false;



//comienzo validaciones

//mail
    var email = document.getElementById("correo-inicio");
    if(email.value === ""){
        mjsMostrar = "Debe agregar un email";
        enviar = true;
    }else{ //retornar el estado sin aviso, enviar = false
        mjsMostrar = "";
        enviar = false;
    }
    if(enviar){
        mensaje4.innerHTML = mjsMostrar;
    }
// //contraseña
var pass = document.getElementById("pass-inicio");
    if(pass.value === ""){
        mjsMostrar = "Debe agregar una contraseña";
        enviar = true;
    }else{ //retornar el estado sin aviso, enviar = false
        mjsMostrar = "";
        enviar = false;
    }
    if(enviar){
        mensaje5.innerHTML = mjsMostrar;
    }
    //if(!enviar){e.preventDefault();}
    
});
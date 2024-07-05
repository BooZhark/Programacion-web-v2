$(document).ready(function () {
    $("#btnGenerar").click(function () {
        let rut = $("#txtRut").val();
        let nombre = $("#txtNombre").val();
        let appaterno = $("#txtAppaterno").val();
        let apmaterno = $("#txtApmaterno").val();
        let mail = $("#txtMail").val();
        let telefono = $("#txtTelefono").val();
        let res = validarDatos(rut, nombre, appaterno, apmaterno, telefono, mail);
        if (res) {
            $("#exampleModal").modal("show");
            $("#res").html("")
            $("#res").append("<p>");
            $("#res").append("Rut: " + rut + "<br>");
            $("#res").append("Nombre Completo: " + nombre + " " + appaterno + " " + apmaterno + "<br>");
            $("#res").append("Correo: " + mail + "<br>");
            $("#res").append("Telefono: " + telefono + "<br>");
            $("#res").append("</p>");
            $("#formulario")[0].reset();
        }
    });

    function validarDatos(rut, nombre, appaterno, apmaterno, celular, email) {
        if (String(rut).length < 9 || String(rut).length > 10) {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Rut debe tener largo entre 9 y 10 caracteres</div>");
        } else if (String(nombre).length < 3 || String(nombre).length > 20) {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Nombre debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(appaterno).length <= 3 || String(appaterno).length >= 20) {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Paterno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(apmaterno).length <= 3 || String(apmaterno).length >= 20) {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Materno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(celular).length < 9 || String(celular).length > 12) {
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Telefono debe tener entre 9 y 12 digitos</div>");
        } else if (!validarCorreo(email)) { 
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Correo electrónico inválido</div>");
        } else {
            $("#check").html("");
            return true;
        }
    }

    
    function validarCorreo(email) {
        return email.includes('@');
    }

    $("#botoncontacto").click(function () {
        console.log("Botón contacto clicado");
        let nombre = $("#nombrec").val();
        let email = $("#emailc").val();
        let mensaje = $("#mensajec").val();
        let res = validarContacto(nombre, email, mensaje);
        if (res) {
            console.log("Validación exitosa");
            $("#exampleModal").modal("show");
            $("#res").html("");
            $("#res").append("<p>");
            $("#res").append("Nombre: " + nombre + "<br>");
            $("#res").append("Correo: " + email + "<br>");
            $("#res").append("Mensaje: " + mensaje + "<br>");
            $("#res").append("</p>");
            $("#formulario")[0].reset();
        }
    });
    
        function validarContacto(nombre, email, mensaje) {
            if (String(nombre).length < 3 || String(nombre).length > 20) {
                $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>Nombre debe tener largo entre 3 y 20 caracteres</div>");
                return false;
            } else if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))) {
                $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>Por favor ingresa un correo electrónico válido.</div>");
                return false;
            } else if (mensaje.trim() === '' || mensaje.length > 300) {
                $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center'>Por favor ingresa un mensaje válido (máximo 300 caracteres).</div>");
                return false;
            } else {
                $("#check").html("<div class='alert alert-success w-50 mx-auto text-center'>Mensaje enviado correctamente.</div>");
                return true;
            }
        }

    $("#btnEnviar").click(function () {
        $("#formulario")[0].reset();
    });
});

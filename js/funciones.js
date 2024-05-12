$(document).ready(function () {

    $("#btnGenerar").click(function () {
        let rut = $("#txtRut").val();
        let nombre = $("#txtNombre").val();
        let appaterno = $("#txtAppaterno").val();
        let apmaterno = $("#txtApmaterno").val();
        let mail = $("#txtMail").val();
        let telefono = $("#txtTelefono").val();
        let res = validarDatos(rut, nombre, appaterno, apmaterno, telefono)
        if (res) {
            $("#exampleModal").modal("show");
            $("#res").html("")
            $("#res").append("<p>");
            $("#res").append("Rut: " + rut + "<br>");
            $("#res").append("Nombre Completo: " + nombre + " " + appaterno + " " + apmaterno + "<br>");
            $("#res").append("Correo: " + mail + "<br>");
            $("#res").append("Telefono: " + telefono + "<br>");
            $("#res").append("</p>");

            // Limpiar campos del formulario
            $("#formulario")[0].reset();
        }
    });

    function validarDatos(rut, nombre, appaterno, apmaterno, celular) {
        if (String(rut).length < 9 || String(rut).length > 10) {
            /* Validacion Rut */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Rut debe tener largo entre 9 y 10 caracteres</div>");
        } else if (String(nombre).length < 3 || String(nombre).length > 20) {
            /* Validacion Nombre */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Nombre debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(appaterno).length <= 3 || String(appaterno).length >= 20) {
            /* Validacion Apellido Paterno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Paterno debe tener largo entre 3 y 20 caracteres</div>");
        } else if (String(apmaterno).length <= 3 || String(apmaterno).length >= 20) {
            /* Validacion Apellido Materno */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Apellido Materno debe tener largo entre 3 y 20 caracteres</div>");
        }   else if (String(celular).length < 9 || String(celular).length > 12) {
            /* Validacion Celular */
            $("#check").html("<div class='alert alert-danger w-50 mx-auto text-center' >Telefono debe tener entre 9 y 12 digitos</div>");
        } else {
            /* Confirmacion */
            return true;
        }
    }
    
    // Limpiar campos del formulario al hacer clic en el botón "Limpiar formulario"
    $("#btnEnviar").click(function () {
        $("#formulario")[0].reset();
    });
});

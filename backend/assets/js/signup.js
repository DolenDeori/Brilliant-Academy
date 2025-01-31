    // Example starter JavaScript for disabling form submissions if there are invalid fields
    (function () {
        'use strict'

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
    })()


//toggle passoword
var input_1 = document.getElementById("validationCustomPassword-1");
var input_2 = document.getElementById("validationCustomPassword-2");

var btn_1 = document.getElementById('inputGroupPrepend-1')
var btn_2 = document.getElementById('inputGroupPrepend-2')
var eye_open = document.getElementById("open")
var eye_open_2 = document.getElementById("open-2")

btn_1.addEventListener('click' , function (){
    if (input_1.type === "password") {
        input_1.type = "text";
        eye_open.classList.remove("fa-eye-slash")
        eye_open.classList.add("fa-eye")
    } else {
        input_1.type = "password";
        eye_open.classList.add("fa-eye-slash")
        eye_open.classList.remove("fa-eye")
    }
})

btn_2.addEventListener('click' , function (){
    if (input_2.type === "password") {
        input_2.type = "text";
        eye_open_2.classList.remove("fa-eye-slash")
        eye_open_2.classList.add("fa-eye")
    } else {
        input_2.type = "password";
        eye_open_2.classList.add("fa-eye-slash")
        eye_open_2.classList.remove("fa-eye")
    }
})
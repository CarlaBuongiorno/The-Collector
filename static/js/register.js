/* jshint esversion: 8 */

function handleSubmit(event) {
    event.preventDefault();
    let isDigit = /[0-9]/;
    let isLower = /[a-z]/;
    let isUpper = /[A-Z]/;

    let password = document.getElementById("password").value;
    let errorMsg = document.getElementById("error-msg");

    if (isDigit.test(password) && isLower.test(password) && isUpper.test(password)) {
        registrationForm.submit();
    } else {
        errorMsg.classList.remove("d-none");
    }
}

let registrationForm = document.getElementById('registration-form');
registrationForm.addEventListener('submit', handleSubmit);
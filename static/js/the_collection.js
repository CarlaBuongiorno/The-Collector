// Modal
// credit -> https://getbootstrap.com/docs/4.0/components/modal/
let myModal = document.getElementById('myModal');
let myInput = document.getElementById('myInput');

myModal.addEventListener('shown.bs.modal', function () {
    myInput.focus();
});
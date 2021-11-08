// Modal
// credit -> https://getbootstrap.com/docs/4.0/components/modal/
var myModal = document.getElementById('myModal');
var myInput = document.getElementById('myInput');

myModal.addEventListener('shown.bs.modal', function () {
  myInput.focus();
});
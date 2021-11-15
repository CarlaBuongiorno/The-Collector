/* jshint esversion: 8 */

// Modal
// credit -> https://getbootstrap.com/docs/4.0/components/modal/
let myModal = document.getElementById('myModal');
let myInput = document.getElementById('myInput');

if (myModal) {
  myModal.addEventListener('shown.bs.modal', function () {
    myInput.focus();
  });
}
/* jshint esversion: 8 */

function copyright() {
    let date = new Date();
    let year = date.getFullYear();
    document.getElementById("copyright").innerHTML = year;
}
copyright();
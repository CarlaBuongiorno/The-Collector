function copyright() {
    var date = new Date();
    var year = date.getFullYear();
    document.getElementById("copyright").innerHTML = year;
}
copyright();
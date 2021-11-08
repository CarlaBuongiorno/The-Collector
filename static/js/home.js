function displayInfo(event) {
    console.log("Hello");

    let catalogueComics = document.getElementById("catalogue-comics");
    let browseComics = document.getElementById("browse-comics");
    let buyAndSell = document.getElementById("buy-&-sell");

    catalogueComics.addEventListener("click", displayInfo);
}
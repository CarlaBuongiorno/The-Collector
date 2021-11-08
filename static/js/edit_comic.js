// Credit Tim Nelson for the solution to get toggler to determine if user can enter a price or not
let forSale = document.getElementById("for_sale");
let price = document.getElementById("price");
forSale.addEventListener("change", function () {
    if (this.checked) {
        // if comic is for sale, require a price
        price.setAttribute("required", "");
        price.removeAttribute("disabled");
    } else {
        // if comic is not for sale, price is optional
        price.removeAttribute("required");
        price.setAttribute("disabled", "");
    }
});
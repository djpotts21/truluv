// Number Input Plus / Minus
document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("age-input");
    plusButton = document.getElementById("age-plus");
    minusButton = document.getElementById("age-miunus");
  
    plusButton.addEventListener("click", function () {
        input.value = parseInt(input.value) + 1;
    });
  
    minusButton.addEventListener("click", function () {
        input.value = parseInt(input.value) - 1;
    });
  
  }); 
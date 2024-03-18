$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

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
// Get the input element
const input = document.getElementById('age-input');

$('form input').on('change', function() {
  $(this).closest('form').submit();
});

// Preview image before upload
var loadprev1 = function(event) {
  var output = document.getElementById('preim1');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
  };
var loadprev2 = function(event) {
  var output = document.getElementById('preim2');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
var loadprev3 = function(event) {
  var output = document.getElementById('preim3');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
var loadprev4 = function(event) {
  var output = document.getElementById('preim4');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
var loadprev5 = function(event) {
  var output = document.getElementById('preim5');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
var loadprev6 = function(event) {
  var output = document.getElementById('preim6');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
var loadprev7 = function(event) {
  var output = document.getElementById('preim7');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
    URL.revokeObjectURL(output.src) // free memory
  }
};
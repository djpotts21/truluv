$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })


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



// Timeout for Messages
$(document).ready(function () {
  if ($('.messages').length) {
    setTimeout(function () {
      $('.messages').hide( "slow");
    }, 5000);
  }
});


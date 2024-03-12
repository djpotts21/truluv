$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

// Number Input Plus / Minus

// Get the input element
const input = document.getElementById('age-input');

$('form input').on('change', function() {
  $(this).closest('form').submit();
});
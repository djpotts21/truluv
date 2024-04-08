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

// Location Map on Profile Page

function initMap() {
  if (document.getElementById("locationset")) {
    var locationValue = document.getElementById("locationset").textContent;
    var [lat, lng] = locationValue.split(",");
    document.getElementById("location").value = locationValue;
    var map = new google.maps.Map(document.getElementById('map'), {
      center: { lat: parseFloat(lat), lng: parseFloat(lng) },
      zoom: 15
    });
    var marker = new google.maps.Marker({
      position: { lat: parseFloat(lat), lng: parseFloat(lng) },
      map
    });
    marker.setMap(map);
    map.addListener("center_changed", function () {
      var center = map.getCenter();
      var lat = center.lat();
      var lng = center.lng();
      document.getElementById("location").value = lat + "," + lng;
      marker.setPosition(map.getCenter());
    });
  } else {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function (position) {
        var lat = position.coords.latitude;
        var lng = position.coords.longitude;
        document.getElementById("location").value = lat + "," + lng;
        var map = new google.maps.Map(document.getElementById('map'), {
          center: { lat: lat, lng: lng },
          zoom: 15
        });
        var marker = new google.maps.Marker({
          position: { lat: lat, lng: lng },
          map
        });
        marker.setMap(map);
        map.addListener("center_changed", function () {
          var center = map.getCenter();
          var lat = center.lat();
          var lng = center.lng();
          document.getElementById("location").value = lat + "," + lng;
          marker.setPosition(map.getCenter());
        });
      });
    }
  }
}



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
function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // Perform login logic and validate credentials
  
    // Redirect to home page on successful login
    window.location.href = 'home.html';
  }
  
  function selectVehicle(vehicle) {
    // Perform vehicle selection logic
  
    // Example: Display selected vehicle
    console.log('Selected vehicle:', vehicle);
  }
  
  function showRoute() {
    var sourceAddress = document.getElementById('source').value;
    var destinationAddress = document.getElementById('destination').value;
  
    // Perform route calculation using Google Maps API
    var map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
}
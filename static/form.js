// Javascript & jQuery to handle form submission

// Event listener

// Document.ready get coordinates
// change the DOM element values
$(document).ready(
	if(navigator.geolocation){
		var position;
		navigator.geolocation.getCurrentPosition(function(position)
			$('latitude').val(position.coords.latitude);
			$('longitude').val(position.coords.longitude);
		);} 
	else {
		console.log("Geolocation is not supported by this browser.");
		}
	);


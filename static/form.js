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

// AJAX call to replace form with Adventure!
// Typical format is $.get(url, [data], successFunction)
function submitForm(evt){
	// Stops form from being submitted so that we can save values to var
	evt.PreventDefault();
	// Sets form input values to an object called formInputs
	var formInputs = $('#form').serialize();

	// Makes the POST request to submit the form data to the route
	// Sends the data in a dictionary called formInputs
	// Calls function getAdventure once back from server
	$.post("/submit-data",
		   formInputs,
		   getAdventure);
}


function getAdventure(result){
	$('#form').html(result);
 }



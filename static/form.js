// Javascript & jQuery to handle form submission
console.log('I loaded!');

window.onload = function(){
	navigator.geolocation.getCurrentPosition(handleGetCurrentPosition);
}

function handleGetCurrentPosition(location){
	var latitude = document.getElementById("latitude");
	var longitude = document.getElementById("longitude");
	latitude.value = location.coords.latitude;
	longitude.value = location.coords.longitude;
}


// AJAX call to replace form with Adventure!
// Typical format is $.get(url, [data], successFunction)
function submitForm(evt){
	// Stops form from being submitted so that we can save values to var
	evt.preventDefault();

	// Sets form input values to an object called formInputs
	var formInputs = $('#form').serialize();

	// Makes the POST request to submit the form data to the route
	// Sends the data in a dictionary called formInputs
	// Calls function getAdventure once back from server
	
	$.post("/submit-data",
		   formInputs,
		   getAdventure);
}

$('#form').on("submit", function(evt){
	submitForm(evt);
});

// Callback function that replaces the form element with the result
function getAdventure(result){
	debugger;
	$('#form').html();
	$('#adventure').html(result);
 }



// Javascript & jQuery to handle form submission
console.log('I loaded!');

$(document).ready( function(){
	navigator.geolocation.getCurrentPosition(handleGetCurrentPosition);
	});

function handleGetCurrentPosition(location){
	var latitude = document.getElementById("latitude");
	var longitude = document.getElementById("longitude");
	latitude.value = location.coords.latitude;
	longitude.value = location.coords.longitude;
};


// AJAX call to replace form with Adventure!
// Typical format is $.get(url, [data], successFunction)
function submitForm(evt){
	evt.preventDefault();
	// Sets form input values to an object 
	var formInputs = {
		"latitude": $('#latitude').val(),
		"longitude": $('#longitude').val(),
		"time_pref": $('#time_pref').val()
	};
	// JSON-ifys javascript object to prep for post
	var stringy = JSON.stringify(formInputs, 
								['latitude', 
								 'longitude', 
								 'time_pref']
								); 
	console.log(stringy);

	// Makes the POST request to submit the form data to the route
	// Calls function getAdventure once back from server
	$.post("/submit-data",
		   formInputs,
		   getAdventure);
}

// Eventhandler, on form submit, call the function submitForm
$('#form').on("submit", function(evt){
	submitForm(evt);
});

// When data is retrieved from post request, call getAdventure

// <div id="result">
// 	<h2>adventah!</h2>
// 	<div id="yay">
// 		<div id="yay_name"></div>
// 		<div id ="yay_location"></div>
// 	</div>
// 	<div id="yum">
// 		<div id="yum_name"></div>
// 		<div id="yum_location"></div>
// 	</div>
// </div>
function getAdventure(result){
	$("#yay_url").attr("href", result.yay.url);
	$("#yay_name").html(result.yay.name);
	// $('#yay_location').append(result.yay.url);
	// $('#result').append(result.yay.location);
	// $('#result').append(result.yay.url);
	// $('#result').append(result.yum.name);
	// $('#result').append(result.yum.location);
	// $('#result').append(result.yum.url);

	console.log("Made it back from flask route :D");
	console.log(result);
};


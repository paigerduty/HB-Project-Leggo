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

function getAdventure(result){
	// debugger;
	console.log("Back with Adventure");
	console.log(result);
	console.log(result.data);
	result = JSON.parse(result);
	$("#yay_url").attr("href", result.yay.url);
	$("#yay_name").html(result.yay.name);
	$('#yay_location').html(result.yay.location);

	$("#yum_url").attr("href", result.yum.url);
	$("#yum_name").html(result.yum.name);
	$("#yum_location").html(result.yum.location);

	console.log("Made it back from flask route :D");
	console.log(result);
};

function swapYay (result) {
	result = JSON.parse(result);
	$("#yay_url").attr("href", result.yay.url);
	$("#yay_name").html(result.yay.name);
	$('#yay_location').html(result.yay.location);
}


function submitSwapYay(evt){
	console.log("Going to get a new Yay!");

	$.get("/swap-yay", swapYay);
}

$('#swap-yay').on("submit", function(evt){
	swapYay(evt);
});


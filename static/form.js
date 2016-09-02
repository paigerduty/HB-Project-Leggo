// Javascript & jQuery to handle form submission
console.log('I loaded!');
var latitude;
var longitude;
var latLng;

// var markerCount = 0;

$(document).ready( function(){
	navigator.geolocation.getCurrentPosition(handleGetCurrentPosition);
	});

function handleGetCurrentPosition(location){
	latitude = document.getElementById("latitude");
	longitude = document.getElementById("longitude");
	latitude.value = location.coords.latitude;
	longitude.value = location.coords.longitude;

};

function submitForm(evt){
	evt.preventDefault();
	// Sets form input values to an object 
	formInputs = {
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

var yays;
var yums;

function getAdventure(result){
	console.log("Back with Adventure");
	console.log(result);
	result = JSON.parse(result);

	yays = result.yays;
	yums = result.yums;

	var current_yay = yays.pop();
	var current_yum = yums.pop();

	initMap(current_yay, current_yum);

	$("#yay_url").attr("href", current_yay.url);
	$("#yay_name").html(current_yay.name);
	$('#yay_location').html(current_yay.location);
	$('#swap-yay').attr("style","");

	$("#yum_url").attr("href", current_yum.url);
	$("#yum_name").html(current_yum.name);
	$("#yum_location").html(current_yum.location);
	$('#swap-yum').attr("style", "");
};

function initMap(current_yum, current_yay){
	console.log("initMap called");
	var map;
	// Makes new map Object
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: parseFloat(latitude.value), lng: parseFloat(longitude.value)},
		zoom: 12
	});

	 var user_marker = new google.maps.Marker({
		position: {lat: parseFloat(latitude.value), lng:parseFloat(longitude.value)},
		map:map,
		title: 'Current Loc <3'
	});

	var loc = current_yay.location;
	loc = loc.replace(",",":").slice(2,-2).split(":");
	yay_latitude = loc[1];
	yay_longitude = loc[3];
	console.log(">>>>>>>>>>>>>>")
	console.log(yay_latitude, yay_longitude);

	var yay_marker = new google.maps.Marker({
		position: {lat: parseFloat(yay_latitude), lng:parseFloat(yay_longitude)},
		map:map
	});

	var yum_marker = new google.maps.Marker({
		position: {lat: parseFloat(current_yum.latitude), lng:parseFloat(current_yum.longitude)},
		map:map
	});

	console.log(map);

}

function addMarkersToMap(latitude, longitude){
	var latLng = new google.maps.LatLng(latitude, longitude);
	var marker = new google.maps.Marker({
		position: latLng,
		map: map,
		animation: google.maps.Animation.DROP,
	});
}

function submitSwapYay(evt){
	console.log("Going to get a new Yay!");
	var current_yay = yays.pop();

	$("#yay_url").attr("href", current_yay.url);
	$("#yay_name").html(current_yay.name);
	$('#yay_location').html(current_yay.location);
}

$('#swap-yay').on("click", function(evt){
	submitSwapYay(evt);
});


function submitSwapYum(evt){
	console.log("Going to get a new Yum!");
	var current_yum = yums.pop();

	$("#yum_url").attr("href", current_yum.url);
	$("#yum_name").html(current_yum.name);
	$("#yum_location").html(current_yum.location);
}

$('#swap-yum').on("click", function(evt){
	submitSwapYum(evt);
});



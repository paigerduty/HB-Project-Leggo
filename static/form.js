// Javascript & jQuery to handle form submission
console.log('I loaded!');
var latitude;
var longitude;
var latLng;

$(document).ready( function(){
	navigator.geolocation.getCurrentPosition(handleGetCurrentPosition);
	});

function handleGetCurrentPosition(location){
	latitude = document.getElementById("latitude");
	longitude = document.getElementById("longitude");
	latitude.value = location.coords.latitude;
	longitude.value = location.coords.longitude;

	$('#btn').attr("style","");

};

function submitForm(evt){
	evt.preventDefault();
	// Sets form input values to an object 
	formInputs = {
		"latitude": $('#latitude').val(),
		"longitude": $('#longitude').val(),
		"time_pref": $('#time_pref').val()
	};
	// JSON-ifys object to prep for POST
	var stringy = JSON.stringify(formInputs, 
								['latitude', 
								 'longitude', 
								 'time_pref']
								); 
	console.log(stringy);

	// Submits form data to Flask route
	// Calls getAdventure once back from server
	$.post("/submit-data",
		   formInputs,
		   getAdventure);
}

// Eventhandler for form submission
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

var map;
var markers;
function initMap(current_yum, current_yay){
	console.log("initMap called");
	map = new google.maps.Map(document.getElementById('map'), {
		center: {lat: parseFloat(latitude.value), lng: parseFloat(longitude.value)},
		zoom: 12
	});

	var loc = current_yay.location;
	loc = loc.replace(",",":").slice(2,-2).split(":");
	yay_latitude = loc[1];
	yay_longitude = loc[3];

	markers = [
		['user_marker', parseFloat(latitude.value),parseFloat(longitude.value),1],
		['yay_marker', parseFloat(yay_latitude),parseFloat(yay_longitude),2],
		['yum_marker', current_yum.latitude, current_yum.longitude,3]
	];

	for (i=0; i<markers.length;i++){
		marker = new google.maps.Marker({
			position: {lat: markers[i][1], lng: markers[i][2]},
			map:map
		});
	}

	console.log(map);

}


function submitSwapYay(evt){
	console.log("Going to get a new Yay!");
	var current_yay = yays.pop();

	$("#yay_url").attr("href", current_yay.url);
	$("#yay_name").html(current_yay.name);
	$('#yay_location').html(current_yay.location);

	var geocoder = new google.maps.Geocoder();

	geocoder.geocode({'address': current_yay.location}, function(results) {
		var yay_lat = results[0].geometry.location.lat();
		var yay_long = results[0].geometry.location.lng();

		console.log("geocoded addy", yay_lat, yay_long);

		markers[1][1] = yay_lat;
		markers[1][2] = yay_long;

		for (i=0;i <markers.length; i++) {
			marker = new google.maps.Marker({
			position: {lat: markers[i][1], lng: markers[i][2]},
			map:map
			});
		}
	});

	console.log("MARKERS", markers);
	
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

	var loc = current_yum.location;
	loc = loc.replace(",",":").slice(2,-2).split(":");
	yum_latitude = loc[1];
	yum_longitude = loc[3];

	console.log(markers[2][1]);
	markers[2][1] = parseFloat(yum_latitude);
	console.log(markers[2][1]);
	markers[2][2] = parseFloat(yum_longitude);

	for (i=0;i <markers.length; i++) {
		marker = new google.maps.Marker({
		position: {lat: markers[i][1], lng: markers[i][2]},
		map:map
		});
	}


	console.log("should have placed new yay marker")
}

$('#swap-yum').on("click", function(evt){
	submitSwapYum(evt);
});



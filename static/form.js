// Javascript & jQuery to handle form submission
console.log('I loaded!');
var latitude;
var longitude;
var latLng;
var markers;
var yay_lat;
var yay_long;
// var markerCount = 0;

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

var map;
var markers;
function initMap(current_yum, current_yay){
	console.log("initMap called");
	// var map;
	// Makes new map Object
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

	// debugger;

	var geocoder = new google.maps.Geocoder();

	var yay_lat;
	var yay_long;
	geocoder.geocode({'address': current_yay.location}, function(results) {
	    console.log("results", results)
	    yay_lat = results[0].geometry.location.lat();
	    // debugger;
	    console.log("yay_lat",yay_lat);
	    yay_long = results[0].geometry.location.lng();
	    console.log("yay_long",yay_long);
	}); 


	console.log(">>>>>>>>>>>>>>");
	console.log("geocoded addy");

	// ONCE MARKER IS ADDED TURN INTO A FUNCTION THEN CALL THAT FXN AND PASS LATLNG
	console.log("YAY INFO INCOMING");
	console.log(markers[1]);
	console.log(markers[1][1]);

	var cur_yay = markers[1];
	console.log("cur_yay",cur_yay);
	debugger;
	cur_yay[1] = yay_lat;
	cur_yay[2] = yay_long;

	console.log("HOPEFULLY STUFF CHANGED");
	console.log("cur_yay", cur_yay);

	var new_marker = new google.maps.Marker({
			position: {lat: markers[i][1], lng: markers[i][2]},
			map:map
		});

	console.log("should have placed new yay marker")
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


	console.log("new yum",markers[2]);
	console.log("new yum lat",markers[2][1]);


	var loc = current_yum.location;
	loc = loc.replace(",",":").slice(2,-2).split(":");
	yum_latitude = loc[1];
	yum_longitude = loc[3];

	var cur_yum = markers[2];
	console.log("cur_yum",cur_yum);
	console.log("Look at methods on current_yum");
	debugger;
	cur_yum[1] = yum_latitude;
	cur_yum[2] = yum_longitude;

	console.log("HOPEFULLY STUFF CHANGED");
	console.log("cur_yay", cur_yay);

	var new_marker = new google.maps.Marker({
			position: {lat: cur_yum[1], lng: cur_yum[2]},
			map:map
		});

	console.log("should have placed new yay marker")
}

$('#swap-yum').on("click", function(evt){
	submitSwapYum(evt);
});



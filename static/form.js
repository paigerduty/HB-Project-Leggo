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
	var formInputs = {
		"latitude": $('input[name="latitude"]').val(),
		"longitude": $('input[name="longitude"]').val(),
		"time_pref": $('#time_pref').val()
	};

	// var formInputs = $("#form").serialize
	console.log(formInputs);

	// Makes the POST request to submit the form data to the route
	// Sends the data in a dictionary called formInputs
	// Calls function getAdventure once back from server
	
	$.post("/submit-data",
		   formInputs,
		   getAdventure);
}

// Eventhandler, on form submit, call the function submitForm
$('#form').on("submit", function(evt){
	submitForm(evt);
});

// Callback function that replaces the form element with the result
function getAdventure(result){
	$('#form').html(result);
	$('#result').html(result);
 };

// $(function() {
// 	$('button').click(function() {
// 		var latitude = $('#latitude').val();
// 		var longitude = $('#longitude').val();
// 		var time_pref = $('#time_pref').val();
// 		$.ajax({
// 			url: '/submit-data',
// 			data: $('form').serialize(),
// 			type: 'POST',
// 			success: function(response) {
// 				console.log(response)
// 			},
// 			error: function(error) {
// 				console.log(error);
// 			}
// 		});
// 	});
// });

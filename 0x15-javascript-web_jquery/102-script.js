$(document).ready(function() {
// Event handler for the button click
	$('#btn_translate').on('click', function() {
	// Get the language code entered by the user
	var languageCode = $('#language_code').val();

	// Make the API request to fetch the translation
	$.ajax({
		url: 'https://www.fourtonfish.com/hellosalut/hello/',
	method: 'GET',
	data: {lang: languageCode },
	success: function(data) {
	// Display the translation in the DIV#hello
		$('#hello').text(data.hello);
	},
		error: function() {
	// Handle errors if needed
	$('#hello').text('Error fetching translation');
		}
	});
	});

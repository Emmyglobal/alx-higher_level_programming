$(document).ready(
$.ajax({
	url:  'https://swapi-api.alx-tools.com/api/films/?format=json',
	method: 'GET',
	success: function(data) {
		// Update the content of DIV#hello with the fetched value
	$('#hello').text(data.hello);
	},
	error: function() {
		// Handle errors if needed
	$('#hello').text('Error fetching translation');
	}
});

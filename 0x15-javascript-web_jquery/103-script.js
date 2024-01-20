/*Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
The translation of “Hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
You must use the JQuery API
You script must work when imported from the <head> tag
	*/

$(document).ready(function() {
// Event handler for the button click
	$('#btn_translate').on('click', function() {
	translateHello();
	});
// Event handler for pressing ENTER on the language_code input
	$('#language_code').on('keydown', function(event) {
	if (event.which === 13) {
	// 13 is the key code for ENTER
		translateHello();
	}
	});
// Function to fetch and display the translation
	function translateHello() {
// Get the language code entered by the user
	var languageCode = $('#language_code').val();
// Make the API request to fetch the translation
	$.ajax({
		url: 'https://www.fourtonfish.com/hellosalut/hello/',
	method: 'GET',
	data: {lang: languageCode},
	success: function(data) {
	// Display the translation in the DIV#hello
		$('#hello').text(data.hello);
	},
		error: function() {
	// Handle errors if needed
		$('#hello').text('Error fetching translation');
		}
	});
	}
});

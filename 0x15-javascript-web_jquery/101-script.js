$(document).ready(function() {
	// Add item to the list
	$('#add_item').on('click', function() {
	// Create a new <li> element
		var newItem = $('<li>Item</li>');
	// Append the new element to Ul.my_list
	$('ul.my_list').append(newItem);
	});
	//Remove the last item from the list
	$('#remove_item').on('click', function() {
	//Remove the last <li> element from Ul.my_list
		$('ul.my_list li:last-child').remove();
	});

	// Clear all items from the list
	$('#clear_list').on('click', function() {
	// Remove all <li> elements from UL.my_list
	$('ul.my_list').empty();
	});
});

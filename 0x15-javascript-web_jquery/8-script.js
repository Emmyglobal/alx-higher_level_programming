$(document).ready(function{
$.ajax({ url: 'https://swapi-api.alx-tools.com/api/films/?format=json', type: 'GET', success: function(data){
$.each(data.results,
function(index, film){
	$('UL#list_movies').append('<li>' + film.title + '</li>');
});
}
});
});

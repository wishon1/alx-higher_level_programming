// Wait for the document to be ready before executing JS script
$(document).ready(function() {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  // Fetch URL and provide a function to handle the response
  $.get(url, function(data) {

    // Extract the array of movie objects from the API response
    var movies = data.results;
    var list = $('ul#list_movies');

    // Iterate over each movie in the array
    $.each(movies, function(_, movie){
      // Append a list item containing the title of the current movie
      list.append("<li>" + movie.title + "</li>");
    });
  });
});

$(document).ready(function() {
  const url = https://swapi-api.alx-tools.com/api/films/?format=json;

  // fecth url and provide a function to handle the response
  $.get(url, function(data) {
    
    // extract the array of movies objeect from api response
    var movies = data.results;
    var list = $('UL#list_movies
  })
});

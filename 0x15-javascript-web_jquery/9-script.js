// Wait for the document to load before executing the JS script
$(document).ready(function() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Send a GET request to fetch the URL and execute the content of the function
  $.get(url, function(data) {

    // Add the text "hello" to the DIV#hello and display it
    $("Div#hello").text(data.hello);
  });
});

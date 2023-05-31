$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  const movies = data.results;
  movies.forEach(function(movie) {
    var listItem = $('<li>').text(movie.title);
    $('#list_movies').append(listItem);
  });
});
~
~
~


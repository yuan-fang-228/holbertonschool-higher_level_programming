$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movieList = data.results;
  $.each(movieList, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});

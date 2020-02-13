$(function (){
  let $movies = $('#list_movies');

  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (movies) {
      $.each(movies.results, function(i, movie) {
        $movies.append('<li>' + movie.title + '</li>');
      });
    }
  });
});

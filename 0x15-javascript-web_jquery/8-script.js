$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
  if (status) {
    data.results.forEach(element => {
      $('ul#list_movies').append('<li>' + element.title + '</li>');
    });
  }
});

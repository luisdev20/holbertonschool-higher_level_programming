$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
  for (let cons movie in data.results) {
    $('UL#list_movies').append(`<li>${data.results[movie].title}</li>`);
  }
});

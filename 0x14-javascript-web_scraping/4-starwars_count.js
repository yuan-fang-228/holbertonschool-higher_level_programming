#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2])
  .then(response => {
    const movies = response.data.results;
    const count = movies.filter(movie => movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')).length;
    console.log(count);
  })
  .catch(error => {
    console.log(error);
  });

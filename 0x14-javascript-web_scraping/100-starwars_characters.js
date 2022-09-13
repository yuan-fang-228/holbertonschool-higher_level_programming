#!/usr/bin/node
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(film => {
    const characters = film.data.characters;
    for (const character of characters) {
      axios.get(character)
        .then(response => {
          console.log(response.data.name);
        });
    }
  })
  .catch(error => {
    console.log(error);
  });

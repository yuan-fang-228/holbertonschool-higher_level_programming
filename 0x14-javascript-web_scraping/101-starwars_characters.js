#!/usr/bin/node
const axios = require('axios');

function printCharacter (characters, index) {
  axios.get(characters[index])
    .then(response => {
      console.log(response.data.name);
      if (index + 1 < characters.length) {
        printCharacter(characters, index + 1);
      }
    });
}

axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(response => {
    const characters = response.data.characters;
    printCharacter(characters, 0);
  })
  .catch(error => {
    console.log(error);
  });

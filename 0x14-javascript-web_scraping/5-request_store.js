#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
axios.get(process.argv[2])
  .then(response => {
    const content = response.data;
    fs.writeFile(process.argv[3], content, err => {
      if (err) {
        console.error(err);
      }
    });
  });

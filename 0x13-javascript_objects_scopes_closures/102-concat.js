#!/usr/bin/node
const fs = require('fs');
const contentFileA = fs.readFileSync(process.argv[2], 'utf-8');
const contentFileB = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFile(process.argv[4], contentFileA + contentFileB, err => {
  if (err) {
    console.log(err);
  }
});

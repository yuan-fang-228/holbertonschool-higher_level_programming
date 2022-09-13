#!/usr/bin/node
const axios = require('axios');
axios.get(process.argv[2])
  .then(response => {
    const todos = response.data;
    const dic = {};
    for (const todo of todos) {
      if (todo.completed) {
        if (dic[todo.userId] === undefined) {
          dic[todo.userId] = 1;
        } else {
          dic[todo.userId] = dic[todo.userId] + 1;
        }
      }
    }
    console.log(dic);
  })
  .catch(error => {
    console.log(error);
  });

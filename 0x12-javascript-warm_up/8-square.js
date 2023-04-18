#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(argv[2]); i++) {
    let str = '';
    for (let j = 0; j < Number(argv[2]); j++) {
      str = str + 'X';
    }
    console.log(str);
  }
}

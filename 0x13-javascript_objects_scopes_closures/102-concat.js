#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');
const file1 = argv[2];
const file2 = argv[3];
const dFile = argv[4];

const content1 = fs.readFileSync(file1, 'utf8');
const content2 = fs.readFileSync(file2, 'utf8');

const concat = content1 + content2;
fs.writeFileSync(dFile, concat, 'utf8');

#!/usr/bin/node

const nbOccurences = (list, searchElement) => list.filter((ls) => searchElement == ls).length;

module.exports = nbOccurences;

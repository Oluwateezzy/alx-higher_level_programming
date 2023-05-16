#!/usr/bin/node

const dict = {
  89: 1,
  90: 2,
  91: 1,
  92: 3,
  93: 1,
  94: 2
};
const newD = {};
for (user in dict) {
  if (dict[user] in newD) {
    newD[dict[user]].push(user);
  } else {
    newD[dict[user]] = [user];
  }
}
console.log(newD);

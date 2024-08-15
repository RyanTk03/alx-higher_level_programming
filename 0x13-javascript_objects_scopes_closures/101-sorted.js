#!/usr/bin/node

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const unique = [...new Set(vals)];
const newDict = {};
for (const i in unique) {
  const list = [];
  for (const j in totalist) {
    if (totalist[j][1] === unique[i]) {
      list.unshift(totalist[j][0]);
    }
  }
  newDict[unique[i]] = list;
}
console.log(newDict);

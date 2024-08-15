#!/usr/bin/node

const numbers = [];
const args = process.argv.slice(2);

for (const n of args) {
  numbers.push(parseInt(n));
}

if (numbers.length <= 1) {
  console.log('0');
}
console.log(numbers.sort()[numbers.length - 2]);

#!/usr/bin/node

const numbers = [];
const args = process.argv.slice(2);

for (const i in args) {
  numbers.push(parseInt(args[i]));
}

if (numbers.length <= 1) {
  console.log('0');
}
console.log(numbers.sort().reverse()[1]);

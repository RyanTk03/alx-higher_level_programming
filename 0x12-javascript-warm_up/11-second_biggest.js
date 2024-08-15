#!/usr/bin/node

const numbers = [];
for (let i in process.argv.slice(2)) {
  numbers.push(parseInt(process.argv[i + 2]));
}

if (numbers.length <= 1) {
  console.log('0');
}
console.log(numbers.sort().reverse()[1]);
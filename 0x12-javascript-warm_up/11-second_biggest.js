#!/usr/bin/node

const numbers = [];
for (let i in process.argv.slice(1)) {
  numbers.push(parseInt(process.argv[i + 1]);
}

if (numbers.length === 0 || numbers.length === 1) {
  console.log('0');
}
console.log(numbers.sort().reverse()[1]);

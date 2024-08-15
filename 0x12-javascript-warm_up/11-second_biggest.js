#!/usr/bin/node

const numbers = [];
const args = process.argv.slice(2);

args.forEach(function (a) {
  numbers.push(parseInt(a));
});

if (numbers.length <= 1) {
  console.log('0');
} else {
  const sorted = numbers.sort();
  
  console.log(sorted);
  console.log(sorted[sorted.length - 2]);
}

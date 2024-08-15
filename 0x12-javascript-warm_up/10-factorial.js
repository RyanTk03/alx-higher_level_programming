#!/usr/bin/node

function factorial(n) {
  if (!n && n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const n = parseInt(process.argv[1]);
const f = factorial(n);

console.log(f);

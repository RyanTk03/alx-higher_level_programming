#!/usr/bin/node

function add(a, b) {
  console.log(a + b);
}

const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

add(n1, n2);

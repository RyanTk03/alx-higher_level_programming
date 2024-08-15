#!/usr/bin/node

if (process.argv.length === 0) {
  console.log("No argument");
} else {
  console.log(`Argument${process.argv.length > 1 ? 's' : ''} found`);
}

#!/usr/bin/node

if (process.argv.length < 3) {
  console.log('No argument');
} else {
  console.log(`Argument${process.argv.length > 3 ? 's ' : ' '}found`);
}

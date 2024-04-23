#!/usr/bin/node

let x = 0;
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  x = Number(process.argv[2]);
}

for (let i = 0; i < x; i++) {
  console.log('C is fun');
}

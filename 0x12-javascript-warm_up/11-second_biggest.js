#!/usr/bin/node

function findSecondLargest (numbers) {
  numbers.sort((a, b) => b - a);
  if (numbers.lenght < 2) {
    return 0;
  }
  const secondLargest = numbers[1];
  console.log(secondLargest);
}
const args = process.argv.slice(2).map(Number);
if (args.length <= 2) {
  console.log(0);
} else {
  findSecondLargest(args);
}

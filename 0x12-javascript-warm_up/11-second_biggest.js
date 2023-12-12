#!/usr/bin/node
// Convert arguments into an array
let args = process.argv.slice(2);

// Convert all arguments to integers
let numbers = args.map(Number);

// Sort the array in descending order
numbers.sort((a, b) => b - a);

// Find the second largest number
if (numbers.length < 2 || numbers[0] === numbers[1]) {
   console.log(0);
} else {
   console.log(numbers[1]);
}

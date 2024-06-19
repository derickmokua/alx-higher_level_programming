#!/usr/bin/node
/**
 * Script that imports an array from a module and computes a new array.
 * The new array contains the product of each element in the original array
 * and its index.
 */
const list = require('./100-data.js').list;

const newList = list.map((val, idx) => val * idx);
console.log(list);
console.log(newList);

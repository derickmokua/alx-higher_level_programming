#!/usr/bin/node
// Script that concatenates the contents of two files and writes the result to a third file.

const args = process.argv.slice(2);
const fs = require('fs');
const first = fs.readFileSync('./' + args[0]);
const second = fs.readFileSync('./' + args[1]);
fs.writeFileSync('./' + args[2], first + second);

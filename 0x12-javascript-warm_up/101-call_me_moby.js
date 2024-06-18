#!/usr/bin/node
/**
 * Exports a function named 'callMeMoby' that accepts two arguments:
 *   - 'x': A number representing how many times to call the callback function.
 *   - 'theFunction': A callback function to be executed 'x' times.
 *
 * The 'callMeMoby' function runs a loop 'x' times, and in each iteration,
 * it calls 'theFunction'.
 *
 * @param {number} x - The number of times to call the callback function.
 * @param {function} theFunction - The callback function to execute 'x' times.
 */
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};

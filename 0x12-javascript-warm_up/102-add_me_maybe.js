#!/usr/bin/node
/**
 * Exports a function named 'addMeMaybe' that accepts two arguments:
 *   - 'number': A number to be incremented.
 *   - 'theFunction': A callback function to be called with the incremented number.
 *
 * The 'addMeMaybe' function increments the 'number' argument by 1,
 * then calls 'theFunction' with the incremented value.
 *
 * @param {number} number - The number to increment.
 * @param {function} theFunction - The callback function to execute with the incremented number.
 */
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};

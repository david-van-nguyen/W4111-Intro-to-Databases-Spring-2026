Source URL: https://www.mongodb.com/docs/manual/reference/mql/expressions.md
Title: Expressions

# Expressions

Expressions are MQL (MongoDB Query Language) components that resolve to a value. Expressions are stateless, meaning they return a value without mutating any of the values used to build the expression. You can use expressions in the following MQL contexts:

- Some aggregation pipeline stages, such as [`$project`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/project/#mongodb-pipeline-pipe.-project), [`$addFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields), and [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group)

- [Query predicates](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-query-predicate) that use [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr)

- Find command [projections](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/tutorial/project-fields-from-query-results/#std-label-read-operations-projection)

In the MongoDB Query Language, you can build expressions from the following components:

<table>
<tr>
<th id="Component">
Component

</th>
<th id="Example">
Example

</th>
</tr>
<tr>
<td headers="Component">
Constants

</td>
<td headers="Example">
`3`

</td>
</tr>
<tr>
<td headers="Component">
Operators

</td>
<td headers="Example">
[`$add`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/add/#mongodb-expression-exp.-add)

</td>
</tr>
<tr>
<td headers="Component">
Field path expressions

</td>
<td headers="Example">
`"$<path.to.field>"`

</td>
</tr>
</table>For example, `{ $add: [ 3, "$inventory.total" ] }` is an expression that consists of the `$add` operator and two operands:

- The constant `3`

- The [field path expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/aggregation-pipeline/#std-label-agg-quick-ref-field-paths)
  `"$inventory.total"`

The expression returns the result of adding 3 to the value at path `inventory.total` of the input document.

Expression operators are similar to functions that take arguments. In general, these operators take an array of arguments and have the following form:

```javascript
{ <operator>: [ <argument1>, <argument2> ... ] }
```

If an operator accepts a single argument, you can omit the outer array designating the argument list:

```javascript
{ <operator>: <argument> }
```

This page lists operators that you can use to construct [expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-expression).

## Arithmetic Operators

Arithmetic expressions perform mathematic operations on numbers. Some arithmetic expressions can also support date arithmetic.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$abs`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/abs/#mongodb-expression-exp.-abs)

</td>
<td headers="Description">
Returns the absolute value of a number.

</td>
</tr>
<tr>
<td headers="Name">
[`$add`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/add/#mongodb-expression-exp.-add)

</td>
<td headers="Description">
Adds numbers to return the sum, or adds numbers and a date to return a new date. If adding numbers and a date, treats the numbers as milliseconds. Accepts any number of argument expressions, but at most, one expression can resolve to a date.

</td>
</tr>
<tr>
<td headers="Name">
[`$ceil`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/ceil/#mongodb-expression-exp.-ceil)

</td>
<td headers="Description">
Returns the smallest integer greater than or equal to the specified number.

</td>
</tr>
<tr>
<td headers="Name">
[`$divide`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/divide/#mongodb-expression-exp.-divide)

</td>
<td headers="Description">
Returns the result of dividing the first number by the second. Accepts two argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$exp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/exp/#mongodb-expression-exp.-exp)

</td>
<td headers="Description">
Raises *e* to the specified exponent.

</td>
</tr>
<tr>
<td headers="Name">
[`$floor`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/floor/#mongodb-expression-exp.-floor)

</td>
<td headers="Description">
Returns the largest integer less than or equal to the specified number.

</td>
</tr>
<tr>
<td headers="Name">
[`$ln`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/ln/#mongodb-expression-exp.-ln)

</td>
<td headers="Description">
Calculates the natural log of a number.

</td>
</tr>
<tr>
<td headers="Name">
[`$log`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/log/#mongodb-expression-exp.-log)

</td>
<td headers="Description">
Calculates the log of a number in the specified base.

</td>
</tr>
<tr>
<td headers="Name">
[`$log10`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/log10/#mongodb-expression-exp.-log10)

</td>
<td headers="Description">
Calculates the log base 10 of a number.

</td>
</tr>
<tr>
<td headers="Name">
[`$mod`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/mod/#mongodb-expression-exp.-mod)

</td>
<td headers="Description">
Returns the remainder of the first number divided by the second. Accepts two argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$multiply`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/multiply/#mongodb-expression-exp.-multiply)

</td>
<td headers="Description">
Multiplies numbers to return the product. Accepts any number of argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$pow`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/pow/#mongodb-expression-exp.-pow)

</td>
<td headers="Description">
Raises a number to the specified exponent.

</td>
</tr>
<tr>
<td headers="Name">
[`$round`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/round/#mongodb-expression-exp.-round)

</td>
<td headers="Description">
Rounds a number to to a whole integer *or* to a specified decimal place.

</td>
</tr>
<tr>
<td headers="Name">
[`$sigmoid`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sigmoid/#mongodb-expression-exp.-sigmoid)

</td>
<td headers="Description">
Returns the result of the sigmoid function (the integration of the normal distribution with standard deviation 1).

</td>
</tr>
<tr>
<td headers="Name">
[`$sqrt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sqrt/#mongodb-expression-exp.-sqrt)

</td>
<td headers="Description">
Calculates the square root.

</td>
</tr>
<tr>
<td headers="Name">
[`$subtract`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/subtract/#mongodb-expression-exp.-subtract)

</td>
<td headers="Description">
Returns the result of subtracting the second value from the first. If the two values are numbers, return the difference. If the two values are dates, return the difference in milliseconds. If the two values are a date and a number in milliseconds, return the resulting date. Accepts two argument expressions. If the two values are a date and a number, specify the date argument first as it is not meaningful to subtract a date from a number.

</td>
</tr>
<tr>
<td headers="Name">
[`$trunc`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/trunc/#mongodb-expression-exp.-trunc)

</td>
<td headers="Description">
Truncates a number to a whole integer *or* to a specified decimal place.

</td>
</tr>
</table>

## Array Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$arrayElemAt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/arrayElemAt/#mongodb-expression-exp.-arrayElemAt)

</td>
<td headers="Description">
Returns the element at the specified array index.

</td>
</tr>
<tr>
<td headers="Name">
[`$arrayToObject`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/arrayToObject/#mongodb-expression-exp.-arrayToObject)

</td>
<td headers="Description">
Converts an array of key value pairs to a document.

</td>
</tr>
<tr>
<td headers="Name">
[`$concatArrays`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concatArrays/#mongodb-expression-exp.-concatArrays)

</td>
<td headers="Description">
Concatenates arrays to return the concatenated array.

</td>
</tr>
<tr>
<td headers="Name">
[`$filter`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/filter/#mongodb-expression-exp.-filter)

</td>
<td headers="Description">
Selects a subset of the array to return an array with only the elements that match the filter condition.

</td>
</tr>
<tr>
<td headers="Name">
[`$firstN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/firstN/#mongodb-expression-exp.-firstN)

</td>
<td headers="Description">
Returns a specified number of elements from the beginning of an array. Distinct from the [`$firstN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/firstN/#mongodb-group-grp.-firstN) accumulator.

</td>
</tr>
<tr>
<td headers="Name">
[`$in`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/in/#mongodb-expression-exp.-in)

</td>
<td headers="Description">
Returns a boolean indicating whether a specified value is in an array.

</td>
</tr>
<tr>
<td headers="Name">
[`$indexOfArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/indexOfArray/#mongodb-expression-exp.-indexOfArray)

</td>
<td headers="Description">
Searches an array for an occurrence of a specified value and returns the array index of the first occurrence. Array indexes start at zero.

</td>
</tr>
<tr>
<td headers="Name">
[`$isArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/isArray/#mongodb-expression-exp.-isArray)

</td>
<td headers="Description">
Determines if the operand is an array. Returns a boolean.

</td>
</tr>
<tr>
<td headers="Name">
[`$lastN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lastN/#mongodb-expression-exp.-lastN)

</td>
<td headers="Description">
Returns a specified number of elements from the end of an array. Distinct from the [`$lastN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lastN/#mongodb-group-grp.-lastN) accumulator.

</td>
</tr>
<tr>
<td headers="Name">
[`$map`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/map/#mongodb-expression-exp.-map)

</td>
<td headers="Description">
Applies a subexpression to each element of an array and returns the array of resulting values in order. Accepts named parameters.

</td>
</tr>
<tr>
<td headers="Name">
[`$maxN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/maxN-array-element/#mongodb-expression-exp.-maxN)

</td>
<td headers="Description">
Returns the `n` largest values in an array. Distinct from the [`$maxN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/maxN/#mongodb-group-grp.-maxN) accumulator.

</td>
</tr>
<tr>
<td headers="Name">
[`$minN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/minN-array-element/#mongodb-expression-exp.-minN)

</td>
<td headers="Description">
Returns the `n` smallest values in an array. Distinct from the [`$minN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/minN/#mongodb-group-grp.-minN) accumulator.

</td>
</tr>
<tr>
<td headers="Name">
[`$objectToArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/objectToArray/#mongodb-expression-exp.-objectToArray)

</td>
<td headers="Description">
Converts a document to an array of documents representing key-value pairs.

</td>
</tr>
<tr>
<td headers="Name">
[`$range`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/range/#mongodb-expression-exp.-range)

</td>
<td headers="Description">
Outputs an array containing a sequence of integers according to user-defined inputs.

</td>
</tr>
<tr>
<td headers="Name">
[`$reduce`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/reduce/#mongodb-expression-exp.-reduce)

</td>
<td headers="Description">
Applies an expression to each element in an array and combines them into a single value.

</td>
</tr>
<tr>
<td headers="Name">
[`$reverseArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/reverseArray/#mongodb-expression-exp.-reverseArray)

</td>
<td headers="Description">
Returns an array with the elements in reverse order.

</td>
</tr>
<tr>
<td headers="Name">
[`$size`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/size/#mongodb-expression-exp.-size)

</td>
<td headers="Description">
Returns the number of elements in the array. Accepts a single expression as argument.

</td>
</tr>
<tr>
<td headers="Name">
[`$slice`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/slice/#mongodb-expression-exp.-slice)

</td>
<td headers="Description">
Returns a subset of an array.

</td>
</tr>
<tr>
<td headers="Name">
[`$sortArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sortArray/#mongodb-expression-exp.-sortArray)

</td>
<td headers="Description">
Sorts the elements of an array.

</td>
</tr>
<tr>
<td headers="Name">
[`$zip`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/zip/#mongodb-expression-exp.-zip)

</td>
<td headers="Description">
Merge two arrays together.

</td>
</tr>
</table>

## Bitwise Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$bitAnd`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bitAnd/#mongodb-expression-exp.-bitAnd)

</td>
<td headers="Description">
Returns the result of a bitwise `and` operation on an array of `int` or `long` values.

</td>
</tr>
<tr>
<td headers="Name">
[`$bitNot`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bitNot/#mongodb-expression-exp.-bitNot)

</td>
<td headers="Description">
Returns the result of a bitwise `not` operation on a single argument or an array that contains a single `int` or `long` value.

</td>
</tr>
<tr>
<td headers="Name">
[`$bitOr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bitOr/#mongodb-expression-exp.-bitOr)

</td>
<td headers="Description">
Returns the result of a bitwise `or` operation on an array of `int` or `long` values.

</td>
</tr>
<tr>
<td headers="Name">
[`$bitXor`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bitXor/#mongodb-expression-exp.-bitXor)

</td>
<td headers="Description">
Returns the result of a bitwise `xor` (exclusive or) operation on an array of `int` and `long` values.

</td>
</tr>
</table>

## Boolean Operators

Boolean expressions evaluate their argument expressions as booleans and return a boolean as the result.

In addition to the `false` boolean value, Boolean expression evaluates as `false` the following: `null`, `0`, and `undefined` values. The Boolean expression evaluates all other values as `true`, including non-zero numeric values and arrays.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$and`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/and/#mongodb-expression-exp.-and)

</td>
<td headers="Description">
Returns `true` only when *all* its expressions evaluate to `true`. Accepts any number of argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$not`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/not/#mongodb-expression-exp.-not)

</td>
<td headers="Description">
Returns the boolean value that is the opposite of its argument expression. Accepts a single argument expression.

</td>
</tr>
<tr>
<td headers="Name">
[`$or`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/or/#mongodb-expression-exp.-or)

</td>
<td headers="Description">
Returns `true` when *any* of its expressions evaluates to `true`. Accepts any number of argument expressions.

</td>
</tr>
</table>

## Comparison Operators

Comparison expressions return a boolean except for [`$cmp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/cmp/#mongodb-expression-exp.-cmp) which returns a number.

The comparison expressions take two argument expressions and compare both value and type, using the [specified BSON comparison order](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/bson-type-comparison-order/#std-label-bson-types-comparison-order) for values of different types.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$cmp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/cmp/#mongodb-expression-exp.-cmp)

</td>
<td headers="Description">
Returns `0` if the two values are equivalent, `1` if the first value is greater than the second, and `-1` if the first value is less than the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$eq`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/eq/#mongodb-expression-exp.-eq)

</td>
<td headers="Description">
Returns `true` if the values are equivalent.

</td>
</tr>
<tr>
<td headers="Name">
[`$gt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gt/#mongodb-expression-exp.-gt)

</td>
<td headers="Description">
Returns `true` if the first value is greater than the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$gte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gte/#mongodb-expression-exp.-gte)

</td>
<td headers="Description">
Returns `true` if the first value is greater than or equal to the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$lt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lt/#mongodb-expression-exp.-lt)

</td>
<td headers="Description">
Returns `true` if the first value is less than the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$lte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte)

</td>
<td headers="Description">
Returns `true` if the first value is less than or equal to the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$ne`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/ne/#mongodb-expression-exp.-ne)

</td>
<td headers="Description">
Returns `true` if the values are *not* equivalent.

</td>
</tr>
</table>

## Conditional Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$cond`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/cond/#mongodb-expression-exp.-cond)

</td>
<td headers="Description">
A ternary operator that evaluates one expression, and depending on the result, returns the value of one of the other two expressions. Accepts either three expressions in an ordered list or three named parameters.

</td>
</tr>
<tr>
<td headers="Name">
[`$ifNull`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/ifNull/#mongodb-expression-exp.-ifNull)

</td>
<td headers="Description">
Returns either the non-null result of the first expression or the result of the second expression if the first expression results in a null result. Null result encompasses instances of undefined values or missing fields. Accepts two expressions as arguments. The result of the second expression can be null.

</td>
</tr>
<tr>
<td headers="Name">
[`$switch`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/switch/#mongodb-expression-exp.-switch)

</td>
<td headers="Description">
Evaluates a series of case expressions. When it finds an expression which evaluates to `true`, `$switch` executes a specified expression and breaks out of the control flow.

</td>
</tr>
</table>

## Custom Aggregation Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$accumulator`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/accumulator/#mongodb-group-grp.-accumulator)

</td>
<td headers="Description">
Defines a custom accumulator function.

</td>
</tr>
<tr>
<td headers="Name">
[`$function`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/function/#mongodb-expression-exp.-function)

</td>
<td headers="Description">
Defines a custom function.

</td>
</tr>
</table>

## Data Size Operators

The following operators return the size of a data element:

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$binarySize`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/binarySize/#mongodb-expression-exp.-binarySize)

</td>
<td headers="Description">
Returns the size of a given string or binary data value's content in bytes.

</td>
</tr>
<tr>
<td headers="Name">
[`$bsonSize`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bsonSize/#mongodb-expression-exp.-bsonSize)

</td>
<td headers="Description">
Returns the size in bytes of a given document (i.e. bsontype `Object`) when encoded as [BSON](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-BSON).

</td>
</tr>
</table>

## Date Operators

The following operators returns date objects or components of a date object:

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$dateAdd`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateAdd/#mongodb-expression-exp.-dateAdd)

</td>
<td headers="Description">
Adds a number of time units to a date object.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateDiff`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateDiff/#mongodb-expression-exp.-dateDiff)

</td>
<td headers="Description">
Returns the difference between two dates.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateFromParts`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateFromParts/#mongodb-expression-exp.-dateFromParts)

</td>
<td headers="Description">
Constructs a BSON Date object given the date's constituent parts.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateFromString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateFromString/#mongodb-expression-exp.-dateFromString)

</td>
<td headers="Description">
Converts a date/time string to a date object.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateSubtract`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateSubtract/#mongodb-expression-exp.-dateSubtract)

</td>
<td headers="Description">
Subtracts a number of time units from a date object.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateToParts`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateToParts/#mongodb-expression-exp.-dateToParts)

</td>
<td headers="Description">
Returns a document containing the constituent parts of a date.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateToString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateToString/#mongodb-expression-exp.-dateToString)

</td>
<td headers="Description">
Returns the date as a formatted string.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateTrunc`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateTrunc/#mongodb-expression-exp.-dateTrunc)

</td>
<td headers="Description">
Truncates a date.

</td>
</tr>
<tr>
<td headers="Name">
[`$dayOfMonth`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dayOfMonth/#mongodb-expression-exp.-dayOfMonth)

</td>
<td headers="Description">
Returns the day of the month for a date as a number between 1 and 31.

</td>
</tr>
<tr>
<td headers="Name">
[`$dayOfWeek`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dayOfWeek/#mongodb-expression-exp.-dayOfWeek)

</td>
<td headers="Description">
Returns the day of the week for a date as a number between 1 (Sunday) and 7 (Saturday).

</td>
</tr>
<tr>
<td headers="Name">
[`$dayOfYear`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dayOfYear/#mongodb-expression-exp.-dayOfYear)

</td>
<td headers="Description">
Returns the day of the year for a date as a number between 1 and 366 (leap year).

</td>
</tr>
<tr>
<td headers="Name">
[`$hour`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/hour/#mongodb-expression-exp.-hour)

</td>
<td headers="Description">
Returns the hour for a date as a number between 0 and 23.

</td>
</tr>
<tr>
<td headers="Name">
[`$isoDayOfWeek`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/isoDayOfWeek/#mongodb-expression-exp.-isoDayOfWeek)

</td>
<td headers="Description">
Returns the weekday number in ISO 8601 format, ranging from `1` (for Monday) to `7` (for Sunday).

</td>
</tr>
<tr>
<td headers="Name">
[`$isoWeek`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/isoWeek/#mongodb-expression-exp.-isoWeek)

</td>
<td headers="Description">
Returns the week number in ISO 8601 format, ranging from `1` to `53`. Week numbers start at `1` with the week (Monday through Sunday) that contains the year's first Thursday.

</td>
</tr>
<tr>
<td headers="Name">
[`$isoWeekYear`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/isoWeekYear/#mongodb-expression-exp.-isoWeekYear)

</td>
<td headers="Description">
Returns the year number in ISO 8601 format. The year starts with the Monday of week 1 (ISO 8601) and ends with the Sunday of the last week (ISO 8601).

</td>
</tr>
<tr>
<td headers="Name">
[`$millisecond`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/millisecond/#mongodb-expression-exp.-millisecond)

</td>
<td headers="Description">
Returns the milliseconds of a date as a number between 0 and 999.

</td>
</tr>
<tr>
<td headers="Name">
[`$minute`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/minute/#mongodb-expression-exp.-minute)

</td>
<td headers="Description">
Returns the minute for a date as a number between 0 and 59.

</td>
</tr>
<tr>
<td headers="Name">
[`$month`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/month/#mongodb-expression-exp.-month)

</td>
<td headers="Description">
Returns the month for a date as a number between 1 (January) and 12 (December).

</td>
</tr>
<tr>
<td headers="Name">
[`$second`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/second/#mongodb-expression-exp.-second)

</td>
<td headers="Description">
Returns the seconds for a date as a number between 0 and 60 (leap seconds).

</td>
</tr>
<tr>
<td headers="Name">
[`$toDate`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toDate/#mongodb-expression-exp.-toDate)

</td>
<td headers="Description">
Converts value to a Date.

</td>
</tr>
<tr>
<td headers="Name">
[`$week`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/week/#mongodb-expression-exp.-week)

</td>
<td headers="Description">
Returns the week number for a date as a number between 0 (the partial week that precedes the first Sunday of the year) and 53 (leap year).

</td>
</tr>
<tr>
<td headers="Name">
[`$year`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/year/#mongodb-expression-exp.-year)

</td>
<td headers="Description">
Returns the year for a date as a number (e.g. 2014).

</td>
</tr>
</table>The following arithmetic operators can take date operands:

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$add`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/add/#mongodb-expression-exp.-add)

</td>
<td headers="Description">
Adds numbers and a date to return a new date. If adding numbers and a date, treats the numbers as milliseconds. Accepts any number of argument expressions, but at most, one expression can resolve to a date.

</td>
</tr>
<tr>
<td headers="Name">
[`$subtract`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/subtract/#mongodb-expression-exp.-subtract)

</td>
<td headers="Description">
Returns the result of subtracting the second value from the first. If the two values are dates, return the difference in milliseconds. If the two values are a date and a number in milliseconds, return the resulting date. Accepts two argument expressions. If the two values are a date and a number, specify the date argument first as it is not meaningful to subtract a date from a number.

</td>
</tr>
</table>

## Expressions Associated with Accumulators

Some accumulators for the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage are also available for use as expressions. When used as expressions, they calculate an aggregate value over the given input arguments or input array.

The following operators are accumulators, but they are also available as expressions which accept an array of values as input.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$avg`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/avg/#mongodb-group-grp.-avg)

</td>
<td headers="Description">
Returns an average of the specified expression or list of expressions for each document. Ignores non-numeric values.

</td>
</tr>
<tr>
<td headers="Name">
[`$concatArrays`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concatArrays/#mongodb-group-grp.-concatArrays)

</td>
<td headers="Description">
Returns a single array that combines the elements of two or more arrays.

</td>
</tr>
<tr>
<td headers="Name">
[`$first`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/first/#mongodb-group-grp.-first)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the first document in a group.

</td>
</tr>
<tr>
<td headers="Name">
[`$last`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/last/#mongodb-group-grp.-last)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the last document in a group.

</td>
</tr>
<tr>
<td headers="Name">
[`$max`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/max/#mongodb-group-grp.-max)

</td>
<td headers="Description">
Returns the maximum of the specified expression or list of expressions for each document

</td>
</tr>
<tr>
<td headers="Name">
[`$median`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/median/#mongodb-group-grp.-median)

</td>
<td headers="Description">
Returns an approximation of the [median](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-median), the 50th [percentile](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-percentile), as a scalar value.

</td>
</tr>
<tr>
<td headers="Name">
[`$min`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/min/#mongodb-group-grp.-min)

</td>
<td headers="Description">
Returns the minimum of the specified expression or list of expressions for each document

</td>
</tr>
<tr>
<td headers="Name">
[`$percentile`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/percentile/#mongodb-group-grp.-percentile)

</td>
<td headers="Description">
Returns an array of scalar values that correspond to specified [percentile](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-percentile) values.

</td>
</tr>
<tr>
<td headers="Name">
[`$setUnion`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setUnion/#mongodb-group-grp.-setUnion)

</td>
<td headers="Description">
Takes two or more arrays and returns an array containing the elements that appear in any input array.

</td>
</tr>
<tr>
<td headers="Name">
[`$stdDevPop`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/stdDevPop/#mongodb-group-grp.-stdDevPop)

</td>
<td headers="Description">
Returns the population standard deviation of the input values.

</td>
</tr>
<tr>
<td headers="Name">
[`$stdDevSamp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/stdDevSamp/#mongodb-group-grp.-stdDevSamp)

</td>
<td headers="Description">
Returns the sample standard deviation of the input values.

</td>
</tr>
<tr>
<td headers="Name">
[`$sum`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sum/#mongodb-group-grp.-sum)

</td>
<td headers="Description">
Returns a sum of numerical values. Ignores non-numeric values.

</td>
</tr>
</table>

## Literal Expression Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$literal`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/literal/#mongodb-expression-exp.-literal)

</td>
<td headers="Description">
Return a value without parsing. Use for values that the aggregation pipeline may interpret as an expression. For example, use a [`$literal`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/literal/#mongodb-expression-exp.-literal) expression to a string that starts with a  dollar sign (`$`) to avoid parsing as a field path.

</td>
</tr>
</table>

## Miscellaneous Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$getField`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/getField/#mongodb-expression-exp.-getField)

</td>
<td headers="Description">
Returns the value of a specified field from a document. You can use [`$getField`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/getField/#mongodb-expression-exp.-getField) to retrieve the value of fields with names that contain periods (`.`) or start with dollar signs (`$`).

</td>
</tr>
<tr>
<td headers="Name">
[`$rand`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/rand/#mongodb-expression-exp.-rand)

</td>
<td headers="Description">
Returns a random float between 0 and 1

</td>
</tr>
<tr>
<td headers="Name">
[`$sampleRate`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sampleRate/#mongodb-expression-exp.-sampleRate)

</td>
<td headers="Description">
Randomly select documents at a given rate. Although the exact number of documents selected varies on each run, the quantity chosen approximates the sample rate expressed as a percentage of the total number of documents.

</td>
</tr>
<tr>
<td headers="Name">
[`$toHashedIndexKey`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toHashedIndexKey/#mongodb-expression-exp.-toHashedIndexKey)

</td>
<td headers="Description">
Computes and returns the hash of the input expression using the same hash function that MongoDB uses to create a hashed index.

</td>
</tr>
</table>

## Object Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$mergeObjects`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/mergeObjects/#mongodb-expression-exp.-mergeObjects)

</td>
<td headers="Description">
Combines multiple documents into a single document.

</td>
</tr>
<tr>
<td headers="Name">
[`$objectToArray`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/objectToArray/#mongodb-expression-exp.-objectToArray)

</td>
<td headers="Description">
Converts a document to an array of documents representing key-value pairs.

</td>
</tr>
<tr>
<td headers="Name">
[`$setField`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setField/#mongodb-expression-exp.-setField)

</td>
<td headers="Description">
Adds, updates, or removes a specified field in a document. You can use [`$setField`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setField/#mongodb-expression-exp.-setField) to add, update, or remove fields with names that contain periods (`.`) or start with dollar signs (`$`).

</td>
</tr>
</table>

## Set Operators

Set expressions performs set operation on arrays, treating arrays as sets. Set expressions ignores the duplicate entries in each input array and the order of the elements.

If the set operation returns a set, the operation filters out duplicates in the result to output an array that contains only unique entries. The order of the elements in the output array is unspecified.

If a set contains a nested array element, the set expression does *not* descend into the nested array but evaluates the array at top-level.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$allElementsTrue`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/allElementsTrue/#mongodb-expression-exp.-allElementsTrue)

</td>
<td headers="Description">
Returns `true` if *no* element of a set evaluates to `false`, otherwise, returns `false`. Accepts a single argument expression.

</td>
</tr>
<tr>
<td headers="Name">
[`$anyElementTrue`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/anyElementTrue/#mongodb-expression-exp.-anyElementTrue)

</td>
<td headers="Description">
Returns `true` if *any* elements of a set evaluate to `true`; otherwise, returns `false`. Accepts a single argument expression.

</td>
</tr>
<tr>
<td headers="Name">
[`$setDifference`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setDifference/#mongodb-expression-exp.-setDifference)

</td>
<td headers="Description">
Returns a set with elements that appear in the first set but not in the second set; i.e. performs a [relative complement](http://en.wikipedia.org/wiki/Complement_(set_theory)) of the second set relative to the first. Accepts exactly two argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$setEquals`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setEquals/#mongodb-expression-exp.-setEquals)

</td>
<td headers="Description">
Returns `true` if the input sets have the same distinct elements. Accepts two or more argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$setIntersection`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setIntersection/#mongodb-expression-exp.-setIntersection)

</td>
<td headers="Description">
Returns a set with elements that appear in *all* of the input sets. Accepts any number of argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$setIsSubset`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setIsSubset/#mongodb-expression-exp.-setIsSubset)

</td>
<td headers="Description">
Returns `true` if all elements of the first set appear in the second set, including when the first set equals the second set; i.e. not a [strict subset](http://en.wikipedia.org/wiki/Subset). Accepts exactly two argument expressions.

</td>
</tr>
<tr>
<td headers="Name">
[`$setUnion`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setUnion/#mongodb-expression-exp.-setUnion)

</td>
<td headers="Description">
Returns a set with elements that appear in *any* of the input sets.

</td>
</tr>
</table>

## String Operators

String expressions, with the exception of [`$concat`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concat/#mongodb-expression-exp.-concat), only haveString expressions, with the exception of [`$concat`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concat/#mongodb-expression-exp.-concat), only have a well-defined behavior for strings of ASCII characters.

[`$concat`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concat/#mongodb-expression-exp.-concat) behavior is well-defined regardless of the characters used.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$concat`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concat/#mongodb-expression-exp.-concat)

</td>
<td headers="Description">
Concatenates any number of strings.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateFromString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateFromString/#mongodb-expression-exp.-dateFromString)

</td>
<td headers="Description">
Converts a date/time string to a date object.

</td>
</tr>
<tr>
<td headers="Name">
[`$dateToString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/dateToString/#mongodb-expression-exp.-dateToString)

</td>
<td headers="Description">
Returns the date as a formatted string.

</td>
</tr>
<tr>
<td headers="Name">
[`$indexOfBytes`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/indexOfBytes/#mongodb-expression-exp.-indexOfBytes)

</td>
<td headers="Description">
Searches a string for an occurrence of a substring and returns the UTF-8 byte index of the first occurrence. If the substring is not found, returns `-1`.

</td>
</tr>
<tr>
<td headers="Name">
[`$indexOfCP`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/indexOfCP/#mongodb-expression-exp.-indexOfCP)

</td>
<td headers="Description">
Searches a string for an occurrence of a substring and returns the UTF-8 code point index of the first occurrence. If the substring is not found, returns `-1`

</td>
</tr>
<tr>
<td headers="Name">
[`$ltrim`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/ltrim/#mongodb-expression-exp.-ltrim)

</td>
<td headers="Description">
Removes whitespace or the specified characters from the beginning of a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$regexFind`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/regexFind/#mongodb-expression-exp.-regexFind)

</td>
<td headers="Description">
Applies a regular expression (regex) to a string and returns information on the *first* matched substring.

</td>
</tr>
<tr>
<td headers="Name">
[`$regexFindAll`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/regexFindAll/#mongodb-expression-exp.-regexFindAll)

</td>
<td headers="Description">
Applies a regular expression (regex) to a string and returns information on the all matched substrings.

</td>
</tr>
<tr>
<td headers="Name">
[`$regexMatch`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/regexMatch/#mongodb-expression-exp.-regexMatch)

</td>
<td headers="Description">
Applies a regular expression (regex) to a string and returns a boolean that indicates if a match is found or not.

</td>
</tr>
<tr>
<td headers="Name">
[`$replaceOne`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/replaceOne/#mongodb-expression-exp.-replaceOne)

</td>
<td headers="Description">
Replaces the first instance of a matched string in a given input.

</td>
</tr>
<tr>
<td headers="Name">
[`$replaceAll`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/replaceAll/#mongodb-expression-exp.-replaceAll)

</td>
<td headers="Description">
Replaces all instances of a matched string in a given input.

</td>
</tr>
<tr>
<td headers="Name">
[`$rtrim`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/rtrim/#mongodb-expression-exp.-rtrim)

</td>
<td headers="Description">
Removes whitespace or the specified characters from the end of a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$split`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/split/#mongodb-expression-exp.-split)

</td>
<td headers="Description">
Splits a string into substrings based on a delimiter. Returns an array of substrings. If the delimiter is not found within the string, returns an array containing the original string.

</td>
</tr>
<tr>
<td headers="Name">
[`$strLenBytes`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/strLenBytes/#mongodb-expression-exp.-strLenBytes)

</td>
<td headers="Description">
Returns the number of UTF-8 encoded bytes in a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$strLenCP`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/strLenCP/#mongodb-expression-exp.-strLenCP)

</td>
<td headers="Description">
Returns the number of UTF-8 [code points](http://www.unicode.org/glossary/#code_point) in a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$strcasecmp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/strcasecmp/#mongodb-expression-exp.-strcasecmp)

</td>
<td headers="Description">
Performs case-insensitive string comparison and returns: `0` if two strings are equivalent, `1` if the first string is greater than the second, and `-1` if the first string is less than the second.

</td>
</tr>
<tr>
<td headers="Name">
[`$substr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/substr/#mongodb-expression-exp.-substr)

</td>
<td headers="Description">
Deprecated. Use [`$substrBytes`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/substrBytes/#mongodb-expression-exp.-substrBytes) or [`$substrCP`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/substrCP/#mongodb-expression-exp.-substrCP).

</td>
</tr>
<tr>
<td headers="Name">
[`$substrBytes`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/substrBytes/#mongodb-expression-exp.-substrBytes)

</td>
<td headers="Description">
Returns the substring of a string. Starts with the character at the specified UTF-8 byte index (zero-based) in the string and continues for the specified number of bytes.

</td>
</tr>
<tr>
<td headers="Name">
[`$substrCP`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/substrCP/#mongodb-expression-exp.-substrCP)

</td>
<td headers="Description">
Returns the substring of a string. Starts with the character at the specified UTF-8 [code point (CP)](http://www.unicode.org/glossary/#code_point) index (zero-based) in the string and continues for the number of code points specified.

</td>
</tr>
<tr>
<td headers="Name">
[`$toLower`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toLower/#mongodb-expression-exp.-toLower)

</td>
<td headers="Description">
Converts a string to lowercase. Accepts a single argument expression.

</td>
</tr>
<tr>
<td headers="Name">
[`$toString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toString/#mongodb-expression-exp.-toString)

</td>
<td headers="Description">
Converts value to a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$trim`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/trim/#mongodb-expression-exp.-trim)

</td>
<td headers="Description">
Removes whitespace or the specified characters from the beginning and end of a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$toUpper`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toUpper/#mongodb-expression-exp.-toUpper)

</td>
<td headers="Description">
Converts a string to uppercase. Accepts a single argument expression.

</td>
</tr>
</table>
### Encrypted String Operators

Encrypted string expressions evaluate an argument against an encrypted field in a collection with [Queryable Encryption](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/queryable-encryption/#std-label-qe-manual-feature-qe) enabled, and return a boolean.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$encStrContains`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/encStrContains/#mongodb-expression-exp.-encStrContains)

</td>
<td headers="Description">
Returns `true` if a subset of characters in the encrypted string match the specified string.

</td>
</tr>
<tr>
<td headers="Name">
[`$encStrEndsWith`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/encStrEndsWith/#mongodb-expression-exp.-encStrEndsWith)

</td>
<td headers="Description">
Returns `true` if the last characters of the encrypted string match the specified string.

</td>
</tr>
<tr>
<td headers="Name">
[`$encStrNormalizedEq`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/encStrNormalizedEq/#mongodb-expression-exp.-encStrNormalizedEq)

</td>
<td headers="Description">
Returns `true` if the [normalized string](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-normalized-string) form of the encrypted string matches normalized string form of the specified string.

</td>
</tr>
<tr>
<td headers="Name">
[`$encStrStartsWith`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/encStrStartsWith/#mongodb-expression-exp.-encStrStartsWith)

</td>
<td headers="Description">
Returns `true` if the first characters of the encrypted string match the specified string.

</td>
</tr>
</table>

## Text Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$meta`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/meta/#mongodb-expression-exp.-meta)

</td>
<td headers="Description">
Access available per-document metadata related to the aggregation operation.

</td>
</tr>
</table>

## Timestamp Operators

Timestamp expression operators return values from a [timestamp](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/bson-types/#std-label-document-bson-type-timestamp).

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$tsIncrement`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/tsIncrement/#mongodb-expression-exp.-tsIncrement)

</td>
<td headers="Description">
Returns the incrementing ordinal from a [timestamp](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/bson-types/#std-label-document-bson-type-timestamp) as a [`long`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json-v1/#mongodb-bsontype-data_numberlong).

</td>
</tr>
<tr>
<td headers="Name">
[`$tsSecond`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/tsSecond/#mongodb-expression-exp.-tsSecond)

</td>
<td headers="Description">
Returns the seconds from a [timestamp](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/bson-types/#std-label-document-bson-type-timestamp) as a [`long`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json-v1/#mongodb-bsontype-data_numberlong).

</td>
</tr>
</table>

## Trigonometry Operators

Trigonometry expressions perform trigonometric operations on numbers. Values that represent angles are always input or output in  radians. Use [`$degreesToRadians`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/degreesToRadians/#mongodb-expression-exp.-degreesToRadians) and [`$radiansToDegrees`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/radiansToDegrees/#mongodb-expression-exp.-radiansToDegrees) to convert between degree and radian measurements.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$sin`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sin/#mongodb-expression-exp.-sin)

</td>
<td headers="Description">
Returns the sine of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$cos`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/cos/#mongodb-expression-exp.-cos)

</td>
<td headers="Description">
Returns the cosine of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$tan`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/tan/#mongodb-expression-exp.-tan)

</td>
<td headers="Description">
Returns the tangent of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$asin`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/asin/#mongodb-expression-exp.-asin)

</td>
<td headers="Description">
Returns the inverse sin (arc sine) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$acos`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/acos/#mongodb-expression-exp.-acos)

</td>
<td headers="Description">
Returns the inverse cosine (arc cosine) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$atan`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/atan/#mongodb-expression-exp.-atan)

</td>
<td headers="Description">
Returns the inverse tangent (arc tangent) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$atan2`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/atan2/#mongodb-expression-exp.-atan2)

</td>
<td headers="Description">
Returns the inverse tangent (arc tangent) of `y / x` in radians, where `y` and `x` are the first and second values passed to the expression respectively.

</td>
</tr>
<tr>
<td headers="Name">
[`$asinh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/asinh/#mongodb-expression-exp.-asinh)

</td>
<td headers="Description">
Returns the inverse hyperbolic sine (hyperbolic arc sine) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$acosh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/acosh/#mongodb-expression-exp.-acosh)

</td>
<td headers="Description">
Returns the inverse hyperbolic cosine (hyperbolic arc cosine) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$atanh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/atanh/#mongodb-expression-exp.-atanh)

</td>
<td headers="Description">
Returns the inverse hyperbolic tangent (hyperbolic arc tangent) of a value in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$sinh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sinh/#mongodb-expression-exp.-sinh)

</td>
<td headers="Description">
Returns the hyperbolic sine of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$cosh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/cosh/#mongodb-expression-exp.-cosh)

</td>
<td headers="Description">
Returns the hyperbolic cosine of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$tanh`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/tanh/#mongodb-expression-exp.-tanh)

</td>
<td headers="Description">
Returns the hyperbolic tangent of a value that is measured in radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$degreesToRadians`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/degreesToRadians/#mongodb-expression-exp.-degreesToRadians)

</td>
<td headers="Description">
Converts a value from degrees to radians.

</td>
</tr>
<tr>
<td headers="Name">
[`$radiansToDegrees`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/radiansToDegrees/#mongodb-expression-exp.-radiansToDegrees)

</td>
<td headers="Description">
Converts a value from radians to degrees.

</td>
</tr>
</table>

## Type Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$convert`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/convert/#mongodb-expression-exp.-convert)

</td>
<td headers="Description">
Converts a value to a specified type.

</td>
</tr>
<tr>
<td headers="Name">
[`$isNumber`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/isNumber/#mongodb-expression-exp.-isNumber)

</td>
<td headers="Description">
Returns boolean `true` if the specified expression resolves to an [`integer`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json/#mongodb-bsontype-Int32), [`decimal`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json/#mongodb-bsontype-Decimal128), [`double`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json/#mongodb-bsontype-Double), or [`long`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mongodb-extended-json/#mongodb-bsontype-Int64).

Returns boolean `false` if the expression resolves to any other [BSON type](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/bson-types/#std-label-bson-types), `null`, or a missing field.

</td>
</tr>
<tr>
<td headers="Name">
[`$toBool`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toBool/#mongodb-expression-exp.-toBool)

</td>
<td headers="Description">
Converts value to a boolean.

</td>
</tr>
<tr>
<td headers="Name">
[`$toDate`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toDate/#mongodb-expression-exp.-toDate)

</td>
<td headers="Description">
Converts value to a Date.

</td>
</tr>
<tr>
<td headers="Name">
[`$toDecimal`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toDecimal/#mongodb-expression-exp.-toDecimal)

</td>
<td headers="Description">
Converts value to a Decimal128.

</td>
</tr>
<tr>
<td headers="Name">
[`$toDouble`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toDouble/#mongodb-expression-exp.-toDouble)

</td>
<td headers="Description">
Converts value to a double.

</td>
</tr>
<tr>
<td headers="Name">
[`$toInt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toInt/#mongodb-expression-exp.-toInt)

</td>
<td headers="Description">
Converts value to an integer.

</td>
</tr>
<tr>
<td headers="Name">
[`$toLong`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toLong/#mongodb-expression-exp.-toLong)

</td>
<td headers="Description">
Converts value to a long.

</td>
</tr>
<tr>
<td headers="Name">
[`$toObjectId`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toObjectId/#mongodb-expression-exp.-toObjectId)

</td>
<td headers="Description">
Converts value to an ObjectId.

</td>
</tr>
<tr>
<td headers="Name">
[`$toString`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toString/#mongodb-expression-exp.-toString)

</td>
<td headers="Description">
Converts value to a string.

</td>
</tr>
<tr>
<td headers="Name">
[`$type`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/type/#mongodb-expression-exp.-type)

</td>
<td headers="Description">
Return the BSON data type of the field.

</td>
</tr>
<tr>
<td headers="Name">
[`$toUUID`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/toUUID/#mongodb-expression-exp.-toUUID)

</td>
<td headers="Description">
Converts a string to a UUID (Universally unique identifier).

</td>
</tr>
</table>

## Variable Operators

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$let`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/let/#mongodb-expression-exp.-let)

</td>
<td headers="Description">
Defines variables for use within the scope of a subexpression and returns the result of the subexpression. Accepts named parameters.

Accepts any number of argument expressions.

</td>
</tr>
</table>

## Window Operators

Window operators return values from a defined span of documents from a collection, known as a *window*. A [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window) is defined in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage, available starting in MongoDB 5.0.

The following window operators are available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

<table>
<tr>
<th id="Name">
Name

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Name">
[`$addToSet`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/addToSet/#mongodb-group-grp.-addToSet)

</td>
<td headers="Description">
Returns an array of all unique values that results from applying an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$avg`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/avg/#mongodb-group-grp.-avg)

</td>
<td headers="Description">
Returns the average for the specified [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions). Ignores non-numeric values.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$bottom`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bottom/#mongodb-group-grp.-bottom)

</td>
<td headers="Description">
Returns the bottom element within a group according to the specified sort order.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$bottomN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/bottomN/#mongodb-group-grp.-bottomN)

</td>
<td headers="Description">
Returns an aggregation of the bottom `n` fields within a group, according to the specified sort order.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count-accumulator/#mongodb-group-grp.-count)

</td>
<td headers="Description">
Returns the number of documents in the group or window.

Distinct from the [`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count/#mongodb-pipeline-pipe.-count) pipeline stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$covariancePop`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/covariancePop/#mongodb-group-grp.-covariancePop)

</td>
<td headers="Description">
Returns the population covariance of two numeric [expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$covarianceSamp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/covarianceSamp/#mongodb-group-grp.-covarianceSamp)

</td>
<td headers="Description">
Returns the sample covariance of two numeric [expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$denseRank`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/denseRank/#mongodb-group-grp.-denseRank)

</td>
<td headers="Description">
Returns the document position (known as the rank) relative to other documents in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage [partition](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-partitionBy). There are no gaps in the ranks. Ties receive the same rank.

</td>
</tr>
<tr>
<td headers="Name">
[`$derivative`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/derivative/#mongodb-group-grp.-derivative)

</td>
<td headers="Description">
Returns the average rate of change within the specified [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window).

</td>
</tr>
<tr>
<td headers="Name">
[`$documentNumber`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/documentNumber/#mongodb-group-grp.-documentNumber)

</td>
<td headers="Description">
Returns the position of a document (known as the document number) in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage [partition](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-partitionBy). Ties result in different adjacent document numbers.

</td>
</tr>
<tr>
<td headers="Name">
[`$expMovingAvg`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/expMovingAvg/#mongodb-group-grp.-expMovingAvg)

</td>
<td headers="Description">
Returns the exponential moving average for the numeric [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$first`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/first/#mongodb-group-grp.-first)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the first document in a group or [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window).

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$integral`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/integral/#mongodb-group-grp.-integral)

</td>
<td headers="Description">
Returns the approximation of the area under a curve.

</td>
</tr>
<tr>
<td headers="Name">
[`$last`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/last/#mongodb-group-grp.-last)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the last document in a group or [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window).

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$linearFill`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/linearFill/#mongodb-group-grp.-linearFill)

</td>
<td headers="Description">
Fills `null` and missing fields in a [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window) using [linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) based on surrounding field values.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$locf`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/locf/#mongodb-group-grp.-locf)

</td>
<td headers="Description">
Last observation carried forward. Sets values for `null` and missing fields in a [window](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-window) to the last non-null value for the field.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$max`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/max/#mongodb-group-grp.-max)

</td>
<td headers="Description">
Returns the maximum value that results from applying an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$min`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/min/#mongodb-group-grp.-min)

</td>
<td headers="Description">
Returns the minimum value that results from applying an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$minN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/minN/#mongodb-group-grp.-minN)

</td>
<td headers="Description">
Returns an aggregation of the `n` minimum valued elements in a group. Distinct from the [`$minN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/minN-array-element/#mongodb-expression-exp.-minN) array operator.

Available in [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group), [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) and as an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$push`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/push/#mongodb-group-grp.-push)

</td>
<td headers="Description">
Returns an array of values that result from applying an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$rank`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/rank/#mongodb-group-grp.-rank)

</td>
<td headers="Description">
Returns the document position (known as the rank) relative to other documents in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage [partition](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-partitionBy).

</td>
</tr>
<tr>
<td headers="Name">
[`$shift`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/shift/#mongodb-group-grp.-shift)

</td>
<td headers="Description">
Returns the value from an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) applied to a document in a specified position relative to the current document in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage [partition](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#std-label-setWindowFields-partitionBy).

</td>
</tr>
<tr>
<td headers="Name">
[`$stdDevPop`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/stdDevPop/#mongodb-group-grp.-stdDevPop)

</td>
<td headers="Description">
Returns the population standard deviation that results from applying a numeric [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$stdDevSamp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/stdDevSamp/#mongodb-group-grp.-stdDevSamp)

</td>
<td headers="Description">
Returns the sample standard deviation that results from applying a numeric [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$sum`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sum/#mongodb-group-grp.-sum)

</td>
<td headers="Description">
Returns the sum that results from applying a numeric [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) to each document.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$top`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/top/#mongodb-group-grp.-top)

</td>
<td headers="Description">
Returns the top element within a group according to the specified sort order.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$topN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/topN/#mongodb-group-grp.-topN)

</td>
<td headers="Description">
Returns an aggregation of the top `n` fields within a group, according to the specified sort order.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
</table>


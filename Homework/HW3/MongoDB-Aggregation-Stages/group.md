# $group (aggregation stage)

## Definition

`$group`
The $group stage combines multiple documents with the same field, fields, or expression into a single document according to a group key. The result is one document per unique group key.

A group key is often a field, or group of fields. The group key can also be the result of an expression. Use the `_id` field in the `$group` pipeline stage to set the group key. See below for [usage examples](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#std-label-ex-agg-group-stage).

In the `$group` stage output, the `_id` field is set to the group key for that document.

The output documents can also contain additional fields that are set using [accumulator expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#std-label-accumulators-group).

[`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) does *not* order its output documents.

## Compatibility

`$group`You can use `$group` for deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully managed service for MongoDB deployments in the cloud

- [MongoDB Enterprise](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-enterprise/#std-label-install-mdb-enterprise): The subscription-based, self-managed version of MongoDB

- [MongoDB Community](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-community/#std-label-install-mdb-community-edition): The source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage has the following prototype form:

```javascript
{
 $group:
   {
     _id: <expression>, // Group key
     <field1>: { <accumulator1> : <expression1> },
     ...
   }
 }
```

<table>
<tr>
<th id="Field">
Field

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Field">
`_id`

</td>
<td headers="Description">
*Required.* The `_id` expression specifies the group key. If you specify an `_id` value of null, or any other constant value, the `$group` stage returns a single document that aggregates values across all of the input documents. [See the Group by Null example](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#std-label-null-example).

</td>
</tr>
<tr>
<td headers="Field">
`field`

</td>
<td headers="Description">
*Optional.* Computed using the [accumulator operators](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#std-label-accumulators-group).

</td>
</tr>
</table>The `_id` and the [accumulator operators](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#std-label-accumulators-group) can accept any valid `expression`. For more information on expressions, see [Expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

## Considerations

### Performance

`$group``$group` is a blocking stage, which causes the pipeline to wait for all input data to be retrieved for the blocking stage before processing the data. A blocking stage may reduce performance because it reduces parallel processing for a pipeline with multiple stages. A blocking stage may also use substantial amounts of memory for large data sets.

### Accumulator Operator

The `<accumulator>` operator must be one of the following accumulator operators:

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
Returns the result of a user-defined accumulator function.

</td>
</tr>
<tr>
<td headers="Name">
[`$addToSet`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/addToSet/#mongodb-group-grp.-addToSet)

</td>
<td headers="Description">
Returns an array of *unique* expression values for each group. Order of the array elements is undefined.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$avg`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/avg/#mongodb-group-grp.-avg)

</td>
<td headers="Description">
Returns an average of numerical values. Ignores non-numeric values.

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
[`$concatArrays`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/concatArrays/#mongodb-group-grp.-concatArrays)

</td>
<td headers="Description">
Returns a single array that combines the elements of two or more arrays.

</td>
</tr>
<tr>
<td headers="Name">
[`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count-accumulator/#mongodb-group-grp.-count)

</td>
<td headers="Description">
Returns the number of documents in a group.

Distinct from the [`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count/#mongodb-pipeline-pipe.-count) pipeline stage.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$first`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/first/#mongodb-group-grp.-first)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the first document in a group.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$firstN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/firstN/#mongodb-group-grp.-firstN)

</td>
<td headers="Description">
Returns an aggregation of the first `n` elements within a group. Only meaningful when documents are in a defined order. Distinct from the [`$firstN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/firstN/#mongodb-expression-exp.-firstN) array operator.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group), [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$last`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/last/#mongodb-group-grp.-last)

</td>
<td headers="Description">
Returns the result of an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) for the last document in a group.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$lastN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lastN/#mongodb-group-grp.-lastN)

</td>
<td headers="Description">
Returns an aggregation of the last `n` elements within a group. Only meaningful when documents are in a defined order. Distinct from the [`$lastN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lastN/#mongodb-expression-exp.-lastN) array operator.

Available in the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group), [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions) and [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stages.

</td>
</tr>
<tr>
<td headers="Name">
[`$max`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/max/#mongodb-group-grp.-max)

</td>
<td headers="Description">
Returns the highest expression value for each group.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$maxN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/maxN/#mongodb-group-grp.-maxN)

</td>
<td headers="Description">
Returns an aggregation of the `n` maximum valued elements in a group. Distinct from the [`$maxN`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/maxN-array-element/#mongodb-expression-exp.-maxN) array operator.

Available in [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group), [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) and as an [expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$median`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/median/#mongodb-group-grp.-median)

</td>
<td headers="Description">
Returns an approximation of the [median](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-median), the 50th [percentile](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-percentile), as a scalar value.

This operator is available as an accumulator in these stages:

- [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group)

- [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields)

It is also available as an [aggregation expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$mergeObjects`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/mergeObjects/#mongodb-expression-exp.-mergeObjects)

</td>
<td headers="Description">
Returns a document created by combining the input documents for each group.

</td>
</tr>
<tr>
<td headers="Name">
[`$min`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/min/#mongodb-group-grp.-min)

</td>
<td headers="Description">
Returns the lowest expression value for each group.

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
[`$percentile`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/percentile/#mongodb-group-grp.-percentile)

</td>
<td headers="Description">
Returns an array of scalar values that correspond to specified [percentile](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-percentile) values.

This operator is available as an accumulator in these stages:

- [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group)

- [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields)

It is also available as an [aggregation expression](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/mql/expressions/#std-label-aggregation-expressions).

</td>
</tr>
<tr>
<td headers="Name">
[`$push`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/push/#mongodb-group-grp.-push)

</td>
<td headers="Description">
Returns an array of expression values for documents in each group.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

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

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$stdDevSamp`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/stdDevSamp/#mongodb-group-grp.-stdDevSamp)

</td>
<td headers="Description">
Returns the sample standard deviation of the input values.

Available in the [`$setWindowFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/setWindowFields/#mongodb-pipeline-pipe.-setWindowFields) stage.

</td>
</tr>
<tr>
<td headers="Name">
[`$sum`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sum/#mongodb-group-grp.-sum)

</td>
<td headers="Description">
Returns a sum of numerical values. Ignores non-numeric values.

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

### `$group` and Memory Restrictions

If the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage exceeds 100 megabytes of RAM, MongoDB writes data to temporary files. However, if the [allowDiskUse](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/command/aggregate/#std-label-aggregate-cmd-allowDiskUse) option is set to `false`, `$group` returns an error. For more information, refer to [Aggregation Pipeline Limits](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/aggregation-pipeline-limits/).

### `$group` Performance Optimizations

This section describes optimizations to improve the performance of [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group). There are optimizations that you can make manually and optimizations MongoDB makes internally.

#### Optimization to Return the First or Last Document of Each Group

If a pipeline [`sorts`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) and [`groups`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) by the same field and the `$group` stage only uses the [`$first`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/first/#mongodb-group-grp.-first) or [`$last`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/last/#mongodb-group-grp.-last) accumulator operator, consider adding an [index](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/indexes/#std-label-indexes) on the grouped field which matches the sort order. In some cases, the `$group` stage can use the index to quickly find the first or last document of each group.

If a collection named `foo` contains an index `{ x: 1, y: 1 }`, the following pipeline can use that index to find the first document of each group:

```js
db.foo.aggregate([
  {
    $sort:{ x : 1, y : 1 }
  },
  {
    $group: {
      _id: { x : "$x" },
      y: { $first : "$y" }
    }
  }
])
```

#### Slot-Based Query Execution Engine

Starting in version 5.2, MongoDB uses the [slot-based execution query engine](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/sbe/#std-label-sbe-landing) to execute [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stages if either:

- `$group` is the first stage in the pipeline.

- All preceding stages in the pipeline can also be executed by the slot-based execution engine.

For more information, see [`$group` Optimization](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/aggregation-pipeline-optimization/#std-label-agg-group-optimization-sbe).

## Examples

<Tabs>

<Tab name="MongoDB Shell">

### Group and Count Documents By Field

In [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh), create a sample collection named `sales` with the following documents:

```javascript
db.sales.insertMany([
  { "_id" : 1, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("2"), "date" : ISODate("2014-03-01T08:00:00Z") },
  { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : Int32("1"), "date" : ISODate("2014-03-01T09:00:00Z") },
  { "_id" : 3, "item" : "xyz", "price" : Decimal128("5"), "quantity" : Int32( "10"), "date" : ISODate("2014-03-15T09:00:00Z") },
  { "_id" : 4, "item" : "xyz", "price" : Decimal128("5"), "quantity" :  Int32("20") , "date" : ISODate("2014-04-04T11:21:39.736Z") },
  { "_id" : 5, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("10") , "date" : ISODate("2014-04-04T21:23:13.331Z") },
  { "_id" : 6, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("5" ) , "date" : ISODate("2015-06-04T05:08:13Z") },
  { "_id" : 7, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("10") , "date" : ISODate("2015-09-10T08:43:00Z") },
  { "_id" : 8, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("5" ) , "date" : ISODate("2016-02-06T20:20:13Z") },
])
```

The following aggregation operation uses the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage to group documents in the `sales` collection by the `price` field. One group contains the items with a price greater than or equal to 10. The second group contains the number of items with a price less than 10. The pipeline then counts the number of documents in each group.

```javascript
db.sales.aggregate(  [
   {
      $group: {
          _id: {
            $cond: {
              if: { $gte: [ "$price", Decimal128("10") ] },
              then: "Price >= 10",
              else: "Price < 10"
            }
          },
          count: { $sum: 1 }
      }
   }
]  )
```

The operation returns the following result:

```javascript
{ _id: 'Price >= 10', count: 4 }, { _id: 'Price < 10', count: 4 }
```

This aggregation operation is equivalent to the following SQL statement:

```sql
SELECT
   CASE
      WHEN price >= 10 THEN 'Price >= 10'
      ELSE 'Price < 10'
   END AS price_group,
   COUNT(*) AS count
FROM
  sales
GROUP BY
  price_group;
```

- [`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count/#mongodb-pipeline-pipe.-count)

- [`$count (aggregation accumulator)`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count-accumulator/#mongodb-group-grp.-count)

### Retrieve Distinct Values

The following aggregation operation uses the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage to retrieve the distinct item values from the `sales` collection:

```javascript
db.sales.aggregate( [ { $group : { _id : "$item" } } ] )
```

The operation returns the following result:

```javascript
{ "_id" : "abc" }
{ "_id" : "jkl" }
{ "_id" : "def" }
{ "_id" : "xyz" }
```

For example, `$group` operations of the following form can result in a `DISTINCT_SCAN`:

```javascript
{ $group : { _id : "$<field>" } }
```

For more information on behavior for retrieving distinct values, see the [distinct command behavior](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/command/distinct/#std-label-distinct-command-behavior).

To see whether your operation results in a `DISTINCT_SCAN`, check your operation's [explain results](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/explain-results/#std-label-explain-results).

### Group by Item Having

The following aggregation operation groups documents by the `item` field, calculating the total sale amount per item and returning only the items with total sale amount greater than or equal to 100:

```javascript
db.sales.aggregate(
  [
    // First Stage
    {
      $group :
        {
          _id : "$item",
          totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } }
        }
     },
     // Second Stage
     {
       $match: { "totalSaleAmount": { $gte: 100 } }
     }
   ]
 )
```

The [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage groups the documents by `item` to retrieve the distinct item values. This stage returns the `totalSaleAmount` for each item.

The [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) stage filters the resulting documents to only return items with a `totalSaleAmount` greater than or equal to 100.

The operation returns the following result:

```javascript
{ "_id" : "abc", "totalSaleAmount" : Decimal128("170") }
{ "_id" : "xyz", "totalSaleAmount" : Decimal128("150") }
{ "_id" : "def", "totalSaleAmount" : Decimal128("112.5") }
```

This aggregation operation is equivalent to the following SQL statement:

```sql
SELECT item,
   Sum(( price * quantity )) AS totalSaleAmount
FROM   sales
GROUP  BY item
HAVING totalSaleAmount >= 100
```

[`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match)

### Calculate Count, Sum, and Average

In [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh), create a sample collection named `sales` with the following documents:

```javascript
db.sales.insertMany([
  { "_id" : 1, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("2"), "date" : ISODate("2014-03-01T08:00:00Z") },
  { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : Int32("1"), "date" : ISODate("2014-03-01T09:00:00Z") },
  { "_id" : 3, "item" : "xyz", "price" : Decimal128("5"), "quantity" : Int32( "10"), "date" : ISODate("2014-03-15T09:00:00Z") },
  { "_id" : 4, "item" : "xyz", "price" : Decimal128("5"), "quantity" :  Int32("20") , "date" : ISODate("2014-04-04T11:21:39.736Z") },
  { "_id" : 5, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("10") , "date" : ISODate("2014-04-04T21:23:13.331Z") },
  { "_id" : 6, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("5" ) , "date" : ISODate("2015-06-04T05:08:13Z") },
  { "_id" : 7, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("10") , "date" : ISODate("2015-09-10T08:43:00Z") },
  { "_id" : 8, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("5" ) , "date" : ISODate("2016-02-06T20:20:13Z") },
])
```

#### Group by Day of the Year

The following pipeline calculates the total sales amount, average sales quantity, and sale count for each day in the year 2014:

```javascript
db.sales.aggregate([
  // First Stage
  {
    $match : { "date": { $gte: new ISODate("2014-01-01"), $lt: new ISODate("2015-01-01") } }
  },
  // Second Stage
  {
    $group : {
       _id : { $dateToString: { format: "%Y-%m-%d", date: "$date" } },
       totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } },
       averageQuantity: { $avg: "$quantity" },
       count: { $sum: 1 }
    }
  },
  // Third Stage
  {
    $sort : { totalSaleAmount: -1 }
  }
 ])
```

The [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) stage filters the documents to only pass documents from the year 2014 to the next stage.

The [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) stage groups the documents by date and calculates the total sale amount, average quantity, and total count of the documents in each group.

The [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) stage sorts the results by the total sale amount for each group in descending order.

The operation returns the following results:

```javascript
{
   "_id" : "2014-04-04",
   "totalSaleAmount" : Decimal128("200"),
   "averageQuantity" : 15, "count" : 2
}
{
   "_id" : "2014-03-15",
   "totalSaleAmount" : Decimal128("50"),
   "averageQuantity" : 10, "count" : 1
}
{
   "_id" : "2014-03-01",
   "totalSaleAmount" : Decimal128("40"),
   "averageQuantity" : 1.5, "count" : 2
}
```

This aggregation operation is equivalent to the following SQL statement:

```sql
SELECT date,
       Sum(( price * quantity )) AS totalSaleAmount,
       Avg(quantity)             AS averageQuantity,
       Count(*)                  AS Count
FROM   sales
WHERE  date >= '01/01/2014' AND date < '01/01/2015'
GROUP  BY date
ORDER  BY totalSaleAmount DESC
```

- [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match)

- [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort)

- [`db.collection.countDocuments()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.countDocuments/#mongodb-method-db.collection.countDocuments) which wraps the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) aggregation stage with a [`$sum`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sum/#mongodb-group-grp.-sum) expression.

#### Group by `null`

The following aggregation operation specifies a group `_id` of `null`, calculating the total sale amount, average quantity, and count of *all* documents in the collection.

```javascript
db.sales.aggregate([
  {
    $group : {
       _id : null,
       totalSaleAmount: { $sum: { $multiply: [ "$price", "$quantity" ] } },
       averageQuantity: { $avg: "$quantity" },
       count: { $sum: 1 }
    }
  }
 ])
```

The operation returns the following result:

```javascript
{
  "_id" : null,
  "totalSaleAmount" : Decimal128("452.5"),
  "averageQuantity" : 7.875,
  "count" : 8
}
```

This aggregation operation is equivalent to the following SQL statement:

```sql
SELECT Sum(price * quantity) AS totalSaleAmount,
       Avg(quantity)         AS averageQuantity,
       Count(*)              AS Count
FROM   sales
```

- [`$count`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/count/#mongodb-pipeline-pipe.-count)

- [`db.collection.countDocuments()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.countDocuments/#mongodb-method-db.collection.countDocuments) which wraps the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) aggregation stage with a [`$sum`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sum/#mongodb-group-grp.-sum) expression.

### Pivot Data

In [`mongosh`](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh), create a sample collection named `books` with the following documents:

```javascript
db.books.insertMany([
  { "_id" : 8751, "title" : "The Banquet", "author" : "Dante", "copies" : 2 },
  { "_id" : 8752, "title" : "Divine Comedy", "author" : "Dante", "copies" : 1 },
  { "_id" : 8645, "title" : "Eclogues", "author" : "Dante", "copies" : 2 },
  { "_id" : 7000, "title" : "The Odyssey", "author" : "Homer", "copies" : 10 },
  { "_id" : 7020, "title" : "Iliad", "author" : "Homer", "copies" : 10 }
])
```

#### Group `title` by `author`

The following aggregation operation pivots the data in the `books` collection to have titles grouped by authors.

```javascript
db.books.aggregate([
   { $group : { _id : "$author", books: { $push: "$title" } } }
 ])
```

The operation returns the following documents:

```javascript
{ "_id" : "Homer", "books" : [ "The Odyssey", "Iliad" ] }
{ "_id" : "Dante", "books" : [ "The Banquet", "Divine Comedy", "Eclogues" ] }
```

#### Group Documents by `author`

The following aggregation operation groups documents by `author`:

```javascript
db.books.aggregate([
   // First Stage
   {
     $group : { _id : "$author", books: { $push: "$$ROOT" } }
   },
   // Second Stage
   {
     $addFields:
       {
         totalCopies : { $sum: "$books.copies" }
       }
   }
 ])
```

[`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) uses the [`$$ROOT`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/aggregation-variables/#mongodb-variable-variable.ROOT) system variable to group the entire documents by authors. This stage passes the following documents to the next stage:

```javascript
{ "_id" : "Homer",
  "books" :
    [
       { "_id" : 7000, "title" : "The Odyssey", "author" : "Homer", "copies" : 10 },
       { "_id" : 7020, "title" : "Iliad", "author" : "Homer", "copies" : 10 }
    ]
 },
 { "_id" : "Dante",
   "books" :
     [
       { "_id" : 8751, "title" : "The Banquet", "author" : "Dante", "copies" : 2 },
       { "_id" : 8752, "title" : "Divine Comedy", "author" : "Dante", "copies" : 1 },
       { "_id" : 8645, "title" : "Eclogues", "author" : "Dante", "copies" : 2 }
     ]
 }
```

[`$addFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields) adds a field to the output containing the total copies of books for each author.

The resulting documents must not exceed the [BSON Document Size](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/limits/#mongodb-limit-BSON-Document-Size) limit of 16 mebibytes.

The operation returns the following documents:

```javascript
{
  "_id" : "Homer",
  "books" :
     [
       { "_id" : 7000, "title" : "The Odyssey", "author" : "Homer", "copies" : 10 },
       { "_id" : 7020, "title" : "Iliad", "author" : "Homer", "copies" : 10 }
     ],
   "totalCopies" : 20
}

{
  "_id" : "Dante",
  "books" :
     [
       { "_id" : 8751, "title" : "The Banquet", "author" : "Dante", "copies" : 2 },
       { "_id" : 8752, "title" : "Divine Comedy", "author" : "Dante", "copies" : 1 },
       { "_id" : 8645, "title" : "Eclogues", "author" : "Dante", "copies" : 2 }
     ],
   "totalCopies" : 5
}
```

</Tab>

<Tab name="C#">

The C# examples on this page use the `sample_mflix` database from the [Atlas sample datasets](https://www.mongodb.com/docs/atlas/sample-data/). To learn how to create a free MongoDB Atlas cluster and load the sample datasets, see [Get Started](https://www.mongodb.com/docs/drivers/csharp/current/quick-start/) in the MongoDB .NET/C# Driver documentation.

The following `Movie` class models the documents in the `sample_mflix.movies` collection:

```csharp
public class Movie
{
    public ObjectId Id { get; set; }

    public int Runtime { get; set; }

    public string Title { get; set; }

    public string Rated { get; set; }

    public List<string> Genres { get; set; }

    public string Plot { get; set; }

    public ImdbData Imdb { get; set; }

    public int Year { get; set; }

    public int Index { get; set; }

    public string[] Comments { get; set; }

    [BsonElement("lastupdated")]
    public DateTime LastUpdated { get; set; }
}
```

The C# classes on this page use Pascal case for their property names, but the field names in the MongoDB collection use camel case. To account for this difference, you can use the following code to register a `ConventionPack` when your application starts:

```csharp
var camelCaseConvention = new ConventionPack { new CamelCaseElementNameConvention() };
ConventionRegistry.Register("CamelCase", camelCaseConvention, type => true);
```

`$group`

[Group()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Group.html)

groups documents by the value of their `Rated` field. Each group's rating is shown in a field named `Rating` in each output document. Each output document also contains fields named `TotalRuntime`, `MedianRuntime`, and `NinetiethPercentileRuntime`, which store the total, median, and 90th percentile runtime values for movies in each group.

To use the MongoDB .NET/C# driver to add a `$group` stage to an aggregation pipeline, call the [Group()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Group.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that groups documents by the value of their `Rated` field. Each group's rating is shown in a field named `Rating` in each output document. Each output document also contains fields named `TotalRuntime`, `MedianRuntime`, and `NinetiethPercentileRuntime`, which store the total, median, and 90th percentile runtime values for movies in each group.

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Group(
        id: m => m.Rated,
        group: g => new
        {
            Rating = g.Key,
            TotalRuntime = g.Sum(m => m.Runtime),
            MedianRuntime = g.Select(m => m.Runtime).Median(),
            NinetiethPercentileRuntime = g.Select(m => m.Runtime).Percentile(new[] { 0.9 })
        }
    );
```

</Tab>

<Tab name="Node.js">

The Node.js examples on this page use the `sample_mflix` database from the [Atlas sample datasets](https://www.mongodb.com/docs/atlas/sample-data/). To learn how to create a free MongoDB Atlas cluster and load the sample datasets, see [Get Started](https://www.mongodb.com/docs/drivers/node/current/get-started/) in the MongoDB Node.js driver documentation.

`$group`

groups documents by the value of their `rated` field. Each output document contains a `rating` field that stores each group's rating. Each output document also contains a field named `totalRuntime` that stores the total runtime of all movies in the group

To use the MongoDB Node.js driver to add a `$group` stage to an aggregation pipeline, use the `$group` operator in a pipeline object.

The following example creates a pipeline stage that groups documents by the value of their `rated` field. Each output document contains a `rating` field that stores each group's rating. Each output document also contains a field named `totalRuntime` that stores the total runtime of all movies in the group. The example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $group: {
      _id: "$rated",
      rating: { $first: "$rated" },
      totalRuntime: { $sum: "$runtime" }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

</Tab>

</Tabs>

## Learn More

The [Group and Total Data](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/tutorial/aggregation-examples/group-and-total/#std-label-agg-example-group-data) tutorial provides an extensive example of the [`$group`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/group/#mongodb-pipeline-pipe.-group) operator in a common use case.

To learn more about related pipeline stages, see the [`$addFields`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/addFields/#mongodb-pipeline-pipe.-addFields) guide.


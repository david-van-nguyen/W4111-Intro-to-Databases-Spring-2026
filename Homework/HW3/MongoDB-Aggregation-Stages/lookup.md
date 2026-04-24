# $lookup (aggregation stage)

## Definition

`$lookup`
Performs a left outer join to a collection in the *same* database to filter in documents from the foreign collection for processing. The [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage adds a new array field to each input document. The new array field contains the matching documents from the foreign collection. The [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage passes these reshaped documents to the next stage.

Starting in MongoDB 5.1, you can use [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) with sharded collections.

To combine elements from two different collections, use the [`$unionWith`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/unionWith/#mongodb-pipeline-pipe.-unionWith) pipeline stage.

Excessive use of `$lookup` may slow down query performance. To reduce reliance on `$lookup`, consider an [embedded data model](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/data-modeling/embedding/#std-label-data-modeling-embedding) to store related data in a single collection.

For details on `$lookup` performance, see [Performance Considerations](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-performance-considerations).

## Compatibility

`$lookup`You can use `$lookup` for deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully managed service for MongoDB deployments in the cloud

- [MongoDB Enterprise](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-enterprise/#std-label-install-mdb-enterprise): The subscription-based, self-managed version of MongoDB

- [MongoDB Community](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-community/#std-label-install-mdb-community-edition): The source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       let: { <var_1>: <expression>, …, <var_n>: <expression> },
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

The [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) accepts a document with these fields:

<table>
<tr>
<th id="Field">
Field

</th>
<th id="Necessity">
Necessity

</th>
<th id="Description">
Description

</th>
</tr>
<tr>
<td headers="Field">
[from](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-from)

</td>
<td headers="Necessity">
Required

</td>
<td headers="Description">
Specifies the foreign collection in the *same* database to join to the local collection.

It is possible in some edge cases to subsitute `from` with `pipeline` with [`$documents`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/documents/#mongodb-pipeline-pipe.-documents) as the first stage. For an example, see [Use a $documents Stage in a $lookup Stage](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/documents/#std-label-documents-lookup-example).

Starting in MongoDB 5.1, the `from` collection can be sharded.

</td>
</tr>
<tr>
<td headers="Field">
[localField](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-localField)

</td>
<td headers="Necessity">
Optional if `pipeline` is specified

</td>
<td headers="Description">
Specifies the field from the documents input to the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) performs an equality match on the `localField` to the `foreignField` from the documents of the `from` collection. If an input document does not contain the `localField`, the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) treats the field as having a value of `null` for matching purposes.

</td>
</tr>
<tr>
<td headers="Field">
[foreignField](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-foreignField)

</td>
<td headers="Necessity">
Optional if `pipeline` is specified

</td>
<td headers="Description">
Specifies the foreign documents' `foreignField` to perform an equality match with the local documents' `localField`.

If a foreign document does not contain a `foreignField` value, the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) uses a `null` value for the match.

</td>
</tr>
<tr>
<td headers="Field">
[let](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-let)

</td>
<td headers="Necessity">
Optional

</td>
<td headers="Description">
Specifies variables to use in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) stages. Use the variable expressions to access the fields from the local collection's documents that are input to the `pipeline`.

To reference variables in [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) stages, use the `"$$<variable>"` syntax.

The [let](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-let) variables can be accessed by the stages in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline), including additional [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stages nested in the `pipeline`.

- A [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) stage requires the use of an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator to access the variables. The [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator allows the use of aggregation expressions inside of the [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) syntax.

  The [`$eq`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/eq/#mongodb-expression-exp.-eq), [`$lt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lt/#mongodb-expression-exp.-lt), [`$lte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte), [`$gt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gt/#mongodb-expression-exp.-gt), and [`$gte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gte/#mongodb-expression-exp.-gte) comparison operators placed in an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator can use an index on the `from` collection referenced in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. Limitations:

  - Indexes can only be used for comparisons between fields and constants, so the `let` operand must resolve to a constant.

    For example, a comparison between `$a` and a constant value can use an index, but a comparison between `$a` and `$b` cannot.

  - Indexes are not used for comparisons where the `let` operand resolves to an empty or missing value.

  - [Multikey](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/indexes/index-types/index-multikey/#std-label-index-type-multikey), [partial](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-partial/#std-label-index-type-partial), or [sparse](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-sparse/#std-label-index-type-sparse) indexes are not used.

- Other (non-[`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match)) stages in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) do not require an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator to access the variables.

</td>
</tr>
<tr>
<td headers="Field">
[pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline)

</td>
<td headers="Necessity">
Optional if `localField` and `foreignField` are specified

</td>
<td headers="Description">
Specifies the `pipeline` to run on the foreign collection. The `pipeline` returns documents from the foreign collection. To return all documents, specify an empty `pipeline: []`.

The `pipeline` cannot include the [`$out`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/out/#mongodb-pipeline-pipe.-out) or [`$merge`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/merge/#mongodb-pipeline-pipe.-merge) stages. Starting in v6.0, the `pipeline` can contain the [MongoDB Search](https://www.mongodb.com/docs/atlas/atlas-search/)
[`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search) stage as the first stage inside the pipeline. To learn more, see [MongoDB Search Support](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-fts-lookup-behavior).

The `pipeline` cannot access fields from input documents. Instead, define variables for the document fields using the [let](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-let) option and then reference the variables in the `pipeline` stages.

To reference variables in [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) stages, use the `"$$<variable>"` syntax.

The [let](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-let) variables can be accessed by the stages in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline), including additional [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stages nested in the `pipeline`.

- A [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) stage requires the use of an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator to access the variables. The [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator allows the use of aggregation expressions inside of the [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) syntax.

  The [`$eq`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/eq/#mongodb-expression-exp.-eq), [`$lt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lt/#mongodb-expression-exp.-lt), [`$lte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte), [`$gt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gt/#mongodb-expression-exp.-gt), and [`$gte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gte/#mongodb-expression-exp.-gte) comparison operators placed in an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator can use an index on the `from` collection referenced in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. Limitations:

  - Indexes can only be used for comparisons between fields and constants, so the `let` operand must resolve to a constant.

    For example, a comparison between `$a` and a constant value can use an index, but a comparison between `$a` and `$b` cannot.

  - Indexes are not used for comparisons where the `let` operand resolves to an empty or missing value.

  - [Multikey](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/indexes/index-types/index-multikey/#std-label-index-type-multikey), [partial](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-partial/#std-label-index-type-partial), or [sparse](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-sparse/#std-label-index-type-sparse) indexes are not used.

- Other (non-[`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match)) stages in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) do not require an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator to access the variables.

</td>
</tr>
<tr>
<td headers="Field">
[as](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-as)

</td>
<td headers="Necessity">
Required

</td>
<td headers="Description">
Specifies the name of the new array field to add to the input documents. The new array field contains the matching documents from the `from` collection. If the specified name already exists in the input document, the existing field is *overwritten*.

</td>
</tr>
</table>
### Equality Match with a Single Join Condition

To perform an equality match between a field from the input documents with a field from the documents of the foreign collection, the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage has this syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

In this example, `pipeline` is optional and runs after the local and foreign equality stage.

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, (
   SELECT ARRAY_AGG(*)
   FROM <collection to join>
   WHERE <foreignField> = <collection.localField>
) AS <output array field>
FROM collection;
```

The SQL statements on this page are included for comparison to the MongoDB aggregation pipeline syntax. The SQL statements aren't runnable.

For MongoDB examples, see these pages:

- [Perform a Single Equality Join with `$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-single-equality-example)

- [Use `$lookup` with an Array](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-unwind-example)

- [Use `$lookup` with `$mergeObjects`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-mergeObjects)

### Join Conditions and Subqueries on a Foreign Collection

MongoDB supports:

- Executing a pipeline on a foreign collection.

- Multiple join conditions.

- Correlated and uncorrelated subqueries.

In MongoDB, an uncorrelated subquery means that every input document will return the same result. A correlated subquery is a [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-pipeline) in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage that uses the local or `input` collection's fields to return results correlated to each incoming document.

Starting in MongoDB 5.0, for an uncorrelated subquery in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) pipeline stage containing a [`$sample`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sample/#mongodb-pipeline-pipe.-sample) stage, the [`$sampleRate`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sampleRate/#mongodb-expression-exp.-sampleRate) operator, or the [`$rand`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/rand/#mongodb-expression-exp.-rand) operator, the subquery is always run again if repeated. Previously, depending on the subquery output size, either the subquery output was cached or the subquery was run again.

MongoDB correlated subqueries are comparable to SQL correlated subqueries, where the inner query references outer query values. An SQL uncorrelated subquery does not reference outer query values.

MongoDB 5.0 also supports [concise correlated subqueries](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-concise-correlated-subquery).

To perform correlated and uncorrelated subqueries with two collections, and perform other join conditions besides a single equality match, use this [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) syntax:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run on foreign collection> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM collection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <collection to join>
   WHERE <pipeline>
);
```

See the following examples:

- [Use Multiple Join Conditions and a Correlated Subquery](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-multiple-joins)

- [Perform an Uncorrelated Subquery with `$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-uncorrelated-subquery)

### Correlated Subqueries Using Concise Syntax

Starting in MongoDB 5.0, you can use a concise syntax for a correlated subquery. Correlated subqueries reference document fields from a foreign collection  *and* the "local" collection on which the [`aggregate()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.aggregate/#mongodb-method-db.collection.aggregate) method was run.

The following new concise syntax removes the requirement for an equality match on the foreign and local fields inside of an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         localField: <field from local collection's documents>,
         foreignField: <field from foreign collection's documents>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM localCollection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <foreignCollection>
   WHERE <foreignCollection.foreignField> = <localCollection.localField>
   AND <pipeline match condition>
);
```

See this example:

- [Perform a Concise Correlated Subquery with `$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-concise-correlated-subquery)

## Behavior

### Encrypted Collections

Starting in MongoDB 8.1, you can reference multiple encrypted collections in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. However, `$lookup` does not support:

- Using an encrypted field as the join field in the `localField` or `foreignField`.

  For drivers using Client-Side Field Level Encryption, you can use an encrypted field as a join field only if you are performing a self-join operation.

- Using any field in an encrypted array. An array is considered as encrypted if it contains any encrypted elements.

  - For example, you can't use any field within the resulting [as](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-as) array of the `$lookup` operation, unless you're using Client-Side Field Level Encryption and [`$unwind`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/unwind/#mongodb-pipeline-pipe.-unwind) the `as` field.

### Views and Collation

If performing an aggregation that involves multiple views, such as with [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) or [`$graphLookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/graphLookup/#mongodb-pipeline-pipe.-graphLookup), the views must have the same [collation](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/collation/#std-label-collation).

### Restrictions

You cannot include the [`$out`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/out/#mongodb-pipeline-pipe.-out) or the [`$merge`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/merge/#mongodb-pipeline-pipe.-merge) stage in the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. That is, when specifying a [pipeline for the foreign collection](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-let-pipeline), you cannot include either stage in the `pipeline` field.

```javascript
{
   $lookup:
   {
      from: <collection to join>,
      let: { <var_1>: <expression>, …, <var_n>: <expression> },
      pipeline: [ <pipeline to execute on the foreign collection> ],  // Cannot include $out or $merge
      as: <output array field>
   }
}
```

### MongoDB Search Support

Starting in MongoDB 6.0, you can specify the [MongoDB Search](https://www.mongodb.com/docs/atlas/atlas-search/) [`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search) or [`$searchMeta`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/searchMeta/#mongodb-pipeline-pipe.-searchMeta) stage in the `$lookup` pipeline to search collections on the Atlas cluster. The [`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search) or the [`$searchMeta`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/searchMeta/#mongodb-pipeline-pipe.-searchMeta) stage must be the first stage inside the `$lookup` pipeline.

For example, when you [Join Conditions and Subqueries on a Foreign Collection](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-let-pipeline) or run [Correlated Subqueries Using Concise Syntax](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-concise-correlated-subquery), you can specify [`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search) or [`$searchMeta`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/searchMeta/#mongodb-pipeline-pipe.-searchMeta) inside the pipeline as shown below:

<Tabs>

<Tab name="$search">

```
[{
  "$lookup": {
    "from": <foreign collection>,
    localField: <field from the input documents>,
    foreignField: <field from the documents of the "from" collection>,
    "as": <output array field>,
    "pipeline": [{
      "$search": {
        "<operator>": {
          <operator-specification>
        }
      },
      ...
    }]
  }
}]
```

</Tab>

<Tab name="$searchMeta">

```
[{
  "$lookup": {
    "from": <foreign collection>,
    localField: <field from the input documents>,
    foreignField: <field from the documents of the "from" collection>,
    "as": <output array field>,
    "pipeline": [{
      "$searchMeta": {
        "<collector>": {
          <collector-specification>
        }
      },
      ...
    }]
  }
}]
```

</Tab>

</Tabs>

To see an example of [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) with [`$search`](https://www.mongodb.com/docs/atlas/atlas-search/aggregation-stages/search/#mongodb-pipeline-pipe.-search), see the MongoDB Search tutorial [Run a MongoDB Search $search Query Using $lookup](https://www.mongodb.com/docs/atlas/atlas-search/tutorial/lookup-with-search/).

### Sharded Collections

Starting in MongoDB 5.1, you can specify [sharded collections](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/sharding/#std-label-sharding-sharded-cluster) in the `from` parameter of [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stages.

Starting in MongoDB 8.0, you can use the `$lookup` stage within a transaction while targeting a sharded collection.

### Slot-Based Query Execution Engine

Starting in version 6.0, MongoDB can use the [slot-based execution query engine](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/sbe/#std-label-sbe-landing) to execute [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stages if *all* preceding stages in the pipeline can also be executed by the slot-based execution engine and none of the following conditions are true:

- The `$lookup` operation executes a pipeline on a foreign collection. To see an example of this kind of operation, see [Join Conditions and Subqueries on a Foreign Collection](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-let-pipeline).

- The `$lookup`'s `localField` or `foreignField` specify numeric components. For example: `{ localField: "restaurant.0.review" }`.

- The `from` field of any `$lookup` in the pipeline specifies a view or sharded collection.

For more information, see [`$lookup` Optimization](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/aggregation-pipeline-optimization/#std-label-agg-lookup-optimization-sbe).

### Performance Considerations

`$lookup` performance depends on the type of operation performed. Refer to the following table for performance considerations for different `$lookup` operations.

<table>
<tr>
<th id="$lookup%20Operation">
`$lookup` Operation

</th>
<th id="Performance%20Considerations">
Performance Considerations

</th>
</tr>
<tr>
<td headers="$lookup%20Operation">
[Equality Match with a Single Join](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-single-equality-example)

</td>
<td headers="Performance%20Considerations">
- `$lookup` operations that perform equality matches with a single join perform better when the foreign collection contains an index on the `foreignField`.

  IMPORTANT: If a supporting index on the `foreignField` does not exist, a `$lookup` operation that performs an equality match with a single join will likely have poor performance.

</td>
</tr>
<tr>
<td headers="$lookup%20Operation">
[Uncorrelated Subqueries](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-uncorrelated-subquery)

</td>
<td headers="Performance%20Considerations">
- `$lookup` operations that contain uncorrelated subqueries perform better when the inner pipeline can reference an index of the foreign collection.

- MongoDB only needs to run the `$lookup` subquery once before caching the query because there is no relationship between the source and foreign collections. The subquery is not based on any value in the source collection. This behavior improves performance for subsequent executions of the `$lookup` operation.

</td>
</tr>
<tr>
<td headers="$lookup%20Operation">
[Correlated Subqueries](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-concise-correlated-subquery)

</td>
<td headers="Performance%20Considerations">
- `$lookup` operations that contain correlated subqueries perform better when the following conditions apply:

  - The foreign collection contains an index on the `foreignField`.

  - The foreign collection contains an index that references the inner pipline.

- If your pipeline passes a large number of documents to the `$lookup` query, the following strategies may improve performance:

  - Reduce the number of documents that MongoDB passes to the `$lookup` query. For example, set a stricter filter during the `$match` stage.

  - Run the inner pipeline of the `$lookup` subquery as a separate query and use `$out` to create a temporary collection. Then, run an [equality match with a single join](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-single-equality).

  - Reconsider the data's schema to ensure it is optimal for the use case.

</td>
</tr>
</table>For general performance strategies, see [Indexing Strategies](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/applications/indexes/#std-label-manual-indexing-strategies) and [Query Optimization](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/query-optimization/#std-label-read-operations-indexing).

## Examples

<Tabs>

<Tab name="MongoDB Shell">

### Perform a Single Equality Join with `$lookup`

Create a collection `orders` with these documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "almonds", price: 12, quantity: 2 },
   { _id: 2, item: "pecans", price: 20, quantity: 1 },
   { _id: 3  }
] )
```

Create another collection `inventory` with these documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, sku: "almonds", description: "product 1", instock: 120 },
   { _id: 2, sku: "bread", description: "product 2", instock: 80 },
   { _id: 3, sku: "cashews", description: "product 3", instock: 60 },
   { _id: 4, sku: "pecans", description: "product 4", instock: 70 },
   { _id: 5, sku: null, description: "Incomplete" },
   { _id: 6 }
] )
```

The following aggregation operation on the `orders` collection joins the documents from `orders` with the documents from the `inventory` collection using the fields `item` from the `orders` collection and the `sku` field from the `inventory` collection:

```javascript
db.orders.aggregate( [
   {
     $lookup:
       {
         from: "inventory",
         localField: "item",
         foreignField: "sku",
         as: "inventory_docs"
       }
  }
] )
```

The operation returns these documents:

```javascript
{
   _id: 1,
   item: "almonds",
   price: 12,
   quantity: 2,
   inventory_docs: [
      { _id: 1, sku: "almonds", description: "product 1", instock: 120 }
   ]
}
{
   _id: 2,
   item: "pecans",
   price: 20,
   quantity: 1,
   inventory_docs: [
      { _id: 4, sku: "pecans", description: "product 4", instock: 70 }
   ]
}
{
   _id: 3,
   inventory_docs: [
      { _id: 5, sku: null, description: "Incomplete" },
      { _id: 6 }
   ]
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, inventory_docs
FROM orders
WHERE inventory_docs IN (
   SELECT *
   FROM inventory
   WHERE sku = orders.item
);
```

For more information, see [Equality Match Performance Considerations](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-equality-match-performance).

### Use `$lookup` with an Array

If the `localField` is an array, you can match the array elements against a scalar `foreignField` without an [`$unwind`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/unwind/#mongodb-pipeline-pipe.-unwind) stage.

For example, create an example collection `classes` with these documents:

```javascript
db.classes.insertMany( [
   { _id: 1, title: "Reading is ...", enrollmentlist: [ "giraffe2", "pandabear", "artie" ], days: ["M", "W", "F"] },
   { _id: 2, title: "But Writing ...", enrollmentlist: [ "giraffe1", "artie" ], days: ["T", "F"] }
] )
```

Create another collection `members` with these documents:

```javascript
db.members.insertMany( [
   { _id: 1, name: "artie", foreign: new Date("2016-05-01"), status: "A" },
   { _id: 2, name: "giraffe", foreign: new Date("2017-05-01"), status: "D" },
   { _id: 3, name: "giraffe1", foreign: new Date("2017-10-01"), status: "A" },
   { _id: 4, name: "panda", foreign: new Date("2018-10-11"), status: "A" },
   { _id: 5, name: "pandabear", foreign: new Date("2018-12-01"), status: "A" },
   { _id: 6, name: "giraffe2", foreign: new Date("2018-12-01"), status: "D" }
] )
```

The following aggregation operation joins documents in the `classes` collection with the `members` collection, matching on the `enrollmentlist` field to the `name` field:

```javascript
db.classes.aggregate( [
   {
      $lookup:
         {
            from: "members",
            localField: "enrollmentlist",
            foreignField: "name",
            as: "enrollee_info"
        }
   }
] )
```

The operation returns the following:

```javascript
{
   _id: 1,
   title: "Reading is ...",
   enrollmentlist: [ "giraffe2", "pandabear", "artie" ],
   days: [ "M", "W", "F" ],
   enrollee_info: [
      { _id: 1, name: "artie", foreign: ISODate("2016-05-01T00:00:00Z"), status: "A" },
      { _id: 5, name: "pandabear", foreign: ISODate("2018-12-01T00:00:00Z"), status: "A" },
      { _id: 6, name: "giraffe2", foreign: ISODate("2018-12-01T00:00:00Z"), status: "D" }
   ]
}
{
   _id: 2,
   title: "But Writing ...",
   enrollmentlist: [ "giraffe1", "artie" ],
   days: [ "T", "F" ],
   enrollee_info: [
      { _id: 1, name: "artie", foreign: ISODate("2016-05-01T00:00:00Z"), status: "A" },
      { _id: 3, name: "giraffe1", foreign: ISODate("2017-10-01T00:00:00Z"), status: "A" }
   ]
}
```

### Use `$lookup` with `$mergeObjects`

The [`$mergeObjects`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/mergeObjects/#mongodb-expression-exp.-mergeObjects) operator combines multiple documents into a single document.

Create a collection `orders` with these documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "almonds", price: 12, quantity: 2 },
   { _id: 2, item: "pecans", price: 20, quantity: 1 }
] )
```

Create another collection `items` with these documents:

```javascript
db.items.insertMany( [
  { _id: 1, item: "almonds", description: "almond clusters", instock: 120 },
  { _id: 2, item: "bread", description: "raisin and nut bread", instock: 80 },
  { _id: 3, item: "pecans", description: "candied pecans", instock: 60 }
] )
```

The following operation first uses the [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage to join the two collections by the `item` fields and then uses [`$mergeObjects`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/mergeObjects/#mongodb-expression-exp.-mergeObjects) in the [`$replaceRoot`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/replaceRoot/#mongodb-pipeline-pipe.-replaceRoot) to merge the foreign documents from `items` and `orders`:

```javascript
db.orders.aggregate( [
   {
      $lookup: {
         from: "items",
         localField: "item",    // field in the orders collection
         foreignField: "item",  // field in the items collection
         as: "fromItems"
      }
   },
   {
      $replaceRoot: { newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$fromItems", 0 ] }, "$$ROOT" ] } }
   },
   { $project: { fromItems: 0 } }
] )
```

The operation returns these documents:

```javascript
{
  _id: 1,
  item: 'almonds',
  description: 'almond clusters',
  instock: 120,
  price: 12,
  quantity: 2
},
{
  _id: 2,
  item: 'pecans',
  description: 'candied pecans',
  instock: 60,
  price: 20,
  quantity: 1
}
```

### Use Multiple Join Conditions and a Correlated Subquery

Pipelines can execute on a foreign collection and include multiple join conditions. The [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator enables more complex join conditions including conjunctions and non-equality matches.

A join condition can reference a field in the local collection on which the [`aggregate()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.aggregate/#mongodb-method-db.collection.aggregate) method was run and reference a field in the foreign collection. This allows a correlated subquery between the two collections.

MongoDB 5.0 supports [concise correlated subqueries](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-concise-correlated-subquery).

Create a collection `orders` with these documents:

```javascript
db.orders.insertMany( [
  { _id: 1, item: "almonds", price: 12, ordered: 2 },
  { _id: 2, item: "pecans", price: 20, ordered: 1 },
  { _id: 3, item: "cookies", price: 10, ordered: 60 }
] )
```

Create another collection `warehouses` with these documents:

```javascript
db.warehouses.insertMany( [
  { _id: 1, stock_item: "almonds", warehouse: "A", instock: 120 },
  { _id: 2, stock_item: "pecans", warehouse: "A", instock: 80 },
  { _id: 3, stock_item: "almonds", warehouse: "B", instock: 60 },
  { _id: 4, stock_item: "cookies", warehouse: "B", instock: 40 },
  { _id: 5, stock_item: "cookies", warehouse: "A", instock: 80 }
] )
```

The following example:

- Uses a correlated subquery with a join on the `orders.item` and `warehouse.stock_item` fields.

- Ensures the quantity of the item in stock can fulfill the ordered quantity.

```javascript
db.orders.aggregate( [
   {
      $lookup:
         {
           from : "warehouses",
           localField : "item",
           foreignField : "stock_item",
           let : { order_qty: "$ordered" },
           pipeline : [
              { $match :
                 { $expr :
                      { $gte: [ "$instock", "$$order_qty" ] }
                 }
              },
              { $project : { stock_item: 0, _id: 0 } }
           ],
           as : "stockdata"
         }
    }
] )
```

The operation returns these documents:

```javascript
{
  _id: 1,
  item: 'almonds',
  price: 12,
  ordered: 2,
  stockdata: [
    { warehouse: 'A', instock: 120 },
    { warehouse: 'B', instock: 60 }
  ]
},
{
  _id: 2,
  item: 'pecans',
  price: 20,
  ordered: 1,
  stockdata: [ { warehouse: 'A', instock: 80 } ]
},
{
  _id: 3,
  item: 'cookies',
  price: 10,
  ordered: 60,
  stockdata: [ { warehouse: 'A', instock: 80 } ]
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, stockdata
FROM orders
WHERE stockdata IN (
   SELECT warehouse, instock
   FROM warehouses
   WHERE stock_item = orders.item
   AND instock >= orders.ordered
);
```

The [`$eq`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/eq/#mongodb-expression-exp.-eq), [`$lt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lt/#mongodb-expression-exp.-lt), [`$lte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lte/#mongodb-expression-exp.-lte), [`$gt`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gt/#mongodb-expression-exp.-gt), and [`$gte`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/gte/#mongodb-expression-exp.-gte) comparison operators placed in an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator can use an index on the `from` collection referenced in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage. Limitations:

- Indexes can only be used for comparisons between fields and constants, so the `let` operand must resolve to a constant.

  For example, a comparison between `$a` and a constant value can use an index, but a comparison between `$a` and `$b` cannot.

- Indexes are not used for comparisons where the `let` operand resolves to an empty or missing value.

- [Multikey](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/indexes/index-types/index-multikey/#std-label-index-type-multikey), [partial](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-partial/#std-label-index-type-partial), or [sparse](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/index-sparse/#std-label-index-type-sparse) indexes are not used.

For example, if the index `{ stock_item: 1, instock: 1 }` exists on the `warehouses` collection:

- The equality match on the `warehouses.stock_item` field uses the index.

- The range part of the query on the `warehouses.instock` field also uses the indexed field in the compound index.

- [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr)

- [Variables in Aggregation Expressions](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/aggregation-variables/)

### Perform an Uncorrelated Subquery with `$lookup`

An aggregation pipeline [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage can execute a pipeline on the foreign collection, which allows uncorrelated subqueries. An uncorrelated subquery does not reference the local document fields.

Starting in MongoDB 5.0, for an uncorrelated subquery in a [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) pipeline stage containing a [`$sample`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sample/#mongodb-pipeline-pipe.-sample) stage, the [`$sampleRate`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sampleRate/#mongodb-expression-exp.-sampleRate) operator, or the [`$rand`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/rand/#mongodb-expression-exp.-rand) operator, the subquery is always run again if repeated. Previously, depending on the subquery output size, either the subquery output was cached or the subquery was run again.

Create a collection `absences` with these documents:

```javascript
db.absences.insertMany( [
   { _id: 1, student: "Ann Aardvark", sickdays: [ new Date ("2018-05-01"),new Date ("2018-08-23") ] },
   { _id: 2, student: "Zoe Zebra", sickdays: [ new Date ("2018-02-01"),new Date ("2018-05-23") ] },
] )
```

Create another collection `holidays` with these documents:

```javascript
db.holidays.insertMany( [
   { _id: 1, year: 2018, name: "New Years", date: new Date("2018-01-01") },
   { _id: 2, year: 2018, name: "Pi Day", date: new Date("2018-03-14") },
   { _id: 3, year: 2018, name: "Ice Cream Day", date: new Date("2018-07-15") },
   { _id: 4, year: 2017, name: "New Years", date: new Date("2017-01-01") },
   { _id: 5, year: 2017, name: "Ice Cream Day", date: new Date("2017-07-16") }
] )
```

The following operation joins the `absences` collection with 2018 holiday information from the `holidays` collection:

```javascript
db.absences.aggregate( [
   {
      $lookup:
         {
           from: "holidays",
           pipeline: [
              { $match: { year: 2018 } },
              { $project: { _id: 0, date: { name: "$name", date: "$date" } } },
              { $replaceRoot: { newRoot: "$date" } }
           ],
           as: "holidays"
         }
    }
] )
```

The operation returns the following:

```javascript
{
  _id: 1,
  student: 'Ann Aardvark',
  sickdays: [
    ISODate("2018-05-01T00:00:00.000Z"),
    ISODate("2018-08-23T00:00:00.000Z")
  ],
  holidays: [
    { name: 'New Years', date: ISODate("2018-01-01T00:00:00.000Z") },
    { name: 'Pi Day', date: ISODate("2018-03-14T00:00:00.000Z") },
    { name: 'Ice Cream Day', date: ISODate("2018-07-15T00:00:00.000Z")
    }
  ]
},
{
  _id: 2,
  student: 'Zoe Zebra',
  sickdays: [
    ISODate("2018-02-01T00:00:00.000Z"),
    ISODate("2018-05-23T00:00:00.000Z")
  ],
  holidays: [
    { name: 'New Years', date: ISODate("2018-01-01T00:00:00.000Z") },
    { name: 'Pi Day', date: ISODate("2018-03-14T00:00:00.000Z") },
    { name: 'Ice Cream Day', date: ISODate("2018-07-15T00:00:00.000Z")
    }
  ]
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, holidays
FROM absences
WHERE holidays IN (
   SELECT name, date
   FROM holidays
   WHERE year = 2018
);
```

For more information, see [Uncorrelated Subquery Performance Considerations](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-uncorrelated-subqueries-performance).

### Perform a Concise Correlated Subquery with `$lookup`

Starting in MongoDB 5.0, an aggregation pipeline [`$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#mongodb-pipeline-pipe.-lookup) stage supports a [concise correlated subquery syntax](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-syntax-concise-correlated-subquery) that improves joins between collections. The new concise syntax removes the requirement for an equality match on the foreign and local fields inside of an [`$expr`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/query/expr/#mongodb-query-op.-expr) operator in a [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) stage.

Create a collection `restaurants`:

```javascript
db.restaurants.insertMany( [
   {
      _id: 1,
      name: "American Steak House",
      food: [ "filet", "sirloin" ],
      beverages: [ "beer", "wine" ]
   },
   {
      _id: 2,
      name: "Honest John Pizza",
      food: [ "cheese pizza", "pepperoni pizza" ],
      beverages: [ "soda" ]
   }
] )
```

Create another collection `orders` with food and optional drink orders:

```javascript
db.orders.insertMany( [
   {
      _id: 1,
      item: "filet",
      restaurant_name: "American Steak House"
   },
   {
      _id: 2,
      item: "cheese pizza",
      restaurant_name: "Honest John Pizza",
      drink: "lemonade"
   },
   {
      _id: 3,
      item: "cheese pizza",
      restaurant_name: "Honest John Pizza",
      drink: "soda"
   }
] )
```

The following example:

- Joins the `orders` and `restaurants` collections by matching the `orders.restaurant_name` [localField](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-localField) with the `restaurants.name` [foreignField](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-subquery-foreignField). The match is performed before the `pipeline` is run.

- Performs an [`$in`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/in/#mongodb-expression-exp.-in) array match between the `orders.drink` and `restaurants.beverages` fields that are accessed using `$$orders_drink` and `$beverages` respectively.

```javascript
db.orders.aggregate( [
   {
      $lookup: {
         from: "restaurants",
         localField: "restaurant_name",
         foreignField: "name",
         let: { orders_drink: "$drink" },
         pipeline: [ {
            $match: {
               $expr: { $in: [ "$$orders_drink", "$beverages" ] }
            }
         } ],
         as: "matches"
      }
   }
] )
```

There is a match for the `soda` value in the `orders.drink` and `restaurants.beverages` fields. This output shows the `matches` array and contains all foreign fields from the `restaurants` collection for the match:

```javascript
{
   _id: 1, item: "filet",
   restaurant_name: "American Steak House",
   matches: [ ]
}
{
   _id: 2, item: "cheese pizza",
   restaurant_name: "Honest John Pizza",
   drink: "lemonade",
   matches: [ ]
}
{
   _id: 3, item: "cheese pizza",
   restaurant_name: "Honest John Pizza",
   drink: "soda",
   matches: [ {
      _id: 2, name": "Honest John Pizza",
      food: [ "cheese pizza", "pepperoni pizza" ],
      beverages: [ "soda" ]
   } ]
}
```

This example uses the older verbose syntax from MongoDB versions before 5.0 and returns the same results as the previous concise example:

```javascript
db.orders.aggregate( [
   {
      $lookup: {
         from: "restaurants",
         let: { orders_restaurant_name: "$restaurant_name",
                orders_drink: "$drink" },
         pipeline: [ {
            $match: {
               $expr: {
                  $and: [
                     { $eq: [ "$$orders_restaurant_name", "$name" ] },
                     { $in: [ "$$orders_drink", "$beverages" ] }
                  ]
               }
            }
         } ],
         as: "matches"
      }
   }
] )
```

The previous examples correspond to this pseudo-SQL statement:

```sql
SELECT *, matches
FROM orders
WHERE matches IN (
   SELECT *
   FROM restaurants
   WHERE restaurants.name = orders.restaurant_name
   AND restaurants.beverages = orders.drink
);
```

For more information, see [Correlated Subquery Performance Considerations](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-correlated-subqueries-performance).

### Namespaces in Subpipelines

Starting in MongoDB 8.0, namespaces in subpipelines within `$lookup` and `$unionWith` are validated to ensure the correct use of `from` and `coll` fields:

- For `$lookup`, omit the `from` field if you use a subpipeline with a stage which doesn't require a specified collection. For example, a [`$documents`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/documents/#mongodb-pipeline-pipe.-documents) stage.

- Similarly, for `$unionWith`, omit the `coll` field.

Unchanged behavior:

- For a `$lookup` that starts with a stage for a collection, for example a [`$match`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/match/#mongodb-pipeline-pipe.-match) or [`$collStats`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/collStats/#mongodb-pipeline-pipe.-collStats) subpipeline, you must include the `from` field and specify the collection.

- Similarly, for `$unionWith`, include the `coll` field and specify the collection.

The following scenario shows an example.

Create a collection `cakeFlavors`:

```javascript
db.cakeFlavors.insertMany( [
   { _id: 1, flavor: "chocolate" },
   { _id: 2, flavor: "strawberry" },
   { _id: 3, flavor: "cherry" }
] )
```

Starting in MongoDB 8.0, the following example returns an error because it contains an invalid `from` field:

```javascript
db.cakeFlavors.aggregate( [ {
   $lookup: {
      from: "cakeFlavors",
      pipeline: [ { $documents: [ {} ] } ],
      as: "test"
   }
} ] )
```

In MongoDB versions before 8.0, the previous example runs.

For an example with a valid `from` field, see [Perform a Single Equality Join with `$lookup`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/lookup/#std-label-lookup-single-equality-example).

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

The following `Comment` class models the documents in the `sample_mflix.comments` collection:

```csharp
public class Comment
{
    public Guid Id { get; set; }

    [BsonElement("movie_id")]
    public Guid MovieId { get; set; }

    public string Text { get; set; }
}
```

`$lookup`

[Lookup()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Lookup.html)

performs a left outer join between the `movies` and `comments` collections. The code joins the `Id` field from each `Movie` document to the `MovieId` field in the `Comment` documents. The comments for each movie are stored in a field named `Comments` in each `Movie` document.

To use the MongoDB .NET/C# driver to add a `$lookup` stage to an aggregation pipeline, call the [Lookup()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Lookup.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that performs a left outer join between the `movies` and `comments` collections. The code joins the `Id` field from each `Movie` document to the `MovieId` field in the `Comment` documents. The comments for each movie are stored in a field named `Comments` in each `Movie` document.

```csharp
var commentCollection = client
    .GetDatabase("aggregation_examples")
    .GetCollection<Comment>("comments");

var pipeline = new EmptyPipelineDefinition<Movie>()
    .Lookup<Movie, Movie, Comment, Movie>(
        foreignCollection: commentCollection,
        localField: m => m.Id,
        foreignField: c => c.MovieId,
        @as: m => m.Comments);
```

</Tab>

<Tab name="Node.js">

The Node.js examples on this page use the `sample_mflix` database from the [Atlas sample datasets](https://www.mongodb.com/docs/atlas/sample-data/). To learn how to create a free MongoDB Atlas cluster and load the sample datasets, see [Get Started](https://www.mongodb.com/docs/drivers/node/current/get-started/) in the MongoDB Node.js driver documentation.

`$lookup`

performs a left outer join between the `movies` and `comments` collections. The code joins the `_id` field from each `movie` document to the `movie_id` field in the `comment` documents. The `comments` field stores the comments for each movie in each `movie` document

To use the MongoDB Node.js driver to add a `$lookup` stage to an aggregation pipeline, use the `$lookup` operator in a pipeline object.

The following example creates a pipeline stage that performs a left outer join between the `movies` and `comments` collections. The code joins the `_id` field from each `movie` document to the `movie_id` field in the `comment` documents. The `comments` field stores the comments for each movie in each `movie` document. The example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "movie_id",
      as: "comments"
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

</Tab>

</Tabs>


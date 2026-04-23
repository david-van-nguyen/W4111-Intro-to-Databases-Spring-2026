# $limit (aggregation stage)

## Definition

`$limit`
Limits the number of documents passed to the next stage in the [pipeline](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/glossary/#std-term-pipeline).

## Compatibility

`$limit`You can use `$limit` for deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully managed service for MongoDB deployments in the cloud

- [MongoDB Enterprise](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-enterprise/#std-label-install-mdb-enterprise): The subscription-based, self-managed version of MongoDB

- [MongoDB Community](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/administration/install-community/#std-label-install-mdb-community-edition): The source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) stage has the following prototype form:

```javascript
{ $limit: <positive 64-bit integer> }
```

[`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) takes a positive integer that specifies the maximum number of documents to pass along.

Starting in MongoDB 5.0, the [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) pipeline aggregation has a 64-bit integer limit. Values passed to the pipeline which exceed this limit will return a invalid argument error.

## Behavior

### Using $limit with Sorted Results

If using the [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) stage with any of:

- the [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) aggregation stage,

- the [`sort()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/cursor.sort/#mongodb-method-cursor.sort) method, or

- the `sort` field to the [`findAndModify`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/command/findAndModify/#mongodb-dbcommand-dbcmd.findAndModify) command or the [`findAndModify()`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify) shell method,

be sure to include at least one field in your sort that contains unique values, before passing results to the [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) stage.

Sorting on fields that contain duplicate values may return an inconsistent sort order for those duplicate fields over multiple executions, especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the `_id` field in your sort query.

See the following for more information on each:

- [Consistent sorting with $sort (aggregation)](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#std-label-sort-aggregation-consistent-sorting)

- [Consistent sorting with the sort() shell method](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/cursor.sort/#std-label-sort-cursor-consistent-sorting)

- [Consistent sorting with the findAndModify command](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/command/findAndModify/#std-label-findandmodify-command-consistent-sorting)

- [Consistent sorting with the findAndModify() shell method](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/method/db.collection.findAndModify/#std-label-findandmodify-method-consistent-sorting)

## Examples

<Tabs>

<Tab name="MongoDB Shell">

Consider the following example:

```javascript
db.article.aggregate([
   { $limit : 5 }
]);
```

This operation returns only the first 5 documents passed to it by the pipeline. [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) has no effect on the content of the documents it passes.

</Tab>

<Tab name="C#">

`$limit`

[Limit()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Limit.html)

limits the number of returned documents to `10`:

To use the MongoDB .NET/C# driver to add a `$limit` stage to an aggregation pipeline, call the [Limit()](https://mongodb.github.io/mongo-csharp-driver/3.7.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Limit.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that limits the number of returned documents to `10`:

```csharp
var pipeline = new EmptyPipelineDefinition<BsonDocument>()
    .Limit(10);
```

</Tab>

<Tab name="Node.js">

`$limit`

limits the number of returned documents to `10`

To use the MongoDB Node.js driver to add a `$limit` stage to an aggregation pipeline, use the `$limit` operator in a pipeline object.

The following example creates a pipeline stage that limits the number of returned documents to `10`. The example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $limit: 10 }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

</Tab>

</Tabs>

When a [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) precedes a [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) and there are no intervening stages that modify the number of documents, the optimizer can coalesce the [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) into the [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort). This allows the [`$sort`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/sort/#mongodb-pipeline-pipe.-sort) operation to only maintain the top `n` results as it progresses, where `n` is the specified limit, and ensures that MongoDB only needs to store `n` items in memory. This optimization still applies when `allowDiskUse` is `true` and the `n` items exceed the [aggregation memory limit](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/core/aggregation-pipeline-limits/#std-label-agg-memory-restrictions).

## Learn More

To learn how to use [`$limit`](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/reference/operator/aggregation/limit/#mongodb-pipeline-pipe.-limit) in a full example, see the [Filter Data](https://mongodbcom-cdn.staging.corp.mongodb.com/docs/tutorial/aggregation-examples/filtered-subset/#std-label-agg-example-filter-data) tutorial.


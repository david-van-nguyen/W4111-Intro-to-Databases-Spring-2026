# W4111 - Introduction to Databases, Spring 2026: Exam 3 Sample Question Answers

## Q1 - Functional Dependencies

1. Meaningful non-trivial functional dependencies visible from the sample data include:
   - `A -> B, D`
   - `D -> A, B`
   - `E -> A, B, C, D`, because every `E` value is unique.
   - `(A, C) -> E`, because each shown `(A, C)` pair uniquely identifies one tuple.
   - `(D, C) -> E`, for the same reason.

2. Specific functional dependencies:
   - (a) `A -> D` holds. Each value of `A` is associated with exactly one value of `D`.
   - (b) `B -> A` does not hold. `B = b1` appears with both `A = a1` and `A = a2`.
   - (c) `A -> B` holds. Each value of `A` is associated with exactly one value of `B`.
   - (d) `(A, C) -> E` holds. Each `(A, C)` combination appears once and determines one `E`.

3. A candidate key is `E`, because every `E` value is unique in the sample and therefore determines all other attributes. Another candidate key is `(A, C)`, since each pair uniquely identifies a tuple and neither `A` nor `C` alone is sufficient.

4. `C -> E` does not hold. For example, `C = c1` appears with `E = e1`, `e3`, and `e5`.

## Q2 - 3NF vs. BCNF

1. The only candidate key is `A`. Since `A -> B` and `B -> C`, the closure of `A` is `A+ = {A, B, C}`.

2. `R` is not in 3NF. The dependency `B -> C` violates 3NF because `B` is not a superkey and `C` is not a prime attribute.

3. `R` is not in BCNF. The dependency `B -> C` violates BCNF because `B` is not a superkey.

4. A BCNF decomposition is:
   - `R1(B, C)`
   - `R2(A, B)`

## Q3 - Join Algorithms

1. A nested-loop join compares each tuple in the outer relation with tuples in the inner relation. An indexed nested-loop join uses an index on the inner relation's join attribute to find matches. A merge join sorts both relations on the join attribute and scans them together. A hash join partitions/builds hash tables on the join attributes to find matching tuples.

2. Nested-loop join works for any join condition but is usually expensive. Indexed nested-loop join is preferred when the join is an equi-join or natural join and the inner relation has an index on the join attribute. Merge join is preferred when inputs are already sorted, or sorting is cheap, and the join is an equi-join or natural join. Hash join is preferred for equi-joins or natural joins when hash partitions fit well in memory.

3. The outer versus inner choice matters because the inner relation may be scanned or probed once for every tuple in the outer relation. A smaller outer relation, or an indexed inner relation, can greatly reduce I/O.

## Q4 - Access Costs

1. Approximate costs as a function of `N`:
   - Full table scan: `O(N)`
   - B+-tree index lookup: `O(log N)`, plus the cost of fetching matching records
   - Hash lookup: average `O(1)` for equality lookup

2. Building an index can be beneficial because the one-time build and maintenance cost can be outweighed by faster selections, lookups, joins, and repeated query execution.

3. A plan that is optimal for one operation may not be optimal for the whole query because operators interact. For example, a merge join might cost more than a hash join locally but produce sorted output that makes a later aggregation cheaper.

## Q5 - Materialization vs. Pipelining

1. Materialization evaluates an operation and stores its intermediate result, often as a temporary relation. Pipelining passes tuples from one operator directly to the next without storing the full intermediate result.

2. Materialization is always applicable and simple to reason about, but writing and reading temporary results can be expensive. Pipelining avoids much of that temporary I/O and can be faster, but it requires operators that can produce and consume tuples incrementally.

3. Pipelining cannot always be used because some operators are blocking. Sorting, some aggregation strategies, and hash join may need to consume a full input before producing output.

## Q6 - Logical vs. Physical Plans

1. Two equivalent relational algebra expressions are:
   - `pi_name(sigma_salary < 75000(instructor))`
   - `pi_name(sigma_salary < 75000(pi_name, salary(instructor)))`

2. The first expression is likely more efficient if the DBMS can use an index on `salary` or otherwise push the selection down. Filtering early reduces the number of tuples carried through the rest of the plan.

## Q7 - Conjunctive vs. Disjunctive Selection

1. For `WHERE name = 'Smith' AND dept_name = 'CS'`, the index on `name` helps the DBMS find rows with `name = 'Smith'`, then it can test `dept_name = 'CS'` on those fetched rows.

2. For `WHERE name = 'Smith' OR dept_name = 'CS'`, the index on `name` alone is usually not enough, because rows with `dept_name = 'CS'` and a different name still must be found. Without an index on `dept_name`, the DBMS may need a scan.

3. The index helps the conjunction because one indexed condition can reduce the candidate rows. For the disjunction, all branches generally need index support to avoid scanning for the unindexed condition.

## Q8 - Join Algorithm Selection

1. An indexed nested-loop join is most appropriate.

2. `R` should be the outer relation because it has only 1,000 tuples. For each tuple in `R`, the DBMS can use the index on `S.join_attr` to find matching tuples in the much larger `S`.

## Q9 - Transaction Execution

1. If the transaction fails after updating account `A` but before updating account `B`, the debit from `A` is reflected but the credit to `B` is not. Money is effectively lost and the database is inconsistent.

2. The violated ACID property is atomicity.

3. The DBMS prevents this with transaction management, logging/write-ahead logging, rollback/undo, and recovery. The transaction's updates are either all committed or all undone.

## Q10 - Isolation Levels

- Read Uncommitted: dirty reads can occur.
- Read Committed: non-repeatable reads can occur.
- Repeatable Read: phantom reads can occur; write skew may also be possible in some systems.
- Serializable: no standard isolation anomaly should occur, because the result must be equivalent to some serial execution.

## Q11 - ACID vs. BASE

1. BASE stands for Basically Available, Soft state, Eventually consistent.

2. ACID emphasizes strong transaction correctness: atomicity, consistency, isolation, and durability. BASE relaxes immediate consistency in order to improve availability, scalability, and partition tolerance in distributed systems.

3. A system may prefer BASE when high availability and scale are more important than immediate consistency, such as in globally distributed services where replicas update asynchronously.

## Q12 - Concurrency Control

1. Strict Two-Phase Locking requires a transaction to acquire shared locks before reading and exclusive locks before writing, and to hold its locks until the transaction completes.

2. It guarantees serializability because locks constrain conflicting operations so the resulting schedule is equivalent to a serial order.

3. It helps prevent cascading aborts, because other transactions cannot read data written by an uncommitted transaction.

## Q13 - Scaling and Architecture

1. Scale-up means replacing a machine with a larger machine, such as one with more CPU, memory, or disk. Scale-out means adding more machines and distributing the workload.

2. A shared-nothing architecture partitions data across independent nodes. Each node has its own CPU, memory, and disk, and requests are routed to the correct shard.

3. Scale-out is challenging for relational operations like joins because related data may be on different nodes. The system may need distributed coordination, data movement, and distributed locking or consistency mechanisms.

## Q14 - Serializability

1. Serializability means that a concurrent schedule has the same effect as some serial execution of the same transactions.

2. It is the main correctness criterion because if each transaction preserves consistency on its own, then any schedule equivalent to a serial execution also preserves consistency.

3. Conflict serializability is based on whether a schedule can be transformed into a serial schedule by swapping non-conflicting operations; it can be tested with an acyclic precedence graph. View serializability is more general and asks whether transactions read the same values and produce the same final writes as some serial schedule.

## Q15 - Cascading Rollbacks

1. A cascading rollback occurs when one transaction aborts and forces other transactions to abort because they read data written by the aborted transaction.

2. It is undesirable because it can undo a large amount of work and complicates recovery.

3. Cascadeless schedules prevent this by requiring a transaction to read another transaction's written data only after the writer has committed.

## Q16 - Strict Two-Phase Locking (2PL)

1. The rules of Strict 2PL are: acquire a shared lock before reading, acquire an exclusive lock before writing, do not allow incompatible locks on the same item, and release locks only when the transaction commits or aborts.

2. It guarantees serializability because the locking rules prevent conflicting operations from interleaving in a way that cannot be represented by a serial order.

3. It simplifies recovery because uncommitted writes are not read by other transactions, reducing or eliminating cascading aborts.

## Q17 - Resource-Oriented Design

1. Possible REST endpoints:
   - Retrieve all sections of a course: `GET /courses/{courseId}/sections`
   - Retrieve all participants in a section: `GET /courses/{courseId}/sections/{sectionId}/participants`

2. A resource is an individual thing with identity and state, such as one course or one section. A collection resource is a container/list of resources of the same type, such as all sections for a course.

## Q18 - Data Engineering Pipeline

1. ETL steps are Extract, Transform, and Load. Data is extracted from source systems, transformed into a clean/common schema, and loaded into the target warehouse or analytics system.

2. ETL transforms data before loading it into the target system. ELT loads raw data first and then performs transformations inside the target system.

3. Data engineering is often the most time-consuming part of analytics because data comes from many sources, has inconsistent formats, contains errors or missing values, and must be integrated into a usable structure before analysis.

## Q19 - Deadlock Prevention vs. Detection

1. Deadlock prevention uses rules that ensure the system never enters a deadlock state. Deadlock detection allows deadlocks to occur, periodically detects them, and resolves them by rolling back one or more transactions.

2. Example prevention techniques:
   - Wait-die: older transactions may wait for younger transactions, but younger transactions abort rather than wait for older ones.
   - Wound-wait: older transactions force younger transactions to roll back, while younger transactions may wait for older ones.
   - Timeout: a transaction waits only for a fixed amount of time before being rolled back.

3. A wait-for graph has transactions as vertices. There is an edge from `Ti` to `Tj` if `Ti` is waiting for a lock held by `Tj`. A cycle indicates a deadlock.

## Q20 - Star Schema Design

1. A fact table stores measurable business events or facts, such as sales transactions.

2. Dimension tables store descriptive context for facts, such as date, product, customer, or location.

3. Example:
   - Fact: `revenue = quantityOrdered * priceEach`
   - Dimensions: `Date(year, quarter, month)` and `Product(productLine, productScale)`

4. This model is useful for analytics because it makes aggregation, roll-up, drill-down, slicing, dicing, and pivot-style queries easier and efficient.

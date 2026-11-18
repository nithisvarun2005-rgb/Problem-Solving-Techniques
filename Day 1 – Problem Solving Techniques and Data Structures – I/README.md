# SET-1

# Online Retailer – Data Structures and Algorithms

## Project Overview

An online retailer processes approximately 50,000 orders per day. Support agents need to retrieve orders quickly, warehouse employees need to rank orders for dispatch, and finance teams need to identify duplicate orders before payment processing.

This project implements searching, sorting, duplicate detection, Stack, Queue, Greedy and Dynamic Programming algorithms using Python.

## Technologies Used

- Python 3
- CSV file handling
- `time` module for benchmarking
- `random` module for test data generation
- `collections.deque` for Queue implementation

## Dataset

**File:** `orders.csv`

The dataset contains the following columns:

| Column | Description |
|---|---|
| orderId | Unique order identifier |
| customerId | Customer identifier |
| amount | Order amount |
| createdAt | Order creation date and time |

A 50,000-record dataset is used for searching benchmarks, and a 10,000-record dataset is used for sorting benchmarks.

## Tasks Completed

### Task 1 – Linear Search and Binary Search

Implemented:

- Linear Search to retrieve an order by ID.
- Binary Search to retrieve an order by ID from sorted data.
- Performance benchmarking on 50,000 orders.
- Comparison of execution times and complexity.

**Time Complexity:**

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

**Space Complexity:** O(1) for both search algorithms.

### Task 2 – Sorting Algorithms

Implemented:

- Bubble Sort – O(n²)
- Merge Sort – O(n log n)
- Python Built-in Sort – O(n log n)

Features:

- Sort orders by amount in descending order.
- Trace the first three passes.
- Benchmark all three algorithms on 10,000 records.
- Compare execution times.

**Space Complexity:**

- Bubble Sort: O(n) including the copied input list.
- Merge Sort: O(n).
- Python Built-in Sort: O(n) auxiliary space in this implementation.

### Task 3 – Duplicate Order Detection

Used a hash-based Python `set` to identify duplicate orders.

Duplicate conditions:

- Same `customerId`.
- Same `amount`.
- Same creation minute.

**Time Complexity:**
- Average: O(n) for processing all orders.
- Worst case: O(n²) due to hash collisions.

**Space Complexity:** O(n).

### Task 4 – Stack and Queue

Implemented custom and built-in data structures.

**Stack:**
- Follows LIFO (Last In, First Out).
- Supports undoing the most recent order edit.
- Implemented using a Python list.

**Queue:**
- Follows FIFO (First In, First Out).
- Models the warehouse dispatch line.
- Implemented using a custom list-based Queue and Python `collections.deque`.

**Time Complexity:**

| Operation | Complexity |
|---|---|
| Stack Push | O(1) amortized |
| Stack Pop | O(1) amortized |
| Queue Enqueue using list | O(1) amortized |
| Queue Dequeue using list `pop(0)` | O(n) |
| Queue Enqueue using deque | O(1) |
| Queue Dequeue using deque `popleft()` | O(1) |

**Space Complexity:** O(n).

### Task 5 – Greedy and Dynamic Programming

Implemented minimum notes and coins calculation for a refund amount.

**Greedy Approach:**
- Selects the largest possible denomination first.
- Efficient for suitable denomination systems.
- May not always produce the minimum number of coins.

**Dynamic Programming:**
- Considers all valid denominations.
- Finds the minimum number of coins when a solution exists.
- Demonstrated using amount 6 and denominations `[4, 3, 1]`.

Greedy result: 3 coins (4 + 1 + 1).

Dynamic Programming result: 2 coins (3 + 3).

**Time and Space Complexity:**

| Algorithm | Time | Space |
|---|---|---|
| Greedy with sorted denominations | O(d) | O(d) for result |
| Dynamic Programming | O(A × d) | O(A) |

Where A is the refund amount and d is the number of denominations.

## Project Structure

```text
Day 1 – Problem Solving Techniques and Data Structures – I/SET-I
│
├── README.md
├── orders.csv
│
├── Day1_Set 1.py
├── Day 1 Set 1 Output.docx
```
## Conclusion

This project demonstrates how appropriate algorithms and data structures can improve the performance of an online retailer's order-processing system.

Binary Search supports fast retrieval, efficient sorting helps warehouse dispatch, hash sets identify duplicate submissions, Stack and Queue manage order operations, and Dynamic Programming finds optimal refund denominations when Greedy fails.

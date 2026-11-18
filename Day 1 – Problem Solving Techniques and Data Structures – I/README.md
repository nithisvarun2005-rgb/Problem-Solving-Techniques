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
Day 1 – Problem Solving Techniques and Data Structures – I/SET-1
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

# SET-2

# Retail Bank – Card Transaction Processing using Data Structures and Algorithms

## 1. Project Overview

This project demonstrates the use of fundamental Data Structures and Algorithms to process daily card transactions in a retail bank.

The bank's operations team reviews daily card transactions. Auditors require quick transaction lookups, correctly ordered customer statements, duplicate transaction detection, efficient manual-review management, and identification of the highest and lowest transaction amounts.

The project implements these operations using Python.

## 2. Business Scenario

A retail bank processes a large number of card transactions every day.

The operations team needs to:

- Search transactions quickly using transaction IDs.
- Sort customer statements by posting date.
- Detect duplicate transaction postings.
- Manage manual-review requests in the order they arrive.
- Reverse the most recent transaction adjustment.
- Find the highest and lowest transaction amounts in a day's file.

## 3. Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** List, Hash Set, Queue, Stack
- **Algorithms:** Binary Search, Linear Search, Insertion Sort, Merge Sort, Divide and Conquer
- **Modules:** `time`, `random`, `csv` (where required)

## 4. Project Tasks

### Task 1 – Binary Search and Linear Search

**Objective:** Search a sorted list of 100,000 transaction IDs.

Algorithms implemented:
- Linear Search
- Binary Search

Comparison metrics:
- Best-case comparisons
- Average-case comparisons
- Worst-case comparisons
- Execution time

**Time Complexity:**

| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |

**Space Complexity:**
- Linear Search: O(1)
- Binary Search: O(1) using an iterative implementation.

Binary search is more efficient for large sorted transaction ID lists.

### Task 2 – Insertion Sort and Merge Sort

**Objective:** Sort a customer's transaction statement by posting date.

Algorithms implemented:
- Insertion Sort
- Merge Sort

The project compares their performance and demonstrates stable sorting.

**Stability:**

A stable sorting algorithm preserves the original relative order of transactions having the same posting timestamp.

This is important when multiple transactions share the same timestamp because their original sequence remains unchanged.

**Time and Space Complexity:**

| Algorithm | Best | Average | Worst | Space |
|---|---|---|---|---|
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

### Task 3 – Duplicate Transaction Detection

**Objective:** Identify duplicate postings based on:

- Same account ID
- Same transaction amount
- Same merchant
- Transactions posted within 60 seconds

A Hash Set or Hash Map is used to efficiently identify matching transaction details.

**Complexity:**

- Average Time Complexity: O(n) for processing all transactions.
- Worst-case Time Complexity: O(n²) due to hash collisions.
- Space Complexity: O(n).

The implementation checks the timestamps of matching transaction keys to identify duplicates within the 60-second window.

### Task 4 – Stack and Queue Implementation

**Objective:** Model bank operations using Stack and Queue without using library collections initially.

**Queue – Manual Review Backlog**

- Follows FIFO (First In, First Out).
- The first transaction submitted for manual review is processed first.
- Supports enqueue and dequeue operations.

**Stack – Reverse Last Adjustment**

- Follows LIFO (Last In, First Out).
- The most recent adjustment is reversed first.
- Supports push and pop operations.

**Complexity:**

| Data Structure | Operation | Time Complexity |
|---|---|---|
| Queue | Enqueue | O(1) |
| Queue | Dequeue | O(1) |
| Stack | Push | O(1) |
| Stack | Pop | O(1) |

Space Complexity for both: O(n).

The queue uses an efficient implementation so removing the first element does not require shifting all remaining elements.

### Task 5 – Divide and Conquer for Minimum and Maximum

**Objective:** Find the highest and lowest transaction amounts in a day's transaction file.

Two approaches are implemented:

1. Brute-force scan
2. Divide-and-conquer approach

**Brute-force approach:**
- Traverse the entire transaction list.
- Update the minimum and maximum amounts whenever necessary.

**Divide-and-conquer approach:**
- Divide the transaction list into smaller parts.
- Find the minimum and maximum in each part.
- Combine the results to obtain the overall minimum and maximum.

**Complexity Comparison:**

| Approach | Best | Average | Worst | Space |
|---|---|---|---|---|
| Brute Force | O(n) | O(n) | O(n) | O(1) |
| Divide and Conquer | O(n) | O(n) | O(n) | O(log n) |

Both approaches have linear time complexity. An optimized divide-and-conquer implementation


## Project Structure

```text
Day 1 – Problem Solving Techniques and Data Structures – I/SET-2
│
├── README.md
├── transactions.csv
│
├── Day1 Set 2 .py
├── Day 1 Set 2 Output.docx

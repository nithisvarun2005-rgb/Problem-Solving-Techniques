# Set 1 – E-Commerce Catalogue and Traffic Analysis

## Business Scenario

An e-commerce platform wants faster category browsing, instant SKU look-ups and an efficient way to analyse peak traffic for infrastructure planning.

This project applies different Data Structures and Algorithms (DSA) concepts to improve product catalogue management, SKU searching, microservice deployment, traffic analysis and gift-card order matching.

## Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** Binary Search Tree, Hash Table, Hash Map, Graph, List
- **Algorithms:** BFS, DFS, Sliding Window, Two Pointers
- **Libraries:** `time`

## Project Objectives

1. Build a Binary Search Tree containing 15 product categories and perform insertion, searching and tree traversals.
2. Implement a hash table with chaining for SKU look-up, demonstrate collision handling and compare it with Python's built-in dictionary.
3. Model microservice deployment dependencies using a graph, find a valid deployment order and detect circular dependencies.
4. Identify the busiest continuous three-hour window from 24 hours of request data using Sliding Window.
5. Find all pairs of order values that equal a given gift-card value using Two Pointers.

---

# Question 1 – Binary Search Tree for Product Categories

## Problem Statement

Build a Binary Search Tree of 15 product categories. Implement insertion and searching operations and display inorder, preorder and postorder traversals.

## Implementation

- Created a Node class to represent each product category.
- Inserted 15 product categories into a BST.
- Implemented a search operation to find a category.
- Implemented three tree traversals:
  - Inorder: Left → Root → Right
  - Preorder: Root → Left → Right
  - Postorder: Left → Right → Root

## Sample Input

```python
categories = [
    "Electronics", "Clothing", "Home",
    "Books", "Footwear", "Furniture",
    "Beauty", "Grocery", "Mobiles",
    "Sports", "Toys", "Watches",
    "Jewellery", "Kitchen", "Laptops"
]
```

## Expected Output

```text
PRODUCT CATEGORY BST

Total Categories: 15

Search Electronics: True
Search Fashion: False

Inorder Traversal:
Beauty Books Clothing Electronics Footwear
Furniture Grocery Home Jewellery Kitchen
Laptops Mobiles Sports Toys Watches

Preorder Traversal:
Electronics Clothing Books Beauty Footwear
Furniture Home Grocery Kitchen Jewellery
Laptops Mobiles Sports Toys Watches

Postorder Traversal:
Beauty Books Furniture Footwear Kitchen
Grocery Jewellery Home Clothing Laptops
Mobiles Sports Toys Watches Electronics
```

## Observation

- Inorder traversal displays categories in alphabetical order.
- Preorder traversal visits the root before its subtrees.
- Postorder traversal visits the subtrees before the root.
- BST searching is efficient when the tree is reasonably balanced.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Insertion | O(log n) | O(n) |
| Search | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

---

# Question 2 – Hash Table with Chaining for SKU Look-up

## Problem Statement

Implement a small hash table with chaining for SKU look-up, demonstrate a collision and compare its performance with Python's built-in hash map using 100,000 SKUs.

## Implementation

- Created a hash table using a fixed number of buckets.
- Implemented a hash function to calculate the bucket index.
- Used chaining to handle collisions.
- Inserted SKU values into the hash table.
- Demonstrated a collision using two different SKUs that produce the same bucket index.
- Implemented the same SKU look-up using Python's built-in dictionary.
- Compared the look-up times for 100,000 SKUs.

## Collision Handling

A collision occurs when two different SKU values generate the same hash index.

Chaining handles collisions by storing multiple entries in the same bucket using a list.

Example:

```text
Bucket 2:
SKU101 → SKU104 → SKU108
```

All three SKUs can be stored in the same bucket.

## Sample Output

```text
SKU HASH TABLE

SKU101 inserted successfully
SKU104 inserted successfully

Collision Detected!
SKU101 and SKU104 are stored in the same bucket.

SKU Search:
SKU101 Found
SKU999 Not Found
```

## Built-in Hash Map Comparison

```text
SKU LOOK-UP PERFORMANCE

Total SKUs: 100000

Custom Hash Table Lookup Time: Depends on execution
Built-in Dictionary Lookup Time: Depends on execution
```

The actual execution times are measured using Python's `time` module. They may differ depending on the computer, Python version and system load.

## Observation

- A custom hash table demonstrates how hashing and chaining work internally.
- Python's built-in dictionary provides optimized hash-based searching.
- Hash maps generally provide O(1) average-case look-up time.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Collision handling | O(1) average per operation | O(n) |

---

# Question 3 – Graph for Microservice Deployment Dependencies

## Problem Statement

Model microservice deployment dependencies such as Cart, Pricing and Inventory using a graph. Produce a valid deployment order using BFS/DFS and detect circular dependencies.

## Sample Microservices

- Cart
- Pricing
- Inventory
- Payment
- Order
- Notification

## Dependency Representation

```text
Cart → Pricing
Cart → Inventory
Pricing → Payment
Inventory → Order
Payment → Order
Order → Notification
```

A directed edge A → B means service A depends on service B. Therefore, B must be deployed before A.

## Implementation

- Represented microservices using a directed graph.
- Used an adjacency list to store dependencies.
- Used topological sorting to determine a valid deployment order.
- Used DFS to detect circular dependencies.
- Introduced a circular dependency to demonstrate cycle detection.

## Expected Output

```text
MICROSERVICE DEPLOYMENT

Valid Deployment Order:
Pricing
Inventory
Payment
Order
Cart
Notification
```

Any valid topological ordering that respects all dependencies is acceptable.

```text
CIRCULAR DEPENDENCY DETECTION

Without Cycle:
False

After Introducing Circular Dependency:
True
```

## Observation

- A graph represents dependencies between microservices.
- Topological sorting produces a valid deployment order for a directed acyclic graph.
- DFS detects circular dependencies.
- A circular dependency prevents a valid topological deployment order.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| BFS / Topological Sorting | O(V + E) |
| DFS Cycle Detection | O(V + E) |

Here:
- V = Number of vertices (microservices).
- E = Number of edges (dependencies).

---

# Question 4 – Sliding Window for Peak Traffic Analysis

## Problem Statement

Given requests-per-minute data for 24 hours, identify the busiest continuous three-hour window using a Sliding Window algorithm.

## Sample Input

The following sample represents the total number of requests recorded per hour.

```python
requests = [
    120, 150, 180, 200, 220, 250,
    300, 350, 400, 450, 500, 550,
    600, 650, 700, 750, 800, 850,
    900, 950, 1000, 900, 850, 800
]
```

## Implementation

- Stored hourly request counts in a list.
- Used a window size of 3 hours.
- Calculated the sum of the first three hours.
- Moved the window forward by removing the outgoing value and adding the incoming value.
- Tracked the maximum total and calculated the average.

## Expected Output

```text
PEAK TRAFFIC ANALYSIS

Window Size: 3 Hours

Busiest Window:
Hour 19 to Hour 21

Total Requests: 2850

Average Requests:
950.0 per hour
```

## Observation

- Sliding Window avoids recalculating the sum for every three-hour period.
- It updates the current window by subtracting the outgoing hour and adding the incoming hour.
- The busiest window helps identify periods requiring additional infrastructure capacity.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Initial Window Calculation | O(k) |
| Sliding Window | O(n) |
| Overall | O(n) |

Where:
- n = Number of hourly records.
- k = Window size (3).

---

# Question 5 – Two Pointers for Gift-Card Order Matching

## Problem Statement

Given a sorted list of order values, use Two Pointers to find all pairs whose sum equals the gift-card value.

## Sample Input

```python
order_values = [
    100, 150, 200, 250,
    300, 350, 400, 450
]

gift_card = 550
```

## Implementation

- Used a sorted list of order values.
- Initialized two pointers:
  - Left pointer at the first element.
  - Right pointer at the last element.
- Calculated the sum of both values.
- If the sum equals the gift-card value, displayed the pair.
- If the sum is smaller, moved the left pointer forward.
- If the sum is greater, moved the right pointer backward.
- Continued until both pointers met.

## Expected Output

```text
GIFT CARD PAIR MATCHING

Gift Card Value: 550

Matching Pairs:

100 + 450 = 550
150 + 400 = 550
200 + 350 = 550
250 + 300 = 550
```

## Observation

- Two Pointers efficiently finds matching pairs in a sorted list.
- The algorithm avoids checking every possible pair.
- The input list must already be sorted.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Pair Matching | O(n) |
| Auxiliary Space | O(1), excluding output |

---

# Final Decision Table

| Question | Problem | Data Structure / Pattern | Reason |
|---|---|---|---|
| 1 | Product category management | Binary Search Tree | Supports insertion, searching and sorted traversal |
| 2 | SKU look-up | Hash Table with Chaining / Hash Map | Provides fast look-up and collision handling |
| 3 | Microservice deployment | Graph, BFS and DFS | Represents dependencies, finds deployment order and detects cycles |
| 4 | Peak traffic analysis | Sliding Window | Identifies the busiest continuous three-hour period efficiently |
| 5 | Gift-card order matching | Two Pointers | Finds matching pairs in a sorted list without nested loops |

---

# Overall Complexity Summary

| Question | Algorithm | Time Complexity |
|---|---|---|
| 1 | BST Insert and Search | O(log n) average |
| 2 | Hash Table Look-up | O(1) average |
| 3 | BFS / DFS | O(V + E) |
| 4 | Sliding Window | O(n) |
| 5 | Two Pointers | O(n) |

---

# Conclusion

This project demonstrates how different Data Structures and Algorithms can solve practical e-commerce problems.

1. **Binary Search Tree:** Organizes product categories and supports efficient searching.
2. **Hash Table:** Provides fast SKU look-ups and handles collisions.
3. **Graph:** Represents microservice dependencies and supports deployment planning.
4. **Sliding Window:** Identifies peak traffic periods for infrastructure planning.
5. **Two Pointers:** Finds order-value pairs that match a gift-card amount.

These techniques improve searching efficiency, data organization, dependency management and performance analysis in an e-commerce platform.


## Project Structure

```text
E-Commerce-Catalogue-and-Traffic-Analysis/SET-1
│
├── question1_bst.py
├── question2_hash_table.py
├── question3_microservice deployment dependencies.py
├── question4_sliding_window.py
├── question5_two_pointers.py
│
└── README.md
```


# Set 2 - Insurance Claims Processing – Data Structures and Algorithms

## Business Scenario

An insurance company needs an efficient system to manage claim submissions, route claims through approval stages, detect duplicate claims and monitor sudden increases in claim volume after regional events.

This project demonstrates the use of Data Structures and Algorithms (DSA) to improve claim management, searching, duplicate detection, workflow processing and data analysis.

## Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** Binary Search Tree, Hash Table, Graph, List
- **Algorithms:** BFS, DFS, Sliding Window, Two Pointers
- **Libraries:** `collections`

## Project Objectives

1. Create a Binary Search Tree of claim IDs with insertion, searching and three traversals.
2. Detect duplicate and near-duplicate claims using hashing and normalization.
3. Represent claim approval stages using a directed graph and find shortest paths using BFS and loops using DFS.
4. Find the longest consecutive run of days on which claims exceeded 100 using Sliding Window.
5. Merge two sorted claim lists from regional offices using Two Pointers without additional sorting.

---

# Question 1 – Binary Search Tree for Claim IDs

## Problem Statement

Create a Binary Search Tree of claim IDs and implement insertion and searching. Display inorder, preorder and postorder traversals and identify which traversal produces sorted claim IDs.

## Implementation

- Created a Node class to represent each claim ID.
- Implemented BST insertion.
- Implemented claim ID searching.
- Implemented three tree traversals:
  - Inorder: Left → Root → Right
  - Preorder: Root → Left → Right
  - Postorder: Left → Right → Root

## Sample Input

```python
claim_ids = [
    105, 102, 108, 101, 104,
    107, 110, 103, 106, 109
]
```

## Expected Output

```text
CLAIM ID BST

Inorder Traversal:
101 102 103 104 105 106 107 108 109 110

Preorder Traversal:
105 102 101 104 103 108 107 106 110 109

Postorder Traversal:
101 103 104 102 106 107 109 110 108 105

Search Claim 105: True
Search Claim 120: False
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal insertion | 105, 102, 108 | All IDs inserted |
| Search existing ID | 105 | True |
| Search missing ID | 120 | False |
| Empty BST search | Empty tree, search 105 | False |
| Duplicate ID | Insert 105 twice | Duplicate goes to right subtree in the given implementation |

## Observation

- Inorder traversal produces claim IDs in ascending sorted order.
- Preorder visits the root before its subtrees.
- Postorder visits the root after its subtrees.
- Searching is efficient when the BST is balanced.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(log n) | O(n) |
| Search | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

---

# Question 2 – Hashing for Duplicate Claim Detection

## Problem Statement

Use hashing to detect duplicate or near-duplicate claims having the same policy number and incident date, even when differences occur in letter case or spacing.

## Implementation

- Used a hash table with chaining.
- Normalized policy numbers by converting them to uppercase and removing spaces.
- Normalized incident dates by removing unnecessary spaces.
- Combined policy number and incident date into a tuple key.
- Checked whether the normalized key already existed.
- Used chaining to handle hash collisions.

## Sample Input

| Claim ID | Policy Number | Incident Date |
|---|---|---|
| C101 | POL123 | 2026-11-10 |
| C102 | pol123 | 2026-11-10 |
| C103 | POL456 | 2026-11-11 |
| C104 | POL123 | 2026-11-10 |
| C105 | POL789 | 2026-11-12 |

## Expected Output

```text
CLAIM DUPLICATE DETECTION

C101 is a new claim
C102 is a duplicate of C101
C103 is a new claim
C104 is a duplicate of C102
C105 is a new claim
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| New claim | POL123, 2026-11-10 | New claim |
| Different letter case | pol123, 2026-11-10 | Duplicate |
| Extra spaces | POL123 with surrounding spaces | Duplicate |
| Different policy number | POL456, 2026-11-10 | New claim |
| Different incident date | POL123, 2026-11-11 | New claim |
| Empty policy number | Empty input | Should be rejected or handled as invalid input |

## Collision Handling

A collision occurs when two different keys produce the same hash table index.

This project uses **chaining** to handle collisions.

Example:

```text
Bucket 3:
(POL123, 2026-11-10)
(POL456, 2026-11-11)
```

Both keys can be stored in the same bucket. The program compares the complete normalized keys to distinguish a real duplicate from a hash collision.

## Observation

- Normalization helps identify claims that differ only in letter case or spacing.
- Hashing provides fast duplicate detection.
- Collision handling prevents different claims from being incorrectly identified as duplicates.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Hash calculation | O(k) | O(k) |
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Duplicate detection | O(1) average, excluding normalization | O(n) |

Here, k represents the length of the normalized key.

---

# Question 3 – Graph for Claim Approval Stages

## Problem Statement

Model the claim approval stages as a directed graph:

- Registration
- Assessment
- Surveyor
- Settlement

Find the shortest path between two stages using BFS and detect loops using DFS.

## Graph Representation

```text
Registration → Assessment
Assessment → Surveyor
Surveyor → Settlement
Settlement → End
```

The directed graph represents the movement of claims through the approval process.

## Implementation

- Represented approval stages using an adjacency list.
- Implemented BFS to find the shortest path.
- Implemented DFS to detect circular dependencies.
- Introduced a loop to test cycle detection.

## Expected Output

```text
CLAIM APPROVAL PROCESS

Shortest Approval Path:
Registration -> Assessment -> Surveyor -> Settlement

DFS Cycle Detection:
False

After Introducing a Loop:

DFS Cycle Detection:
True
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal workflow | Registration to Settlement | Shortest path found |
| Same starting and ending stage | Registration to Registration | Registration |
| Unreachable stage | No route to Settlement | No path |
| No circular dependency | Original graph | False |
| Circular dependency | Settlement → Assessment | True |
| Empty graph | No stages | No path; no cycle |

## Observation

- BFS finds the shortest path in an unweighted graph.
- DFS explores connected stages and detects cycles.
- A cycle may indicate an invalid or unintended approval workflow.

## Time Complexity

| Algorithm | Time Complexity |
|---|---|
| BFS | O(V + E) |
| DFS | O(V + E) |

Where:
- V = Number of approval stages.
- E = Number of directed connections.

---

# Question 4 – Sliding Window for Consecutive High-Claim Days

## Problem Statement

Find the longest consecutive run of days on which the number of claims exceeded 100 using the Sliding Window technique.

## Sample Input

```python
claims_per_day = [
    80, 120, 135, 110, 95, 130, 145,
    160, 90, 105, 115, 125, 70, 140
]
```

## Implementation

- Stored daily claim counts in a list.
- Used a left pointer to track the beginning of the current run.
- Used a right pointer to scan each day.
- Reset the current window when claims were 100 or fewer.
- Updated the longest consecutive run whenever a larger window was found.

## Expected Output

```text
CLAIMS ANALYSIS

Threshold: More than 100

Longest Consecutive Run: 3 days

Starting Day: 2
Ending Day: 4

Claims During Longest Run:
Day 2 : 120
Day 3 : 135
Day 4 : 110
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal data | 80, 120, 135, 110, 95 | Longest run = 3 days |
| All values exceed 100 | 110, 120, 130 | Longest run = 3 days |
| No values exceed 100 | 50, 80, 100 | Longest run = 0 days |
| Empty input | Empty list | Longest run = 0 days |
| Single qualifying day | 120 | Longest run = 1 day |

## Observation

- Sliding Window efficiently finds continuous periods satisfying a condition.
- The left pointer moves forward when a day does not meet the threshold.
- The algorithm scans the input only once.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Scan daily claim counts | O(n) |
| Update longest run | O(1) per day |
| Overall | O(n) |

Auxiliary space complexity: O(1).

---

# Question 5 – Two Pointers for Merging Regional Claim Lists

## Problem Statement

Use Two Pointers to merge two sorted claim lists from different regional offices into one sorted list without performing additional sorting.

## Sample Input

**Regional Office 1**

```python
region1 = [101, 104, 108, 112, 120]
```

**Regional Office 2**

```python
region2 = [102, 105, 109, 115, 118]
```

## Implementation

- Used two sorted input lists.
- Initialized one pointer for each list.
- Compared the values at both pointers.
- Added the smaller value to the merged list.
- Moved the corresponding pointer forward.
- Appended any remaining elements after one list was exhausted.

## Expected Output

```text
REGIONAL CLAIM MERGING

Region 1 Claims: [101, 104, 108, 112, 120]

Region 2 Claims: [102, 105, 109, 115, 118]

Merged Sorted Claims:
[101, 102, 104, 105, 108, 109, 112, 115, 118, 120]
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal lists | [101, 104], [102, 105] | [101, 102, 104, 105] |
| First list empty | [], [102, 105] | [102, 105] |
| Second list empty | [101, 104], [] | [101, 104] |
| Both lists empty | [], [] | [] |
| Duplicate IDs | [101, 104], [101, 105] | [101, 101, 104, 105] |
| Different list sizes | [101], [102, 104, 106] | [101, 102, 104, 106] |

## Observation

- Two Pointers efficiently merges sorted lists.
- No additional sorting operation is required.
- Duplicate claim IDs are retained in the merged list.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Merge two sorted lists | O(n + m) |
| Auxiliary space | O(1), excluding output |
| Output list storage | O(n + m) |

Where:
- n = Number of claims in Regional Office 1.
- m = Number of claims in Regional Office 2.

---

# Final Decision Table

| Question | Problem | Data Structure / Pattern | Reason |
|---|---|---|---|
| 1 | Claim ID management | Binary Search Tree | Supports insertion, searching and sorted traversal |
| 2 | Duplicate claim detection | Hash Table with Chaining | Quickly identifies normalized duplicate claims and handles collisions |
| 3 | Claim approval workflow | Directed Graph, BFS and DFS | Finds shortest approval paths and detects loops |
| 4 | High-claim day analysis | Sliding Window | Finds the longest consecutive period with more than 100 claims |
| 5 | Regional claim merging | Two Pointers | Merges two sorted claim lists without additional sorting |

---

# Overall Complexity Summary

| Question | Algorithm | Time Complexity |
|---|---|---|
| 1 | BST Insert and Search | O(log n) average |
| 2 | Hash Table | O(1) average, excluding normalization |
| 3 | BFS and DFS | O(V + E) |
| 4 | Sliding Window | O(n) |
| 5 | Two Pointers | O(n + m) |

---

# Conclusion

This Insurance Claims Processing project demonstrates the practical use of five important Data Structures and Algorithms.

1. **Binary Search Tree:** Organizes claim IDs and supports efficient searching.
2. **Hashing:** Detects duplicate and near-duplicate claim submissions.
3. **Graph:** Represents claim approval stages and identifies circular workflows.
4. **Sliding Window:** Detects consecutive days with unusually high claim volumes.
5. **Two Pointers:** Combines sorted claim records from multiple regional offices efficiently.

These techniques improve claim processing, duplicate detection, workflow management and operational analysis.


## Project Structure

```text
Insurance-Claims-Processing/SET-2
│
├── question1_binary search-claim.py
├── question2_claim approval.py
├── question3_hashing duplicate.py
├── question4_longest Consecutive day.py
├── question5_merge two sorted claim lists.py
│
└── README.md

```

# SET-3 Insurance Claims Processing – Data Structures and Algorithms

## Business Scenario

An insurance company needs an efficient system to manage claim submissions, route claims through approval stages, detect duplicate claims and monitor sudden increases in claim volume after regional events.

This project demonstrates the use of Data Structures and Algorithms (DSA) to improve claim management, searching, duplicate detection, workflow processing and data analysis.

## Technologies Used

- **Programming Language:** Python 3
- **Data Structures:** Binary Search Tree, Hash Table, Graph, List
- **Algorithms:** BFS, DFS, Sliding Window, Two Pointers
- **Libraries:** `collections`

## Project Objectives

1. Create a Binary Search Tree of claim IDs with insertion, searching and three traversals.
2. Detect duplicate and near-duplicate claims using hashing and normalization.
3. Represent claim approval stages using a directed graph and find shortest paths using BFS and loops using DFS.
4. Find the longest consecutive run of days on which claims exceeded 100 using Sliding Window.
5. Merge two sorted claim lists from regional offices using Two Pointers without additional sorting.

---

# Question 1 – Binary Search Tree for Claim IDs

## Problem Statement

Create a Binary Search Tree of claim IDs and implement insertion and searching. Display inorder, preorder and postorder traversals and identify which traversal produces sorted claim IDs.

## Implementation

- Created a Node class to represent each claim ID.
- Implemented BST insertion.
- Implemented claim ID searching.
- Implemented three tree traversals:
  - Inorder: Left → Root → Right
  - Preorder: Root → Left → Right
  - Postorder: Left → Right → Root

## Sample Input

```python
claim_ids = [
    105, 102, 108, 101, 104,
    107, 110, 103, 106, 109
]
```

## Expected Output

```text
CLAIM ID BST

Inorder Traversal:
101 102 103 104 105 106 107 108 109 110

Preorder Traversal:
105 102 101 104 103 108 107 106 110 109

Postorder Traversal:
101 103 104 102 106 107 109 110 108 105

Search Claim 105: True
Search Claim 120: False
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal insertion | 105, 102, 108 | All IDs inserted |
| Search existing ID | 105 | True |
| Search missing ID | 120 | False |
| Empty BST search | Empty tree, search 105 | False |
| Duplicate ID | Insert 105 twice | Duplicate goes to right subtree in the given implementation |

## Observation

- Inorder traversal produces claim IDs in ascending sorted order.
- Preorder visits the root before its subtrees.
- Postorder visits the root after its subtrees.
- Searching is efficient when the BST is balanced.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Insert | O(log n) | O(n) |
| Search | O(log n) | O(n) |
| Traversal | O(n) | O(n) |

---

# Question 2 – Hashing for Duplicate Claim Detection

## Problem Statement

Use hashing to detect duplicate or near-duplicate claims having the same policy number and incident date, even when differences occur in letter case or spacing.

## Implementation

- Used a hash table with chaining.
- Normalized policy numbers by converting them to uppercase and removing spaces.
- Normalized incident dates by removing unnecessary spaces.
- Combined policy number and incident date into a tuple key.
- Checked whether the normalized key already existed.
- Used chaining to handle hash collisions.

## Sample Input

| Claim ID | Policy Number | Incident Date |
|---|---|---|
| C101 | POL123 | 2026-11-10 |
| C102 | pol123 | 2026-11-10 |
| C103 | POL456 | 2026-11-11 |
| C104 | POL123 | 2026-11-10 |
| C105 | POL789 | 2026-11-12 |

## Expected Output

```text
CLAIM DUPLICATE DETECTION

C101 is a new claim
C102 is a duplicate of C101
C103 is a new claim
C104 is a duplicate of C102
C105 is a new claim
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| New claim | POL123, 2026-11-10 | New claim |
| Different letter case | pol123, 2026-11-10 | Duplicate |
| Extra spaces | POL123 with surrounding spaces | Duplicate |
| Different policy number | POL456, 2026-11-10 | New claim |
| Different incident date | POL123, 2026-11-11 | New claim |
| Empty policy number | Empty input | Should be rejected or handled as invalid input |

## Collision Handling

A collision occurs when two different keys produce the same hash table index.

This project uses **chaining** to handle collisions.

Example:

```text
Bucket 3:
(POL123, 2026-11-10)
(POL456, 2026-11-11)
```

Both keys can be stored in the same bucket. The program compares the complete normalized keys to distinguish a real duplicate from a hash collision.

## Observation

- Normalization helps identify claims that differ only in letter case or spacing.
- Hashing provides fast duplicate detection.
- Collision handling prevents different claims from being incorrectly identified as duplicates.

## Time Complexity

| Operation | Average Case | Worst Case |
|---|---|---|
| Hash calculation | O(k) | O(k) |
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Duplicate detection | O(1) average, excluding normalization | O(n) |

Here, k represents the length of the normalized key.

---

# Question 3 – Graph for Claim Approval Stages

## Problem Statement

Model the claim approval stages as a directed graph:

- Registration
- Assessment
- Surveyor
- Settlement

Find the shortest path between two stages using BFS and detect loops using DFS.

## Graph Representation

```text
Registration → Assessment
Assessment → Surveyor
Surveyor → Settlement
Settlement → End
```

The directed graph represents the movement of claims through the approval process.

## Implementation

- Represented approval stages using an adjacency list.
- Implemented BFS to find the shortest path.
- Implemented DFS to detect circular dependencies.
- Introduced a loop to test cycle detection.

## Expected Output

```text
CLAIM APPROVAL PROCESS

Shortest Approval Path:
Registration -> Assessment -> Surveyor -> Settlement

DFS Cycle Detection:
False

After Introducing a Loop:

DFS Cycle Detection:
True
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal workflow | Registration to Settlement | Shortest path found |
| Same starting and ending stage | Registration to Registration | Registration |
| Unreachable stage | No route to Settlement | No path |
| No circular dependency | Original graph | False |
| Circular dependency | Settlement → Assessment | True |
| Empty graph | No stages | No path; no cycle |

## Observation

- BFS finds the shortest path in an unweighted graph.
- DFS explores connected stages and detects cycles.
- A cycle may indicate an invalid or unintended approval workflow.

## Time Complexity

| Algorithm | Time Complexity |
|---|---|
| BFS | O(V + E) |
| DFS | O(V + E) |

Where:
- V = Number of approval stages.
- E = Number of directed connections.

---

# Question 4 – Sliding Window for Consecutive High-Claim Days

## Problem Statement

Find the longest consecutive run of days on which the number of claims exceeded 100 using the Sliding Window technique.

## Sample Input

```python
claims_per_day = [
    80, 120, 135, 110, 95, 130, 145,
    160, 90, 105, 115, 125, 70, 140
]
```

## Implementation

- Stored daily claim counts in a list.
- Used a left pointer to track the beginning of the current run.
- Used a right pointer to scan each day.
- Reset the current window when claims were 100 or fewer.
- Updated the longest consecutive run whenever a larger window was found.

## Expected Output

```text
CLAIMS ANALYSIS

Threshold: More than 100

Longest Consecutive Run: 3 days

Starting Day: 2
Ending Day: 4

Claims During Longest Run:
Day 2 : 120
Day 3 : 135
Day 4 : 110
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal data | 80, 120, 135, 110, 95 | Longest run = 3 days |
| All values exceed 100 | 110, 120, 130 | Longest run = 3 days |
| No values exceed 100 | 50, 80, 100 | Longest run = 0 days |
| Empty input | Empty list | Longest run = 0 days |
| Single qualifying day | 120 | Longest run = 1 day |

## Observation

- Sliding Window efficiently finds continuous periods satisfying a condition.
- The left pointer moves forward when a day does not meet the threshold.
- The algorithm scans the input only once.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Scan daily claim counts | O(n) |
| Update longest run | O(1) per day |
| Overall | O(n) |

Auxiliary space complexity: O(1).

---

# Question 5 – Two Pointers for Merging Regional Claim Lists

## Problem Statement

Use Two Pointers to merge two sorted claim lists from different regional offices into one sorted list without performing additional sorting.

## Sample Input

**Regional Office 1**

```python
region1 = [101, 104, 108, 112, 120]
```

**Regional Office 2**

```python
region2 = [102, 105, 109, 115, 118]
```

## Implementation

- Used two sorted input lists.
- Initialized one pointer for each list.
- Compared the values at both pointers.
- Added the smaller value to the merged list.
- Moved the corresponding pointer forward.
- Appended any remaining elements after one list was exhausted.

## Expected Output

```text
REGIONAL CLAIM MERGING

Region 1 Claims: [101, 104, 108, 112, 120]

Region 2 Claims: [102, 105, 109, 115, 118]

Merged Sorted Claims:
[101, 102, 104, 105, 108, 109, 112, 115, 118, 120]
```

## Test Cases

| Test Case | Input | Expected Result |
|---|---|---|
| Normal lists | [101, 104], [102, 105] | [101, 102, 104, 105] |
| First list empty | [], [102, 105] | [102, 105] |
| Second list empty | [101, 104], [] | [101, 104] |
| Both lists empty | [], [] | [] |
| Duplicate IDs | [101, 104], [101, 105] | [101, 101, 104, 105] |
| Different list sizes | [101], [102, 104, 106] | [101, 102, 104, 106] |

## Observation

- Two Pointers efficiently merges sorted lists.
- No additional sorting operation is required.
- Duplicate claim IDs are retained in the merged list.

## Time Complexity

| Operation | Time Complexity |
|---|---|
| Merge two sorted lists | O(n + m) |
| Auxiliary space | O(1), excluding output |
| Output list storage | O(n + m) |

Where:
- n = Number of claims in Regional Office 1.
- m = Number of claims in Regional Office 2.

---

# Final Decision Table

| Question | Problem | Data Structure / Pattern | Reason |
|---|---|---|---|
| 1 | Claim ID management | Binary Search Tree | Supports insertion, searching and sorted traversal |
| 2 | Duplicate claim detection | Hash Table with Chaining | Quickly identifies normalized duplicate claims and handles collisions |
| 3 | Claim approval workflow | Directed Graph, BFS and DFS | Finds shortest approval paths and detects loops |
| 4 | High-claim day analysis | Sliding Window | Finds the longest consecutive period with more than 100 claims |
| 5 | Regional claim merging | Two Pointers | Merges two sorted claim lists without additional sorting |

---

# Overall Complexity Summary

| Question | Algorithm | Time Complexity |
|---|---|---|
| 1 | BST Insert and Search | O(log n) average |
| 2 | Hash Table | O(1) average, excluding normalization |
| 3 | BFS and DFS | O(V + E) |
| 4 | Sliding Window | O(n) |
| 5 | Two Pointers | O(n + m) |

---

# Conclusion

This Insurance Claims Processing project demonstrates the practical use of five important Data Structures and Algorithms.

1. **Binary Search Tree:** Organizes claim IDs and supports efficient searching.
2. **Hashing:** Detects duplicate and near-duplicate claim submissions.
3. **Graph:** Represents claim approval stages and identifies circular workflows.
4. **Sliding Window:** Detects consecutive days with unusually high claim volumes.
5. **Two Pointers:** Combines sorted claim records from multiple regional offices efficiently.

These techniques improve claim processing, duplicate detection, workflow management and operational analysis.


## Project Structure

```text
Insurance-Claims-Processing/
│
├── question1_binary search tree-hub codes.py
├── question2_graph-hub routes and connectivity.py
├── question3_hash map-duplicate parcel scans.py
├── question4_highest average parcel in four hours.py
├── question5_palindrome delivery route.py
│
└── README.md
```

**Note:** The execution outputs in this README are expected sample outputs. Actual hash-map benchmark timings depend on the execution environment. The graph deployment order may also vary while remaining valid.

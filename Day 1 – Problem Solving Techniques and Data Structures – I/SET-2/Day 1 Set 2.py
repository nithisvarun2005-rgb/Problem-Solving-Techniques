import csv
import time
from datetime import datetime


def create_transaction_ids(count):
    ids = []
    for i in range(1, count + 1):
        ids.append("TXN" + str(i).zfill(6))
    return ids


# QUESTION 1: LINEAR AND BINARY SEARCH

def binary_search(ids, target):
    low = 0
    high = len(ids) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if ids[mid] == target:
            return mid, comparisons
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def linear_search(ids, target):
    comparisons = 0
    for i in range(len(ids)):
        comparisons += 1
        if ids[i] == target:
            return i, comparisons
    return -1, comparisons


def load_transactions(filename):
    transactions = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append({
                "transaction_id": row["transaction_id"],
                "account": row["account"],
                "amount": float(row["amount"]),
                "merchant": row["merchant"],
                "posting_date": datetime.fromisoformat(row["posting_date"])
            })
    return transactions


# Question 2:INSERTION AND MERGE SORT

def insertion_sort(data):
    result = data.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j]["posting_date"] > key["posting_date"]:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["posting_date"] <= right[j]["posting_date"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(data):
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2
    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])
    return merge(left, right)


# Question 3:Detect duplicates

def find_duplicate_postings(data):
    ordered = sorted(data, key=lambda item: item["posting_date"])
    groups = {}
    duplicates = []

    for item in ordered:
        key = (item["account"], item["amount"], item["merchant"])
        current_time = item["posting_date"]

        if key not in groups:
            groups[key] = []

        for previous in groups[key]:
            seconds = (current_time - previous["posting_date"]).total_seconds()
            if 0 <= seconds <= 60:
                duplicates.append((previous["transaction_id"], item["transaction_id"]))

        groups[key].append(item)

    return duplicates


# Question 4:QUEUE AND STACK

class ManualReviewQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[self.front]
        self.front += 1
        if self.front == len(self.items):
            self.items = []
            self.front = 0
        return item

    def is_empty(self):
        return self.front == len(self.items)

    def display(self):
        return self.items[self.front:]


class AdjustmentStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items.copy()


# Question 5: DIVIDE AND CONQUER

def divide_min_max(values):
    if len(values) == 0:
        return None, None
    if len(values) == 1:
        return values[0], values[0]
    if len(values) == 2:
        if values[0] < values[1]:
            return values[0], values[1]
        return values[1], values[0]

    middle = len(values) // 2
    left_min, left_max = divide_min_max(values[:middle])
    right_min, right_max = divide_min_max(values[middle:])

    minimum = left_min if left_min < right_min else right_min
    maximum = left_max if left_max > right_max else right_max
    return minimum, maximum


def brute_force_min_max(values):
    if len(values) == 0:
        return None, None, 0

    minimum = values[0]
    maximum = values[0]
    comparisons = 0

    for i in range(1, len(values)):
        comparisons += 1
        if values[i] < minimum:
            minimum = values[i]

        comparisons += 1
        if values[i] > maximum:
            maximum = values[i]

    return minimum, maximum, comparisons


def main():
    print("RETAIL BANK TRANSACTION PROCESSING")

    print("\nQUESTION 1: SEARCHING 100,000 TRANSACTION IDS")
    ids = create_transaction_ids(100000)
    target = "TXN075000"

    index, binary_count = binary_search(ids, target)
    linear_index, linear_count = linear_search(ids, target)

    print("Target:", target)
    print("Binary search index:", index)
    print("Binary search comparisons:", binary_count)
    print("Linear search index:", linear_index)
    print("Linear search comparisons:", linear_count)
    print("Binary best case: 1 comparison")
    print("Binary average case: approximately 16 comparisons")
    print("Binary worst case: at most 17 comparisons")
    print("Linear best case: 1 comparison")
    print("Linear average case: 50,000.5 comparisons")
    print("Linear worst case: 100,000 comparisons")

    print("\nQUESTION 2: SORTING CUSTOMER STATEMENT")
    transactions = load_transactions("transactions.csv")
    insertion_result = insertion_sort(transactions)
    merge_result = merge_sort(transactions)

    print("Insertion sort result:")
    for item in insertion_result:
        print(item["transaction_id"], item["posting_date"])

    print("Merge sort result:")
    for item in merge_result:
        print(item["transaction_id"], item["posting_date"])

    print("Both sorts are stable for equal timestamps.")

    print("\nQUESTION 3: DUPLICATE POSTINGS")
    duplicates = find_duplicate_postings(transactions)
    if len(duplicates) == 0:
        print("No duplicate postings found.")
    else:
        for pair in duplicates:
            print("Duplicate pair:", pair[0], "and", pair[1])

    print("\nQUESTION 4: QUEUE AND STACK")
    review_queue = ManualReviewQueue()
    review_queue.enqueue("TXN000101")
    review_queue.enqueue("TXN000102")
    review_queue.enqueue("TXN000103")
    print("Queue before review:", review_queue.display())
    print("Dequeued transaction:", review_queue.dequeue())
    print("Queue after review:", review_queue.display())

    adjustment_stack = AdjustmentStack()
    adjustment_stack.push("Adjustment +500")
    adjustment_stack.push("Adjustment -200")
    adjustment_stack.push("Adjustment +100")
    print("Stack before reversal:", adjustment_stack.display())
    print("Reversed adjustment:", adjustment_stack.pop())
    print("Stack after reversal:", adjustment_stack.display())

    print("\nQUESTION 5: MINIMUM AND MAXIMUM AMOUNT")
    amounts = [item["amount"] for item in transactions]

    start = time.perf_counter()
    minimum, maximum = divide_min_max(amounts)
    divide_time = time.perf_counter() - start

    start = time.perf_counter()
    brute_min, brute_max, comparisons = brute_force_min_max(amounts)
    brute_time = time.perf_counter() - start

    print("Divide-and-conquer minimum:", minimum)
    print("Divide-and-conquer maximum:", maximum)
    print("Brute-force minimum:", brute_min)
    print("Brute-force maximum:", brute_max)
    print("Brute-force comparisons:", comparisons)
    print("Divide-and-conquer time:", divide_time)
    print("Brute-force time:", brute_time)


if __name__ == "__main__":
    main()

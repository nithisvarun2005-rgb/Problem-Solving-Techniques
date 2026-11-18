import csv
import time
from datetime import datetime
from collections import deque

CSV_FILE = "orders.csv"

def load_orders(filename):
    orders = []

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                created_at = datetime.fromisoformat(row["createdAt"])
            except ValueError:
                created_at = row["createdAt"]

            order = {
                "orderId": row["orderId"],
                "customerId": row["customerId"],
                "amount": float(row["amount"]),
                "createdAt": created_at
            }

            orders.append(order)

    return orders


# QUESTION 1:LINEAR SEARCH AND BINARY SEARCH 

def linear_search(orders, target_id):
    for order in orders:
        if order["orderId"] == target_id:
            return order

    return None




def binary_search(sorted_orders, target_id):
    low = 0
    high = len(sorted_orders) - 1

    while low <= high:
        mid = (low + high) // 2

        if sorted_orders[mid]["orderId"] == target_id:
            return sorted_orders[mid]

        elif sorted_orders[mid]["orderId"] < target_id:
            low = mid + 1

        else:
            high = mid - 1

    return None


# QUESTION 2:BUBBLE SORT AND MERGE SORT

def bubble_sort(orders):
    arr = orders.copy()
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if arr[j]["amount"] < arr[j + 1]["amount"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr



def trace_bubble_first_three_passes(orders):
    arr = orders[:6].copy()

    print("\nBUBBLE SORT TRACE")
    print("Initial amounts:",
          [order["amount"] for order in arr])

    for i in range(3):
        for j in range(len(arr) - i - 1):

            if arr[j]["amount"] < arr[j + 1]["amount"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print("Pass", i + 1, ":",
              [order["amount"] for order in arr])




def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i]["amount"] >= right[j]["amount"]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(orders):
    if len(orders) <= 1:
        return orders.copy()

    mid = len(orders) // 2

    left = merge_sort(orders[:mid])
    right = merge_sort(orders[mid:])

    return merge(left, right)



def trace_merge_first_three_levels(orders):
    levels = {}

    def divide_and_merge(arr, level):
        if len(arr) <= 1:
            return arr.copy()

        mid = len(arr) // 2

        left = divide_and_merge(arr[:mid], level + 1)
        right = divide_and_merge(arr[mid:], level + 1)

        result = merge(left, right)

        levels.setdefault(level, []).append(
            [order["amount"] for order in result]
        )

        return result

    divide_and_merge(orders[:6], 1)

    print("\nMERGE SORT TRACE")

    # Display the first three merge levels from bottom to top
    for level in sorted(levels.keys(), reverse=True)[:3]:
        print("\nMerge level", level)

        for result in levels[level]:
            print(result)



# QUESTION 3: Detect duplicate orders 
def find_duplicates(orders):
    seen = {}
    duplicates = []

    for order in orders:

        created_at = order["createdAt"]

        if isinstance(created_at, datetime):
            minute = created_at.replace(
                second=0, microsecond=0
            )
        else:
            minute = str(created_at)[:16]

        key = (
            order["customerId"],
            order["amount"],
            minute
        )

        if key in seen:
            duplicates.append((seen[key], order))

        else:
            seen[key] = order

    return duplicates


# QUESTION 4: STACK AND QUEUE

class OrderEditStack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, edit):
        self.items.append(edit)

    def pop(self):
        if self.isEmpty():
            return None

        return self.items.pop()



class DispatchQueue:

    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, order):
        self.items.append(order)

    def dequeue(self):
        if self.isEmpty():
            return None

        return self.items.popleft()

# QUESTION 5: GREEDY APPROACH

def greedy_change(amount, denominations):
    combination = {}
    remaining = amount

    for coin in sorted(denominations, reverse=True):

        if remaining >= coin:
            count = remaining // coin

            combination[coin] = count
            remaining = remaining % coin

    return combination, remaining



def dp_change(amount, denominations):

    infinity = float("inf")

    dp = [infinity] * (amount + 1)
    previous_coin = [None] * (amount + 1)

    dp[0] = 0

    for current in range(1, amount + 1):

        for coin in denominations:

            if current >= coin:

                if dp[current - coin] + 1 < dp[current]:

                    dp[current] = dp[current - coin] + 1
                    previous_coin[current] = coin

    if dp[amount] == infinity:
        return None, infinity

    combination = {}
    current = amount

    while current > 0:

        coin = previous_coin[current]

        combination[coin] = combination.get(coin, 0) + 1

        current -= coin

    return combination, dp[amount]




def is_sorted_descending(orders):
    for i in range(len(orders) - 1):

        if orders[i]["amount"] < orders[i + 1]["amount"]:
            return False

    return True




def main():

    orders = load_orders(CSV_FILE)

    print("Loaded", len(orders), "orders from", CSV_FILE)

    if not orders:
        print("No orders found in the CSV file.")
        return


    print("\n1. SEARCH")

    target = orders[-1]["orderId"]

    start_time = time.perf_counter()
    linear_result = linear_search(orders, target)
    linear_time = time.perf_counter() - start_time


    id_sorted = sorted(orders, key=lambda x: x["orderId"])

    start_time = time.perf_counter()
    binary_result = binary_search(id_sorted, target)
    binary_time = time.perf_counter() - start_time

    print("Target order:", target)

    print("Linear search found:",
          linear_result["orderId"] if linear_result else None)

    print("Binary search found:",
          binary_result["orderId"] if binary_result else None)

    print("Linear search time:",
          round(linear_time * 1_000_000, 2), "microseconds")

    print("Binary search time:",
          round(binary_time * 1_000_000, 2), "microseconds")

    print("Linear: O(n), Binary: O(log n) after sorting")




    print("\n2. SORTING - 10,000 RECORDS")

    sort_data = orders[:10000]

    # Trace first three Bubble Sort passes
    trace_bubble_first_three_passes(sort_data)

    # Trace Merge Sort levels
    trace_merge_first_three_levels(sort_data)

    # Bubble Sort benchmark
    start_time = time.perf_counter()
    bubble_sorted = bubble_sort(sort_data)
    bubble_time = time.perf_counter() - start_time

    # Merge Sort benchmark
    start_time = time.perf_counter()
    merge_sorted = merge_sort(sort_data)
    merge_time = time.perf_counter() - start_time

    # Built-in Sort benchmark
    start_time = time.perf_counter()
    builtin_sorted = sorted(
        sort_data,
        key=lambda x: x["amount"],
        reverse=True
    )
    builtin_time = time.perf_counter() - start_time

    print("\nSORTING COMPARISON")

    print("Bubble Sort:",
          round(bubble_time, 4), "seconds",
          "| Correct:", is_sorted_descending(bubble_sorted))

    print("Merge Sort:",
          round(merge_time, 4), "seconds",
          "| Correct:", is_sorted_descending(merge_sorted))

    print("Built-in Sort:",
          round(builtin_time, 4), "seconds",
          "| Correct:", is_sorted_descending(builtin_sorted))

    print("\nComplexities:")
    print("Bubble Sort: O(n^2)")
    print("Merge Sort: O(n log n)")
    print("Built-in Sort: O(n log n) worst case")




    print("\n3. DUPLICATE DETECTION")

    duplicates = find_duplicates(orders)

    print("Duplicate pairs found:", len(duplicates))

    print("Key: customerId, amount and createdAt rounded to minute")

    print("Average time complexity: O(n)")
    print("Space complexity: O(n)")




    print("\n4. STACK AND QUEUE")

    # Custom Stack
    custom_stack = OrderEditStack()

    custom_stack.push("Change amount: 100 -> 150")
    custom_stack.push("Change address: A -> B")

    print("Custom stack undo:", custom_stack.pop())

    # Built-in List Stack
    builtin_stack = []

    builtin_stack.append("Change amount: 100 -> 150")
    builtin_stack.append("Change address: A -> B")

    print("Built-in stack undo:", builtin_stack.pop())

    # Custom Queue
    custom_queue = DispatchQueue()

    custom_queue.enqueue("O000001")
    custom_queue.enqueue("O000002")

    print("Custom queue dispatch:", custom_queue.dequeue())

    # Built-in Deque Queue
    builtin_queue = deque()

    builtin_queue.append("O000001")
    builtin_queue.append("O000002")

    print("Built-in queue dispatch:", builtin_queue.popleft())

    print("Stack push/pop: O(1)")
    print("Deque enqueue/dequeue: O(1)")




    print("\n5. REFUND CHANGE")

    amount = 6
    denominations = [4, 3, 1]

    greedy_result, remaining = greedy_change(
        amount, denominations
    )

    dp_result, minimum_count = dp_change(
        amount, denominations
    )

    print("Amount:", amount)
    print("Denominations:", denominations)

    print("Greedy result:", greedy_result)
    print("Remaining amount:", remaining)

    print("Dynamic programming result:", dp_result)
    print("Minimum coins:", minimum_count)

    print("Greedy: 4 + 1 + 1 = 6 (3 coins)")
    print("DP: 3 + 3 = 6 (2 coins)")




    print("\n6. TOP 5 ORDERS BY AMOUNT")

    for order in merge_sorted[:5]:
        print(order)




if __name__ == "__main__":
    main()

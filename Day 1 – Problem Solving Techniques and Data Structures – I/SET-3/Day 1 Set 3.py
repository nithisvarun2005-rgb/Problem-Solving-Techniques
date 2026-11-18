import random
import time
from datetime import datetime, timedelta
from collections import deque


def create_patients(n):
    patients = []

    for i in range(n):
        patients.append({
            "patient_id": "P" + str(i + 1).zfill(6),
            "name": "Patient" + str(i + 1),
            "age": random.randint(1, 90)
        })

    return patients


def create_appointments(n):
    appointments = []
    start_time = datetime(2026, 11, 10, 9, 0)

    for i in range(n):
        appointments.append({
            "patient_id": "P" + str(random.randint(1, 20000)).zfill(6),
            "urgency": random.randint(1, 5),
            "arrival_time": start_time + timedelta(
                minutes=random.randint(0, 480)
            )
        })

    return appointments

# Question 1:Linear and Binary Search

def linear_search(patients, target):
    for i in range(len(patients)):
        if patients[i]["patient_id"] == target:
            return i

    return -1


def binary_search(patients, target):
    low = 0
    high = len(patients) - 1

    while low <= high:
        mid = (low + high) // 2

        if patients[mid]["patient_id"] == target:
            return mid

        elif patients[mid]["patient_id"] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

# Question 2:Compare Selection Sort and Quick Sort


def search_comparison(patients):
    targets = [
        patients[random.randint(0, len(patients) - 1)]["patient_id"]
        for _ in range(1000)
    ]

    start = time.perf_counter()

    for target in targets:
        linear_search(patients, target)

    linear_time = time.perf_counter() - start

    start = time.perf_counter()

    for target in targets:
        binary_search(patients, target)

    binary_time = time.perf_counter() - start

    print("\n1. SEARCH PERFORMANCE")
    print("Patient records:", len(patients))
    print("Number of lookups:", len(targets))
    print("Linear search time:", round(linear_time, 6), "seconds")
    print("Binary search time:", round(binary_time, 6), "seconds")


def selection_sort(records):
    arr = records.copy()
    swaps = 0
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if (
                arr[j]["urgency"],
                arr[j]["arrival_time"]
            ) < (
                arr[min_index]["urgency"],
                arr[min_index]["arrival_time"]
            ):
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return arr, swaps


def quick_sort(records):
    arr = records.copy()
    swaps = [0]

    def partition(low, high):
        pivot = (
            arr[high]["urgency"],
            arr[high]["arrival_time"]
        )

        i = low - 1

        for j in range(low, high):
            current = (
                arr[j]["urgency"],
                arr[j]["arrival_time"]
            )

            if current <= pivot:
                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps[0] += 1

        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps[0] += 1

        return i + 1

    def sort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)
            sort(pivot_index + 1, high)

    sort(0, len(arr) - 1)

    return arr, swaps[0]


def sorting_comparison():
    records = create_appointments(1000)

    start = time.perf_counter()
    selection_result, selection_swaps = selection_sort(records)
    selection_time = time.perf_counter() - start

    start = time.perf_counter()
    quick_result, quick_swaps = quick_sort(records)
    quick_time = time.perf_counter() - start

    print("\n2. SORTING COMPARISON")
    print("Selection sort swaps:", selection_swaps)
    print("Selection sort time:", round(selection_time, 6), "seconds")

    print("Quick sort swaps:", quick_swaps)
    print("Quick sort time:", round(quick_time, 6), "seconds")

    print("\nFirst 5 sorted appointments:")

    for appointment in quick_result[:5]:
        print(appointment)


#Question 3: Detect Double Booking

def find_duplicate_bookings(bookings):
    seen = set()
    duplicates = []

    for booking in bookings:
        key = (
            booking["patient_id"],
            booking["slot"]
        )

        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)

    return duplicates


def duplicate_demo():
    bookings = [
        {"patient_id": "P001", "slot": "09:00"},
        {"patient_id": "P002", "slot": "09:00"},
        {"patient_id": "P001", "slot": "10:00"},
        {"patient_id": "P001", "slot": "09:00"},
        {"patient_id": "P003", "slot": "11:00"},
        {"patient_id": "P002", "slot": "09:00"}
    ]

    duplicates = find_duplicate_bookings(bookings)

    print("\n3. DUPLICATE BOOKING DETECTION")
    print("Duplicate bookings:")

    for duplicate in duplicates:
        print(duplicate)


# Question 4: Queue and Stack

class WalkInQueue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, patient):
        self.queue.append(patient)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return None

        return self.queue.popleft()

    def display(self):
        print("Walk-in queue:", list(self.queue))


class RecentPatientsStack:

    def __init__(self):
        self.stack = deque()

    def push(self, patient):
        self.stack.append(patient)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return None

        return self.stack.pop()

    def display(self):
        print("Recent patients:", list(reversed(self.stack)))


def queue_stack_demo():
    print("\n4. QUEUE AND STACK")

    queue = WalkInQueue()

    queue.enqueue("Patient A")
    queue.enqueue("Patient B")
    queue.enqueue("Patient C")

    queue.display()

    print("Next patient:", queue.dequeue())

    queue.display()

    stack = RecentPatientsStack()

    stack.push("Patient A")
    stack.push("Patient B")
    stack.push("Patient C")

    stack.display()

    print("Most recently viewed:", stack.pop())

    stack.display()

# Question 5: Dynamic Programming

def maximum_appointments_dp(appointments):
    arr = sorted(appointments, key=lambda x: x["end"])

    n = len(arr)
    p = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[j]["end"] <= arr[i]["start"]:
                p[i] = j
                break

    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        include = 1 + dp[p[i - 1] + 1]
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    return dp[n], arr, p, dp


def maximum_appointments_greedy(appointments):
    arr = sorted(appointments, key=lambda x: x["end"])

    selected = []
    last_end = None

    for appointment in arr:
        if last_end is None or appointment["start"] >= last_end:
            selected.append(appointment)
            last_end = appointment["end"]

    return len(selected), selected


def scheduling_demo():
    appointments = [
        {"id": "A", "start": 9, "end": 12},
        {"id": "B", "start": 9, "end": 10},
        {"id": "C", "start": 10, "end": 11},
        {"id": "D", "start": 11, "end": 12},
        {"id": "E", "start": 12, "end": 14},
        {"id": "F", "start": 10, "end": 13}
    ]

    dp_count, sorted_list, p, dp = maximum_appointments_dp(
        appointments
    )

    greedy_count, greedy_selected = maximum_appointments_greedy(
        appointments
    )

    print("\n5. APPOINTMENT SCHEDULING")

    print("DP maximum appointments:", dp_count)
    print("Greedy maximum appointments:", greedy_count)

    print("DP selected appointment count:", dp_count)

    print("Greedy selected appointments:",
          [a["id"] for a in greedy_selected])

    print("DP table:", dp)


def main():
    patients = create_patients(20000)

    patients.sort(key=lambda x: x["patient_id"])

    search_comparison(patients)

    sorting_comparison()

    duplicate_demo()

    queue_stack_demo()

    scheduling_demo()

main()


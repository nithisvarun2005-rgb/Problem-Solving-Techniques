parcel_counts = [
    20, 30, 40, 50, 60, 70,
    80, 90, 100, 110, 120, 130
]

window_size = 4

current_sum = sum(parcel_counts[:window_size])

max_sum = current_sum
best_start = 0


for i in range(window_size, len(parcel_counts)):

    current_sum = (
        current_sum
        - parcel_counts[i - window_size]
        + parcel_counts[i]
    )

    if current_sum > max_sum:

        max_sum = current_sum
        best_start = i - window_size + 1


average = max_sum / window_size

print("PARCEL VOLUME ANALYSIS")

print("\nHighest 4-Hour Window:")

print(
    "Hour",
    best_start + 1,
    "to Hour",
    best_start + window_size
)

print("Total Parcels:", max_sum)

print("Highest Average:", average)

print("\nParcel Counts in Selected Window:")

for i in range(best_start, best_start + window_size):

    print(
        "Hour",
        i + 1,
        ":",
        parcel_counts[i]
    )

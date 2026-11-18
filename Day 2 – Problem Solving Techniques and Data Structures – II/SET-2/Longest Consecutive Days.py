claims_per_day = [
    80, 120, 135, 110, 95, 130, 145,
    160, 90, 105, 115, 125, 70, 140
]

threshold = 100

left = 0
max_length = 0
best_start = 0
best_end = 0

for right in range(len(claims_per_day)):

    if claims_per_day[right] <= threshold:

        left = right + 1

    else:

        current_length = right - left + 1

        if current_length > max_length:

            max_length = current_length
            best_start = left
            best_end = right


print("CLAIMS ANALYSIS")

print("Threshold: More than", threshold)

print("Longest Consecutive Run:", max_length, "days")

print("Starting Day:", best_start + 1)

print("Ending Day:", best_end + 1)

print("\nClaims During Longest Run:")

for i in range(best_start, best_end + 1):
    print("Day", i + 1, ":", claims_per_day[i])

requests = [100] * 1440


for i in range(600, 780):
    requests[i] = 250


window_size = 180


current_sum = sum(requests[:window_size])

max_sum = current_sum
best_start = 0

for i in range(window_size, len(requests)):

    current_sum = (
        current_sum
        - requests[i - window_size]
        + requests[i]
    )

    if current_sum > max_sum:
        max_sum = current_sum
        best_start = i - window_size + 1


def convert_time(minutes):

    hours = minutes // 60
    mins = minutes % 60

    return f"{hours:02d}:{mins:02d}"


start_time = convert_time(best_start)
end_time = convert_time(best_start + window_size)

print("PEAK TRAFFIC ANALYSIS")

print("Busiest Window Start:", start_time)
print("Busiest Window End:", end_time)

print("Total Requests:", max_sum)

print(
    "Average Requests Per Minute:",
    max_sum / window_size
)

parcel_scans = {}

scans = [
    ("TRK101", "H50"),
    ("TRK102", "H30"),
    ("TRK101", "H50"),
    ("TRK103", "H70"),
    ("TRK102", "H30"),
    ("TRK101", "H70")
]

print("PARCEL DUPLICATE SCAN DETECTION\n")

for tracking_number, hub_code in scans:

    key = (tracking_number, hub_code)

    if key in parcel_scans:

        print(
            "Duplicate Scan:",
            tracking_number,
            "at",
            hub_code
        )

        parcel_scans[key] += 1

    else:

        parcel_scans[key] = 1

        print(
            "New Scan:",
            tracking_number,
            "at",
            hub_code
        )

print("\nFinal Scan Counts:")

for key, count in parcel_scans.items():

    print(
        key[0],
        "at",
        key[1],
        "->",
        count,
        "scan(s)"
    )

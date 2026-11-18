class ClaimHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def normalize(self, policy, date):
        policy = "".join(policy.upper().split())
        date = "".join(date.strip().split())

        return (policy, date)

    def hash_function(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, claim_id, policy, date):
        key = self.normalize(policy, date)

        index = self.hash_function(key)

        for item in self.table[index]:
            if item[0] == key:
                print(
                    claim_id,
                    "is a duplicate of",
                    item[1]
                )
                item[1] = claim_id
                return

        self.table[index].append([key, claim_id])

        print(claim_id, "is a new claim")


claims = ClaimHashTable(10)

claim_records = [
    ("C101", "POL123", "2026-11-10"),
    ("C102", " pol123 ", "2026-11-10"),
    ("C103", "POL456", "2026-11-11"),
    ("C104", "POL123", "2026-11-10"),
    ("C105", "POL789", "2026-11-12")
]

print("CLAIM DUPLICATE DETECTION\n")

for claim_id, policy, date in claim_records:
    claims.insert(claim_id, policy, date)

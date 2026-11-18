region1 = [101, 104, 108, 112, 120]
region2 = [102, 105, 109, 115, 118]


i = 0
j = 0

merged_claims = []


while i < len(region1) and j < len(region2):

    if region1[i] < region2[j]:

        merged_claims.append(region1[i])
        i += 1

    else:

        merged_claims.append(region2[j])
        j += 1



while i < len(region1):

    merged_claims.append(region1[i])
    i += 1


while j < len(region2):

    merged_claims.append(region2[j])
    j += 1


print("REGIONAL CLAIM MERGING")

print("Region 1 Claims:", region1)

print("Region 2 Claims:", region2)

print("\nMerged Sorted Claims:")
print(merged_claims)

import re

def check_palindrome(route):


    hubs = re.split(r"\s*(?:->|,|;)\s*", route.strip())
    hubs = [hub.strip().upper() for hub in hubs if hub.strip()]
   
    left = 0
    right = len(hubs) - 1

    while left < right:

        if hubs[left] != hubs[right]:
            return False

        left += 1
        right -= 1

    return True



route1 = "h1 -> H2 -> h3 -> H2 -> H1"
route2 = "H1 -> H2 -> H3 -> H4"

print("DELIVERY ROUTE PALINDROME CHECK")

print("\nRoute 1:", route1)

if check_palindrome(route1):
    print("Result: Palindrome")
else:
    print("Result: Not a Palindrome")


print("\nRoute 2:", route2)

if check_palindrome(route2):
    print("Result: Palindrome")
else:
    print("Result: Not a Palindrome")

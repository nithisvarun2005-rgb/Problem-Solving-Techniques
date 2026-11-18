order_values = [
    100, 150, 200, 250,
    300, 350, 400, 450
]

gift_card = 550

left = 0
right = len(order_values) - 1

print("GIFT CARD PAIR MATCHING")
print("Gift Card Value:", gift_card)

print("\nMatching Pairs:")

while left < right:

    total = order_values[left] + order_values[right]

    if total == gift_card:

        print(
            order_values[left],
            "+",
            order_values[right],
            "=",
            gift_card
        )

        left += 1
        right -= 1

    elif total < gift_card:

        left += 1

    else:

        right -= 1

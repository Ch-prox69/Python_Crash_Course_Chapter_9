from random import choice

numbers = [1,2,3,4,5,6,7,8,9,10,'a','b','c','e']

winning_lottery_ticket = []
print("Your ticket combination is...")

while len(winning_lottery_ticket) < 4:
    pulled_item = choice(numbers)

    if pulled_item not in winning_lottery_ticket:
        print(f"You pulled a {pulled_item}!")
        winning_lottery_ticket.append(pulled_item)

print(f"\nThe final winning ticket is: {winning_lottery_ticket}")



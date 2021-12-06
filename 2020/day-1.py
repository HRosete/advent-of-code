"""

--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

Your puzzle answer was 633216.

--- Part Two ---
The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?

Your puzzle answer was 68348924.

"""

expense_report = open("day-1-input.txt", "r")
expense_list = []

# Transfer expenses from input.txt to expense_list
for expense in expense_report:
    expense_list.append(int(expense))

# Find the two entries that sum to 2020
for number in expense_list:
    # print("The number is ", number)

    for x in range(0, len(expense_list)):
        addend = expense_list[x]
        sum = number + addend
        # print("Sum: ", sum)

        if not sum == 2020:
            x += 1
        elif sum == 2020:
            product = number * addend
            print(f"The numbers are {number} and {addend}.")
            print(f"The sum is equal to {sum}.")
            print(f"The product is {product}.")
            raise SystemExit


# Find the two entries that sum to 2020
for number in expense_list:
    # print(f"The number is {number}.")

    for x in range(0, len(expense_list)):
        addend1 = expense_list[x]
        # print(f"The range is {x}.")
        # print(f"Addend 1 is {addend1}.")

        for y in range(1, len(expense_list)):
            addend2 = expense_list[y]
            # print(f"Addend 2 is {addend2}.")
            sum = number + addend1 + addend2

            if not sum == 2020:
                y += 1
            elif sum == 2020:
                product = number * addend1 * addend2
                print(f"The numbers are {number}, {addend1}, and {addend2}.")
                print(f"The sum is equal to {sum}.")
                print(f"The product is {product}.")
                raise SystemExit
        x += 1

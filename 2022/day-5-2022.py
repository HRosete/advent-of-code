"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was SHQWSRBDL.

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

Your puzzle answer was CDTQZHBRS.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

If you still want to see it, you can get your puzzle input.

You can also [Share] this puzzle.
"""
# Instructions Parsing
f = open("day-5-2022-input-instructions.txt", "r")
f_list = f.readlines()
instructions = [x.strip() for x in f_list]

# # Sample Crates
# crates = {
#     "crate_1": ["N", "Z"],
#     "crate_2": ["D", "C", "M"],
#     "crate_3": ["P"],
# }

# Crates
crates = {
    "crate_1": ["R", "C", "H"],
    "crate_2": ["F", "S", "L", "H", "J", "B"],
    "crate_3": ["Q", "T", "J", "H", "D", "M", "R"],
    "crate_4": ["J", "B", "Z", "H", "R", "G", "S"],
    "crate_5": ["B", "C", "D", "T", "Z", "F", "P", "R"],
    "crate_6": ["G", "C", "H", "T"],
    "crate_7": ["L", "W", "P", "B", "Z", "V", "N", "S"],
    "crate_8": ["C", "G", "Q", "J", "R"],
    "crate_9": ["S", "F", "P", "H", "R", "T", "D", "L"],
}


def second_mover(lst, _crate):
    to_add = lst
    for i in range(len(lst)):
        _add = to_add.pop()
        _crate.insert(0, _add)
    return _crate


# Manipulate instructions
for inst in instructions:
    _inst = inst.split(" ")
    _move = _inst[1]
    _from = _inst[3]
    _to = _inst[5]
    crate_to_pop = crates[f"crate_{_from}"]
    crate_to_insert = crates[f"crate_{_to}"]
    crate_to_be_stacked = crates[f"crate_{_to}"]

    popped_items = []
    for i in range(int(_move)):
        popped = crate_to_pop.pop(0)
        popped_items.append(popped)
        # crate_to_insert.insert(0, popped)  # Uncomment for first puzzle

    crate_to_be_stacked = second_mover(popped_items, crate_to_be_stacked)

top_of_crates = ""
for i, (key, value) in enumerate(crates.items()):
    crate = crates[f"{key}"]
    top_of_crates += crate[0]

print("Top of Crates:", top_of_crates)

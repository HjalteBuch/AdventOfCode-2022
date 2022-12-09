import copy
with open('input_day_5.txt') as f:
    lines = f.readlines();

# Part 1
stacks = [];
stacks.append(["test"]);

line_number = 0;
for n in range(9):
    stack = [];

    for i in range(8):
        crate = lines[i][line_number: line_number+3]

        if crate != "   ":
            stack.append(crate);

    line_number += 4;
    stacks.append(stack);

stacks_two = copy.deepcopy(stacks);
def max_list_len(list):
    list_len = [len(i) for i in list];
    return max(list_len)

# Print stacks beautifully
def print_stack(stacks):
    for i in reversed(range(max_list_len(stacks))):
        for stack in stacks:
            if "test" in stack:
                continue;

            if len(stack)-1 >= i:
                print(stack[len(stack)-i-1], end = " ")
            else:
                print("   ", end = " ")
        print("")

    print(" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ")

def part_one(stacks):

    #print_stack(stacks);
    counter = 0;
    for operation in lines:
        if operation[0:4] != "move":
            continue;

        operation = operation.replace("\n", "");
        instructions = operation.split(' ');

        for n in range(int(instructions[1])):
            stacks[int(instructions[5])].insert(0, stacks[int(instructions[3])].pop(0));

        #print("Instructions: " + operation)
        #print_stack(stacks);
        #if counter > 10: break;
        counter += 1;

def part_two(stacks):

    #print_stack(stacks);
    counter = 0;
    for operation in lines:
        if operation[0:4] != "move":
            continue;

        operation = operation.replace("\n", "");
        instructions = operation.split(' ');

        for n in reversed(range(int(instructions[1]))):
            stacks[int(instructions[5])].insert(0, stacks[int(instructions[3])].pop(n));

        #print("Instructions: " + operation)
        #print_stack(stacks);
        #if counter > 10: break;
        counter += 1;




part_one(stacks);
print("")
print("------------------------------------------")
print("Part 1 result: ")
print_stack(stacks)

part_two(stacks_two);
print("")
print("------------------------------------------")
print("Part 2 result: ")
print_stack(stacks_two)

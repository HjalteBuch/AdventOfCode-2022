# Part 1
import string

class Rucksack:
    one = "";
    two = "";

priorities = list(' ' + string.ascii_lowercase + string.ascii_uppercase);
with open('input_day_3.txt') as f:
    lines = f.readlines();

rucks = [];
for line in lines:
    rucks.append(line.replace("\n", ""));

rucksacks = [];
for ruck in rucks: 
    rucksack = Rucksack();
    rucksack.one = ruck[0 : len(ruck)//2];
    rucksack.two = ruck[len(ruck)//2 : len(ruck)];
    rucksacks.append(rucksack);

common_items = [];
for rucksack in rucksacks:
    common_items.append(''.join(set(rucksack.one).intersection(rucksack.two)));

result = 0;
for item in common_items:
    result += priorities.index(item);
print("The answer to the first part is: " + str(result))

# part 2
commons = [];
for i, ruck in enumerate(rucks):
    if i % 3 != 0:
        #print("continue")
        continue;

    #print("index: " + str(i));
    first = rucks[i];
    second = rucks[i+1];
    third = rucks[i+2];
    first_second = ''.join(set(first).intersection(second));
    commons.append(''.join(set(first_second).intersection(third)));

result = 0;
for item in commons:
    result += priorities.index(item);
print("The answer to the second part is: " + str(result))

# Part 1
with open('input_day_2.txt') as f:
    lines = f.readlines();

strategy = [];
for line in lines:
    line = line.rstrip("\n");
    strategy.append(line);
    
def points(elf, me):
    if elf == 'A' and me == 'X': return 3
    if elf == 'A' and me == 'Y': return 6
    if elf == 'A' and me == 'Z': return 0

    if elf == 'B' and me == 'X': return 0
    if elf == 'B' and me == 'Y': return 3
    if elf == 'B' and me == 'Z': return 6

    if elf == 'C' and me == 'X': return 6
    if elf == 'C' and me == 'Y': return 0
    if elf == 'C' and me == 'Z': return 3

    print("Didn't find a result")
    return 0;

def match_result(match):
    elf = match[0];
    me = match[2];
    result = points(elf, me);
    if me == 'X': result += 1;
    if me == 'Y': result += 2;
    if me == 'Z': result += 3;
    return result

result = list(map(match_result, strategy));

print("The answer to the first part is: " + str(sum(result)))



# Part 2
def points2(elf, me):
    if elf == 'A' and me == 'X': return 3
    if elf == 'A' and me == 'Y': return 4
    if elf == 'A' and me == 'Z': return 8

    if elf == 'B' and me == 'X': return 1
    if elf == 'B' and me == 'Y': return 5
    if elf == 'B' and me == 'Z': return 9

    if elf == 'C' and me == 'X': return 2
    if elf == 'C' and me == 'Y': return 6
    if elf == 'C' and me == 'Z': return 7

    print("Didn't find a result")
    return 0;

def match_result2(match):
    elf = match[0];
    me = match[2];
    result = points2(elf, me);
    return result

result = list(map(match_result2, strategy));
print("The answer to the first part is: " + str(sum(result)))

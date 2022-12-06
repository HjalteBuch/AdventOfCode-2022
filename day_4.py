# Part 1
with open('input_day_4.txt') as f:
    lines = f.readlines();

pairs = []
for line in lines:
    pairs.append(line.replace("\n", ""));

result = 0;
for pair in pairs:
    split = pair.split(",");

    one = split[0].split("-");
    two = split[1].split("-");

    if int(one[0]) <= int(two[0]):
        if int(one[1]) >= int(two[1]):
            result += 1;
            continue;
    if int(one[0]) >= int(two[0]):
        if int(one[1]) <= int(two[1]):
            result += 1;

print(result)

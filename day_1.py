# Part 1
with open('input_day_1.txt') as f:
    calories = f.readlines();

maxCalories = 0;
currentCal = 0;

for elf in calories:
    if elf == '\n':
        if currentCal > maxCalories:
            maxCalories = currentCal
        currentCal = 0;
        continue;

    currentCal += int(elf);

print("The answer to the first part is: " + str(maxCalories))



# Part 2
maxCalories = 0;
currentCal = 0;
elfs = [];

for elf in calories:
    if elf == '\n':
        elfs.append(currentCal);
        currentCal = 0;
        continue;

    currentCal += int(elf);

elfs.sort(reverse = True);
print("The answer to the second part is: " + str(elfs[0] + elfs[1] + elfs[2]));

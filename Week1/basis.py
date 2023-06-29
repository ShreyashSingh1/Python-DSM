print(10 & 4)
print(10 | 4)
print(~20)
# Adds one and put minus in front
print(~12)
# Right Shift
a = 8
print(a >> 2)

# left Shift
a = 10
print(a << 2)

i = 1
n = 4
while i < n:
    print(i)
    i += 1
    if i == 3:
        break
else:
    # If while is completed successfully
    print("done")

for i in range(0, 10):
    # print(i)
    if i == 6:
        continue
    print(i)
else:
    print("done")

sum = 0
for i in range(1, 6):
    sum += i
print(sum)

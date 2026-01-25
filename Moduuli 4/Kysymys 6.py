import random

count_of_dots_int = int(input())

inside_int = 0
counter = 0

while counter < count_of_dots_int:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y < 1:
        inside_int += 1

    counter += 1

pi = 4 * inside_int / count_of_dots_int

print("Approximation of pi: " + str(pi))
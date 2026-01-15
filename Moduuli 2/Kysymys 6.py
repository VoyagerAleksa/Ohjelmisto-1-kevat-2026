import random
string = f"3-digit code: "
for _ in range(3):
    satunnainen_luku = random.randint(0, 9)
    string = string + str(satunnainen_luku)
print(string)

string = f"4-digit code: "
for _ in range(4):
    satunnainen_luku = random.randint(1, 6)
    string = string + str(satunnainen_luku)
print(string)

#დაბეჭდე რიცხვები 1-დან 30-მდე, რომლებიც იყოფა 4-ზე:
r = 0
for i in range(1, 31):
    if i % 4 == 0:
        r += i
print(r)
# 1) შექმენით სია რომელშიც იქნება 15 ელემენტი შემდეგ გამოიტანეთ სიის ყველა ელემენტი while loop-ის გამოყენებით და ასევე for loop-ითაც
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(16):
    print(numbers[i])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 0
while i <= 15:
    print(numbers[i])
    i += 1
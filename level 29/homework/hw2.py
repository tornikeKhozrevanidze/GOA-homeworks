#2) python - შექმენით რიცხვებით სავსე სია შემდეგ კი შექმენით პროგრამა რომელიც დაგვიბეჭდავს ამ სიიდან უდიდესს, გაიხსენეთ ბატონი ნიკას მოცემული დავალება გამოგადგებათ
list1 = [ 2, 3, 4, 6, 8, 9, 0, 0, 6, 43, 2, 1, 43, 64, 7]
a = 0
for i in list1:
    if i > a:
        a = i
print(a)
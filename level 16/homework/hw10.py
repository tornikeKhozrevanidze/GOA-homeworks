# 10) დაბეჭდეთ 1 დან 100 მდე დაბეჭდეთ მხოლოდ ის რიცხვები რომლებიც 3 ჯერადიც არის და 5 ჯერადიც
i = 1
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1
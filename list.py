import random
list=[random.randint(-10,10) for i in range(10)]
if abs(max(list)-min(list))>10:
    print(sorted(list))
else:
    print("Difference is less than 10")
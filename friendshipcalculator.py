score = 0

names = input("Enter the names of 2 friends Eg(john&jim): ")

name1, name2 = names.split("&")
data = names.split("&")

for name in data:
    for character in name:
        if character in 'aeiou':
            score += 5
        if character in 'friend':
            score += 10
if(len(name1) == len(name2)):
    score += 15
print(score)
if(score > 100):
    print("Best Friends")

        





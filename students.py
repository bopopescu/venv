#test
marksheet = []
scorelist=[]
for i in range(int(input())):
        name = input()
        score = float(input())

        marksheet += [[name, score]]
        scorelist += [score]
b = sorted(list(set(scorelist)))[1]
print(b)
for a, c in sorted(marksheet):
    if c == b:
        print(a)

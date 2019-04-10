"""
UPDATED by eu9327
lab from onlie
"""

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

print("thats finish")

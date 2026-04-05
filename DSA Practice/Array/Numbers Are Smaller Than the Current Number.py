nums = list(map(int, input("Enter numbers with space:").split()))

answer = []
for i in nums:
    c=0
    for j in nums:
        if j<i:
            c = c +1
    answer.append(c)

print(answer)
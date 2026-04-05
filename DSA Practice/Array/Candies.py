candies = list(map(int, input("Enter candies: ").split()))
extraCandies = int(input("Extra candies: "))
maxcandy = max(candies)
ans =[]
for i in candies:
    if i + extraCandies >= maxcandy:
        ans.append(True)
    else:
        ans.append(False)
print(ans)
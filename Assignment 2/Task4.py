#This code simply prints the sum of all digits one by one till the end
# num=range(1,51)
# for i in num:
#     sum=(i*(i+1))/2
#     sum=int(sum)
#     print(sum)


def range_sum(l, r):
    sum = 0
    for i in range(l, r + 1): #why r+1 because  it run till 50 not 49
        sum += i
    return sum
# ans=range_sum(1,3)
# print(ans)

# def range_sum(l, r):
#     sum=(r * (r + 1)) // 2 - ((l - 1) * l) // 2 # this is the direct formula method
#     return sum

l,r=1,50
print (f"The sum of numbers from {l} to {r} is : {range_sum(l,r)}")

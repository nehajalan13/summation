li = [2,3,7,5]
s = 5

#find the number whose sum is 5 from the list
def sum(li,s):
    for i in range(len(li)):
        a = s-li[i]
        if a in li[i:]:
            return (li[i],a)

res = sum(li,s)
print(res)


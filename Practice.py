'''def fun(x):
    return x**2
newlist = [1,2,3,4,5]
print(list(map(fun,newlist)))
print(list(map(lambda x : x+2,newlist)))
print(list(map(lambda x : x%2==0,newlist)))
print(list(filter(lambda x : x%2==0,newlist)))'''

'''generator
def fun():
    counter = 0
    while counter<5:
        yield counter
        counter +=1
for x in fun():
    print(x)'''

'''def even(x):
    for i in range (x):
        if i%2==0:
            yield i

print(list(even(20)))'''

result =  (lambda x : x*(x+5)^2)(5)
print(result)

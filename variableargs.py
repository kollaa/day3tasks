def add(*ad):
   # print(ad)
    #return sum(ad)
    total = 0
    for a in ad:
        total = total+a    
    return total

print(add(5,6))
print(add(5,6,7))
print(add())
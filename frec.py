dict= {"TV":2, "Computer":1, "Phone":2, "Laptop":1}
print(dict)
count=0
a= 2
for key in dict:
    if dict[key]==a:
        count=count+1
print(count)
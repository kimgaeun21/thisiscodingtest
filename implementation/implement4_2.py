h = int(input())
count =0
for i in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(m) or '3' in str(s) or '3' in str(i): # '3' in str(i) + str(m) + str(s)
                count += 1
print (count)
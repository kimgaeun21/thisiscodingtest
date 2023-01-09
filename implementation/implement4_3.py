move = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
now= input()
location= (int(ord(now[0])-ord('a'))+1, int(now[1]))
count=0

for i in range(len(move)):
    nx= location[0] + move[i][0]
    ny= location[1] + move[i][1]

    if nx > 9 or nx < 1 or nx > 9 or ny < 1 :
        continue

    # print(nx, ny)
    count += 1

print (count)
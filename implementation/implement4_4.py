
n, m = map(int,input().split())
x, y, d = map(int, input().split())

map_game = []
for i in range(m):
    map_game.append(list(map(int, input().split())))

direction=[0, 1, 2, 3]
move={ 0 : (0, -1),
       1 : (1, 0),
       2 : (0, 1),
       3 : (-1, 0)}

# 왼쪽 회전
def turn_left(dir):
    return direction[dir-1]

turn = 0
count = 1
map_game[y][x] = 2
while True:
    next_dic = turn_left(d)
    #print (next_dic)
    n_x = x + move[next_dic][0]
    n_y = y + move[next_dic][1]
    #print(n_x, n_y)

    if map_game[n_y][n_x] == 0:
        count += 1
        x = n_x
        y = n_y
        map_game[y][x] = 2
        turn = 0
        d = next_dic
        #print(x, y, d)
    else :
        if turn < 4 :
            d = next_dic
            turn += 1
        else :
            n_x = x + move[turn_left(next_dic)][0]
            n_y = y + move[turn_left(next_dic)][1]
            if map_game[n_y][n_x] != 1:
                x = n_x
                y = n_y
                #print(x, y, d)
                trun = 0
            else:
                break
#print(map_game)

print(count)




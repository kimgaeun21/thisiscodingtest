move={'D': [1, 0],
      'U': [-1, 0],
      'L': [0, -1],
      'R': [0, 1]}
n = int(input())
movement = list(input().split())
location = (1, 1)
print (location)

for i in range(len(movement)):
    next_x = location[0] + move[movement[i]][0]
    next_y = location[1] + move[movement[i]][1]

    if next_x < 1 or next_x > n or next_y < 1 or next_y > n:
        continue

    location = next_x, next_y

print(location)

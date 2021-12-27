data = list(input())
move_type = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
# x = data[0] == 'a' ? 1 : data[0] == 'b' ? 2 :
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
}
# column = int(ord(data[0]) - int(ord('a')))+ 1 #
x = dictionary[data[0]]
y = int(data[1])
result = 0

for move in move_type:
    dx = move[0] + x
    dy = move[1] + y
    if dx <= 0 or dy <= 0 or dx > 8 or dy > 8:
        continue
    result += 1

print(result)

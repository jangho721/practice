import sys

# Series number
# n = int(input())
n = int(sys.stdin.readline())

# First movie number
movie_number = 666

# Count cases containing 666
cnt = 0
while True:
    # Int type cannot use 'in'
    # So you have to use string type
    if '666' in str(movie_number):
        cnt += 1

    if cnt == n:
        break

    movie_number += 1

print(movie_number)

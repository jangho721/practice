import sys
from collections import deque

test_case = int(sys.stdin.readline().strip())

# R(reverse), D(delete: first element)
# Error occurs when the array is empty and D is used
# sys.stdin.readline() -> str

# Instead of executing reverse every time,
# keep track of the number of reversals,
# and only perform the reversal if the count is odd

# When using join(List), the elements in the List must be of type str

for _ in range(test_case):
    commends = sys.stdin.readline().strip()
    ln = int(sys.stdin.readline().strip())
    queue = deque(sys.stdin.readline().strip()[1:-1].split(','))

    # Exception handling
    if ln == 0:
        queue = deque()

    flag = 0
    rev = 0
    for e in commends:
        if e == 'R':
            rev += 1
        elif e == 'D':
            if len(queue) == 0:
                flag = 1
                print('error')
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if rev % 2 == 0:
            print("[" + ','.join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ','.join(queue) + "]")

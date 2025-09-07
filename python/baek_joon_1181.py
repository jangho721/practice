import sys

# The number of words n
# n = int(input())
n = int(sys.stdin.readline())

# Remove duplicates with set function
data = set([sys.stdin.readline().strip() for i in range(n)])

# Sort alphabetically
data = sorted(data)

# Length sort
# key = lambda x:len(x)
data = sorted(data, key=len)

# for i in data : print(i)
print("\n".join(data))

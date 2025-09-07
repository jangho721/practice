import re
import sys

# Regular Expressions, RegEx
# ^: Starts with the specified pattern
# ?: The preceding pattern appears 0 or 1 time
# $: Ends with the specified pattern
# +: The preceding pattern appears one or more times

# match: Checks if the regular expression matches from the beginning of the string
# search: Searches the entire string to see if it matches the regular expression
# findall: Returns a list of all substrings that match the regular expression
# finditer: Returns an iterator yielding match objects for all matching substrings

n = int(sys.stdin.readline().strip())
f = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(n):
    seq = str(sys.stdin.readline().strip())
    # print('Good') if f.match(seq) is None else print('Infected') # Error
    print('Infected!' if f.match(seq) else 'Good')

from collections import Counter

# 단어 입력 받음
word = input().upper()
counts = Counter(word)

# 가장 많은 빈도수
max_count = max(counts.values())

# 최대 빈도 수를 가진 key 값 선별
temp_list = [key for key, value in counts.items() if value == max_count]

# key 값이 2개 이상 이면 : ?
# 1개면 해당 문자 출력
if len(temp_list) > 1:
    print('?')
else:
    print(temp_list[0])

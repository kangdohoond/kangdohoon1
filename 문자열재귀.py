def find(curr, tail, size):
    if curr == tail:
        return 0 # 0 뜨면 조합 성공
    elif len(curr) == size:
        return 1

    find(curr + 'A', tail, size) # 이진트리 느낌
    if find(curr + 'A', tail, size) == 0:
        return 0

    curr += 'B' # 하노이탑 알고리즘이랑 비슷
    curr = curr[::-1] # 역순으로 바꿔주는 코드
    find(curr, tail, size)   # 이진트리 느낌

    return find(curr, tail, size)

arr = input("A와 B로 이루어진 문자열 입력: ")
end = input("조합할 AB: ")

find(arr, end, len(end)) # current,tail,tail길이

if find(arr, end, len(end)) == 0:
    print("1")
else:
    print("0") # 0
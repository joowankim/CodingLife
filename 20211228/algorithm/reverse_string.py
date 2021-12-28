# 문제 출처: https://www.acmicpc.net/problem/1439
# 연속된 숫자만 뒤집을 수 있다
# 필요한 것
# 1. 모두 같은 숫자인지 판별하기 - 전부 1로 만드는 경우, 전부 0으로 만드는 경우
# 2. 뒤집는 횟수 세기
#   - zero_count
#       - 모든 수를 0으로 바꾸기 위한 뒤집는 횟수 반환
#   - one_count
#       - 모든 수를 1로 바꾸기 위한 뒤집는 횟수 반환
# 3. 연속된 숫자 뒤집기
#   - 부분 문자열을 받는다
#   - 어느 숫자로 바꾸는지를 파라미터로 받는다
#   - 1로 만들 때: 1인 인덱스 반환
#   - 0으로 만들 때: 0인 인덱스 반환
#   - 끝까지 뒤집으면 -1 반환

def reverse(sub_s, change_to):
    for i in range(len(sub_s)):
        if change_to == "1" and sub_s[i] == "1":
            return i
        elif change_to == "0" and sub_s[i] == "0":
            return i
    return len(sub_s)


def zero_count(s):
    cnt = 0
    zero_index = 0
    length = len(s)
    while zero_index < length:
        if s[zero_index] == "1":
            zero_index += reverse(s[zero_index:], "0")
            cnt += 1
        zero_index += 1
    return cnt


def one_count(s):
    cnt = 0
    one_index = 0
    length = len(s)
    while one_index < length:
        if s[one_index] == "0":
            one_index += reverse(s[one_index:], "1")
            cnt += 1
        one_index += 1
    return cnt


def solution(s):
    return min(zero_count(s), one_count(s))


assert reverse("000001", "1") == 5
assert reverse("00110", "1") == 2
assert reverse("00000", "1") == 5
assert reverse("1111", "0") == 4
assert reverse("11110", "0") == 4
assert reverse("110011", "0") == 2

assert zero_count("0001100") == 1
assert zero_count("1") == 1
assert zero_count("0") == 0
assert zero_count("11111") == 1
assert zero_count("0000000001") == 1
assert zero_count("1100110011001100000001") == 5
assert zero_count("11101101") == 3

assert one_count("0001100") == 2
assert one_count("1") == 0
assert one_count("0") == 1
assert one_count("11111") == 0
assert one_count("0000000001") == 1
assert one_count("1100110011001100000001") == 4
assert one_count("11101101") == 2

assert solution("0001100") == 1
assert solution("1") == 0
assert solution("0") == 0
assert solution("11111") == 0
assert solution("00000001") == 1
assert solution("11001100110011000001") == 4
assert solution("11101101") == 2

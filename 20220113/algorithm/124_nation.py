# 프로그래머스 - 124 나라의 숫자
#
# 4진법인가?
# 4진법은 아닌데 아래를 보자
# 7 = 3 * 2 + 1
# 13 = ( 3 * 1 + 1 ) * 3 + 1


def solution(n):
    answer = ""
    while n > 0:
        share = n // 3
        remainder = n % 3
        if remainder == 0:
            n = share - 1
            answer = "4" + answer
        else:
            n = share
            answer = "412"[remainder] + answer
        if n < 3:
            answer = "012"[n] + answer
            break
    return str(int(answer))


assert solution(1) == "1"
assert solution(2) == "2"
assert solution(3) == "4"
assert solution(4) == "11"
assert solution(5) == "12"
assert solution(6) == "14"

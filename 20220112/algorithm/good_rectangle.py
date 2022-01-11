# 프로그래머스 - 멀쩡한 사각형
#
# 한 쪽 모서리에서 시작한 대각선이 만나는 첫 격자점
#   - 가로, 세로를 최대공약수로 나눈점
# 최대 공약수 구하기
# 대각선에 닿지 않는 사각형의 개수
#   - 직각 삼각형에서 사용할 수 있는 사각형의 개수
from math import gcd, ceil


def available_rectangles(min_w, min_h):
    answer = (ceil(min_w) - 1) * (min_h - 1)
    return answer


def solution(w, h):
    g = gcd(w, h)
    available = available_rectangles(w // g, h // g)
    return w * h - (w // g * h // g - available) * g


assert solution(8, 12) == 80
assert solution(3, 4) == 6
assert solution(100000000, 1) == 0

assert available_rectangles(2, 3) == 2
assert available_rectangles(3, 4) == 6

# 프로그래머스 - 짝지어 제거하기
#
# 1. 연속적으로 같은 문자가 있는지 검색한다.
# 2. 같은 문자 연속되면 나오면 해당 문자열을 지운다.
# 3. 이전 문자랑 비교하기 위해 스택을 사용한다.


def remove_continuous(s):
    stack = [s[0]]

    for c in s[1:]:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


def solution(s):
    removed = remove_continuous(s)
    return 0 if removed else 1


assert remove_continuous("baabaa") == ""
assert remove_continuous("cdcd") == "cdcd"

assert solution("baabaa") == 1
assert solution("cdcd") == 0

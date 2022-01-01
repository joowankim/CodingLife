# 프로그래머스 - N으로 표현
#
# 생각이 안 나
# 점화식이... 아닌데..
# DP는 점화식 세우는 게 능사가 아닌가보다
# N이 사용된 개수를 변수로 하는 점화식
# k번째 스텝에 메모이제이션되는 원소들은 N을 k번 활용해서 만들 수 있는 수


def solution(N, number):
    limit = 8
    steps = [{}]

    for num in range(1, limit+1):
        possible_numbers = set()
        possible_numbers.add(int(str(N) * num))

        for num_of_n in range(1, num):
            for x in steps[num_of_n]:
                for y in steps[num - num_of_n]:
                    possible_numbers.add(x + y)
                    possible_numbers.add(x - y)
                    possible_numbers.add(x * y)
                    if y != 0:
                        possible_numbers.add(x // y)
        steps.append(possible_numbers)
        if number in steps[num]:
            return num
    return -1


assert solution(5, 12) == 4
assert solution(2, 11) == 3
assert solution(1, 1) == 1

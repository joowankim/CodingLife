def solution(N):
    cnt = 0
    for hour in range(N+1):
        for min in range(60):
            for sec in range(60):
                if hour == 3:
                    cnt += 1
                elif '3' in str(min):
                    cnt += 1
                elif '3' in str(sec):
                    cnt += 1
    return cnt


assert solution(5) == 11475

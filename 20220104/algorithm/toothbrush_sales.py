# 프로그래머스 - 다단계 칫솔 판매
#
# 각 판매원에게 배분된 이익금 리스트 (enroll에 적힌 이름 순으로)
# 구현해야 하는 내용
# 1. 사람마다 이익금 계산하기 - 칫솔 개당 이익금: 100원
# 2. 계산한 이익금을 분배하기
#   - 추천인 타고 올라가야 된다. - 그래프 사용할까? 링크드리스트?
#   - 추천인에 대한 자료구조는 리스트로 충분했다.
# 3. 모든 인원에 대해 1, 2 반복


def distribute(referrals, referred, profit, distributed):
    mine = profit
    while referred:
        send = mine // 10
        if send == 0:
            distributed[referred] += mine
            return
        mine -= send
        distributed[referred] += mine
        referred = referrals[referred]
        mine = send


def solution(enroll, referral, seller, amount):
    profits = list(map(lambda x: x * 100, amount))
    distributed = [0] * (len(enroll) + 1)
    user_ids = {name: (user_id + 1) for user_id, name in enumerate(enroll)}
    referrals = [0] + [user_ids.get(referral_name, 0) for referral_name in referral]

    for a_seller, profit in zip(seller, profits):
        distribute(referrals, user_ids[a_seller], profit, distributed)
    return distributed[1:]


assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10]
) == [360, 958, 108, 0, 450, 18, 180, 1080]
assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4]
) == [0, 110, 378, 180, 270, 450, 0, 0]

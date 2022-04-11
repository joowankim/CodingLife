# 1. 펜을 선택할 수 있다.
# 2. 종이가 존재한다.
# 3. 사방으로 이동할 수 있다.
# 4. 이동거리에 단위가 존재한다.(cm)


class Paper:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

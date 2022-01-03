# 프로그래머스 - 정수  삼각형

문제 링크: https://programmers.co.kr/learn/courses/30/lessons/43105

## 문제 푸는 타임라인

1. 문제 파악: 30분 - 2차원 일반항 정의
2. 1차 제출: 45분 - 다이나믹 프로그래밍으로 구현 - 성공

## 후기

- 문제를 클릭하면서 해답 유형을 볼 수 밖에 없어서 DP로 생각을 고정해서 푼 것 같다.
- 그래도 일반항을 정의하기가 쉽지만은 않았다.
- 처음에는 층수(h)만을 변수로 하는 일반항을 만들어보려고 했다.
  - h층에서의 최대값
- 하지만 현재 가리키고 있는 수의 인덱스 또한 변수라는 것을 파악하는데에는 시간이 좀 걸렸던 것 같다.
- 결국은 **h층에서의 k번째 수를 선택했을 때의 최대값**을 일반항으로 잡았다.
  - a<sub>hk</sub> = max(a<sub>h-1k-1</sub>, a<sub>h-1k</sub>) + triangle<sub>hk</sub>
n = int(input())

number = []
for i in range(n):
    number.append(list(map(int, input().split(' '))))

# DP 테이블
dp = []
j = 0
# DP 테이블 또한 피라미드 형태로
for i in range(n):
    j += 1
    dp.append([0] * j)
# DP 테이블 초기값
dp[0] = number[0]
# DP 진행, 피라미드 꼭대기부터 시작
# 피라미드 형태의 dp 값을 하나씩 보기 위해 1씩 증가하는 j를 생성
j = 1
for i in range(1, n):
    j += 1
    for k in range(j):
        # 피라미드의 양 끝에 있는 경우 고려
        if k == 0:
            dp[i][k] = number[i][k] + dp[i - 1][k]
        elif k == (j - 1):
            dp[i][k] = number[i][k] + dp[i - 1][k - 1]
        else:
            dp[i][k] = number[i][k] + max(dp[i - 1][k - 1], dp[i - 1][k])
# 피라미드의 맨 아래줄에서 가장 큰 수가 최대값
print(max(dp[n-1]))

"""
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.

입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.

출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.

예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
"""
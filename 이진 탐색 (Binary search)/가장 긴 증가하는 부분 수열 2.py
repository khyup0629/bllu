# 가장 긴 증가하는 부분 수열의 시간 복잡도를 O(NlogN)으로 만들 수 있는 아이디어는 아래와 같다.
# 먼저 부분수열이 들어갈 리스트를 하나 생성한다. 이 리스트에는 오름차순 순으로 입력된 수열의 요소가 들어간다.
# 입력된 수열을 앞에서부터 하나씩 탐색하고, 현재 수가 부분수열의 최대값보다 크다면 부분수열의 맨 끝에 추가한다.
# 현재 수가 부분수열의 맨 끝 수보다 작다면, 이진 탐색을 통해 오름차순으로 들어갈 수 있는 위치를 찾고 그 위치값을 대신한다.
# 부분수열의 오른쪽 끝 최댓값보다 작은 수를 오름차순으로 들어갈 부분에 덮어씌움으로써
# 부분수열의 길이 변화 없이 작은 수에 대해 처리할 수 있다.
# 따라서, 이 최적화법은 가장 긴 증가하는 부분 수열의 길이를 구하는데 사용가능하다.
# 하지만, 가장 긴 증가하는 부분 수열을 찾는 것은 불가능한 알고리즘.
from bisect import bisect_left
n = int(input())
array = list(map(int, input().split()))
# 부분 수열
dp = [array[0]]
# 입력된 수열을 앞에서부터 하나씩 탐색
for num in array[1:]:
    # 현재 수가 부분수열의 최대값보다 크다면 부분수열의 맨 끝에 추가한다.
    if num > dp[-1]:
        dp.append(num)
    # 현재 수가 부분수열의 맨 끝 수보다 작다면
    else:
        # 이진 탐색을 통해 오름차순으로 들어갈 수 있는 위치를 찾고 그 위치값을 대신한다.
        index = bisect_left(dp, num)
        dp[index] = num

print(len(dp))

"""
(예시)
수열 = [30, 10, 20, 35, 25, 40, 60]
1. 부분 수열 = [30]
2. 10은 부분 수열의 최댓값인 30보다 작으므로 이진 탐색을 통해 부분 수열에서 오름차순으로
10이 들어갈 인덱스를 찾는다. 인덱스의 결과는 0. 그럼 부분수열[0]의 위치를 10으로 덮어씌운다.
부분 수열 = [10]
3. 20은 부분 수열의 최댓값인 10보다 크므로 부분 수열의 끝에 추가한다.
부분 수열 = [10, 20]
4. 35는 부분 수열의 최댓값인 20보다 크므로 부분 수열의 끝에 추가한다.
부분 수열 = [10, 20, 35]
5. 25는 부분 수열의 최댓값인 35보다 작으므로 이진 탐색을 통해 부분 수열에서 오름차순으로
25가 들어갈 인덱스를 찾는다. 인덱스의 결과는 2. 그럼 부분수열[2]의 위치를 25로 덮어씌운다.
부분 수열 = [10, 20, 25]
6. 40는 부분 수열의 최댓값인 25보다 크므로 부분 수열의 끝에 추가한다.
부분 수열 = [10, 20, 25, 40]
7. 60는 부분 수열의 최댓값인 40보다 크므로 부분 수열의 끝에 추가한다.
부분 수열 = [10, 20, 25, 40, 60]
따라서, 가장 긴 증가하는 부분 수열의 길이는 5.

문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 
길이는 4이다.

입력
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

출력
첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

예제 입력 1 
6
10 20 10 30 20 50
예제 출력 1 
4
"""
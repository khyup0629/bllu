# 문제 풀이 아이디어 참고 : https://mygumi.tistory.com/245
# 부모 노드가 바로 다음 비행기가 들어갈 자리이다.
# 비행기가 들어오면 gi자리를 먼저 탐색하고 자리가 없으면 gi-1에 넣는 식의 풀이를 할 수 있는데,
# gi의 부모 노드를 gi-1로 기록을 해 놓으면 gi의 부모 노드를 찾는 것만으로 다음 비행기가 들어갈 자리를 빠르게 찾아낼 수 있다.
# union(gi의 부모 노드, gi-1의 부모 노드)를 통해 gi의 부모 노드를 gi - 1로 기록한다.
# find(gi) == 0 이면 비행기가 더이상 들어갈 자리가 없으므로 반복을 멈추고 cnt를 출력한다.
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]


def find(x):  # 부모 노드 찾기
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):  # 부모 노드 설정
    a = find(a)
    b = find(b)
    parent[a] = b


cnt = 0
for i in range(p):
    gi = int(input())
    x = find(gi)  # gi의 부모 노드
    if x != 0:
        union(x, x-1)  # gi의 부모 노드를 gi-1로 기록
        cnt += 1
    else:
        break

print(cnt)

"""
문제
오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 
당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 
비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

입력
첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.

두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.

이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.

출력
승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.

예제 입력 1 
4
3
4
1
1
예제 출력 1 
2
예제 입력 2 
4
6
2
2
3
3
4
4
예제 출력 2 
3
힌트
예제 1 : [2][?][?][1] 형태로 도킹시킬 수 있다. 3번째 비행기는 도킹시킬 수 없다.

예제 2 : [1][2][3][?] 형태로 도킹 시킬 수 있고, 4번째 비행기는 절대 도킹 시킬 수 없어서 이후 추가적인 도킹은 불가능하다.
"""
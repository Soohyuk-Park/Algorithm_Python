# https://www.acmicpc.net/problem/15649 #

n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m: ## m이라는 길이가 되면 출력 해줘야지~
        print(' '.join(map(str, s)))# 이부분도 중요한데. s라는 리스트를 문자열로 바꾸고 그냥 쭉 합치면 된다는거지
        return

    for i in range(1, n + 1):
        if i not in s:#처음엔 빈 리스트라 아무것도 없으니 하나씩 채워주고.
            s.append(i)
            dfs() #이걸로 반복해서 돌면서 이미 있는것들은 빼고 없는것만 추가적으로 채워진다.
            s.pop() # n,m = 5, 3일때를 예시로 들면 처음에는 123이 나오겠지
            #그 다음엔 3을 팝 하면서 for문에 의해 4가 들어가서 124나오고 -> 125나오고 ...
            #마지막엔 542 -> 543 나오면서 마무리 되겠지


dfs()

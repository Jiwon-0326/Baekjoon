from collections import deque

def solution(n, wires):
    # 1. 인접 리스트 만들기
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 2. BFS 함수 (전선 하나 끊은 상태에서 노드 개수 세기)
    def bfs(start, cut_a, cut_b):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        count = 1

        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                # 끊은 전선이면 건너뜀
                if (node == cut_a and next_node == cut_b) or \
                   (node == cut_b and next_node == cut_a):
                    continue

                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
                    count += 1

        return count

    # 3. 모든 전선을 하나씩 끊어보며 최소 차이 계산
    answer = n
    for a, b in wires:
        cnt = bfs(a, a, b)
        diff = abs(n - 2 * cnt)
        answer = min(answer, diff)

    return answer

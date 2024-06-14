from collections import defaultdict, deque
from pprint import pprint

def alien_order(words):
    # pprint(words)

    # initialize graph vertexes
    n = len(words)
    graph = defaultdict(list)
    for i in range(n):
        m = len(words[i])
        for j in range(m):
            graph[words[i][j]]

    # initialize graph edges
    for i in range(1, n):
        p = len(words[i - 1])
        q = len(words[i])
        m = min(p, q)
        d = False
        for j in range(m):
            if not words[i - 1][j] == words[i][j] and not d:
                graph[words[i - 1][j]].append(words[i][j])
                d = True
        if not d and p > q:
            return str()

    # pprint(graph)

    # initialize inbound counter
    inbound = defaultdict(int)
    for v in graph:
        inbound[v]
        for u in graph[v]:
            inbound[u] += 1

    # pprint(inbound)
    # if all([inbound[v] == 0 for v in inbound]):
    #     if len(words) == 1:
    #         return inbound.keys()
    #     else:
    #         return str()

    # initialize bfs queue
    queue = deque()
    for v in inbound:
        if inbound[v] == 0:
            queue.append(v)

    # sort vertexes
    ordered = str()
    while queue:
        v = queue.popleft()
        ordered += v

        for u in graph[v]:
            inbound[u] -= 1
            if inbound[u] == 0:
                queue.append(u)

    # print(ordered)

    if len(ordered) == len(graph):
        return ordered
    return str()

if __name__ == "__main__":
    cases = [
        # (["hello", "world", "world"], "helordw"),
        # (["xro","xma","per","prt","oxh","olv"], "xaethvlprom"),
        # (["o","l","m","s"], "olms"),
        # (["mdx","mars","avgd","dkae"], ""),
        # (["mdxok","mrolw","mroqs","kptz","klr","klon","zvef","zrsu","zzs","orm","oqt"], "mdxwsptnvefuklrqzo"),
        (["m","mx","mxe","mxer","mxerl","mxerlo","mxerlos","mxerlost","mxerlostr","mxerlostrpq","mxerlostrp"], ""),
        (["mtaky","mtakyxy","mtakyxyrr","mtakyxyrrvc","mtakyxyrrvcuq","mtakyxyrrvcuqnu","mtakyxyrrvcuqnufn","mtakyxyrrvcuqnufnam"], ""),
        # (["wgencorejikhdiwnbhx"], "wgencorjikhdbx")
    ]
    for input, expected in cases:
        actual = alien_order(input)
        assert actual == expected

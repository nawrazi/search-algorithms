from collections import defaultdict
import heapq

from numpy import Inf
def dijkstra(graph, start, target):
    if start not in graph.nodes or target not in graph.nodes:
        return []

    heap = [(0, graph.nodes[start])]
    seen = {node : float("inf") for node in graph.nodes}
    seen[start] = 0

    while heap:
        cur_distance, cur_node = heapq.heappop(heap)
        if cur_node.val == target:
            # print(cur_distance)
            return cur_distance

        for edge in graph.edges[cur_node]:
            nex_node = edge.tail
            nex_distance = cur_distance + edge.weight

            if nex_distance > seen[nex_node.val]:
                continue
            if nex_distance < seen[nex_node.val]:
                heapq.heappush(heap, (nex_distance, nex_node))
                seen[nex_node.val] = nex_distance 
                

    return 0
# Rui Wang
# bxe5fd
# PA5: EDP and VDP 

import networkx as nx

def solve_edp_vdp(v, edges, mode):
    G = nx.DiGraph()

    source = 0
    sink = v - 1

    if mode == 'E':
        #edge disjoint: add each edge with capacity 1
        for u, w in edges:
            G.add_edge(u, w, capacity=1)
    elif mode == 'V':
        #vertext disjoint: split all nodes except source/sink
        for u in range(v):
            if u == source or u == sink:
                continue
            G.add_edge(f"{u}_in", f"{u}_out", capacity=1)

        for u, w in edges:
            from_u = u if u in (source, sink) else f"{u}_out"
            to_w = w if w in (source, sink) else f"{w}_in"
            G.add_edge(from_u, to_w, capacity=1)

    #determine correct source/sink nodes for flow
    flow_source = source
    flow_sink = sink
    if mode == 'V':
        flow_source = source
        flow_sink = sink

    flow_value, flow_dict = nx.maximum_flow(G, flow_source, flow_sink)

    #reconstruct paths from flow_dict
    paths = []
    used = set()

    def reconstruct_path(u, path):
        if (mode == 'V' and u == sink) or (mode == 'E' and u == sink):
            return True
        for v in flow_dict[u]:
            if flow_dict[u][v] > 0 and (u, v) not in used:
                used.add((u, v))
                path.append(v)
                if reconstruct_path(v, path):
                    return True
                path.pop()
                used.remove((u, v))
        return False

    for _ in range(flow_value):
        path = [flow_source]
        if reconstruct_path(flow_source, path):
            final_path = []
            for node in path:
                if isinstance(node, int):
                    node_id = node
                else:
                    node_id = int(str(node).split("_")[0])
                if not final_path or final_path[-1] != node_id:
                    final_path.append(node_id)
            paths.append(final_path)

    return paths

#input reading
test_cases = int(input())
for _ in range(test_cases):
    v, e, mode = input().split()
    v = int(v)
    e = int(e)
    edge_data = list(map(int, input().split()))
    edges = [(edge_data[i], edge_data[i + 1]) for i in range(0, len(edge_data), 2)]

    result_paths = solve_edp_vdp(v, edges, mode)

    print(len(result_paths))
    for path in result_paths:
        print(' '.join(map(str, path)))
    print()

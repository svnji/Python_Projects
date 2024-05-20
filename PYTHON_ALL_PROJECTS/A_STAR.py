class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1
        }

        return H[n]

    def a_star_algorithm(self, start, stop):
        open_lst = {start}  # {A}
        closed_lst = set([])  # explored

        cost_to_reach = {start: 0}

        parnt = {start: start}

        while len(open_lst) > 0:
            n = None  # {A,D,C}

            for v in open_lst:
                if n is None or cost_to_reach[v] + self.h(v) < cost_to_reach[n] + self.h(n):  # f(A) < F(D)
                    n = v

            if n is None:
                print('Path does not exist!')
                return None

            if n == stop:
                reconst_path = []

                while parnt[n] != n:  # {B:A, D:B, A:A}
                    reconst_path.append(n)
                    n = parnt[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):  # {B:1, D:7, C:3}
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    parnt[m] = n  # {B:A}
                    cost_to_reach[m] = cost_to_reach[n] + weight  # {}

                else:
                    if cost_to_reach[m] > cost_to_reach[n] + weight:  # 6 .  7
                        cost_to_reach[m] = cost_to_reach[n] + weight
                        parnt[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None


adjac_lis = {
    'S': [('D', 5), ('A', 2)],
    'D': [('A', 2), ('E', 2)],
    'A': [('D', 2), ('B', 1)],
    'B': [('C', 4), ('E', 5)],
    'E': [('B', 5), ('')],
    'C': [('A', 3)],
    'F': [],
    'G': []
}

graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')

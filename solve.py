#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import itertools
import random
import heapq


N_COLORS = 3
N_BUCKETS = 5
FULL_VISIBILITY = True


class PQ:
    def __init__(self):
        self.__heap = []
        self.__dict = {}
        self.__count = itertools.count()

    def __len__(self):
        return len(self.__dict)

    def __remove(self, item):
        elem = self.__dict.pop(item)
        elem[-1] = None

    def push(self, item, priority):
        if item in self.__dict:
            if self.__dict[item][0] <= priority:
                return
            self.__remove(item)
        elem = [priority, next(self.__count), item]
        heapq.heappush(self.__heap, elem)
        self.__dict[item] = elem

    def pop(self):
        while self.__heap:
            priority, _, item = heapq.heappop(self.__heap)
            if item is not None:
                del self.__dict[item]
                return item, priority
        raise KeyError('PQ Empty')


class Layout:
    @staticmethod
    def random():
        balls = list(range(N_COLORS)) * 4
        random.shuffle(balls)
        buckets = {i: [] for i in range(N_BUCKETS)}
        buckets.update({i: balls[i * 4:(i + 1) * 4] for i in range(len(balls) // 4)})
        return Layout(buckets)

    def __init__(self, buckets):
        self.buckets = buckets

    def __hash__(self):
        # maybe slower than it needs to be
        return hash(tuple(tuple(self.buckets[i]) for i in range(N_BUCKETS)))

    def __eq__(self, other):
        # maybe slower than it needs to be
        return self.buckets == other.buckets

    def __repr__(self):
        return '\n'.join(str(self.buckets[i]) for i in range(N_BUCKETS))

    def is_organized(self):
        # maybe slower than it needs to be
        return all(len(set(e)) <= 1 for e in self.buckets.values())

    def get_moves_and_resulting_layouts(self):
        res = []
        for i_buck in range(N_BUCKETS):
            if len(self.buckets[i_buck]) == 0:
                continue
            i_col = self.buckets[i_buck][-1]
            for f_buck in range(N_BUCKETS):
                if f_buck == i_buck or len(self.buckets[f_buck]) == 4:
                    continue
                if len(self.buckets[f_buck]) != 0 and self.buckets[f_buck][-1] != i_col:
                    continue
                # this is going to be the slowest part
                n_bucks = {k: list(v) for k, v in self.buckets.items()}
                n_bucks[f_buck].append(n_bucks[i_buck].pop())
                res.append((f'{i_col} in {i_buck} to {f_buck}', Layout(n_bucks)))
        return res

    def get_dist_to_organized_heuristic(self):
        # could improve this heuristic
        # right now it assumes you could directly move all balls of a color to the tube with the max of that color
        return sum(4 - max(len([f == i for f in e]) for e in self.buckets.values()) for i in range(N_COLORS))


class SearchState:
    def __init__(self, layout, parent, move, dist):
        self.layout = layout
        self.parent = parent
        self.move = move
        self.dist = dist

    def __hash__(self):
        return hash(self.layout)

    def __eq__(self, other):
        return self.layout == other.layout

    def is_valid(self):
        return True

    def is_finished(self):
        return self.layout.is_organized()

    def get_neighbors(self):
        return [SearchState(f, self, e, self.dist + 1) for e, f in self.layout.get_moves_and_resulting_layouts()]

    def get_dist_from_start(self):
        return self.dist

    def get_dist_to_finish_heuristic(self):
        # note that this implementation of non-full visibility is naive because we could remember what we have seen
        if not FULL_VISIBILITY:
            return 0
        return self.layout.get_dist_to_organized_heuristic()


def search(start):
    q = PQ()
    q.push(start, start.get_dist_from_start())
    vis = set()
    while q:
        curr, _ = q.pop()
        if not curr.is_valid():
            continue
        if curr in vis:
            continue
        vis.add(curr)
        if curr.is_finished():
            return curr
        for nbor in curr.get_neighbors():
            q.push(nbor, nbor.get_dist_from_start() + nbor.get_dist_to_finish_heuristic())
    return None


def main():
    layout = Layout.random()
    start = SearchState(layout, None, None, 0)
    end = search(start)
    cur = end
    moves = []
    while cur:
        moves.insert(0, cur.move)
        cur = cur.parent
    print(layout)
    print('\n'.join(moves))


if __name__ == '__main__':
    main()

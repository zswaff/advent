import itertools
from heapq import heappush, heappop
from collections import namedtuple

from abc import ABC, abstractmethod


ALWAYS_IGNORED_VARS = {"dist", "ignored_vars"}


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
        heappush(self.__heap, elem)
        self.__dict[item] = elem

    def pop(self):
        while self.__heap:
            priority, _, item = heappop(self.__heap)
            if item is not None:
                del self.__dict[item]
                return item, priority
        raise KeyError("PQ Empty")


class BaseSearchState(ABC):
    Result = namedtuple("Result", ["distance", "visited", "end_state"])

    def __init__(self, ignored_vars=None):
        if ignored_vars is None:
            ignored_vars = set()
        self.ignored_vars = ignored_vars | ALWAYS_IGNORED_VARS

    def __hash__(self):
        return hash(tuple(v for _, v in sorted(self.get_vars().items())))

    def __eq__(self, other):
        return self.get_vars() == other.get_vars()

    def __repr__(self):
        return self.get_vars()

    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def is_finished(self):
        pass

    @abstractmethod
    def get_neighbors(self):
        pass

    @abstractmethod
    def get_dist_from_start(self):
        pass

    def get_vars(self):
        return {k: v for k, v in vars(self).items() if k not in self.ignored_vars}

    def get_dist_to_finish_heuristic(self):
        return 0

    def process(self):
        pass

    def search(self):
        q = PQ()
        q.push(self, self.get_dist_from_start())
        vis = set()
        while q:
            curr, _ = q.pop()
            if not curr.is_valid():
                continue
            if curr in vis:
                continue
            vis.add(curr)
            curr.process()
            if curr.is_finished():
                return BaseSearchState.Result(curr.get_dist_from_start(), vis, curr)
            for nbor in curr.get_neighbors():
                q.push(
                    nbor,
                    nbor.get_dist_from_start() + nbor.get_dist_to_finish_heuristic(),
                )
        return BaseSearchState.Result(None, vis, None)

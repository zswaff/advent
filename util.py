import itertools
from heapq import heappush, heappop


from abc import ABC, abstractmethod


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
        raise KeyError('PQ Empty')


class BaseSearchState(ABC):
    def __raise_not_implemented_error(self):
        import inspect
        stack = inspect.stack()
        fn = stack[1].function
        cls = type(self).__name__.split('.')[-1]
        raise NotImplementedError(f'{fn} not implemented on {cls}')

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    def __repr__(self):
        self.__raise_not_implemented_error()

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

    def bfs(self):
        q = [self]
        vis = set()
        while q:
            curr = q.pop(0)
            if not curr.is_valid():
                continue
            if curr.is_finished():
                return curr.get_dist_from_start()
            if curr in vis:
                continue
            vis.add(curr)
            for nbor in curr.get_neighbors():
                q.append(nbor)

    def get_dist_to_finish_heuristic(self):
        self.__raise_not_implemented_error()

    def a_star(self):
        q = PQ()
        q.push(self, self.get_dist_from_start())
        vis = set()
        while q:
            curr, _ = q.pop()
            if not curr.is_valid():
                continue
            if curr.is_finished():
                return curr.get_dist_from_start()
            if curr in vis:
                continue
            vis.add(curr)
            for nbor in curr.get_neighbors():
                q.push(nbor, nbor.get_dist_from_start() + nbor.get_dist_to_finish_heuristic())

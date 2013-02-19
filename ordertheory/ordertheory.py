import itertools
import pickle

class Powerset(object):

    def powerset(self, iterable):
        l = list(iterable)
        return itertools.chain.from_iterable(itertools.combinations(l, r) for r in range(len(l)+1))

####################################################################################################################
####################################################################################################################

class FunctionalSpace(object):

    def __rel(self, list0, list1):
        prod = itertools.product(list0, list1)
        pset = Powerset().powerset(prod)
        for rel in pset:
            yield dict(list(rel))

    def funcs(self, list0, list1):
        dom = list(list0)
        codom = list(list1)
        if dom == [] and codom == []:
            return []
        elif dom != [] and codom == []:
            return []
        elif dom == [] and codom != []:
            return [[]]
        elif dom != [] and codom != []:
            rel = self.__rel(dom, codom)
            return [dict(tupleized).items() for tupleized in set(tuple(item.items()) for item in rel) if len(dict(tupleized).keys()) == len(dom)]

####################################################################################################################
####################################################################################################################

class StrictTotalOrders(object):

    def __recurse(self, l, orders=[]):
        if l:
            orders = orders + list(itertools.product([l[0]], list(l[1:])))
            return self.__recurse(list(l[1:]), orders)
        else:
            return orders

    def orders(self, iterable):
        l = list(iterable)
        permutations = itertools.permutations(l)
        for permutation in permutations:
            yield frozenset(self.__recurse(permutation))

####################################################################################################################
####################################################################################################################

class StrictOrders(object):

    lattice = {}

    def __is_not_transitive(self, relation):
        product = itertools.product(list(relation), list(relation))
        for x in product:
            if x[0][1] == x[1][0]:
                if (x[0][0], x[1][1]) not in list(relation):
                    return True

    def __orders(self, l):
        torders = list(StrictTotalOrders().orders(l))
        for order in torders:
            pset = Powerset().powerset(list(order))
            for relation in pset:
                if self.__is_not_transitive(relation) != True:
                    yield frozenset(relation)

    def get_orders(self, iterable):
        l = list(iterable)
        torders = list(StrictTotalOrders().orders(l))
        for s, t in itertools.product(self.__orders(l), self.__orders(l)):
            try:
                self.lattice[s]
            except:
                self.lattice.update({s:{'max':set([]), 'up':set([]), 'down':set([])}})
            if s.issuperset(t):
                self.lattice[s]['down'].add(t)
                if s.issubset(t):
                    self.lattice[s]['up'].add(t)
                    if t in torders:
                        self.lattice[s]['max'].add(t)
            elif s.issubset(t):
                self.lattice[s]['up'].add(t)
                if t in torders:
                    self.lattice[s]['max'].add(t)
        return self.lattice

    def write_to_pickle(self, iterable):
        l = list(iterable)
        length = len(l)
        pickle.dump(self.get_orders(l), open('gspace_%scons.p' %(length), 'wb'))
        return 'Orders written.'


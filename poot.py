__author__ = "Alex Djalali"
__date__ = "2013-02-15"
__version__ = "1.0"
__maintainer__ = "Alex Djalali"
__email__ = "See the author's website"

##############################################################################
##############################################################################

import cPickle
import itertools
import dataset
from ordertheory import Powerset

##############################################################################
##############################################################################

class PoOT(object):

    def __init__(self):
        self._dset    = []
        self._lattice = {}

    @property
    def dset(self):
        return self._dset

    @dset.setter
    def dset(self, value):
        self.lattice = value
        self._dset = self._dset + value

    @property
    def lattice(self):
        return self._lattice

    @lattice.setter
    def lattice(self, value):
        cons = len(value[0]['vvector'].keys())
        self._lattice = cPickle.load(open('lattices/gspace_%scons.p' %(cons,), 'rb'))

    def get_optimal_candidates(self):
        """Get all optimal candidates."""
        PoOT = dataset.PoOTDataSet()
        PoOT.dset = self.dset
        opt = [cand.cand for cand in PoOT.dset if cand.opt == True]
        return opt

    def get_nonoptimal_candidates(self):
        """Get all non-optimal candidates."""
        PoOT = dataset.PoOTDataSet()
        PoOT.dset = self.dset
        nonopt = [cand.cand for cand in PoOT.dset if cand.opt == False]
        return nonopt

    def get_harmonically_bounded_candidates(self):
        """Get all harmonically bound candidates."""
        l = []
        PoOT = dataset.PoOTDataSet()
        PoOT.dset = self.dset
        PoOT.cdset = PoOT.dset
        for cand0 in PoOT.cdset.keys():
            for cand1 in PoOT.cdset[cand0].keys():
                if PoOT.cdset[cand0][cand1].hbounded == True:
                    l.append((cand0.cand, cand1.cand))
                else:
                    pass
        return l

    def get_grammars(self, classical=True):
        """Get all grammars compatible with a dataset."""
        PoOT = dataset.PoOTDataSet()
        PoOT.dset = self.dset
        PoOT.fdset = PoOT.dset
        pootdset = PoOT.get_pootdset(PoOT.fdset, self.lattice)
        return Grammars().get_grammars(pootdset, classical)

    def is_compatible_COT_grammar(self, grammar):
        """Check whether COT grammar is compatible
        with the dataset."""
        cots = self.get_grammars(classical=True)
        if grammar in cots:
            return True
        else:
            return False

    def is_compatible_PoOT_grammar(self, grammar):
        """Check whether PoOT grammar is compatible
        with the dataset."""
        poots = self.get_grammars(classical=False)
        if grammar in poots:
            return True
        else:
            return False

    def is_min_grammar(self, grammar):
        """Check whether PoOT grammar is a
        minimally compatible grammar."""
        up = set(self.lattice[grammar]['down'])
        grams = self.get_grammars(classical=False)
        if len(up.intersection(grams)) == 1:
            return True
        else:
            return False

    def min(self, grammars):
        """Get all minimal grammars."""
        s = set([])
        for grammar in grammars:
            if self.is_min_grammar(grammar) == True:
                s.add(grammar)
        return s

    def is_max_grammar(self, grammar):
        """Check whether PoOT grammar is a
        maximally compatible grammar."""
        up = set(self.lattice[grammar]['up'])
        grams = self.get_grammars(classical=False)
        if len(up.intersection(grams)) == 1:
            return True
        else:
            return False

    def max(self, grammars):
        """Get all maximal grammars."""
        s = set([])
        for grammar in grammars:
            if self.is_max_grammar(grammar) == True:
                s.add(grammar)
        return s

    def get_entailments(self, atomic=True):
        """Get candidate entailments. If 'atomic = True',
        get atomic entailments.  Else, get entailments between
        sets of candidates."""
        PoOT = dataset.PoOTDataSet()
        PoOT.edset = self.dset
        PoOT.fdset = PoOT.edset
        pootdset = PoOT.get_pootdset(PoOT.fdset, self.lattice)
        return Entailments().get_entails(pootdset, atomic)

##############################################################################
##############################################################################

class Grammars(object):

    def opt_grams(self, candinfo, classical=True):
        l = []
        for cand0 in candinfo.keys():
            if classical == True:
                l.append(candinfo[cand0].cots)
            elif classical == False:
                l.append(candinfo[cand0].poots)
        return set.intersection(*map(set, l))

    def get_grammars(self, dset, classical=True):
        """Get grammars compatible with dataset."""
        try:
            pos = set.intersection(*map(set, [self.opt_grams(dset[cand], classical) for cand in dset.keys() if cand.opt == True]))
        except:
            pos = set([])
        try:
            neg = set.union(*map(set, [self.opt_grams(dset[cand], classical) for cand in dset.keys() if cand.opt == False]))
        except:
            neg = set([])
        return pos.difference(neg)

##############################################################################
##############################################################################

class Entailments(object):

    def __mapping(self, dset):
        """Map candidates to the set of all and only the
        PoOT grammars that make that candidate optimal."""
        grams = Grammars()
        return [(cand, grams.opt_grams(dset[cand])) for cand in dset.keys()]

    def get_entails(self, dset, atomic=True):
        """Get entailments between (sets of) candidates."""
        lattice = {}
        mapping = self.__mapping(dset)
        if atomic == True:
            prod = itertools.product(mapping, mapping)
        elif atomic == False:
            pset = list(Powerset().powerset(mapping))
            prod = itertools.product(pset, pset)
        for x, y in prod:
            if x != () and y != ():
                if atomic == True:
                    s = frozenset([x[0].cand])
                    t = frozenset([y[0].cand])
                    u = x[1]
                    v = y[1]
                elif atomic == False:
                    s = frozenset([pair[0].cand for pair in x])
                    t = frozenset([pair[0].cand for pair in y])
                    u = set.intersection(*map(set, [pair[1] for pair in x]))
                    v = set.intersection(*map(set, [pair[1] for pair in y]))
                try:
                    lattice[s]
                except:
                    lattice.update({s:{'up':set([]), 'down':set([])}})
                if u.issuperset(v):
                    lattice[s]['down'].add(t)
                    if u.issubset(v):
                        lattice[s]['up'].add(t)
                elif u.issubset(v):
                    lattice[s]['up'].add(t)
        return lattice

##############################################################################
##############################################################################

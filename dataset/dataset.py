import itertools
from ..ordertheory import ordertheory

class DataSet(object):
    """Construct Dataset object."""

    def __init__(self):
        """Empty initialization."""
        self._dset = []
        self._edset = []

    @property
    def dset(self):
        """Dataset getter."""
        return self._dset

    @dset.setter
    def dset(self, value):
        """Dataset setter."""
        self._dset = self.get_dset(value)

    def get_dset(self, dset):
        """Turns list of dictionaries into list of
        'Candidate' objects"""
        return [Candidate(cand) for cand in dset]

    @property
    def edset(self):
        """Entailment dataset getter."""
        return self._edset

    @edset.setter
    def edset(self, value):
        """Entailment dataset setter."""
        self._edset = self.get_edset(value)

    def get_edset(self, dset):
        """Turns list of dictionaries into list of 'Candidate'
        objects, setting their optimal values to True."""
        dset = self.get_dset(dset)
        for cand in dset:
            cand.opt = True
        return dset

#################################################################################################
#################################################################################################

class Candidate(object):

    def __init__(self, dict0):
        self._inp = dict0['input']
        self._out = dict0['output']
        self._vvec = dict0['vvector']
        self._opt = dict0['optimal']
        self.cand = (self._inp, self._out)

    @property
    def inp(self):
        return self._inp

    @inp.setter
    def inp(self, value):
        self._inp = value

    @property
    def out(self):
        return self._out

    @out.setter
    def out(self, value):
        self._out = value

    @property
    def vvec(self):
        return self._vvec

    @out.setter
    def out(self, value):
        self._vvec = value

    @property
    def opt(self):
        return self._opt

    @opt.setter
    def opt(self, value):
        self._opt = value

#################################################################################################
#################################################################################################

class ComparativeDataSet(DataSet):

    def __init__(self):
        DataSet.__init__(self)
        self._cdset = {}

    @property
    def cdset(self):
        return self._cdset

    @cdset.setter
    def cdset(self, value):
        self._cdset = self.get_cdset(value)

    def __comp(self, dict0, dict1):
        win = []
        lose = []
        for n in dict0.keys():
            if dict0[n] < dict1[n]:
                win.append(n)
            elif dict0[n] > dict1[n]:
                lose.append(n)
        return {'win': win, 'lose': lose}

    def __init_cdset(self, dset):

        def helper(x, y):
            try:
                return self._cdset[x].update({y : {}})
            except:
                return self._cdset.update({x : {y :{}}})

        for x, y in itertools.product(dset, dset):
            if x.opt == True:
                if x.inp == y.inp:
                    if x.out != y.out:
                        helper(x, y)
            if x.opt == False:
                if y.opt == True:
                    if x.inp == y.inp:
                        if x.out != y.out:
                            helper(x, y)
        return self._cdset

    def get_cdset(self, dset):
        cdset = self.__init_cdset(dset)
        for cand0 in cdset.keys():
            for cand1 in cdset[cand0].keys():
                compinfo = cdset[cand0][cand1]
                comps = self.__comp(cand0.vvec, cand1.vvec)
                compinfo.update(comps)
                cdset[cand0][cand1] = ComparativeInfo(compinfo)
        return cdset

#################################################################################################
#################################################################################################

class ComparativeInfo(object):

    def __init__(self, dict0):
        self.info = dict0
        self.win = dict0['win']
        self.lose = dict0['lose']

#################################################################################################
#################################################################################################

class FunctionalDataSet(ComparativeDataSet):

    def __init__(self):
        ComparativeDataSet.__init__(self)
        self._fdset = {}

    @property
    def fdset(self):
        return self._fdset

    @fdset.setter
    def fdset(self, value):
        value = super(FunctionalDataSet, self).get_cdset(value)
        self._fdset = self.get_fdset(value)

    def get_fdset(self, cdset):
        fspace = ordertheory.FunctionalSpace()
        for cand0 in cdset.keys():
            for cand1 in cdset[cand0].keys():
                finfo = cdset[cand0][cand1]
                funcs = fspace.funcs(finfo.lose, finfo.win)
                finfo.info.update({'fspace' : funcs })
                cdset[cand0][cand1] = FunctionalInfo(finfo.info)
        return cdset

#################################################################################################
#################################################################################################

class FunctionalInfo(ComparativeInfo):

    def __init__(self, dict0):
        ComparativeInfo.__init__(self, dict0)
        self.fspace = dict0['fspace']

#################################################################################################
#################################################################################################

class COTDataSet(FunctionalDataSet):

    def get_cotdset(self, fdset, lattice):
        for cand0 in fdset.keys():
            for cand1 in fdset[cand0].keys():
                s = set([])
                cotinfo = fdset[cand0][cand1]
                if cotinfo.fspace == []:
                    cotinfo.info.update({'cots': s})
                    fdset[cand0][cand1] = COTInfo(cotinfo.info)
                else:
                    for f in cotinfo.fspace:
                        cots = lattice[frozenset(f)]['max']
                        s.update(cots)
                    cotinfo.info.update({'cots': s})
                    fdset[cand0][cand1] = COTInfo(cotinfo.info)
        return fdset

#################################################################################################
#################################################################################################

class COTInfo(FunctionalInfo):

    def __init__(self, dict0):
        FunctionalInfo.__init__(self, dict0)
        self.cots = dict0['cots']

#################################################################################################
#################################################################################################

class PoOTDataSet(COTDataSet):

    def get_pootdset(self, fdset, lattice):
        cotdset = super(PoOTDataSet, self).get_cotdset(fdset, lattice)
        for cand0 in cotdset.keys():
            for cand1 in cotdset[cand0].keys():
                pootinfo = cotdset[cand0][cand1]
                if pootinfo.cots == set([]):
                    poots = pootinfo.cots
                else:
                    poots = set.union(*map(set, [lattice[frozenset(cot)]['down'] for cot in pootinfo.cots]))
                pootinfo.info.update({'poots': poots})
                cotdset[cand0][cand1] = PoOTInfo(pootinfo.info)
        return cotdset

#################################################################################################
#################################################################################################

class PoOTInfo(COTInfo):

    def __init__(self, dict0):
        COTInfo.__init__(self, dict0)
        self.poots = dict0['poots']

#################################################################################################
#################################################################################################

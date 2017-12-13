#!/usr/bin/python3
from schema2 import session, Family
from multiprocessing import Pool
import json


def getFamStats(fam):
    session.add(fam)
    protnames = set([])
    gounion = set([])
    for a in fam.proteins:
        pname = a.protein.name
        protnames.add(pname)
        gounion |= set([term.name for term in a.protein.GOterms])
    famsize = len(protnames)
    return (famsize, len(gounion))


if __name__ == '__main__':
    with Pool() as p:
        allfams = session.query(Family).all()
        multiple_results = \
            [p.apply_async(getFamStats, [fam]) for fam in allfams]
        numfams = len(multiple_results)
        sizes, funcs = [], []
        for res in multiple_results:
            (famsize, numfuncs) = res.get()
            sizes.append(famsize)
            funcs.append(numfuncs)
        output = {}
        output['sizes'] = sizes
        output['funcs'] = funcs
        print(json.dumps(output))

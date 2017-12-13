#!/usr/bin/python3
from schema2 import session, Protein, GO, Protein2GO
from multiprocessing import Pool
import json


def getProtStats(prot):
    session.add(prot)
    pname = prot.name
    termset = set([term.name for term in prot.GOterms])
    return (pname, list(termset))


if __name__ == '__main__':
    with Pool() as p:
        allprots = session.query(Protein).all()
        multiple_results = \
            [p.apply_async(getProtStats, [prot]) for prot in allprots]

        prots = {}
        for res in multiple_results:
            (pname, terms) = res.get()
            prots[pname] = terms
        print(json.dumps(prots))

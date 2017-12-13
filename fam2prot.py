#!/usr/bin/python3
from schema2 import session, Family
from multiprocessing import Pool
import json

def getFamlist(fam):
    session.add(fam)
    protnames = set([])
    for a in fam.proteins:
        pname = a.protein.name
        protnames.add(pname)
    return (fam.name, sorted(list(protnames)))

if __name__ == '__main__':
    with Pool() as p:
        allfams = session.query(Family).all()
        multiple_results = \
            [p.apply_async(getFamlist, [fam]) for fam in allfams]
        output = {}
        for res in multiple_results:
            (famname, protnames) = res.get()
            output[famname] = protnames
        print(json.dumps(output))

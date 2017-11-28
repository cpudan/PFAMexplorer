#!/usr/bin/python3

import numpy as np, re, sys, argparse
from scipy.sparse import csgraph

def printmatrix(matrix):
    for row in matrix:
        for cell in row:
            print("%.2f" % round(cell,2),end=' ')
        print()

def processMatrix(matrix,threshold):
    threshold = threshold / 100
    size = len(matrix)
    for i in range(0,size):
        for j in range(i+1,size):
            if matrix[i,j] < threshold:
                matrix[i,j] = 0; matrix[j,i] = 0;
    n = csgraph.connected_components(matrix, directed=False)[0]
    #if size > 2 and n >= size-4:
        #disconnected = True
    return n

p = argparse.ArgumentParser()
p.add_argument('thresholds', metavar='N', type=float, nargs='*', help='''\
        Calculates number of connected components in results output with\
        values cut off to 0 at each of these threshold percentages.''')
args = p.parse_args()
if len(args.thresholds) == 0:
    args.thresholds = [90]
args.thresholds = sorted(args.thresholds)

matpat = '>(.+)\n([^>]+)'
content = sys.stdin.read()
i = 0
for m in re.findall(matpat,content):
    header = m[0].rstrip()
    matrix = m[1].split('\n')[0:-1]
    matrix = [[float(entry) for entry in row.strip().split(' ')] for row in matrix]
    matrix = np.array(matrix)
    results = [processMatrix(matrix,t) for t in args.thresholds]
    n = len(results)
    '''for r in range(n):
        for p in range(n):
            if r == p: continue;
            if results[r] != results[p]:
                print(header)
    '''
    #print(header)
    output = header
    for r in results:
        output += ' '+r.__repr__()
    #output = output.replace(' ',',')
    print(output)
    #header = tuple(header.split())
    #name=header[0]
    #size,pannot,minlen,maxlen,diff = tuple([float(x) for x in header[1:]])
    #[print(t,end=' ') for t in args.thresholds]
    #print()
'''
    if i > 2:
        break
    i+=1
print(matrix)
'''

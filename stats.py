import json
from statistics import mean, stdev


famdata = json.load(open('famstats.json'))
protdata = json.load(open('protstats.json'))

family = {}
family['size'] = {'average': mean(famdata['sizes']),
                  'stdev': stdev(famdata['sizes'])}


family['funcs'] = {'average': mean(famdata['funcs']),
                   'stdev': stdev(famdata['funcs'])}

lens = list(filter(lambda x: x is not 0, map(len, protdata.values())))
nfuns = {'average': mean(lens), 'stdev': stdev(lens)}

print(json.dumps(family))

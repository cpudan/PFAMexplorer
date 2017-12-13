import json
from statistics import mean, stdev, mode


famdata = json.load(open('famstats.json'))
protdata = json.load(open('protstats.json'))

family = {}
famsizes = list(filter(lambda x: x is not 0, famdata['sizes']))
family['size'] = {'average': mean(famsizes),
                  'stdev': stdev(famsizes),
                  'mode': mode(famsizes)}


famfuncs = list(filter(lambda x: x is not 0, famdata['funcs']))
family['funcs'] = {'average': mean(famfuncs),
                   'stdev': stdev(famfuncs),
                   'mode': mode(famfuncs)}

lens = list(filter(lambda x: x is not 0, map(len, protdata.values())))
nfuns = {'average': mean(lens), 'stdev': stdev(lens)}

print(json.dumps(family))

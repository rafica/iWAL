import re 
import sys 
from testcases_iyaccer import iWALTestCases 
sys.path.append('../compiler')
import iyaccer

parser = iyaccer.testingYacc()

for attr in iWALTestCases.__dict__.keys():
    if not re.match(r'^__.*__$', attr):
        print getattr(iWALTestCases, attr)
        result = parser.parse(getattr(iWALTestCases, attr))
        print result
        f = open('testfiles/' + attr+'.txt', 'w') 
        f.write(result.__str__())
        f.close()

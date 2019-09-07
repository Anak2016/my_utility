#--insert system path
import sys
sys.path.insert(0, "/path/to/your/package_or_module")

#=====================
#==json
#=====================
import json
#--------read json
json.load(f) # f must have read method eg. object of open()

#--------write json
json.dump("json like string", f, sort_keys=True, indent=2) # f must have read method eg. object of open()
    eg.
        json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4, separators=(',', ': '))

#=====================
#==dictionary
#=====================

#--------dictionary set key value to [] if key does not exist
# 1 way (best and most pythonic and fastest)
    defaultdict(lambda: {})
# 2 way
    dic.setdefault(key,[]).append(value)

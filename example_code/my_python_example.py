#===================
#==collections
#===================
#-----defaultdict
from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla')
ice_cream['Sarah'] = 'Chunky Monkey'
print(ice_cream['Sarah'])
# Chunky Monkey
print(ice_cream['Joe'])
# Vanilla

#=====================
#==json file
#=====================
#--------read
with open(path, 'r') as f:
    print(f"readin from {path}...")
    print(json.load(f))

#--------write
with open(path, 'w') as f:
    print(f"writing to {oath}...")
    json.dump(json_data, f, indent=2)
#---broad casting
import numpy as np
x = np.ones((4,5,2))
nor = np.expand_dims(x.sum(1),1)# expand dimension that is squeezed.
nor_x = x/nor
print(nor_x) # no error


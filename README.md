# funcnotation
## Mathematica Pre/Post Fix Function Notation in Python
An example for creating pip installable packages

### Setup
```bash
pip install git+https://github.com/tomginsberg/funcnotation.git
```
### Example 1
```python
from funcnotation import PrePostFix as P
# find the sum of 8 random integers squared
P(sum) @ ([randint(0, 10) for _ in range(8)] // P(lambda x: [i**2 for i in x]))
```
### Example 2
```python
import numpy as np
def reshape(*size):
    def f(x):
        return np.reshape(x, size=args)
    return P(f)
    
[1,2,3,4] // reshape(2,2)

# array([[1, 2],
#       [3, 4]])
```

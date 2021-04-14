# funcnotation
## Mathematica Pre/Post Fix Function Notation in Python
An example for creating pip installable packages

### Setup
```bash
pip install git+https://github.com/tomginsberg/funcnotation.git
```
### Example
```python
from funcnotation import PrePostFix as P
# find the sum of 8 random intergers squared
P(sum) @ ([randint(0, 10) for _ in range(8)] // P(lambda x: [i**2 for i in x]))
```

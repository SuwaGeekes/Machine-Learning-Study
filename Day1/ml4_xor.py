from ml1_and import AND
from ml2_or import OR
from ml3_nand import NAND

def NOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))

if __name__=='__main__':
  for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    y = NOR(xs[0], xs[1])
    print(str(xs) + " -> " + str(y))
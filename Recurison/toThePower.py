count = 0
newVal = 0
def toThePower(base,exp):
      if exp == 1:
          return(base)
      elif exp != 1:
          return (base*toThePower(base,exp-1))


toThePower(2,3)
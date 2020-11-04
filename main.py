#Fish Tank problem
#Wrte a subroutine that will output the volume of a fish tank
L = 100
h = 50
d = 30
#Subroutine to calculate volume in milmetres
def VinML(L):
  return (L * h * d /1000)
#Main Program
V = VinML(L)
print("The volume is:",V,"litres")
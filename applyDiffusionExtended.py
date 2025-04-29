import numpy as N
import reflectingGrid from reflectingLat.py

def applyDiffusionExtended(latExt):
  reflectingLat(latExt)
  deffusion(diffustionRate, site)

for i in range (len(latExt)):
  if(i == 0):
   #cells are in rows 1 through m and cols 1 though n
    
  else if (i == 1):
    #internal cells are in 2 throught m + 1 and col 2 though n + 1


for j in range(len(latExt)):
  #each
'''
  * take in extened lattice
      rows = m + 2
      col = n + 2
      call defusion

      if(array tool begins with 0):
        cells are in rows 1 through m and cols 1 though n

      if(array tool begins with 1):
        internal cells are in 2 throught m + 1 and col 2 though n + 1

      add an upper bound to remove all rows and cols iwth or without one or more neighbor
      
      
        
  * returns internal lattics with diffusion applied to each site
'''


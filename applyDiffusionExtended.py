import numpy as N
import reflectingGrid from reflectingLat.py

def applyDiffusionExtended(latExt, diffusionRate):
  m_plus_2, n_plus_2 = latExt.shape
  m, n = m_plus_2 -2, n_plus_2 -2

reflectingGrid(latExt)
newLat = latExt.copy()

for i in range(1, m + 1):
  for j in range(1, n + 1):
    
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


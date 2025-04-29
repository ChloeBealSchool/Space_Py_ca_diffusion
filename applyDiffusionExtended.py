from Diffusion import diffusion
import numpy as np

def applyDiffusionExtended(latExt, diffRate):
    data = np.zeros(np.shape(latExt[1:-1, 1:-1]))
    
    # Columns
    for i in range(1, np.shape(data)[0]+1):
        # Rows
        for j in range(1, np.shape(data)[1]+1):
            
            # Current site
            site = latExt[i, j]
            
            # Find the values for the surounding sites
            N = latExt[i, j+1]
            NE = latExt[i+1, j+1]
            E = latExt[i+1, j]
            SE = latExt[i+1, j-1]
            S = latExt[i, j-1]
            SW = latExt[i-1, j-1]
            W = latExt[i-1, j]
            NW = latExt[i-1, j+1]
            
            # Apply the diffusion
            data[i-1, j-1] = diffusion(diffRate, site, N, NE, E, SE, S, SW, W, NW)

    return data
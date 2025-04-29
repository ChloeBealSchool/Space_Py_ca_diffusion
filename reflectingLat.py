#pg 426
def reflectingLat(lat):
    '''
    Accepts a grid and to return a grid extended one cell in each direction 
    with reflecting boundary conditions.

    Method Arguments:
    * lat: A 2D array of numeric values

    Output:
    * A 2D array larger by 1 in each direction with reflected boundary 
    conditions
    
    Using numpy array logic, each side is copied to another row/column to 
    create boundaries for the grid.
    '''
    # Imports
    import numpy as np
    
    # Create the output array
    reflectionShape = np.shape(lat)
    reflectedGrid = np.zeros((reflectionShape[0] + 2, reflectionShape[1] + 2))
    
    # Copy regular data into the output array
    reflectedGrid[1:-1, 1:-1] = lat
    
    # Copy the collums
    reflectedGrid[0,:] = reflectedGrid[1,:]
    reflectedGrid[-1,:] = reflectedGrid[-2,:]
    
    # Copy the rows
    reflectedGrid[:,0] = reflectedGrid[:,1]
    reflectedGrid[:,-1] = reflectedGrid[:,-2]
    return reflectedGrid
import numpy as np

def calculate(list_input):
    """
    Calculate mean, variance, standard deviation, max, min, and sum
    for a 3x3 matrix along both axes and for the flattened matrix.
    
    Args:
        list_input: A list containing 9 numbers
        
    Returns:
        A dictionary containing the calculated statistics
        
    Raises:
        ValueError: If the input list doesn't contain exactly 9 numbers
    """
    
    # Check if the list contains exactly 9 elements
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Calculate statistics
    # axis=0: along columns (vertical), axis=1: along rows (horizontal)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # mean of each column
            matrix.mean(axis=1).tolist(),  # mean of each row  
            matrix.mean().tolist()         # mean of flattened matrix
        ],
        'variance': [
            matrix.var(axis=0).tolist(),   # variance of each column
            matrix.var(axis=1).tolist(),   # variance of each row
            matrix.var().tolist()          # variance of flattened matrix
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),   # std dev of each column
            matrix.std(axis=1).tolist(),   # std dev of each row
            matrix.std().tolist()          # std dev of flattened matrix
        ],
        'max': [
            matrix.max(axis=0).tolist(),   # max of each column
            matrix.max(axis=1).tolist(),   # max of each row
            matrix.max().tolist()          # max of flattened matrix
        ],
        'min': [
            matrix.min(axis=0).tolist(),   # min of each column
            matrix.min(axis=1).tolist(),   # min of each row
            matrix.min().tolist()          # min of flattened matrix
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),   # sum of each column
            matrix.sum(axis=1).tolist(),   # sum of each row
            matrix.sum().tolist()          # sum of flattened matrix
        ]
    }
    
    return calculations

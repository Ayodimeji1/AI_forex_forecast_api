import numpy as np
from fastapi import HTTPException


def preprocess_input(data):
    time_steps = 10
    features = 21
    
    if len(data) != time_steps:
        raise ValueError(f"Expected input with {time_steps} time steps, but got {len(data)}.")
    for step in data:
        if len(step) != features:
            raise ValueError(f"Each time step must have {features} features.")
    
    # Reshape to [batch_size, time_steps, features] -> [1, 10, 21]
    return np.array(data).reshape(1, time_steps, features).astype(np.float32)

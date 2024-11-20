import uvicorn, numpy as np
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def index():
    return "Hello World!"

@app.get("/test")
def index():
    # Target moderate CPU usage through controlled computation
    size = 1000  # Significantly reduced matrix size to prevent memory issues
    iterations = 2  # Reduced number of iterations
    
    try:
        # Initialize smaller matrices
        matrices = []
        for _ in range(iterations):
            matrices.append(np.random.rand(size, size))
        
        # Perform fewer matrix operations
        result = matrices[0]
        for i in range(1, iterations):
            result = np.dot(result, matrices[i])
            # Simplified operations
            result = np.sin(result)
        
        # Clean up to free memory
        del matrices
        
        # Use smaller buffer
        buffer = np.zeros((size//2, size//2))
        buffer += result[:size//2, :size//2]  # Store only a portion
        
        # Clean up
        del result
        del buffer
        
    except Exception as e:
        print(f"Error in computation: {e}")
        return "Computation error"

    return "Test!"
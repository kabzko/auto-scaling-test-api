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
    # Increased workload for CPU testing
    size = 2000  # Larger matrix size
    iterations = 5  # More iterations
    
    try:
        matrices = []
        for _ in range(iterations):
            matrices.append(np.random.rand(size, size))
        
        # More intensive computations
        result = matrices[0]
        for i in range(1, iterations):
            result = np.dot(result, matrices[i])
            # Added more CPU-intensive operations
            result = np.sin(np.cos(np.tan(result)))
            result = np.sqrt(np.abs(result))
            
            # Add some extra matrix operations
            temp = np.transpose(result)
            result = np.dot(result, temp)
        
        # Additional computations to increase load
        for _ in range(3):
            result = np.fft.fft2(result)
            result = np.fft.ifft2(result)
        
        del matrices
        del result
        
    except Exception as e:
        print(f"Error in computation: {e}")
        return "Computation error"

    return "Test completed!"
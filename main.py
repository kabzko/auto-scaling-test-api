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
    # Target ~60% CPU usage through controlled computation
    size = 5000  # Reduced matrix size for more controlled CPU usage
    iterations = 3  # Number of matrix operations to perform
    
    # Initialize matrices
    matrices = []
    for _ in range(iterations):
        matrices.append(np.random.rand(size, size))
    
    # Perform matrix operations to achieve ~60% CPU load
    result = matrices[0]
    for i in range(1, iterations):
        result = np.dot(result, matrices[i])
        # Add element-wise operations to fine-tune CPU usage
        result = np.sin(result) + np.cos(result)
    
    # Moderate memory usage
    buffer = np.zeros((size, size))
    buffer += result  # Keep the result in memory
    return "Test!"
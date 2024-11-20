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
    # Create an infinite CPU-intensive loop
    while True:
        # Perform heavy mathematical calculations
        np.random.rand(10000, 10000).dot(np.random.rand(10000, 10000))

    return "Test completed!"
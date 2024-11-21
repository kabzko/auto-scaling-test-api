import psutil, socket, requests, uvicorn
import numpy as np
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def index():
    # Get local IP address
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Could not determine IP"
        
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent()
    
    return {
        "server_name": hostname,
        "server_ip": ip,
        "cpu_usage": f"{cpu_usage}%"
    }

@app.get("/test")
def index():
    # Create an infinite CPU-intensive loop
    while True:
        # Perform heavy mathematical calculations
        np.random.rand(10000, 10000).dot(np.random.rand(10000, 10000))

    return "Test completed!"
import psutil, requests, uvicorn, numpy as np
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def index():
    # Get EC2 instance IP
    try:
        ip = requests.get('http://169.254.169.254/latest/meta-data/public-ipv4', timeout=1).text
    except:
        ip = "Not running on EC2"
        
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent()
    
    return {
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
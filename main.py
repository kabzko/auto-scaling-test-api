import psutil, socket, requests, time, uvicorn
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
        "server_ip": ip,
        "cpu_usage": f"{cpu_usage}%"
    }

@app.get("/test")
def index():
    # Calculate target CPU usage over time
    start_time = time.time()
    duration = 30 * 60  # 30 minutes in seconds
    target_cpu = 80  # Target 80% CPU usage per call
    
    # Get initial CPU usage
    initial_cpu = psutil.cpu_percent(interval=1)
    
    while time.time() - start_time < duration:
        # Get current CPU usage with a small interval for more accurate reading
        current_cpu = psutil.cpu_percent(interval=0.1)
        
        # Calculate the CPU usage contributed by this process
        process_cpu = current_cpu - initial_cpu
        
        # If process CPU usage is below target, do calculations
        if process_cpu < target_cpu:
            # Adjust matrix size based on current usage
            matrix_size = int(400 * (target_cpu / process_cpu)) if process_cpu > 0 else 800
            matrix_size = min(max(matrix_size, 200), 2000)  # Increased bounds for higher CPU usage
            
            # Matrix multiplication with adjusted size
            np.random.rand(matrix_size, matrix_size).dot(np.random.rand(matrix_size, matrix_size))
        else:
            # Very short sleep when above target since we want very high CPU usage
            time.sleep(0.05)

    return "Test completed!"
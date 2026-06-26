import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# We start with the functions
def create_telemetry_logs(entries=500):
    start_time = datetime.now() - timedelta(minutes=entries)

    timestamps = [start_time + timedelta(minutes=i) for i in range(entries)]

    #Simulate model behavior
    fps = np.random.uniform(27.5, 32.5, entries) #Size between 27.5 and 32.5
    latency = np.random.uniform(10.0, 20.0, entries) #Latency between 10 and 20
    confidence = np.random.uniform(85.0, 99.0, entries)

    for i in range (10, entries, 50):
        confidence[i:i+5] = np.random.uniform(60.0, 73.0, 5)
        fps[i:i+5] = np.random.uniform(15.0, 22.0, 5)
        latency[i:i+5] = np.random.uniform(25.0, 35.0, 5)
    
    df = pd.DataFrame({
        'timestamp': timestamps,
        'fps': fps,
        'latency_ms': latency,
        'confidence_score': confidence
    })

    df.to_csv('edge_model_logs.csv', index=False)
    print(".csv saved")

if __name__ == "__main__":
    create_telemetry_logs()
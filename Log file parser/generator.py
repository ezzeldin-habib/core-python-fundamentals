import random
from datetime import datetime, timedelta

levels = ["INFO", "WARNING", "ERROR"]

messages = {
    "INFO": [
        "User admin logged in",
        "User john logged in",
        "Backup completed successfully",
        "Cache cleared",
        "Scheduled job started"
    ],
    "WARNING": [
        "High memory usage: 87%",
        "Disk space low: 12% remaining",
        "Slow response time: 3200ms",
        "Deprecated API endpoint called"
    ],
    "ERROR": [
        "Failed to connect to database at 192.168.1.5",
        "Timeout connecting to 10.0.0.4",
        "Null pointer exception in module auth",
        "Failed to write to disk",
        "Connection refused from 192.168.1.12"
    ]
}

start_time = datetime(2026, 7, 18, 9, 0, 0)

with open("app.log", "w") as file:
    current_time = start_time
    for _ in range(40):
        level = random.choice(levels)
        message = random.choice(messages[level])
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} {level} {message}\n")
        current_time += timedelta(seconds=random.randint(5, 300))
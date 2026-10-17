"""
[2026-09-11 10:00:01] 192.168.1.50 /login 200
[2026-09-11 10:00:05] 10.0.0.12 /dashboard 200
[2026-09-11 10:01:14] 192.168.1.50 /api/data 500
[2026-09-11 10:02:00] 172.16.0.5 /login 401
[2026-09-11 10:02:15] 10.0.0.12 /dashboard 200
[2026-09-11 10:05:30] 192.168.1.50 /login 200
[2026-09-11 10:06:01] 172.16.0.5 /admin 403
[2026-09-11 10:08:22] 10.0.0.12 /api/data 200
"""
import json
from collections import Counter, namedtuple
#1
LogEntry = namedtuple("LogEntry", ["timestamp", "ip_address", "endpoint", "status_code"])
logs=[]
#2(parsing) 
with open("server_logs.txt", "r", encoding="utf-8") as file:
    for line in file:
        
        k=line.strip()
        if not k:
            continue
        lines=k.split()
        times=lines[0]+ " " +lines[1]  
        timestamps=times.strip("[]")     
        e=LogEntry (
            timestamp = timestamps ,
            ip_address = lines[2],
            endpoint = lines[3],
            status_code = lines[4]
        )
        logs.append(e)
#3
unique_ips = list(set(e.ip_address for e in logs))
#unique_ips = list(set(map(lambda e: e.ip_address, logs))
#4
endpoints_list = [e.endpoint for e in logs]
endpoint_counts = dict(Counter(endpoints_list))
#5
failed_requests = [
    {
        "ip": e.ip_address,
        "endpoint": e.endpoint,
        "status": e.status_code
    }
    for e in logs if e.status_code != "200"
]
#6
security_report = {
    "total_requests": len(logs),
    "unique_ips": unique_ips,
    "endpoint_counts": endpoint_counts,
    "failed_requests": failed_requests,
}
with open("security_report.json", "w", encoding="utf-8") as file:
    json.dump(security_report, file, indent=4)
    
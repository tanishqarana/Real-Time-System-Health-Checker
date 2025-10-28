import psutil

prev_net_io = psutil.net_io_counters()
def get_network_speed():
    global prev_net_io
    current_net_io = psutil.net_io_counters()

    upload_speed = (current_net_io.bytes_sent - prev_net_io.bytes_sent) / 1024  # KB since last check
    download_speed = (current_net_io.bytes_recv - prev_net_io.bytes_recv) / 1024

    prev_net_io = current_net_io  # update baseline

    return {
        "upload_speed_kbps": round(upload_speed, 2),
        "download_speed_kbps": round(download_speed, 2)
    }

def get_system_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()
    metrics = {
        "cpu_usage" : psutil.cpu_percent(interval=0.0),
        "memory" : {
            "total_gb" : round(memory.total/(1024**3),2),
            "used_gb" : round(memory.used/(1024**3),2),
            "percent_gb" : memory.percent
        },
        "disk" : {
            "total" : round(disk.total/(1024**3),2),
            "used" : round(disk.used/(1024**3),2),
            "percent" : disk.percent
        } ,
        "network": {
            "bytes_sent_mb": round(net_io.bytes_sent / (1024**2), 2),
            "bytes_recv_mb": round(net_io.bytes_recv / (1024**2), 2)
        }  
    }
    return metrics


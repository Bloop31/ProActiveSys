def identify_root_cause(row):
    cpu, memory, disk, network, swap = row

    if cpu > 90:
        return "CPU Spike (high load, scheduling risk)"
    if memory > 90 and swap > 0:
        return "Memory Leak (swap usage detected)"
    if disk > 300:
        return "Disk I/O Bottleneck"
    if network > 4000:
        return "Network Traffic Burst"

    return "Unknown anomaly"

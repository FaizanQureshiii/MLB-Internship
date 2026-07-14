height = 2880
width = 5120
channels = 3
bit_depth = 8

memory_bytes = height * width * channels * (bit_depth // 8)

memory_mb = memory_bytes / (1024 * 1024)

print("Memory bytes", memory_bytes)
print("Memory (MB):", memory_mb)
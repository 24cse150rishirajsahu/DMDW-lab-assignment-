data = [10, 12, 15, 18, 20, 20, 22, 25]
freq = {}
for i in data:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
mode = None
max_count = 0
for key, value in freq.items():
    if value > max_count:
        max_count = value
        mode = key
print("Mode =", mode)

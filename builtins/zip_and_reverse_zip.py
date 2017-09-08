stream_a = [1, 2, 3]
stream_b = [4, 5, 6]

print(stream_a)
print(stream_b)

# Turn pair of streams into stream of pairs
for item in zip(stream_a, stream_b):
    print(item)

# Reverse
for item in zip(*zip(stream_a, stream_b)):
    print(item)

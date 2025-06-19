vectors = [
    [23, 11, 73],
    [4, 12, 74],
    [15, 9, 1],
    [15, 1, 4],
    [28, 12, 8]
]
print(vectors)

def vmag(v):
    return (v[0]**2 + v[1]**2 + v[2]**2)**0.5

# Finding min and max
magnitudes = []
for v in vectors:
    print(f"Vector {v}: mag = {vmag(v)}")
    magnitudes.append(vmag(v))

min_index = magnitudes.index(min(magnitudes))
max_index = magnitudes.index(max(magnitudes))

min_vector = vectors[min_index]  
max_vector = vectors[max_index]  

print('The minimum magnitude :', min(magnitudes), ' with the vector :', min_vector)
print('The maximum magnitude :', max(magnitudes), ' with the vector :', max_vector)
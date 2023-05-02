import random

def generate_values_to_insert(n):
    return random.sample(range(1, n+1), n)

def generate_values_to_search(n, values_to_insert):
    values = set(values_to_insert)
    while len(values) < n:
        values.add(random.randint(1, 100))
    return list(values)

def generate_values_to_delete(n, values_to_insert):
    return random.sample(values_to_insert, n)

# Generate values to insert, search, and delete
n = 1000
values_to_insert = generate_values_to_insert(n)
values_to_search = generate_values_to_search(n + 1, values_to_insert)
values_to_delete = generate_values_to_delete(3, values_to_insert)

print('values_to_insert = ')
print(values_to_insert)
print('values_to_search = ')
print(values_to_search)
print('values_to_delete = ')
print(values_to_delete)

#n = 10
# values_to_insert = [70, 62, 72, 34, 69, 32, 91, 14, 46, 10]
# values_to_search = [70, 62, 72, 34, 69, 32, 91, 14, 46, 10, 68]
# values_to_delete = [91, 32, 72]

#n = 100
# values_to_insert = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177]
# values_to_search = [895, 886, 624, 97, 354, 61, 293, 725, 267, 956, 250, 688, 231, 584, 186, 352, 327, 791, 544, 424, 91, 774, 468, 926, 539, 891, 543, 408, 384, 45, 451, 402, 642, 817, 253, 463, 127, 864, 424, 140, 715, 150, 173, 530, 289, 899, 845, 171, 258, 510, 151, 187, 296, 527, 94, 327, 298, 985, 998, 540, 617, 458, 413, 632, 868, 144, 114, 270, 547, 342, 532, 191, 904, 768, 639, 791, 873, 205, 883, 571, 168, 166, 335, 593, 447, 877, 699, 914, 168, 717, 639, 786, 299, 291, 32, 417, 546, 484, 10, 319, 328, 862, 177, 1000]
# values_to_delete = [191, 332, 639]

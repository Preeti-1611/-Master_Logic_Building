arr = list(map(int, input("Enter numbers: ").split()))
freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    print(key, "→", value)

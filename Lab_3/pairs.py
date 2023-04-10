import sys

def find_pairs_with_sum(arr, target_sum):
    
    pairs = []
    seen = set()
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

if __name__ == "__main__":
    
    args = sys.argv[1:]
    
    numbers = list(map(int, args))
    
    pairs = find_pairs_with_sum(numbers, 10)
    
    if pairs:
        for pair in pairs:
            print(f"{pair[0]} + {pair[1]}")
    else:
        print("Немає пар чисел з однаковою сумою")   

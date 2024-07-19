def max_xor_sum(A, K):
    N = len(A)
    max_bit = K.bit_length() - 1
    
    bit_counts = [0] * 32  # Assuming 32-bit integers
    for a in A:
        for i in range(32):
            if a & (1 << i):
                bit_counts[i] += 1
    
    x = 0
    for bit in range(max_bit, -1, -1):
        if x + (1 << bit) > K:
            continue
        
        with_bit = sum(N - bit_counts[i] if i == bit else max(bit_counts[i], N - bit_counts[i]) for i in range(32))
        without_bit = sum(max(bit_counts[i], N - bit_counts[i]) for i in range(32))
        
        if with_bit > without_bit:
            x += 1 << bit
    
    return sum(x ^ a for a in A)



# Example usage:
A=[7,4,0,3]
K=9
print(max_xor_sum(A, K))
def find_min_square_size(h, w, n):
    bigger = w

    if h > w:
        bigger = h

    lesser = w

    if bigger == w:
        lesser = h

    low = lesser
    high = bigger * n
    i = 0

    while low <= high:
        i += 1
        mid = (low + high) // 2
        
        if n <= (mid // w) * (mid // h):
            high = mid - 1
        else:
            low = mid + 1
            
    print(f"(H={h}, W={w}, N={n}), iterations = {i}")
    return low

 


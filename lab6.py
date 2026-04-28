def solve():
    tokens = []
    while True:
        try:
            tokens.extend(input().split())
        except EOFError:
            break
    if not tokens:
        return

    n = int(tokens[0])
    b = int(tokens[1])
    
    prices = [int(x) for x in tokens[2:2+b]]
    likes = "".join(tokens[2+b:])

    beers = []
    for j in range(b):
        mask = 0
        for i in range(n):
            if likes[i * b + j] == 'Y':
                mask |= (1 << i)
        if mask > 0:
            beers.append((mask, prices[j]))

    beers.sort(key=lambda x: sum((x[0] >> i) & 1 for i in range(n)), reverse=True)
    b_len = len(beers)
    
    target = (1 << n) - 1

    def backtrack(beer_idx, current_mask, current_cost, min_cost):
        if current_mask == target:
            return current_cost if current_cost < min_cost else min_cost
        
        if current_cost >= min_cost or beer_idx == b_len:
            return min_cost

        res1 = backtrack(beer_idx + 1, current_mask | beers[beer_idx][0], current_cost + beers[beer_idx][1], min_cost)
        return backtrack(beer_idx + 1, current_mask, current_cost, res1)

    max_possible_cost = sum(prices) + 1
    print(backtrack(0, 0, 0, max_possible_cost))

if __name__ == '__main__':
    solve()
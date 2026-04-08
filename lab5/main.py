def solve_knight_path():
    print("Введіть розмір дошки (наприклад, 8):")
    N = int(input().strip())
    
    print("Введіть старт (рядок,стовпець, наприклад 0,0):")
    start_r, start_c = map(int, input().split(','))
    start_pos = (start_r, start_c)
    
    print("Введіть фініш (рядок,стовпець, наприклад 7,7):")
    end_r, end_c = map(int, input().split(','))
    end_pos = (end_r, end_c)
    
    obstacles = set()
    print("Вводьте координати перешкод (рядок,стовпець). Натисніть Enter, щоб завершити:")
    while True:
        obs = input().strip()
        if not obs:
            break
        orow, ocol = map(int, obs.split(','))
        obstacles.add((orow, ocol))

    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    queue = [(start_pos[0], start_pos[1], [start_pos])]
    visited = {start_pos}
    final_path = []

    while queue:
        r, c, path = queue.pop(0)
        
        if (r, c) == end_pos:
            final_path = path
            break
            
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if (nr, nc) not in visited and (nr, nc) not in obstacles:
                    visited.add((nr, nc))
                    queue.append((nr, nc, path + [(nr, nc)]))

    print("\n--- РЕЗУЛЬТАТ ---")
    if final_path:
        print(f"Мінімальна кількість кроків: {len(final_path) - 1}")
    else:
        print("Шлях не знайдено (-1)")

    print("\nКарта дошки:")
    for r in range(N):
        row_str = ""
        for c in range(N):
            if (r, c) == start_pos:
                row_str += "S "
            elif (r, c) == end_pos:
                row_str += "F "
            elif (r, c) in obstacles:
                row_str += "# "
            elif final_path and (r, c) in final_path:
                row_str += "* "
            else:
                row_str += ". "
        print(row_str)

if __name__ == "__main__":
    solve_knight_path()

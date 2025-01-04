 queue = [(entrance[0], entrance[1])]
        n = len(maze)
        m = len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'
        count = 0
        while queue:
            qlen = len(queue)
            for _ in range(qlen):
                x, y = queue.pop(0)
                
                if (x == 0 or y == 0 or x == n-1 or y == m-1) and [x, y] != entrance:
                    return count
                if x > 0 and maze[x-1][y] != '+':
                    queue.append((x-1, y))
                    maze[x-1][y] = '+'
                if x < n-1 and maze[x+1][y] != '+':
                    queue.append((x+1, y))
                    maze[x+1][y] = '+'
                if y > 0 and maze[x][y-1] != '+':
                    queue.append((x, y-1))
                    maze[x][y-1] = '+'
                if y < m-1 and maze[x][y+1] != '+':
                    queue.append((x, y+1))
                    maze[x][y+1] = '+'
            count += 1
        
        return -1

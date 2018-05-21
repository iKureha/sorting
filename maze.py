# encoding="utf-8"

maze = []
n = 3
m = 4


def valid():
    for i in range(n):
        for j in range(m):
            if maze[i][j] == "*":
                return -1
    return 1


def change(x, y):
    if maze[x][y] == ".":
        maze[x][y] = "*"
    else:
        maze[x][y] = "."


def switch(x, y):
    change(x, y)
    if x > 0:
        change(x-1, y)
    if x < n-1:
        change(x+1, y)
    if y > 0:
        change(x, y-1)
    if y < m-1:
        change(x, y+1)


def run(x, y):
    switch(x, y)
    step = 0
    if valid == 1:
        return True

    if x > 0 and not run(x-1, y):
        step += 1
    if x < n-1 and not run(x+1, y):
        step += 1
    if y > 0 and not run(x, y-1):
        step += 1
    if y < m-1 and not run(x, y+1):
        step += 1

    print(step, maze)

if __name__ == "__main__":
    maze = [[".", ".", ".", "."],
            [".", "*", ".", "."],
            [".", ".", ".", "."]]

    flag = valid()
    if flag == 1:
        print("OK!")
    run(0, 0)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        p1, p2 = None, None

        width, height = len(self.puzzle[0]) - 1, len(self.puzzle) - 1

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1),    # → ← ↓ ↑
                      (-1, -1), (1, -1), (-1, 1), (1, 1))  # ↖ ↗ ↙ ↘

        points = []
        for x in range(width + 1):
            for y in range(height + 1):
                if self.puzzle[y][x] == word[0]:
                    points.append((x,y))

        STOP = "STOP"
        for x, y in points:
            p1 = Point(x, y)

            for direction in directions:
                line = []
                x2, y2 = x, y

                while 0 <= x2 <= width and 0 <= y2 <= height:
                    line.append(self.puzzle[y2][x2])

                    if word == ''.join(line):
                        p2 = Point(x2, y2)
                        return p1, p2

                    else:
                        x2 += direction[0]
                        y2 += direction[1]

        return None

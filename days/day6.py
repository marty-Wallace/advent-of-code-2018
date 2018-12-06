from days.day import Day


class Day6(Day):

    def part_one(self):
        coords = []

        max_i = 0
        max_j = 0

        for line in self.input_stream:
            i, j = [int(x) for x in line.replace(' ', '').split(',')]

            coords.append((i, j))

            if i > max_i:
                max_i = i
            if j > max_j:
                max_j = j

        infinites = {}

        for i in range(max_i):
            self.test_points(i, 0, coords, infinites)
            self.test_points(i, max_j, coords, infinites)

        for j in range(max_j):
            self.test_points(0, j, coords, infinites)
            self.test_points(max_i, j, coords, infinites)

        print(infinites)
        high_num = 2**63
        grid = []
        for i in range(max_i):
            grid.append([])
            for j in range(max_j):
                grid[i].append(('', high_num))

        self.expand(grid, coords, max(max_i, max_j))

        maxi = 0
        for i in range(len(coords)):
            x, y = coords[i]
            s = str(x) + '-' + str(y)
            sum_s = 0
            if s not in infinites:
                for line in grid:
                    for ss, cc in line:
                        if ss == s:
                            sum_s += 1
            if sum_s > maxi:
                maxi = sum_s

        print(maxi, file=self.output_stream)

    def expand(self, grid, coords, n):
        for x, y in coords:
            for i in range(-n, n):
                for j in range(-n, n):
                    if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]):
                        man = abs(x - (x+i)) + abs(y - (y+j))
                        if man < grid[x+i][y+j][1]:
                            grid[x+i][y+j] = (str(x) + '-' + str(y), man)
                        elif man == grid[x+i][y+j][1]:
                            grid[x+i][y+j] = ('.', man)





    def test_points(self, i, j, coords, infinites):
        second_best = 2**64
        best = 2**64
        b_p = ''
        for x, y in coords:
            man = abs(i - x) + abs(j - y)

            if man < best:
                second_best = best
                best = man
                b_p = str(x) + '-' + str(y)
        if second_best != best:
            infinites[b_p] = True

    def part_two(self):
        coords = []

        max_i = 0
        max_j = 0

        for line in self.input_stream:
            i, j = [int(x) for x in line.replace(' ', '').split(',')]

            coords.append((i, j))

            if i > max_i:
                max_i = i
            if j > max_j:
                max_j = j

        grid = []
        for i in range(max_i):
            grid.append([])
            for j in range(max_j):
                grid[i].append(0)

        for x, y in coords:
            for i in range(max_i):
                for j in range(max_j):
                    man = abs(x - i) + abs(y -j)
                    grid[i][j] += man

        sum = 0
        for line in grid:
            for num in line:
                if num < 10000:
                    sum += 1
        print(sum, file=self.output_stream)




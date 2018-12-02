from days.day import Day


class Day2(Day):

    def part_one(self):
        twos = 0
        threes = 0

        for line in self.input_stream:
            chars = [0] * 256
            for c in line:
                chars[ord(c)] = chars[ord(c)] + 1
            if 2 in chars:
                twos += 1
            if 3 in chars:
                threes += 1

        print(twos * threes, file=self.output_stream)

    # @TODO make this not n*n
    def part_two(self):
        strings = []
        for line in self.input_stream:
            strings.append(line)

        for s in strings:
            for z in strings:
                if s == z:
                    continue
                misses = 0
                for c, d in zip(s, z):
                    if c != d:
                        misses += 1
                        if misses > 1:
                            break
                if misses == 1:
                    print("".join(c if c == d else '' for c, d in zip(s, z)), file=self.output_stream)
                    return






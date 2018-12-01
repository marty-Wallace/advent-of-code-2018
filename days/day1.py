from days.day import Day


class Day1(Day):

    def part_one(self):
        print(sum([int(line) for line in self.input_stream]), file=self.output_stream)

    def part_two(self):
        seen = set()
        total = 0
        nums = []
        for line in self.input_stream:
            nums.append(int(line))
        i = 0
        while total not in seen:
            seen.add(total)
            total += nums[i]
            i = (i + 1) % len(nums)
        print(total, file=self.output_stream)

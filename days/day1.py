from days.day import Day


class Day1(Day):

    def part_one(self):
        print(sum([int(line) for line in self.input_stream]), file=self.output_stream)

    def part_two(self):
        seen = []
        total = 0
        nums = []
        for line in self.input_stream:
            nums.append(int(line))

        for num in nums:
            seen.append(total)
            total += num
            if total in seen:
                print(total, file=self.output_stream)
                return

        # add the last total to the seen
        seen.append(total)
        # the total is now the frequency of one cycle
        freq = total

        best = 2**32
        best_amount = 0
        for n in seen:
            for m in seen:
                if (n-m) % freq == 0:
                    count = (n-m) // freq
                    if count < best:
                        best = count
                        best_amount = m

        print(best_amount, file=self.output_stream)

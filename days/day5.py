from days.day import Day


class Day5(Day):

    def part_one(self):
        s = ''
        for line in self.input_stream:
            s = s + line
        changed = True
        while changed:
            changed = False
            s = list(s)
            for i in range(len(s) - 1):
                if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    s[i] = '_'
                    s[i+1] = '_'
                    changed = True

            s = "".join(s)
            s = s.replace('_', '')
        print(len(s), file=self.output_stream)


    def reduce(self, s):
        changed = True
        while changed:
            changed = False
            s = list(s)
            for i in range(len(s) - 1):
                if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    s[i] = '_'
                    s[i+1] = '_'
                    changed = True
            s = "".join(s)
            s = s.replace('_', '')
        return s

    def part_two(self):
        s = ''
        for line in self.input_stream:
            s = s + line
        s = self.reduce(s)

        chars = set(s.lower())
        best = 2**64
        s_copy = str(s)
        for char in chars:
            s_copy = s_copy.replace(char.lower(), '')
            s_copy = s_copy.replace(char.upper(), '')
            s_copy = self.reduce(s_copy)
            if len(s_copy) < best:
                best = len(s_copy)

            s_copy = str(s)

        print(best, file=self.output_stream)





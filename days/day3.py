from days.day import Day


class Day3(Day):

    def part_one(self):
        seen = dict()
        for line in self.input_stream:
            claim_id, trash, coords, dimens = line.split()
            claim_id = int(claim_id.replace("#", ''))
            coords = coords.replace(':', '')
            from_left = int(coords.split(',')[0])
            from_top = int(coords.split(',')[1])
            width = int(dimens.split('x')[0])
            height = int(dimens.split('x')[1])

            for i in range(from_left, from_left + width):
                for j in range(from_top, from_top + height):
                    hash = str(i) + '-' + str(j)
                    if hash not in seen:
                        seen[hash] = 1
                    else:
                        seen[hash] = seen[hash] + 1
        count = 0
        for k in seen:
            if seen[k] > 1:
                count += 1
        print(count, file=self.output_stream)

    # @TODO make this not n*n
    def part_two(self):
        seen = dict()
        claims = []
        for line in self.input_stream:
            claim_id, trash, coords, dimens = line.split()
            claim_id = int(claim_id.replace("#", ''))
            coords = coords.replace(':', '')
            from_left = int(coords.split(',')[0])
            from_top = int(coords.split(',')[1])
            width = int(dimens.split('x')[0])
            height = int(dimens.split('x')[1])

            claims.append((claim_id, from_left, from_top, width, height))

            for i in range(from_left, from_left + width):
                for j in range(from_top, from_top + height):
                    hash = str(i) + '-' + str(j)
                    if hash not in seen:
                        seen[hash] = 1
                    else:
                        seen[hash] = seen[hash] + 1

        for claim_id, from_left, from_top, width, height in claims:
            seenB = True
            for i in range(from_left, from_left + width):
                for j in range(from_top, from_top + height):
                    hash = str(i) + '-' + str(j)
                    if hash not in seen or seen[hash] != 1:
                        seenB = False
            if seenB:
                print(claim_id, file=self.output_stream)


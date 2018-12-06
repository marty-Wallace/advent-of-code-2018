from days.day import Day


class Day4(Day):

    def part_one(self):
        guards = self.generate_minutes_from_input()
        maximum = 0
        minute = -1
        guard_id = -1
        for i, g in enumerate(guards):
            t = sum(g)
            if t > maximum:
                maximum = t
                guard_id = i
                max2 = 0
                for ii in range(len(g)):
                    if g[ii] > max2:
                        max2 = g[ii]
                        minute = ii

        print(guard_id * minute, file=self.output_stream)

    def part_two(self):
        guards = self.generate_minutes_from_input()
        max2 = 0
        minute = -1
        guard_id = -1
        for i, g in enumerate(guards):
            for ii in range(len(g)):
                if g[ii] > max2:
                    max2 = g[ii]
                    minute = ii
                    guard_id = i

        print(guard_id * minute, file=self.output_stream)

    def generate_minutes_from_input(self):
        actions = []
        wake_up = 2
        fall_asleep = 1
        start_shift = 3
        max_guard = 0
        for line in self.input_stream:
            year_month_day, time, action1, action2, *_ = line.split()
            year_month_day = year_month_day.replace('[', '')
            time = time.replace(']', '')

            date_time = year_month_day + time
            guard = 0
            if action1 == 'wakes':
                action = wake_up
            elif action1 == 'falls':
                action = fall_asleep
            else:
                action = start_shift
                guard = int(action2.replace('#', ''))
                if guard > max_guard:
                    max_guard = guard

            actions.append((date_time, action, guard))

        actions.sort(key=lambda tup: tup[0])

        guards = []
        for i in range(max_guard + 1):
            guards.append([0] * 60)

        current_guard = -1
        state = wake_up
        current_time = ''
        for date_time, action, guard in actions:
            if action == start_shift:
                current_guard = guard
                state = wake_up
            elif action == fall_asleep and current_guard != -1 and state != fall_asleep:
                state = fall_asleep
                time = date_time[13:]
                current_time = int(time)
            elif action == wake_up and current_guard != -1 and state == fall_asleep:
                time = int(date_time[13:])
                for i in range(current_time, time):
                    guards[current_guard][i] += 1
                state = wake_up
                current_time = ''
        return guards


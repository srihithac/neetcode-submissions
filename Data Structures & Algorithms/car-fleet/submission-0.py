class Solution:
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed), reverse=True)

        stack = []  # stores fleet arrival times

        for pos, spd in cars:
            time = (target - pos) / spd

            # if this car is slower or equal, it joins fleet
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)



      
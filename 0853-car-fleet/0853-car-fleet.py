class Solution(object):

    def carFleet(self, target, position, speed):

        # Pair each car's position with its speed.
        #
        # Example:
        # position = [10, 8, 0]
        # speed    = [2, 4, 1]
        #
        # zip() gives us:
        # [(10, 2), (8, 4), (0, 1)]
        cars = zip(position, speed)

        # We want to look at the cars closest to the target FIRST.
        #
        # reverse=True means we sort from biggest position
        # to smallest position.
        #
        # Example:
        # [(10, 2), (8, 4), (0, 1)]
        # is already sorted in this case.
        cars = sorted(cars, reverse=True)

        # This will keep track of how many fleets we have.
        fleets = 0

        # This stores the arrival time of the fleet in front.
        #
        # We start at 0 because we haven't seen a car yet.
        last_time = 0

        # Go through each car, starting with the car closest
        # to the target.
        for position, speed in cars:

            # Calculate how long this car needs to reach the target.
            #
            # distance = target - position
            # time = distance / speed
            time = float(target - position) / speed

            # If this car takes LONGER than the fleet in front,
            # it cannot catch that fleet.
            #
            # Therefore, this car creates a NEW fleet.
            if time > last_time:

                fleets += 1

                # This becomes the time for the fleet in front.
                last_time = time

            # If time <= last_time:
            #
            # This car catches the fleet in front (or arrives at
            # the same time), so it becomes part of that fleet.
            #
            # We DON'T increase fleets.
        
        return fleets
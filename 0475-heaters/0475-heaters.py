class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_radius = 0

        for house in houses:
            closest_heater = bisect_left(heaters, house)
            distance_left = abs(heaters[closest_heater - 1] - house) if closest_heater > 0 else float('inf')
            distance_right = abs(heaters[closest_heater] - house) if closest_heater < len(heaters) else float('inf')

            min_radius = max(min_radius, min(distance_left, distance_right))

        return min_radius
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        # Slope
        initial_slope = (y1 - y0) / (x1 - x0) if x1 - x0 != 0 else float('inf')

        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]

            # Slope Comparison
            slope = (yi - y1) / (xi - x1) if xi - x1 != 0 else float('inf')

            # False case
            if slope != initial_slope:
                return False

            x1, y1 = xi, yi

        return True

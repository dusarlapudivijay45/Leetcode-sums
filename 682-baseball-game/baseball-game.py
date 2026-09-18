class Solution:
    def calPoints(self, operations: list[str]) -> int:
        points = []
        for i in operations:
            if i == "D":
                val = points.append(points[-1]*2)
            elif i == "C":
                points.pop()

            elif i == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(i))
        return sum(points)
        
        
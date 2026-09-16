class Solution:
    def isPathCrossing(self, path: str) -> bool:
        crossed = {(0, 0)}
        current_x = 0
        current_y = 0 

        for i in path:
            if i == "N":
                current_x += 1
            elif i == "E":
                current_y += 1
            elif i == "S":
                current_x -= 1
            else:
                current_y -= 1

            if (current_x, current_y) in crossed:
                return True
            else:
                crossed.add((current_x, current_y))
        return False
            
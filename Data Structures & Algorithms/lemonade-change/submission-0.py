class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # T: O(n)
        # S: O(1)
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives:
                    tens += 1
                    fives -= 1
                else:
                    return False
            else: # bill is 20
                if fives >= 1 and tens >= 1:
                    fives -= 1
                    tens -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True

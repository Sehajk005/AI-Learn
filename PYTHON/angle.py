class Solution:
    def getAngle(self, s: str) -> float:
        hour = int(s[:2])%12
        minutes = int(s[3:])
        
        minutes_angle = 6*minutes
        hour_angle = hour*30 + minutes*0.5
        
        difference = abs(hour_angle-minutes_angle)
        
        angle = min(difference, 360-difference)
        
        return angle

s = Solution()
time = input("Enter time in HH:MM format: ")
print(s.getAngle(time))
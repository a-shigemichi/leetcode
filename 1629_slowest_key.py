class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_duration = releaseTimes[0]
        slowest_key = keysPressed[0]
        
        for i in range(1, len(keysPressed)):
            duration = releaseTimes[i] - releaseTimes[i-1]
            
            if (duration > max_duration or 
                (duration == max_duration and keysPressed[i] > slowest_key)):
                max_duration = duration
                slowest_key = keysPressed[i]
                
        return slowest_key
        
                

def main():
    releaseTimes = [23,34,43,59,62,80,83,92,97]
    keysPressed = "qgkzzihfc"
    my_object = Solution()        
    judgement = my_object.slowestKey(releaseTimes,keysPressed)
    print(judgement)

if __name__ == "__main__":
   main()
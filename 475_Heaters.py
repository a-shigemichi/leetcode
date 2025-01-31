class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        house_len, heater_len = len(houses), len(heaters)
        house_pointer = heater_pointer = ans = 0
        
        while house_pointer < house_len:
            while heater_pointer < heater_len - 1 and abs(heaters[heater_pointer] - houses[house_pointer])>= abs(heaters[heater_pointer + 1] - houses[house_pointer]):
                heater_pointer += 1
                
            ans = max(ans, abs(heaters[heater_pointer] - houses[house_pointer]))
            house_pointer += 1
            
        return ans
    
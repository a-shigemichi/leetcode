class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """
        Converts a temperature from Celsius to Kelvin and Fahrenheit.
        
        Args:
            celsius: A non-negative floating point number rounded to two decimal places representing temperature in Celsius.
            
        Returns:
            A list containing two floating point numbers [kelvin, fahrenheit] representing the temperature in Kelvin and Fahrenheit respectively.
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        
        return [kelvin, fahrenheit]

class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Return a defanged version of the input IPv4 address.
        
        A defanged IP address replaces every period "." with "[.]".
        
        Args:
            address: A valid IPv4 address string
            
        Returns:
            str: The defanged IP address
        """
        return address.replace(".", "[.]")
    
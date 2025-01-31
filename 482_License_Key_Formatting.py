class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        Reformat the license key string `s` such that each group contains exactly `k` characters and all lowercase letters are converted to uppercase,
        except for the first group, which could be shorter but must contain at least one character.

        Args:
            s (str): The original license key.
            k (int): The desired size of each group after reformatting.

        Returns:
            str: The reformatted license key.
        """
        no_hyphens = ''.join(s.split('-')).upper()

        first_group_size = self.find_first_group_size(no_hyphens, k)
        reformatted_license_key = self.split_into_groups(first_group_size, no_hyphens, k)

        return reformatted_license_key

    def find_first_group_size(self, no_hyphens: str, k: int) -> int:
        """
        Determine the size of the first group based on the length of 'no_hyphens' and the integer 'k'.

        Args:
            no_hyphens (str): The string to be split into groups (already uppercase, no hyphens).
            k (int): The desired size of each group after reformatting.

        Returns:
            int: The size of the first group.
        """
        if len(no_hyphens) % k != 0:
            return len(no_hyphens) % k
        else:
            return k

    def split_into_groups(self, first_group_size: int, no_hyphens: str, k: int) -> str:
        """
        Splits the string 'no_hyphens' into groups where the first group has 'first_group_size' characters
        and the subsequent groups have 'k' characters each. The groups are joined with hyphens.

        Args:
            first_group_size (int): The size of the first group.
            no_hyphens (str): The string to be split into groups (already uppercase, no hyphens).
            k (int): The desired size of each group after reformatting.

        Returns:
            str: The reformatted license key.
        """
        result = []

        result.append(no_hyphens[:first_group_size])
        for i in range(first_group_size, len(no_hyphens), k):
            result.append(no_hyphens[i:i + k])

        return '-'.join(result)

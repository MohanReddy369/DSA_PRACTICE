class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for ch in s:
            # Convert uppercase to lowercase
            if 'A' <= ch <= 'Z':
                ch = chr(ord(ch) + 32)

            # Keep only alphanumeric characters
            if ('a' <= ch <= 'z') or ('0' <= ch <= '9'):
                result += ch

        # Check palindrome
        return result == result[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    obj = Solution()
    print(obj.isPalindrome(s))

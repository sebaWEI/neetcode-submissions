class Solution:
    def is_ascii_alnum(self, ch):
        return ch.isascii() and ch.isalnum()

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(ch for ch in s if self.is_ascii_alnum(ch))
        s_reversed = "".join(reversed(s))
        if s == s_reversed:
            return True
        else:
            return False
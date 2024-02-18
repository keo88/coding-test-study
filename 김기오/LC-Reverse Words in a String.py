class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(list(filter(lambda a: a != '', s.split()))))

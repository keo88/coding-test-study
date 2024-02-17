class Solution:
    def convertDigit(self, digit: int, big:str, mid: str, small: str) -> str:
        ans = ''
        if 0 < digit <= 3:
            ans = small * digit
        elif digit == 4:
            ans = f'{small}{mid}'
        elif 5 <= digit < 9:
            ans = mid + small * (digit - 5)
        elif digit == 9:
            ans = f'{small}{big}'
        return ans

    def intToRoman(self, num: int) -> str:
        digits = []
        while num != 0:
            digits.append(num % 10)
            num //= 10
        
        ans = ''

        if len(digits) == 4:
            ans += self.convertDigit(digits[3], '', '', 'M')
        if len(digits) >= 3:
            ans += self.convertDigit(digits[2], 'M', 'D', 'C')
        if len(digits) >= 2:
            ans += self.convertDigit(digits[1], 'C', 'L', 'X')
        ans += self.convertDigit(digits[0], 'X', 'V', 'I')

        return ans

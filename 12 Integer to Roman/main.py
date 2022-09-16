class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        t = []
        while num > 0:
            cur = num % 10
            num //= 10

            mod = pow(10, len(t))
            cur *= mod
            if (cur + mod) % (5*mod) == 0:
                r = d[mod] + d[cur + mod]
            else:
                if cur >= 5*mod:
                    r = d[5*mod] + (d[mod] * int(cur//mod - 5))
                else:
                    r = d[mod] * int(cur//mod)
            t.append(r)
        
        print("".join(t[::-1]))


a = Solution()
a.intToRoman(3)
a.intToRoman(58)
a.intToRoman(1994)

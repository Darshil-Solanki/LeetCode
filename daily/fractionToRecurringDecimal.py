class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator: return "0"
        if numerator%denominator==0:
            return str(numerator//denominator)
        rem = {}
        before, after = str(numerator/denominator).split(".")
        zero = "-0" if (numerator>0 and denominator<0) or (denominator>0 and numerator<0) else "0"
        ans = [zero if "e-" in after else before, "."]
        numerator, denominator = abs(numerator), abs(denominator)
        fraction = []
        numerator = (numerator%denominator) * 10

        while numerator:
            if numerator in rem:
                fraction.insert(rem[numerator], "(")
                fraction.append(")")
                return "".join(ans+fraction)
            rem[numerator] = len(fraction)
            fraction.append(str(numerator//denominator))
            numerator = (numerator%denominator) * 10
        
        return  "".join(ans+fraction)

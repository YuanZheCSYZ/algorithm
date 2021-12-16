class LCM:
    def getLCM(self, a, b):
        """
        Least common multiple
        """
        return a // self.getGCD(a, b) * b

    def getGCD(self, a, b):
        """
        Greatest common divisor
        """
        if b == 0:
            return a

        return self.getGCD(b, a % b)

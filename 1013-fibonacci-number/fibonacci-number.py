class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        prev = 1
        current = 1

        number = 0

        for i in range(2, n):

            number = prev + current
            prev, current = current, number

        return number
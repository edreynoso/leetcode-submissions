class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        digits = []

        letters = []

        l_log = []

        for log in logs:

            j = 0

            while log[j] != " ":
                j += 1
                
            j +=1

            if log[j].isdigit():
                digits.append(log)
            else:
                l_log.append((log[j:len(log)], log[0:j]))

        l_log.sort(key = lambda x: (x[0], x[1]))

        res = []

        for suf, pre in l_log:

            log = pre + suf

            res.append(log)

        for number in digits:

            res.append(number)

        return res

        
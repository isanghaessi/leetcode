class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(data, count):
            if count > 4 or len(data) != count:
                
                return False
            if count == 1:

                return data[0][0] == '0'
            else:
                first = ('1' * count) + '0'
                rest = '10'
                for i, d in enumerate(data):
                    if i == 0 and d[0:count + 1] != first:

                        return False
                    if i > 0 and d[0:2] != rest:

                        return False

                return True
        
        
        data = list(map(lambda a: bin(a)[2:].rjust(8, '0'), data))
        i = 0
        while i < len(data):
            current = data[i]
            j = 0
            while j < 8 and current[j] == '1':
                j += 1
            if not check(data[i:i + (j if j > 0 else 1)], j if j > 0 else 1):
                
                return False
            i += j if j > 0 else 1
            print(i, len(data))
            
        return True
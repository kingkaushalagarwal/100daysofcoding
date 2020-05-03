#interview bit question - grid illumination
class Solution:
    def solve(self, A, B, C):
        N = A
        lamps = B
        queries = C
        
        from collections import defaultdict
        ans = []
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        dig_add_dict = defaultdict(int)
        dig_sub_dict = defaultdict(int)
 
        lamps_set = set([tuple(x) for x in lamps])
 
        for row, col in lamps_set:
            row_dict[row] += 1
            col_dict[col] += 1
            dig_add_dict[row+col] += 1
            dig_sub_dict[row-col] += 1
 
        for row, col in queries:
            if any([row_dict[row], col_dict[col], dig_add_dict[row+col], dig_sub_dict[row-col]]):
                ans.append(1)
 
                close_lamp = set(filter(lambda x: (abs(x[0]-row)<=1) & (abs(x[1]-col)<=1), lamps_set))
                lamps_set = lamps_set - close_lamp
 
                for c_row, c_col in close_lamp:
                    row_dict[c_row] -= 1
                    col_dict[c_col] -= 1
                    dig_add_dict[c_row+c_col] -= 1
                    dig_sub_dict[c_row-c_col] -= 1
                    
            else:
                ans.append(0)
 
        return ans


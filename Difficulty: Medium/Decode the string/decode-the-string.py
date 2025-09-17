class Solution:
    def decodedString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_str = ""
                curr_num = 0
            elif char == "]":
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * repeat
            else:
                curr_str += char
        return curr_str

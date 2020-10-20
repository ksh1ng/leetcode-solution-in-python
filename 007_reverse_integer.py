'''
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your
function returns 0 when the reversed integer overflows.

Example
Input: x = 123
Output: 321

'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #for constraints:
        if -2 ** 31 > x or x > 2 ** 31 - 1:
            return 0

        #check if symbol "-" exists
        str_x = str(x)
        if str_x[0] == "-":
            reverse_str_x = "-" + str_x[1:][::-1]
        else:
            reverse_str_x = str_x[::-1]

        if -2 ** 31 > int(reverse_str_x) or int(reverse_str_x)  > 2 ** 31 - 1:
            return 0

        return int(reverse_str_x)


if __name__ == "__main__":

    print(Solution().reverse(x=1534236469))

'''
Implement atoi which converts a string to an integer.
    1.Discards as many whitespace characters as necessary until the first non-whitespace character is found.
    2.starting from this character takes an optional initial plus or minus sign followed by as many numerical
      digits as possible, and interprets them as a numerical value.


Note:
    - Only the space character ' ' is considered a whitespace character.
    -32-bit signed integer range: [−2^31,  2^31 − 1] is considered. If
      the numerical value is out of the range of representable values, 2^31 − 1 or −2^31 is returned
    -If no valid conversion could be performed, a zero value is returned.

Example
Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
'''


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '', 1) #remove white space

        if s == '': #empty input itself is non-valid
            return 0

        #remove white space until the first non-whitespace character is found
        non_whitespace_index = len(s) - 1

        for i in range(len(s)):
            if s[i] == ' ':
                pass
            else:
                non_whitespace_index = i
                break

        new_s = s[non_whitespace_index:]

        #manipulate new string after remove pre-whitespace
        if new_s[0] not in '-+0123456789': #first sequence of non-whitespace characters in str is not a valid integral number
            return 0

        int_in_s = new_s[0]

        for ch in new_s[1:]:
            if ch in '0123456789':
                int_in_s += ch
            else:
                break

        #check if int_in_s is valid string integer
        if len(int_in_s) == 0 or int_in_s == "-" or int_in_s == "+":
            return 0

        #check  32-bits signed int constraints
        if int(int_in_s) < 0:
            return max(int(int_in_s), -2 ** 31)
        else:
            return min(int(int_in_s), 2 ** 31 - 1)


        return int(int_in_s)


if __name__ == "__main__":

    print(Solution().myAtoi(s="   -42"))

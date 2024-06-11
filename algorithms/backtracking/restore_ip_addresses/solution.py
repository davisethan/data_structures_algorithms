"""
production algorithm
"""


class Solution:
    def restore_ip_addresses(self, s):
        """
        time complexity XXX
        space complexity XXX
        """
        n = len(s)
        result = list()

        for i in range(1, 4):
            for j in range(i + 1, min(i + 4, n)):
                for k in range(j + 1, min(j + 4, n)):
                    if 4 < n - k:
                        continue
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if not self.has_leading_zeros(s1) and 0 <= int(s1) <= 255 and\
                            not self.has_leading_zeros(s2) and 0 <= int(s2) <= 255 and\
                            not self.has_leading_zeros(s3) and 0 <= int(s3) <= 255 and\
                            not self.has_leading_zeros(s4) and 0 <= int(s4) <= 255:
                        result.append(f"{s1}.{s2}.{s3}.{s4}")

        return result

    def has_leading_zeros(self, s):
        return 1 < len(s) and len(s.lstrip("0")) < len(s)

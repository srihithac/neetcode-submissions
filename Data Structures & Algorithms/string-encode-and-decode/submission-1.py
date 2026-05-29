class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        decoded = []
        i = 0

        while i < len(s):

            # Find the separator #
            j = i
            while s[j] != "#":
                j += 1

            # Length of the string
            length = int(s[i:j])

            # Extract the string
            word = s[j + 1 : j + 1 + length]

            decoded.append(word)

            # Move pointer to next encoded string
            i = j + 1 + length

        return decoded
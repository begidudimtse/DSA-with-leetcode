class Codec:
   def encode(self, strs: list[str]) -> str:
       """Encodes a list of strings to a single string."""
       encoded = []
       for s in strs:
         encoded.append(f"{len(s)}#{s}")
         return "".join(encoded)

   def decode(self, s: str) -> list[str]:
       """Decodes a single string to a list of strings."""
       res = []
       i = 0

       while i < len(s):
        # Find the delimiter '#' starting from index i
        j = i
        while s[j] != '#':
            j += 1

        # Extract length of the upcoming string
        length = int(s[i:j])

        # Extract the actual string using the known length
        start = j + 1
        end = start + length
        res.append(s[start:end])

        # Move index past the current string
        i = end

        return res
from collections import Counter
from collections import defaultdict

class Solution:
    def using_counter(self,txt):
        words = txt.split()
        freq = Counter(words)
        return freq

    def using_normal_dict(self, txt):
        words = txt.split()
        freq={}
        for w in words:
            freq[w]=freq.get(w,0)+1
        return freq

    # ✅ 4. Using defaultdict(int)
    def using_default_dict(self, txt):
        freq = defaultdict(int)
        words = txt.split()
        for word in words:
            freq[word] += 1
        return dict(freq)

txt = "apple banana apple orange banana apple"
print(Solution().using_counter(txt))
print(Solution().using_normal_dict(txt))
print(Solution().using_default_dict(txt))

"""
✅ What is defaultdict?
defaultdict is a dictionary from collections module that automatically provides 
a default value for a missing key without throwing a KeyError.

🔹 defaultdict
You specify a default factory (like int, list, etc.) which generates a default value automatically when a key is missing.
Example with int:
"""
from collections import defaultdict
d = defaultdict(int)
print(d["a"])    # ✔ returns 0 (default int value)



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, base: str) -> str:
        d= { chr(i):chr(i) for i in range(97,97+26) }


        def find(x):
            if d[x] != x:
                d[x] = find(d[x])
            return d[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if d[rx] < d[ry]:
                d[ry] = rx
            else:
                d[rx] = ry

        for a, b in zip(s1, s2):
            union(a, b)

        # step3
        ans = ''
        for s in base:
            ans += find(s)
        return ans

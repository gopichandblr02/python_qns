class Solution:
    def simplifyPath(self, path):
        stack = []
        ss = path.split('/')
        for s in ss:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)

        return '/' + '/'.join(stack)


path="/a/./b/../../c/"
print(Solution().simplifyPath(path))
# /c
path1="/home/"
print(Solution().simplifyPath(path1))

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix :
                return "No letter in common."
            
    return prefix 

strs = input("Enter a array of strings, separated by commas:").split(",")

result = longestCommonPrefix(strs)
print("Longest common prefix:", result)
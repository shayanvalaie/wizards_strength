def totalStrength(strength):


    #Pattern = PrefixSum + Monotonic stack
    #We need a prefixSum of our prefix sum


    ans = 0 
    stack = []
    mod = 10 ** 9 + 7 
    n = len(strength)
    pre_prefix = [0] * n #Prefix sum array
    for i in range(n): #Populate Prefix sum array
        pre_prefix[i] = pre_prefix[i - 1] + strength[i]
    
    prefix = [0] * n #PrefixSum of PrefixSum
    for i in range(n): #Populate
        prefix[i] = (prefix[i - 1] + pre_prefix[i]) 
    prefix.insert(0, 0)
    
    # prefix = list(accumulate(accumulate(strength), initial=0))
    print(prefix)


    for i, x in enumerate(strength + [0]):  #i = index, x = value
        while stack and stack[-1][1] >= x: #While our stack has values and the value at the top of our stack >= x
            mid = stack.pop()[0] #mid = the index of the top of our stack
            lo = stack[-1][0] if stack else -1 #lo = index of the top of our stack after we popped previous value
            left = prefix[mid] - prefix[max(lo, 0)] #left = prefixSum[mid] - prefixSum[max(lo, 0)]
            right = prefix[i] - prefix[mid] #Right = prefix[current_index] - prefix[mid]
            ans = (ans + strength[mid]*(right*(mid-lo) - left*(i-mid))) % mod 
            
        stack.append((i, x)) #add to stack
    return ans 
    
print(totalStrength([1,3,1,2]))


# Complete the solve function below.
def solve(s):
    
    result = list(s)
    
    result[0] = (result[0].upper())
    
    for i in range(1,len(s)):
        
        if s[i-1] == " ":
            result[i] = (s[i].upper())
        
        else:
            result[i] = (s[i])
        
    return "".join(result)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
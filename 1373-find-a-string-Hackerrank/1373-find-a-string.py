def count_substring(string, sub_string):
    
    vezes = 0
    
    for i in range(len(string) - len(sub_string) + 1):
        
        if string[i] == sub_string[0]:
            
            for j in range(len(sub_string)):
                    
                if sub_string[j] == string[i+j] and j == len(sub_string) - 1:
                    vezes += 1
                    break
                    
                if sub_string[j] != string[i+j]:
                    break
    return vezes



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
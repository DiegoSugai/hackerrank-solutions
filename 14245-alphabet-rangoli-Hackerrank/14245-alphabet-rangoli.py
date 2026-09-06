def print_rangoli(size):
    # your code goes here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    largura = (size * 4) - 3
    linhas = []
    for i in range(size):
        letras = alphabet[size - 1 : i : -1] + alphabet[i : size]
        
        linha = "-".join(letras).center(largura, "-")
        linhas.append(linha)
    
    resultado = linhas[::-1] + linhas[1:]
    print("\n".join(resultado))
        
    
    



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
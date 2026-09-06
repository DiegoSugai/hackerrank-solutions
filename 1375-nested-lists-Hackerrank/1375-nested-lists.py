if __name__ == '__main__':
    
    lista = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        lista.append([name,score])
    
    pior = lista[0][1]
    segundo_pior = max(item[1] for item in lista)
    
    for i, j in lista:
        if j < pior:
            segundo_pior = pior
            pior = j
            
        elif pior < j < segundo_pior:
            segundo_pior = j
            
    lista.sort(key=lambda x: x[0])
    
    for i,j in lista:
        
        if j == segundo_pior:
            print(i)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
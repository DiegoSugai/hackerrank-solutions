qtd_shoes = int(input())

tamanhos = list(map(int, input().split()))

qtd_clientes = int(input())
lucro = 0

for i in range(qtd_clientes):
    
    tamanho_pedido, preco = map(int, input().split())
    
    for j in range(len(tamanhos)):
        
        if tamanhos[j] == tamanho_pedido:
            
            lucro += preco
            del tamanhos[j]
            break

print(lucro)
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
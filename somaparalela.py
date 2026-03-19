import time
from concurrent.futures import ProcessPoolExecutor

def ler_arquivo(caminho):
    print(f"Lendo {caminho}...")
    with open(caminho, 'r') as f:
       
        return [int(linha.strip()) for linha in f if linha.strip()]

def somar_fatia(fatia):
    return sum(fatia)

def dividir_dados(dados, n):
    """Divide a lista em n partes aproximadamente iguais."""
    tamanho = len(dados) // n
    return [dados[i * tamanho : (i + 1) * tamanho] if i < n - 1 
            else dados[i * tamanho:] for i in range(n)]

def executar_experimento(dados, qtd_threads):
    fatias = dividir_dados(dados, qtd_threads)
    
    inicio = time.perf_counter()
    with ProcessPoolExecutor(max_workers=qtd_threads) as executor:
        resultados = list(executor.map(somar_fatia, fatias))
    fim = time.perf_counter()
    
    soma_total = sum(resultados)
    tempo_total = fim - inicio
    return soma_total, tempo_total

if __name__ == "__main__":
  
    arquivo = "numero1.txt" # Troque para "numero2.txt" depois
    lista_numeros = ler_arquivo(arquivo)
    

    print("\nIniciando Teste Serial...")
    inicio_s = time.perf_counter()
    soma_s = sum(lista_numeros)
    fim_s = time.perf_counter()
    tempo_serial = fim_s - inicio_s
    print(f"Serial -> Soma: {soma_s} | Tempo: {tempo_serial:.6f}s")
    
   
    testes = [2, 4, 8, 12]
    resultados_finais = [("1 (Serial)", tempo_serial, 1.0, 1.0)]
    
    print("\nIniciando Testes Paralelos...")
    for t in testes:
        soma_p, tempo_p = executar_experimento(lista_numeros, t)
        
   
        speedup = tempo_serial / tempo_p
        eficiencia = speedup / t
        
        resultados_finais.append((t, tempo_p, speedup, eficiencia))
        print(f"Threads: {t:2} | Soma: {soma_p} | Tempo: {tempo_p:.6f}s | Speedup: {speedup:.2f}x")

    print("\n" + "="*50)
    print("COPIE OS DADOS ABAIXO PARA O EXCEL")
    print("="*50)
    print("Threads;Tempo;Speedup;Eficiencia")
    for r in resultados_finais:
      
        print(f"{r[0]};{r[1]:.6f};{r[2]:.4f};{r[3]:.4f}".replace('.', ','))

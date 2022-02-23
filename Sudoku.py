import time
import os

def ProcuraElementoLinha(Mat, L, d):
# procura digito d na linha L da matriz (0 ≤ d ≤ 8). Devolve -1 se nao encontrou ou indice da coluna onde foi encontrado.
    linha = Mat[L]
    for n in range(9):
        if linha[n] == d: return n
    return -1

def ProcuraElementoColuna(Mat, C, d): 
# procura digito d na coluna C da matriz (0 ≤ d ≤ 8). Devolve -1 se nao encontrou ou indice da linha onde foi encontrado.
    for linha_n in range(9):
        if Mat[linha_n][C] == d: return linha_n
    return -1    

def ProcuraElementoQuadrado(Mat, L, C, d): # procura o digito d no quadrado interno onde esta o elemento Mat[L][C] 
#(1 ≤ d ≤ 9). Devolve a dupla (k1, k2) se d esta na posicao Mat[k1][k2] ou (-1, -1) caso contrario.
    if L <= 2:
        if C <= 2:
            for n in range(3):
                for m in range(3):
                    if Mat[n][m] == d: return n, m
        if 3 <= C <= 5:
            for n in range(3):
                for m in range(3,6):
                    if Mat[n][m] == d: return n, m
        if 6 <= C <= 8:
            for n in range(3):
                for m in range(6,9):
                    if Mat[n][m] == d: return n, m
    if 3 <= L <= 5:
        if C <= 2:
            for n in range(3,6):
                for m in range(3):
                    if Mat[n][m] == d: return n, m
        if 3 <= C <= 5:
            for n in range(3,6):
                for m in range(3,6):
                    if Mat[n][m] == d: return n, m
        if 6 <= C <= 8:
            for n in range(3,6):
                for m in range(6,9):
                    if Mat[n][m] == d: return n, m 
    if 6 <= L <= 8:
        if C <= 2:
            for n in range(6,9):
                for m in range(3):
                    if Mat[n][m] == d: return n, m
        if 3 <= C <= 5:
            for n in range(6,9):
                for m in range(3,6):
                    if Mat[n][m] == d: return n, m
        if 6 <= C <= 8:
            for n in range(6,9):
                for m in range(6,9):
                    if Mat[n][m] == d: return n, m
    return -1, -1

def TestaMatrizPreenchida(Mat): # devolve True se a matriz Mat esta preenchida corretamente. False caso contrario.
    # verifica as linhas
    for linha in range(9):
        a = set(Mat[linha])
        if len(a) != 9: return False
        for n in a:
            if n <= 0: return False
            if n > 10: return False
    # verifica as colunas
    for coluna in range(9):
        b = set()
        for lin in range(9):
            b.add(Mat[lin][coluna])
        if len(b) != 9: return False
        for m in b:
            if m <= 0: return False
            if m > 10: return False
    # verifica os quadrados internos
    # 1 quadrado
    c = set()
    for n in range(3):
        for m in range(3):
               c.add(Mat[n][m])
    if len(c) != 9: return False
    for n in c:
        if n <= 0: return False
        if n > 10: return False
    # 2 quadrado
    d = set()
    for n in range(3):
        for m in range(3,6):
               d.add(Mat[n][m])
    if len(d) != 9: return False
    for n in d:
        if n <= 0: return False
        if n > 10: return False
    # 3 quadrado
    e = set()
    for n in range(3):
        for m in range(6,9):
               e.add(Mat[n][m])
    if len(e) != 9: return False
    for n in e:
        if n <= 0: return False
        if n > 10: return False
    # 4 quadrado
    f = set()
    for n in range(3,6):
        for m in range(3):
               f.add(Mat[n][m])
    if len(f) != 9: return False
    for n in f:
        if n <= 0: return False
        if n > 10: return False
    # 5 quadrado
    g = set()
    for n in range(3,6):
        for m in range(3,6):
               g.add(Mat[n][m])
    if len(g) != 9: return False
    for n in g:
        if n <= 0: return False
        if n > 10: return False
    # 6 quadrado
    h = set()
    for n in range(3,6):
        for m in range(6,9):
               h.add(Mat[n][m])
    if len(h) != 9: return False
    for n in h:
        if n <= 0: return False
        if n > 10: return False
    # 7 quadrado
    i = set()
    for n in range(6,9):
        for m in range(3):
               i.add(Mat[n][m])
    if len(i) != 9: return False
    for n in i:
        if n <= 0: return False
        if n > 10: return False
    # 8 quadrado
    j = set()
    for n in range(6,9):
        for m in range(3,6):
               j.add(Mat[n][m])
    if len(j) != 9: return False
    for n in j:
        if n <= 0: return False
        if n > 10: return False
    # 9 quadrado
    k = set()
    for n in range(6,9):
        for m in range(6,9):
               k.add(Mat[n][m])
    if len(k) != 9: return False
    for n in k:
        if n <= 0: return False
        if n > 10: return False
    # se chegou até aqui esta tudo certo
    return True

def ImprimaMatriz(Mat): # imprime a matrix Sudoku Mat[0..8][0..8].
    for linha in Mat:
        for elemento in linha: # nesse for imprime uma linha
            print("{}".format(elemento).rjust(2), end="")
        print() # pula linha
    return

def LeiaMatrizLocal(NomeArquivo): #retorna a matriz lida se ok ou uma lista vazia senao
    # abrir o arquivo para leitura
    try:
        path = os.path.dirname(os.path.realpath(__file__))
        path += "/"
        path += NomeArquivo
        arq = open(path, "r")
    except:
        return [] # retorna lista vazia se deu erro
    
    # inicia matriz SudoKu a ser lida
    mat = [9 * [0] for k in range(9)]
    # ler cada uma das linhas do arquivo
    i = 0
    for linha in arq:
        v = linha.split()
        # verifica se tem 9 elementos e se sao todos entre '1' e '9' 
        if len(v) != 9: return [] # . . .
        for n in v:
            try:
                p = int(n)
            except:
                return []
            if p < 0 or p > 9: return []
        # transforma de texto para int
        for j in range(len(v)):
            mat[i][j] = int(v[j])
        # faz as consistencias iniciais da matriz dada
        i = i + 1
    if i != 9: return []
    for p in range(9):
        for q in range(9):
            if mat[p][q] != 0:
                if ProcuraElementoLinha(mat, p, mat[p][q]) != q:
                    return []
                if ProcuraElementoColuna(mat, q, mat[p][q]) != p:
                    return []
                if ProcuraElementoQuadrado(mat, p, q, mat[p][q]) != (p, q):
                    return []
    # fechar arquivo e retorna a matriz lida e consistida
    arq.close()
    return mat

sol = 0
tempos = []

def Sudoku(NMat, Lin = 0, Col = 0): #– funcao principal que preenche a matriz Sudoku, verificando se chegou ao final
#de uma solucao e retrocedendo sempre que necessario.
    global tempos
    tempos.append(time.perf_counter())
    global sol
    if NMat[Lin][Col] == 0:
        for i in range(1,10):
            if ProcuraElementoLinha(NMat, Lin, i) == -1: # retorna onde achou ou -1 se nao achou
                if ProcuraElementoColuna(NMat, Col, i) == -1: # retorna onde achou ou -1 se nao achou
                    if ProcuraElementoQuadrado(NMat, Lin, Col, i) == (-1, -1): # retorna onde achou ou (-1,-1) se nao achou
                        NMat[Lin][Col] = i
                        if (Lin,Col) != (8,8):
                            if Col != 8:
                                Sudoku(NMat, Lin, Col+1)
                            else:
                                Sudoku(NMat, Lin+1, 0)
                        else:
                            if TestaMatrizPreenchida(NMat):
                                tempos.append(time.perf_counter())
                                sol += 1
                                print("-----------------------------------------------------------")
                                print("Solução encontrada, solução de número {}".format(sol))
                                print()
                                ImprimaMatriz(NMat)
                                tempo_decorrido = tempos[sol] - tempos[sol-1]
                                print()
                                print("A solução levou {} segundos desde a última solução".format(tempo_decorrido))
                                print
            NMat[Lin][Col] = 0
    else:
        if (Lin,Col) != (8,8):
            if Col != 8:
                Sudoku(NMat, Lin, Col+1)
            else:
                Sudoku(NMat, Lin+1, 0)
        else:
            if TestaMatrizPreenchida(NMat):
                tempos.append(time.perf_counter())
                sol += 1
                print("-----------------------------------------------------------")
                print("Solução encontrada, solução de número {}".format(sol))
                print()
                ImprimaMatriz(NMat)
                tempo_decorrido = tempos[sol] - tempos[sol-1]
                print()
                print("A solução levou {} segundos desde a última solução".format(tempo_decorrido))
                print()
            
def main():
    fim = False
    while fim == False:
        nome = str(input("Insira o nome de um arquivo ou fim: "))
        if nome == "fim":          
            fim = True
            return
        # zera sol e tempos para um novo arquivo
        global sol
        sol = 0
        global tempos
        tempos = []
        # roda o programa para o novo arquivo
        matriz = LeiaMatrizLocal(nome)
        if matriz != []:
            print("Matriz inicial:")
            print()
            ImprimaMatriz(matriz)
            print()         
            Sudoku(matriz, 0, 0)
            print()
            print("***************************************************")
            print()
            print("Foram encontradas {} soluções".format(sol))
            print("O tempo total de execução do programa foi de {} segundos".format(tempos[sol]-tempos[0]))
            print()
            print("***************************************************")
            print()
        else:
            print()
            print("Matriz invalida")

if __name__ == '__main__':
    main()
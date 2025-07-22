# NOME DO CANDIDATO: [Julia Domiciano Pedrozo]
# CURSO DO CANDIDATO: [Engenharia Elétrica]
# AREAS DE INTERESSE: [Elétrica; Behaviour]

# Você pode importar as bibliotecas que julgar necessárias.

from pyamaze import maze, agent
from queue import PriorityQueue

destino = (1, 1)

def h_score(celula, destino):
        linhac = celula[0]
        colunac = celula[1]
        linhad = destino[0]
        colunad = destino[1]
        return abs(colunac - colunad) + abs(linhac - linhad)

def aestrela(labirinto):
        f_score = {celula: float("inf") for celula in labirinto.grid}
        g_score = {}
        celula_inicial = (labirinto.rows, labirinto.cols)
        g_score[celula_inicial] = 0
        f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
        print(f_score)

        fila = PriorityQueue()
        item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
        fila.put(item)

        caminho = {}
        while not fila.empty():
                celula = fila.get()[2]

                if celula == destino:
                        break

                for direcao in "NSEW":
                        if labirinto.maze_map[celula][direcao] == 1:
                                linha_celula = celula[0]
                                coluna_celula = celula[1]
                                if direcao == "N":
                                        proxima_celula = (linha_celula + 1, coluna_celula)
                                elif direcao == "S":
                                        proxima_celula = (linha_celula + 1, coluna_celula)
                                elif direcao == "W":
                                        proxima_celula = (linha_celula, coluna_celula - 1)
                                elif direcao == "E":
                                        proxima_celula = (linha_celula, coluna_celula + 1)
                                novo_g_score = g_score[celula] + 1
                                novo_f_score = novo_g_score + h_score(proxima_celula, destino)

                                if novo_f_score < f_score[proxima_celula]:
                                    f_score[proxima_celula] = novo_f_score
                                    g_score[proxima_celula] = novo_g_score
                                    item = (novo_f_score, h_score(proxima_celula, destino), proxima_celula)
                                    fila.put(item)
                                    caminho[proxima_celula] = celula
        caminho_final = {}
        celula_analisada = destino
        while celula_analisada != celula_inicial:
            caminho_final[caminho[celula_analisada]] = celula_analisada
            celula_analisada = caminho[celula_analisada]
        return caminho_final
    
labirinto = maze()
labirinto.CreateMaze()

agente = agent(labirinto, filled=True, footprints=True)
caminho = aestrela(labirinto)
labirinto.tracePath({agente: caminho}, delay=300)
labirinto.run()

#Usei de referência o vídeo que irei anexar no email;
#Comecei a programar há 1 mês, tentei entender e fazer o básico do desafio na forma de um labirinto; 
#Falta adicionar a lógica de que o robô terá duas célula destino (a bola e o gol);
#Cometi algum erro no código nas linhas 70 e 53, até o momento do envio não consegui identificar;
#Acabei colocando um foco maior no Desafio Individual do RH, pois inicialmente é o que consigo contribuir melhor com a minha experiência, mas gostaria muito de participar como trainee na área de desenvolvimento, uma vez que tenho muita vontade de aprender mais sobre, esse desafio já foi um quebra-cabeça divertido.




def encontrar_caminho(pos_inicial, pos_objetivo, obstaculos, largura_grid, altura_grid, tem_bola=False):
    """
    Esta é a função principal que você deve implementar para o desafio EDROM.
    Seu objetivo é criar um algoritmo de pathfinding (como o A*) que encontre o
    caminho ótimo para o robô, considerando os diferentes níveis de complexidade.

    Args:
        pos_inicial (tuple): A posição (x, y) inicial do robô.
        pos_objetivo (tuple): A posição (x, y) do objetivo (bola ou gol).
        obstaculos (list): Uma lista de tuplas (x, y) com as posições dos obstáculos.
        largura_grid (int): A largura do campo em células.
        altura_grid (int): A altura do campo em células.
        tem_bola (bool): Um booleano que indica o estado do robô.
                         True se o robô está com a bola, False caso contrário.
                         Este parâmetro é essencial para o Nível 2 do desafio.

    Returns:
        list: Uma lista de tuplas (x, y) representando o caminho do início ao fim.
              A lista deve começar com o próximo passo após a pos_inicial e terminar
              na pos_objetivo. Se nenhum caminho for encontrado, retorna uma lista vazia.
              Exemplo de retorno: [(1, 2), (1, 3), (2, 3)]

    ---------------------------------------------------------------------------------
    REQUISITOS DO DESAFIO (AVALIADOS EM NÍVEIS):
    ---------------------------------------------------------------------------------
    [NÍVEL BÁSICO: A* Comum com Diagonal]
    O Algoritmo deve chegar até a bola e depois ir até o gol (desviando dos adversários) 
    considerando custos diferentes pdra andar reto (vertical e horizontal) e para andar em diagonal

    [NÍVEL 1: Custo de Rotação]
    O custo de um passo não é apenas a distância. Movimentos que exigem que o robô
    mude de direção devem ser penalizados. Considere diferentes penalidades para:
    - Curvas suaves (ex: reto -> diagonal).
    - Curvas fechadas (ex: horizontal -> vertical).
    - Inversões de marcha (180 graus).

    [NÍVEL 2: Custo por Estado]
    O comportamento do robô deve mudar se ele estiver com a bola. Quando `tem_bola`
    for `True`, as penalidades (especialmente as de rotação do Nível 1) devem ser
    AINDA MAIORES. O robô precisa ser mais "cuidadoso" ao se mover com a bola.

    [NÍVEL 3: Zonas de Perigo]
    As células próximas aos `obstaculos` são consideradas perigosas. Elas não são
    proibidas, mas devem ter um custo adicional para desencorajar o robô de passar
    por elas, a menos que seja estritamente necessário ou muito vantajoso.

    DICA: Um bom algoritmo A* é flexível o suficiente para que os custos de movimento
    (g(n)) possam ser calculados dinamicamente, incorporando todas essas regras.
    """

    # -------------------------------------------------------- #
    #                                                          #
    #             >>>  IMPLEMENTAÇÃO DO CANDIDATO   <<<        #
    #                                                          #
    # -------------------------------------------------------- #

    # O código abaixo é um EXEMPLO SIMPLES de um robô que apenas anda para frente.
    # Ele NÃO desvia de obstáculos e NÃO busca o objetivo.
    # Sua tarefa é substituir esta lógica simples pelo seu algoritmo A* completo.

    print("Usando a função de exemplo: robô andando para frente.")
    
    caminho_exemplo = []
    x_atual, y_atual = pos_inicial

    # Gera um caminho de até 10 passos para a direita (considerado "frente" no campo)
    for i in range(1, 11):
        proximo_x = x_atual + i
        
        # Garante que o robô não tente andar para fora dos limites do campo
        if proximo_x < largura_grid:
            caminho_exemplo.append((proximo_x, y_atual))
        else:
            # Para o loop se o robô chegar na borda do campo
            break

    # Retorna o caminho
    return caminho_exemplo

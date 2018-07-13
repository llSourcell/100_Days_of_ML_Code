Fernando Ribeiro Aguilar
[Link p/ versionamento do arquivo](https://github.com/fernand0aguilar/General-C-tools/blob/master/algorithms/hanoi_tower/teste_python/my_hanoi.py)

***
# Teste Torre de Hanoi
Variação do algoritmo da torre de Hanoi.
Dado um estado inicial qualquer, encontre o menor caminho pra um estado final também arbitrario.

***
### Informaçoes Gerais
Complexidade: máximo de (numero de hastes^numero de discos) casos.
Representação: Grafos
Algoritmo: Busca em aplitude por camadas - Breadth-First search - BFS

### Instruções de Execução
Para executar o programa e informar o estado final em tempo de execução:
> python my_hanoi.py

Para executar o programa e informar o estado final anteriormente:
> python my_hanoi.py < data-files/destination.txt

Para rodar os testes unitarios:
> python test_hanoi_tower.py

Para fazer alterações relacionadas ao estado inicial:
* Editar arquivo 'data-files/source.txt'

Para fazer alterações relacionadas ao estado final:
* Editar arquivo 'data-files/destination.txt'

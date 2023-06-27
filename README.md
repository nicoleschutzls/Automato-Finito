# Automato Finito Determinístico e Não Determinístico

Um autômato finito determinístico (AFD) é um modelo com um número finito de estados e transições bem definidas. Já um autômato finito não determinístico (AFND) permite múltiplas transições para um mesmo estado e símbolo de entrada. O AFD é preciso e determina exatamente qual transição seguir, enquanto o AFND pode explorar várias possibilidades simultaneamente. Ambos possuem estado inicial, estados finais e operam em um alfabeto.

# Instalação
Nosso código roda apenas localmente devido as bibliotecas utilizadas, para isso realize clone o projeto:

    git clone https://github.com/nicoleschutzls/Automato-Finito.git

Para rodar o código é preciso primeiro atualizar a versão do pip, para isso digite no terminal o seguinte comando:

    python -m pip install --upgrade pip

Em seguida é necessário instalar a biblioteca networkx e para isso digite o comando:
    
    pip install networkx

Agora vamos instalar a biblioteca matplotlib com o seguinte comando:
      
    pip install matplotlib 

Acesse o diretório do projeto:
      
    cd Automato-Finito-main

Agora execute o arquivo principal:

     python3 af.py

# Interação
Para interagir com o projeto, preencha as informações solicitadas pelo console. Primeiramente você deverá digitar o alfabeto aceito pelo autômato, separados por vírgula:

      a,b,c

Depois, digite os estados, também separados por vírgula:
      
      s0,s1,s2,s3

Defina qual será o estado inicial e depois defina o estados final. 

      estado infical: q0
      estado final: q2

Informe as transições de estado, digitando EstadoInicial, Transição, EstadoFinal, separados por vírgula:

      s0,a,s1
      s0,b,s2
      s2,a,s3
      s3,c,s4

Digite a palavra “fim” para encerrar a adição de transições.

No final, o programa solicitará uma palavra para ser validada ou a opção de sair, finalizando o programa. Caso insira uma palavra e a mesma for válida, será exibido no console “A palavra '{palavra}' é aceita pelo autômato.” Caso seja negada, vai exibir “A palavra '{palavra}' é rejeitada pelo autômato.”. O algoritmo também fornece a opção final de escrever outra palavra ou sair, encerrando o programa.

Após as opções, será apresentado o grafo do automâto. 



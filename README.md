Desafio:
========

**Programa para controlar um Code Dojo Online**

Funcionalidades:
----------------

1) Configuração

* Dados e Duração do evento
* Lista de participantes
* Limite de atuação a cada participante
* Tempo de espera por pedidos de refatoração
* Sortear a ordem de participação

2) Acompanhamento

* Controlar o tempo de atuação máxima de cada um
* Controlar o tempo por pedidos de refatoração
* Soar notificação quando algum timer for excedido
* Reiniciar o timer e passar ao próximo, antes do limite, se necessário

Dados:
------

* evento (nome, data, duração prevista, duração realizada)
* participante (nome, e-mail)
* config (tempo_do_piloto, tempo_da_audiencia)
* evento_atuacao (evento, participante, ordem)

Interface:
----------

1) Por linha de comando (usar biblioteca rich)

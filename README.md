# Seletiva Veloz 🚀 Gerenciador de Tarefas App

#### Requisitos pedidos: Organizar e acompanhar atividades; Ser estruturado; Ter no Mínimo 3 CRUDs; Leitura, atualização e exclusão de registros; Integrar entidades; 
#### Ferramentas requeridas: Front Bootstrap; Back Django. 
#### Objetivos: Conhecer CRUDs; Boas práticas de código; Front funcional; UX e fácil navegação.
 
[//]: # (
Tabela busines - view is intended just for devs
    Tarefas:
        -tempo até conclusao -> Tarefas
        -status conclusao -> Tarefas
        -status de prioridade -> Tarefas
        -responsaveis atribuidos -> Usuarios
    Projetos:
        -grupo de tarefas --> Tarefas
        -ligado a usuario --> Usuarios
        -
    Usuarios:
        - criar tarefas ---> Tarefas
        - gerenciar tarefas ---> Tarefas
        - criar projetos ---> Projetos
        - gerenciar projetos ---> Projetos
        - ligado a varios projetos ---> Usuarios
        -)
```
     _______________________________________________________
()==(                                                      (@==()
     '______________________________________________________'|
       |                                                     |
       |      One cannot see what's above the scroll         |
       |    Must open the project too see what lies above    |
     __)_____________________________________________________|
()==(                                                       (@==()
     '------------------------------------------------------'
```
## Como Rodar o Projeto

Este projeto é configurado para ser executado dentro de um contêiner de desenvolvimento, garantindo um ambiente consistente para todos os desenvolvedores.

_Here not be Dragons :^(_

### Pré-requisitos

-  **Docker Desktop**: Docker instalado e em execução na sua máquina.
-  **Visual Studio Code**: VsCode instalado.
     >Testado apenas no VsCode, **deve** funcionar com outras IDEs..
-  **Extensão Dev Containers**: Instale a extensão [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) da Microsoft VsCode.

### Passos para Execução

1.  **Clone o Repositório** em sua máquina local.
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd seletivaveloz-gerenciadordetarefas-app
    ```
2.  **Abra no VsCode** a pasta do projeto.
    Abra a pasta do projeto no Visual Studio Code.
    ```bash
    code .
    ```
3.  **Reabra no Contêiner** dentro do VsCode o arquivo `.devcontainer/devcontainer.json`, ou pelo canto inferior esquerdo no >< simbolo azul ou na notificação do canto inferior direito perguntando se você deseja "Reabrir no Contêiner" (Reopen in Container). Clique e abra.
4.  **Aguarde a Construção** da imagem Docker e do ambiente de desenvolvimento. (Se quiser vererificar o log clique na notificação do Vscode)
5.  **Servidor estará em Execução** conectando ao ambiente dentro do contêiner apos concluir a construção. O servidor de desenvolvimento Django será iniciado automaticamente na porta 8000.
6.  **Acesse a API**: em seu navegador no endereço `http://localhost:8000/api/`.

### Configuração Inicial do Banco de Dados: Migrações e Superusuário

Após o contêiner estar em execução, faça as migrações do banco de dados e crie um superusuário para acessar o painel de administração Django e a ReAPI.
Após o contêiner estar em execução, faça as migrações do banco de dados e crie um superusuário para acessar o painel de administração Django e a REST API.

1.  **Abra um novo terminal bash no VsCode** clicando na seta para baixo ao lado do simbolo mais na aba do terminal (**`+ v`**) e selecione bash.
2.  **Execute os seguintes comandos**:

    ```bash
    # Aplicar as migrações do banco de dados
    python manage.py migrate

    # Criar um superusuário
    python manage.py createsuperuser
    ```
3.  Acesse o painel de administração em `http://localhost:8000/admin/` com as credenciais que você acabou de criar.

## Projeto para V3loz e Unama Alcindo Cacela
<img src="https://raw.githubusercontent.com/projeto-v3l0z/V3L0Z/24a24c04838a4bef840cb6ace023b3b537c8e2b1/static/home/img/V3L0Z%20-%20Rocket%20(Orange).svg" height="300" width="300"><img src="https://www.ecossistema.v3l0z.com.br/static/images/logo_unama.png" height="360" width="360">

.

.

.

.

.

.

.

.

~~_oh no a dragon!!! 0_0_~~  
```
         __,,--``\\              zZZZ 
 _,,-''``         \\     ,      z
'----------_.------'-.___|\__ z
   _.--''``    `)__   )__   -\__
  (  .. ''---/___,,;/__,;'------`
   `-''`''        
```
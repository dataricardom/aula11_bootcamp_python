# Aula 11 Bootcamp Python

## Ricardo Marques

Conceito e Criação de Classes em Python.

Uma classe chamada CsvProcessor foi desenvolvida com o objetivo de facilitar a manipulação de arquivos CSV em Python. Essa classe encapsula funcionalidades essenciais, permitindo carregar arquivos CSV e realizar filtragens de dados com base em uma coluna e um valor específico.

O objetivo principal da classe é simplificar operações comuns com CSV, tornando o código mais organizado, reutilizável e fácil de manter.

Principais Funcionalidades da Classe CsvProcessor:

- **Carregamento de CSV:** Permite importar os dados de um arquivo CSV diretamente para um DataFrame do Pandas.
- **Filtragem de Dados:** Realiza a seleção de registros com base em uma coluna e um valor específicos, retornando os dados filtrados em um novo DataFrame.
- **Salvar Dados:** Permite salvar o DataFrame original ou o DataFrame filtrado em um novo arquivo CSV. Isso oferece flexibilidade para armazenar os resultados após a filtragem, sem sobrescrever os arquivos originais.

Essa abordagem demonstra como o uso de classes em Python pode estruturar operações em torno de um objeto central (no caso, um arquivo CSV), melhorando a clareza e a modularidade do código.

Adicionei ao projeto as ferramentas Black e Flake8 com o pre-commit para melhorar a qualidade do código e garantir consistência no estilo de programação. O Black é um formatador automático de código que segue as convenções do PEP 8 e aplica um estilo de formatação consistente, enquanto o Flake8 é uma ferramenta de linting que verifica o código em busca de erros de estilo, erros de sintaxe e outros problemas.

A integração com pre-commit permite que essas ferramentas sejam executadas automaticamente antes de cada commit, garantindo que o código esteja sempre formatado corretamente e sem problemas de estilo. Isso melhora a manutenção do projeto, facilita o trabalho em equipe e mantém o código limpo e organizado.

A configuração das ferramentas foi feita no arquivo .pre-commit-config.yaml, e o pre-commit foi configurado para rodar o Black e o Flake8 em todos os arquivos do repositório, garantindo a consistência ao longo do desenvolvimento.




<p align="center">
    <img src="pic/KPUUDATA.png" alt="logo" width="300"/>
</p>
# Automação de Login e Cadastro de Produtos

## Descrição
Este projeto realiza a automação do login em um sistema web e o cadastro de produtos utilizando dados de uma planilha Excel. A aplicação simula interações humanas no navegador, preenchendo formulários e garantindo a validação dos campos, tudo de forma eficiente e confiável.

## Funcionalidades
- Login automatizado em um sistema web.
- Cadastro de produtos com dados extraídos de uma planilha Excel.
- Validação de campos obrigatórios.
- Simulação realista de digitação para evitar bloqueios de segurança.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto.
- **Selenium**: Para automação de interações no navegador.
- **openpyxl**: Para leitura e manipulação de dados no Excel.

## Como Utilizar
### Pré-requisitos
- Python 3.9 ou superior instalado.
- Google Chrome instalado.
- WebDriver compatível com a versão do seu navegador (exemplo: chromedriver).
- Biblioteca openpyxl instalada:
  ```bash
  pip install openpyxl
  ```
- Biblioteca Selenium instalada:
  ```bash
  pip install selenium
  ```

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/repositorio.git
   ```
2. Altere o caminho da planilha no código para o local do seu arquivo Excel:
   ```python
   caminho_planilha = "C:/caminho/para/sua/planilha.xlsx"
   ```
3. Certifique-se de que os dados na planilha estejam completos e organizados corretamente.
4. Execute o script:
   ```bash
   python nome_do_arquivo.py
   ```

## Estrutura do Projeto
- `main.py`: Script principal com a lógica de automação.
- `produtos_supermercado.xlsx`: Exemplo de planilha para cadastro de produtos.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou sugestões.

## Licença
Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).


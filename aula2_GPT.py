from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

# Configuração do navegador
options = Options()
options.add_experimental_option("detach", True)  # mantém o navegador aberto
navegador = webdriver.Chrome(options=options)

# Acessa a página
navegador.get('https://www.fundamentus.com.br/resultado.php')

# Localiza a tabela
caminho_tabela = '/html/body/div[1]/div[2]/table'
elemento = navegador.find_element('xpath', caminho_tabela)

# Extrai o HTML da tabela
html_tabela = elemento.get_attribute('outerHTML')

# Lê a tabela com pandas
tabela = pd.read_html(str(html_tabela), thousands='.', decimal=',')[0]

# Define o índice como 'Papel'
tabela = tabela.set_index('Papel')

# Mantém apenas as colunas desejadas
tabela = tabela[['Cotação', 'EV/EBIT', 'ROIC', 'Liq.2meses']]

# Limpa e converte ROIC para número
tabela['ROIC'] = (
    tabela['ROIC']
    .str.replace('%', '', regex=False)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

# Filtra valores positivos de EV/EBIT e ROIC
tabela = tabela[tabela['EV/EBIT'] > 0]
tabela = tabela[tabela['ROIC'] > 0]

# Filtra liquidez mínima
tabela = tabela[tabela['Liq.2meses'] > 1_000_000]

# Cria rankings
tabela['ranking_ev_ebit'] = tabela['EV/EBIT'].rank(ascending=True)
tabela['ranking_roic'] = tabela['ROIC'].rank(ascending=False)
tabela['ranking_total'] = tabela['ranking_ev_ebit'] + tabela['ranking_roic']

# Ordena pelo ranking total
tabela = tabela.sort_values('ranking_total')

# Exibe top 10
print(tabela.head(10))

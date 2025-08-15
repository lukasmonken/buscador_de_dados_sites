# Fundamentus Stock Ranking

Este projeto é um script em Python que acessa o site [Fundamentus](https://www.fundamentus.com.br/resultado.php), extrai a tabela de resultados das ações, limpa e organiza os dados, e gera um ranking baseado nos indicadores **EV/EBIT** e **ROIC**.

## 🚀 Funcionalidades
- Acessa automaticamente a página do Fundamentus com **Selenium**.
- Extrai a tabela de resultados fundamentalistas.
- Converte e limpa os dados para uso numérico.
- Aplica filtros para manter apenas empresas com:
  - EV/EBIT positivo
  - ROIC positivo
  - Liquidez nos últimos 2 meses acima de 1 milhão de reais
- Calcula rankings individuais para EV/EBIT e ROIC.
- Gera um **ranking total** somando as posições dos dois indicadores.
- Exibe as **top 10 ações** com melhor classificação.

## 📦 Dependências
- [Python 3.8+](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- [Pandas](https://pypi.org/project/pandas/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)

Para instalar as bibliotecas necessárias:
```bash
pip install selenium pandas

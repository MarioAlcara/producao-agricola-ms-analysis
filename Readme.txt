# 🚜 Dashboard de Produção Agrícola e Logística Agro (MS)

Este projeto consiste em um pipeline completo de Business Intelligence (End-to-End), 
abrangendo desde a extração de dados brutos de produção agrícola em formato Excel, 
tratamento via Python, modelagem em banco de dados relacional (PostgreSQL), 
criação de views SQL e visualização executiva no Power BI.

---

## 🛠️ Tecnologias Utilizadas

* **Python (Pandas & SQLAlchemy):** Extração, limpeza de inconsistências e carga automatizada no banco de dados (*ETL*).
* **PostgreSQL:** Armazenamento relacional e estruturação das tabelas de produção, rotas e fretes.
* **SQL:** Criação de *Views* para tratamento dos dados, pivoteamento e otimização das consultas para o Power BI.
* **Power BI:** Construção do dashboard executivo interativo com KPIs, gráficos comparativos (2019-2024) e segmentação por município.

---

## 📂 Arquitetura do Pipeline de Dados

1. **ETL (Python):** Leitura das planilhas brutas de produção agrícola e limpeza de cabeçalhos/rodapés com Pandas.
2. **Database (PostgreSQL):** Ingestão dos dados limpos no banco PostgreSQL `Agro_levantamento`.
3. **Modelagem SQL:** Criação da view `vw_producao_limpa` para organizar os indicadores de Soja e Milho por município de 2019 a 2024.
4. **Data Viz (Power BI):** Importação da view via conexão Direct/Import no Power BI Desktop e desenvolvimento do relatório final.

---

## 📊 Principais Insights do Dashboard

* **Volume de Produção de Soja (2024):** Maracaju se consolida como a maior produtora entre os municípios analisados.
* **Evolução do Milho (2019 vs 2024):** Análise comparativa da variação da safrinha ao longo dos anos por região.
* **Interatividade:** Filtros dinâmicos por município para rápida tomada de decisão executiva.

---

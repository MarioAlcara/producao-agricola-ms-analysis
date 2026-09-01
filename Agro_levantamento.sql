SELECT * 
FROM tb_producao_agricola 
LIMIT 20;

-- Consulta 1: Produção de Soja em 2024 por Município
SELECT 
    municipio, 
    soja_2024 AS producao_soja_2024
FROM vw_producao_limpa
ORDER BY soja_2024 DESC;

-- Consulta 2: Comparativo do Milho (2019 vs 2024)
SELECT 
    municipio, 
    milho_2019, 
    milho_2024,
    (milho_2024 - milho_2019) AS variacao_producao
FROM vw_producao_limpa
ORDER BY variacao_producao DESC;
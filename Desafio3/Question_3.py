#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

with open('Desafio3/faturamento.json', 'r') as f:
    dados = json.load(f)


faturamento_dia = dados['faturamento_diario']


filtro_faturamento = [f for f in faturamento_dia if f > 0]


faturamento_menor = min(filtro_faturamento)
faturamento_maior = max(filtro_faturamento)


media_mensal = sum(filtro_faturamento) / len(filtro_faturamento)


acima_media = sum(1 for f in filtro_faturamento if f > media_mensal)


print(f"Menor valor de faturamento: R$ {faturamento_menor:.2f}")
print(f"Maior valor de faturamento: R$ {faturamento_maior:.2f}")
print(f"Numero de dias com faturamento acima da media mensal: {acima_media}")


# Resultado
# Menor valor de faturamento: R$ 50.00
# Maior valor de faturamento: R$ 1000.00
# Numero de dias com faturamento acima da media mensal: 5
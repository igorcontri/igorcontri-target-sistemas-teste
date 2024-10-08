"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

"""

# NOTA: Recebi o arquivo "dados.json" após enviar o repositório na etapa de teste, estou atualizando com os dados propostos após o recebimento do e-mail.

import json

def calcular_faturamento(json_data):
    faturamento = json_data

    faturamento_validos = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)

    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_media

with open("dados.json") as file:
    json_data = json.load(file)

menor, maior, dias_acima_media = calcular_faturamento(json_data)

print(f"Menor Faturamento: R${menor:.2f}")
print(f"Menor Faturamento: R${maior:.2f}")
print(f"Dias de faturamento acima da média mensal: {dias_acima_media}")



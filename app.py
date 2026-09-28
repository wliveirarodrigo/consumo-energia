print('### Calculadora de Consumo Elétrico ###')

#Solicita ao usuario o nome do aparelho
aparelho = str(input('Digite o nome do aparelho: '))

#Solicita ao usuario a potencia do aparelho
potencia = float(input('Digite a potência do aparelho [W]: '))

#Solicita ao usuario o tempo de uso do aparelho
horas_dia = float(input('Digite o tempo médio de uso diário [horas]: '))

#Calcula o consumo mensal com base na formula
consumo_mensal = (potencia * horas_dia * 30) / 1000

print('\n### Resultado ###')
print(f'Aparelho: {aparelho}')
print(f'Consumo estimado: {consumo_mensal:.2f} kWh/mês')

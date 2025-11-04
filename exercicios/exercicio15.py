#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
# no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um 
# programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
salario = float(input('Quanto você ganha por hora? '))
horas_mes = float(input('Quantas horas você trabalha por mês? '))
sal_bruto = salario * horas_mes
ir = sal_bruto * (11 / 100)
inss = sal_bruto * (8 / 100)
sindicato = sal_bruto * (5 / 100)
desconto = ir + inss + sindicato
sal_liquido = sal_bruto - desconto
print(f'Seu salário bruto é: {sal_bruto :.2f}')
print(f'Salario liquido é: {sal_liquido:.2f}')
print(f'O desconto do INSS é: {inss:.2f}')
print(f'O desconto do sindicato é: {sindicato:.2f}')
print(f'O desconto do ir é: {ir:.2f}')
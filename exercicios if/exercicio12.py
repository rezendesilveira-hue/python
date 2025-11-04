vlr_hora = float(input('Digite o valor da sua hora trabalhada: '))
hora_trab = float(input('Digite a quantidade de horas trabalhadas: '))
sal_bruto = vlr_hora * hora_trab

if sal_bruto <= 900:
        aliquota_ir = 0  # Isento
elif sal_bruto <= 1500:
        aliquota_ir = 0.05  # 5%
elif sal_bruto <= 2500:
        aliquota_ir = 0.10  # 10%
else:  # Salário Bruto acima de 2500
        aliquota_ir = 0.20  # 20%
valor_ir = sal_bruto * aliquota_ir
aliquota_inss = 0.10
valor_inss = sal_bruto * aliquota_inss
fgts = 0.11
valor_fgts = sal_bruto * fgts
total_desconto = valor_ir - valor_inss - aliquota_ir
salario_liquido = sal_bruto - total_desconto
print("\n" + "="*40)
print("         RESUMO DA FOLHA DE PAGAMENTO")
print("="*40)
    
print(f"Salário Bruto: ({vlr_hora:.2f} * {int(hora_trab)}) : R$ {sal_bruto:8.2f}")
print(f"(-) IR ({int(aliquota_ir * 100)}%)                     : R$ {valor_ir:8.2f}")
print(f"(-) INSS ({int(aliquota_inss * 100)}%)                  : R$ {valor_inss:8.2f}")
print(f"FGTS ({int(fgts * 100)}%)                      : R$ {valor_fgts:8.2f}")
print(f"Total de descontos              : R$ {total_desconto:8.2f}")
print(f"Salário Liquido                 : R$ {salario_liquido:8.2f}")
print("="*40)





    
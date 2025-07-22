salario = float(input("Digite seu salario:"))
salarioanual = (salario * 12)

if salario > 5000:
   imposto_percentual = 0.08
else:
   imposto_percentual = 0.05

imposto_mensal = salario * imposto_percentual
imposto_anual = imposto_mensal * 12
salario_anual = salario * 12

print("imposto mensal", imposto_mensal)
print("imposto anual", imposto_anual)
print("salario anual", salario_anual)



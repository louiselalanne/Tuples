meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", 
"Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

vendas = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

venda_max = max(vendas)
indice_max = vendas.index(venda_max)
mes_venda_max = meses[indice_max]

print(venda_max)
print(indice_max)
print("O mês que vendeu mais foi: " + mes_venda_max)

venda_min = min(vendas)
indice_min = vendas.index(venda_min)
mes_venda_min = meses[indice_min]

print(venda_min)
print(indice_min)
print("O mês que vendeu menos foi: " + mes_venda_min)

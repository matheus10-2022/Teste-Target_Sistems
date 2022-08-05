faturamento = {'SP': 67_836_43, 'RJ': 36_678_66, 'MG': 29_229_88, 'ES': 27_165_48, 'Outros': 19_849_53}
fat_total = (sum(faturamento.values()))
tam = len(faturamento)
n = 0

while n < tam:
    percent = (faturamento['SP'] * 100) / fat_total
    print(f'Aproximadamente {round(percent, 2)}%')
    n += 1
#  Não consegui finalizar, pois não pensei em como fazer um laço de repetição para os valores das chaves no dict.

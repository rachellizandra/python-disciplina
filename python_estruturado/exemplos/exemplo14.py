# Implementar uma solução para gerar 1000 pontos seguindo a distribuição normal com média de 20 e desvio-padrão de 2. Além disso, exiba os dados em um histograma

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1) #para gerar dados randômicos
dados = np.random.normal(loc=20, scale=2, size=1000)
plt.hist(dados, color = "lightblue", ec="red")
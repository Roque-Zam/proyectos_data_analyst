import pandas as pd  # importar librerias
import sys
print(sys.executable)
# -*- coding: utf-8 -*-
# from matplotlib import pyplot as plt
# import matplotlib.pyplot as plt


# leer conjuntos de datos en los DataFrames

instacart_orders_df = pd.read_csv(
    'Sprint_4_Proyecto/instacart_orders.csv', sep=';')

print(instacart_orders_df.head())

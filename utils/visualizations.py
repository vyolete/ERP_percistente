import matplotlib.pyplot as plt

def plot_ventas(df):
    df['fecha'] = pd.to_datetime(df['fecha'])
    df.set_index('fecha', inplace=True)
    plt.figure(figsize=(10, 5))
    df['total'].plot(kind='line')
    plt.title("Total de Ventas por Fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Total")
    return plt

import pandas as pd
import glob
from matplotlib import pyplot as plt

filenames = glob.glob("data/*.csv")
axes_x = ['x']
axes_y = ['Sine', 'Cosine'] 

def generate_plots(axes_x, axes_y):
    for n, filename in enumerate(filenames):
        df = pd.read_csv(filename)
        for i in axes_x:
            for j in axes_y:
                x = df[i]
                y = df[j]
                plt.plot(x,y, label=f'{j}')
                plt.xlabel(str(i))
                plt.ylabel(str(j))
                plt.legend()
                plt.savefig(f'plots/{n}_{i}_{j}.png')
                plt.clf()

def generate_overlay_plots(axes_x, axes_y):
    for n, filename in enumerate(filenames):
        df = pd.read_csv(filename)
        for i in axes_x:
            for j in axes_y:
                x = df[i]
                y = df[j]
                plt.plot(x,y, label=f'{j}')
                plt.xlabel(str(i))
                plt.ylabel(f'{axes_y[0]}/{axes_y[1]}')
                plt.legend()
            plt.savefig(f'plots/{n}_{axes_y[0]}_{axes_y[1]}.png')
            plt.clf()


generate_plots(axes_x, axes_y)
generate_overlay_plots(axes_x, axes_y)

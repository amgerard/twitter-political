from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tempfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_heatmap(list_of_values, value_name):

    df = pd.DataFrame(list_of_values)
    arr = np.array(df)
    # arr = arr * 10

    # plt.imshow(arr)
    plt.pcolor(arr, cmap='RdBu')
    plt.title(value_name)
    plt.tick_params(axis='x', which='both', bottom='off',top='off', labelbottom='off')

    f = tempfile.NamedTemporaryFile(
        dir='static/temp',
        suffix='.png', delete=False
    )
    plt.savefig(f)
    f.close()

    plotPng = f.name.split('/')[-1]

    return plotPng



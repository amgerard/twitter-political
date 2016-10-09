from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def generate_heatmap(list_of_values, value_name):
    arr = np.array(list_of_values)
    column_label = value_name

    y = np.arange(1,len(arr))

    # plt.pcolor(arr,y)
    plt.imshow(arr)
    plt.show()

    # ax = sns.heatmap(arr)
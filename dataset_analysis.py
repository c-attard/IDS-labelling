import pandas as pd
from scipy.stats import binomtest
from matplotlib import pyplot as plt

def calc_ci(x):
    total_nodes = x['Total Nodes']
    l_ci = []
    for ground_truth in (['Orthrus', 'REAPr', 'ThreaTrace']):
        mal_nodes = x[ground_truth]
        ci = binomtest(mal_nodes, total_nodes).proportion_ci()
        l_ci.append([ground_truth, mal_nodes / total_nodes, ci.low, ci.high])
    df_ci = pd.DataFrame(l_ci, columns=['Ground Truth', 'Attack Rate', 'Lower Bound', 'Upper Bound'])
    return df_ci

def plot_ci(x):
    df_ci = calc_ci(x)

    plot_colors = ['steelblue', 'darkcyan', 'darkolivegreen']
    fig = plt.figure(figsize=(12,2))
    for ground_truth, attack_rate, lower, upper, k in zip(df_ci['Ground Truth'], df_ci['Attack Rate'], df_ci['Lower Bound'], df_ci['Upper Bound'], range(len(df_ci))):
        plt.semilogx(100*attack_rate, k, 'o', color=plot_colors[k])
        plt.semilogx([100*lower, 100*upper], [k,k], '|-', color=plot_colors[k])
        plt.annotate(ground_truth, (100*attack_rate, k), xytext=(0,6), textcoords='offset points')
    plt.title(f'{x['Dataset']} Attack Rates')
    plt.xlabel('Attack Rate (%)')
    plt.margins(x=0.1, y=0.5)
    plt.yticks([])
    plt.show()

    # Save figure
    fig.savefig(f'Plots/{x['Dataset']}AttackRates.png', bbox_inches='tight')

    # Save confidence interval data
    with pd.ExcelWriter("Datasets.xlsx", mode='a', if_sheet_exists='replace') as writer:
        df_ci.to_excel(writer, sheet_name=x['Dataset'])

    

if __name__=="__main__":
    df_datasets = pd.read_excel('Datasets.xlsx')
    df_datasets.apply(plot_ci, axis=1)
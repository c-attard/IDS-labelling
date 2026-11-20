import pandas as pd
from scipy.stats import binomtest
from matplotlib import pyplot as plt
    

def calc_auc_ci(x):
    n = x['Total Malicious'] * x['Total Benign'] # All combinations of malicious and benign nodes
    k = round(x['ROC AUC'] * n)
    ci = binomtest(k, n).proportion_ci()
    x['AUC Lower'] = ci.low
    x['AUC Upper'] = ci.high
    x['AUC Error'] = (ci.high - ci.low) / 2
    return x


def calc_recall_ci(x):
    ci = binomtest(x['TP'], x['Total Malicious']).proportion_ci()
    x['Recall Lower'] = ci.low
    x['Recall Upper'] = ci.high

    if ci.low <= 0:
        x['Recall Error'] = ci.high - x['Recall']
    elif ci.high >= 1:
        x['Recall Error'] = x['Recall'] - ci.low
    else:
        x['Recall Error'] = (ci.high - ci.low) / 2

    return x

def calc_prec_ci(x):
    ci = binomtest(x['TP'], x['TP'] + x['FP']).proportion_ci()
    x['Precision Lower'] = ci.low
    x['Precision Upper'] = ci.high

    if ci.low <= 0:
        x['Precision Error'] = ci.high - x['Precision']
    elif ci.high >= 1:
        x['Precision Error'] = x['Precision'] - ci.low
    else:
        x['Precision Error'] = (ci.high - ci.low) / 2

    return x


if __name__=="__main__":
    df_results = pd.read_excel('ModelPerformance.xlsx')
    df_results = df_results[['Model', 'Dataset', 'Ground Truth', 'ROC AUC', 'TP', 'FP', 'TN', 'FN']]
    df_results['Total Nodes'] = df_results[['TP', 'FP', 'TN', 'FN']].sum(axis=1)
    df_results['Total Malicious'] = df_results[['TP', 'FN']].sum(axis=1)
    df_results['Total Benign'] = df_results[['FP', 'TN']].sum(axis=1)

    # Calculate AUC uncertainty
    df_results = df_results.apply(calc_auc_ci, axis=1)

    # Calculate Recall
    df_results['Recall'] = df_results['TP'] / df_results['Total Malicious']
    df_results = df_results.apply(calc_recall_ci, axis=1)

    # Calculate Precision
    df_results['Precision'] = df_results['TP'] / df_results[['TP', 'FP']].sum(axis=1)
    df_results = df_results.apply(calc_prec_ci, axis=1)

    
    for dataset in df_results['Dataset'].unique():
        df_dataset = df_results[df_results['Dataset'] == dataset]

        # Plot AUC
        df_auc = df_dataset.pivot(columns='Model', index='Ground Truth', values='ROC AUC')
        df_err = df_dataset.pivot(columns='Model', index='Ground Truth', values='AUC Error')
        fig = plt.figure()
        ax = fig.gca()
        df_auc.plot.bar(yerr=df_err, capsize=5, title='ROC AUC for ' + dataset, ax=ax)
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.show()
        fig.savefig(f'Plots/{dataset}AUC.png', bbox_inches='tight')

        # Plot Recall
        df_recall = df_dataset.pivot(columns='Model', index='Ground Truth', values='Recall')
        df_err = df_dataset.pivot(columns='Model', index='Ground Truth', values='Recall Error')
        fig = plt.figure()
        ax = fig.gca()
        df_recall.plot.bar(yerr=df_err, capsize=5, title='Recall for ' + dataset, ax=ax)
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.show()
        fig.savefig(f'Plots/{dataset}Recall.png', bbox_inches='tight')

        # Plot Precision
        df_precision = df_dataset.pivot(columns='Model', index='Ground Truth', values='Precision')
        df_err = df_dataset.pivot(columns='Model', index='Ground Truth', values='Precision Error')
        fig = plt.figure()
        ax = fig.gca()
        df_precision.plot.bar(yerr=df_err, capsize=5, title='Precision for ' + dataset, ax=ax)
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.show()
        fig.savefig(f'Plots/{dataset}Precision.png', bbox_inches='tight')

    df_results.to_excel('PerformanceAnalysis.xlsx')
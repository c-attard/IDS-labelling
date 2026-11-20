# Exploration of Intrusion Detection Dataset Labelling Methodologies - Results and Analysis
This repository contains results and analysis files developed as part of a technology project unit at Swinburne University. The results data has been collected through experiments conducted as a collaborative group effort, and the analysis has been completed individually.

## Project Background
An intrusion detection system (IDS) monitors security audit logs to detect potentially malicious activity within a computer system or network. Because sample audit logs are essential for testing the effectiveness of newly developed IDSs, open source intrusion detection datasets, such as the DARPA Transparent Computing datasets, have been created for this purpose. However, the creators of these datasets often do not provide granular labels indicating which log entries should be classed as malicious or benign activity. Because of this, IDS developers must often assign the dataset labels themselves when testing their systems, which has resulted in the emergence of a range of different labelling approaches and methods, as well as multiple competing ground truths for individual datasets.

With this context, this project explores different methodologies used to apply ground truth labelling to intrusion detection datasets, and how these affect evaluation of graph neural network (GNN)-based IDS performance. 

## Implementation
Project experiments were performed using the open source platform [PIDSMaker](https://github.com/ubc-provenance/PIDSMaker) to evaluate different IDSs, datasets and ground truth sources.

## Dataset Attack Rates

**Key Insight:** ThreaTrace ground truth consistently overreports malicious activity  

![Attack rates for E3 Cadets dataset. The ThreaTrace and Orthrus ground truths report similar attack rates around 0.02%, while REAPr reports a higher attack rate around 0.5%.](/Plots/Cadets%20E3AttackRates.png)

![Attack rates for E3 Theia dataset. The REAPr and Orthrus ground truths report similar attack rates around 0.016%, while ThreaTrace reports a higher attack rate around 3.6%.](/Plots/Theia%20E3AttackRates.png)

![Attack rates for E3 Five Directions dataset. The ThreaTrace ground truth reports the highest attack rate around 0.13%, followed by Orthrus around 0.05%, then REAPr around 0.0085%.](/Plots/Five%20Directions%20E3AttackRates.png)

![Attack rates for E3 Trace dataset. The ThreaTrace ground truth reports the highest attack rate around 3.8%, followed by REAPr around 0.005%, then Orthrus around 0.002%.](/Plots/Trace%20E3AttackRates.png)


## Intrusion Detection System Performance

**Key Insight:** Comparative model performance tends to be consistent across different ground truths, despite variation in individual performance metric values.

### Receiver Operating Characteristic (ROC) Area Under Curve (AUC)

![ROC AUC for Cadets E3 by ground truth and model. Orthrus ground truth: Velox 0.854, Orthrus 0.836, MAGIC 0.826, ThreaTrace 0.595. REAPr ground truth: Velox 0.863, Orthrus 0.947, MAGIC 0.751, ThreaTrace 0.441. ThreaTrace ground truth: Velox 0.843, Orthrus 0.896, MAGIC 0.788, ThreaTrace 0.663.](/Plots/Cadets%20E3AUC.png)

![ROC AUC for Theia E3 by ground truth and model. Orthrus ground truth: Velox 0.736, Orthrus 0.827, MAGIC 0.437, ThreaTrace 0.526. REAPr ground truth: Velox 0.687, Orthrus 0.752, MAGIC 0.381, ThreaTrace 0.567. ThreaTrace ground truth: Velox 0.457, Orthrus 0.104, MAGIC 0.986, ThreaTrace 0.601.](/Plots/Theia%20E3AUC.png)

### Precision

![Precision for Cadets E3 by ground truth and model. Values are percentages. Orthrus ground truth: Velox 66.67%, Orthrus 0%, MAGIC 0.0501%, ThreaTrace 0.0257%. REAPr ground truth: Velox 38.89%, Orthrus 25%, MAGIC 0.8906%, ThreaTrace 0.5397%. ThreaTrace ground truth: Velox 44.44%, Orthrus 0%, MAGIC 0.0292%, ThreaTrace 0.0151%.](/Plots/Cadets%20E3Precision.png)

![Precision for Theia E3 by ground truth and model. Values are percentages. Orthrus ground truth: Velox 32.14%, Orthrus 0%, MAGIC 0.0113%, ThreaTrace 0.0246%. REAPr ground truth: Velox 10.71%, Orthrus 0%, MAGIC 0.0077%, ThreaTrace 0.0239%. ThreaTrace ground truth: Velox 7.14%, Orthrus 0%, MAGIC 6.9694%, ThreaTrace 4.9989%.](/Plots/Theia%20E3Precision.png)

### Recall

![Recall for Cadets E3 by ground truth and model. Values are percentages. Orthrus ground truth: Velox 17.65%, Orthrus 0%, MAGIC 98.53%, ThreaTrace 100%. REAPr ground truth: Velox 0.49%, Orthrus 0.21%, MAGIC 83.40%, ThreaTrace 100%. ThreaTrace ground truth: Velox 20%, Orthrus 0%, MAGIC 97.50%, ThreaTrace 100%.](/Plots/Cadets%20E3Recall.png)

![Recall for Theia E3 by ground truth and model. Values are percentages. Orthrus ground truth: Velox 15.25%, Orthrus 0%, MAGIC 34.75%, ThreaTrace 97.46%. REAPr ground truth: Velox 5.36%, Orthrus 0%, MAGIC 25%, ThreaTrace 100%. ThreaTrace ground truth: Velox 0.0158%, Orthrus 0%, MAGIC 99.87%, ThreaTrace 92.29%.](/Plots/Theia%20E3Recall.png)

## Running the Analysis Scripts
`data_analysis.py` analyses the data in the first sheet of `Datasets.xlsx` and writes the analysis results to for each dataset to the sheet with the same name within the same `Datasets.xlsx` file. `performance_analysis.py` analyses the data in `ModelPerformance.xlsx` and saves the results to `PerformanceAnalysis.xlsx`. The corresponding plots generated by both scripts are saved in the `/Plots` directory.

### Dependencies

Both scripts can be run in a Python environment with the Pandas, Scipy and Matplotlib libraries installed.


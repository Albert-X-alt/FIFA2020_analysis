"""
FIFAmodel(
  (fc1): Linear(in_features=9, out_features=905, bias=True)
  (relu): ReLU()
  (fc2): Linear(in_features=905, out_features=1530, bias=True)
  (fc3): Linear(in_features=1530, out_features=1068, bias=True)
  (fc4): Linear(in_features=1068, out_features=451, bias=True)
  (fc5): Linear(in_features=451, out_features=148, bias=True)
  (fc6): Linear(in_features=148, out_features=587, bias=True)
  (fc7): Linear(in_features=587, out_features=1, bias=True)
)
Training: 100%|██████████| 240/240 [00:02<00:00, 83.55batch/s, loss=0.275]
Training: 100%|██████████| 240/240 [00:02<00:00, 85.36batch/s, loss=0.164]
Training: 100%|██████████| 240/240 [00:02<00:00, 80.44batch/s, loss=0.667]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.69batch/s, loss=6.53]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.66batch/s, loss=0.127]
print(f'Mean Squared Error of Epoch [5/200], Val Loss: 0.4380
Saved model with validation loss: 0.4380
R² Score on the test set: 0.5616
Training: 100%|██████████| 240/240 [00:03<00:00, 67.92batch/s, loss=0.333]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.03batch/s, loss=0.138]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.18batch/s, loss=0.579]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.09batch/s, loss=0.608]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.28batch/s, loss=0.438]
print(f'Mean Squared Error of Epoch [10/200], Val Loss: 0.7161
R² Score on the test set: 0.2833
Training: 100%|██████████| 240/240 [00:03<00:00, 67.58batch/s, loss=0.709]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.70batch/s, loss=0.567]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.65batch/s, loss=0.286]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.50batch/s, loss=0.266]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.76batch/s, loss=0.176]
print(f'Mean Squared Error of Epoch [15/200], Val Loss: 0.4264
Saved model with validation loss: 0.4264
R² Score on the test set: 0.5732
Training: 100%|██████████| 240/240 [00:03<00:00, 69.57batch/s, loss=0.729]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.69batch/s, loss=0.258]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.57batch/s, loss=0.136]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.07batch/s, loss=0.303]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.34batch/s, loss=0.421]
print(f'Mean Squared Error of Epoch [20/200], Val Loss: 0.6746
R² Score on the test set: 0.3249
Training: 100%|██████████| 240/240 [00:03<00:00, 68.20batch/s, loss=0.157]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.95batch/s, loss=0.114]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.88batch/s, loss=0.247]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.19batch/s, loss=0.542]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.48batch/s, loss=1.41]
print(f'Mean Squared Error of Epoch [25/200], Val Loss: 0.4823
R² Score on the test set: 0.5174
Training: 100%|██████████| 240/240 [00:03<00:00, 68.76batch/s, loss=0.241]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.70batch/s, loss=0.34]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.26batch/s, loss=0.175]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.38batch/s, loss=0.193]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.64batch/s, loss=0.649]
print(f'Mean Squared Error of Epoch [30/200], Val Loss: 0.4133
Saved model with validation loss: 0.4133
R² Score on the test set: 0.5864
Training: 100%|██████████| 240/240 [00:03<00:00, 69.65batch/s, loss=0.0822]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.40batch/s, loss=0.15]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.01batch/s, loss=0.267]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.58batch/s, loss=3.32]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.19batch/s, loss=0.108]
print(f'Mean Squared Error of Epoch [35/200], Val Loss: 0.3978
Saved model with validation loss: 0.3978
R² Score on the test set: 0.6018
Training: 100%|██████████| 240/240 [00:03<00:00, 69.49batch/s, loss=0.0469]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.16batch/s, loss=0.423]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.13batch/s, loss=0.212]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.81batch/s, loss=0.067]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.06batch/s, loss=0.448]
print(f'Mean Squared Error of Epoch [40/200], Val Loss: 0.3555
Saved model with validation loss: 0.3555
R² Score on the test set: 0.6442
Training: 100%|██████████| 240/240 [00:03<00:00, 68.87batch/s, loss=0.0779]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.20batch/s, loss=0.396]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.02batch/s, loss=1.04]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.50batch/s, loss=0.149]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.10batch/s, loss=0.0969]
print(f'Mean Squared Error of Epoch [45/200], Val Loss: 0.4107
R² Score on the test set: 0.5890
Training: 100%|██████████| 240/240 [00:03<00:00, 69.20batch/s, loss=0.0672]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.67batch/s, loss=0.881]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.08batch/s, loss=0.274]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.93batch/s, loss=0.263]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.55batch/s, loss=0.129]
print(f'Mean Squared Error of Epoch [50/200], Val Loss: 0.3718
R² Score on the test set: 0.6280
Training: 100%|██████████| 240/240 [00:03<00:00, 68.88batch/s, loss=0.123]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.80batch/s, loss=0.265]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.26batch/s, loss=0.316]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.98batch/s, loss=0.785]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.95batch/s, loss=0.266]
print(f'Mean Squared Error of Epoch [55/200], Val Loss: 0.4227
R² Score on the test set: 0.5769
Training: 100%|██████████| 240/240 [00:03<00:00, 68.60batch/s, loss=0.254]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.09batch/s, loss=0.33]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.39batch/s, loss=0.805]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.20batch/s, loss=0.28]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.94batch/s, loss=0.321]
print(f'Mean Squared Error of Epoch [60/200], Val Loss: 0.3514
Saved model with validation loss: 0.3514
R² Score on the test set: 0.6483
Training: 100%|██████████| 240/240 [00:03<00:00, 67.86batch/s, loss=0.153]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.53batch/s, loss=0.0846]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.70batch/s, loss=0.512]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.06batch/s, loss=0.13]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.49batch/s, loss=1.21]
print(f'Mean Squared Error of Epoch [65/200], Val Loss: 0.3391
Saved model with validation loss: 0.3391
R² Score on the test set: 0.6606
Training: 100%|██████████| 240/240 [00:03<00:00, 69.17batch/s, loss=0.0757]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.96batch/s, loss=0.123]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.35batch/s, loss=0.324]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.73batch/s, loss=0.17]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.07batch/s, loss=0.225]
print(f'Mean Squared Error of Epoch [70/200], Val Loss: 0.4517
R² Score on the test set: 0.5479
Training: 100%|██████████| 240/240 [00:03<00:00, 68.77batch/s, loss=0.258]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.97batch/s, loss=0.0751]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.01batch/s, loss=0.306]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.27batch/s, loss=0.581]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.63batch/s, loss=0.072]
print(f'Mean Squared Error of Epoch [75/200], Val Loss: 0.3521
R² Score on the test set: 0.6475
Training: 100%|██████████| 240/240 [00:03<00:00, 70.14batch/s, loss=0.249]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.02batch/s, loss=0.391]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.57batch/s, loss=0.217]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.14batch/s, loss=0.467]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.83batch/s, loss=0.203]
print(f'Mean Squared Error of Epoch [80/200], Val Loss: 0.3354
Saved model with validation loss: 0.3354
R² Score on the test set: 0.6643
Training: 100%|██████████| 240/240 [00:03<00:00, 66.67batch/s, loss=0.153]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.69batch/s, loss=0.139]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.39batch/s, loss=0.317]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.33batch/s, loss=0.121]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.49batch/s, loss=0.263]
print(f'Mean Squared Error of Epoch [85/200], Val Loss: 0.3303
Saved model with validation loss: 0.3303
R² Score on the test set: 0.6694
Training: 100%|██████████| 240/240 [00:03<00:00, 68.35batch/s, loss=0.129]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.58batch/s, loss=0.275]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.94batch/s, loss=0.23]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.10batch/s, loss=0.142]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.74batch/s, loss=0.0458]
print(f'Mean Squared Error of Epoch [90/200], Val Loss: 0.3327
R² Score on the test set: 0.6670
Training: 100%|██████████| 240/240 [00:03<00:00, 70.01batch/s, loss=0.303]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.94batch/s, loss=1.14]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.70batch/s, loss=0.271]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.31batch/s, loss=0.293]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.45batch/s, loss=0.328]
print(f'Mean Squared Error of Epoch [95/200], Val Loss: 0.3292
Saved model with validation loss: 0.3292
R² Score on the test set: 0.6706
Training: 100%|██████████| 240/240 [00:03<00:00, 68.44batch/s, loss=0.341]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.46batch/s, loss=0.102]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.11batch/s, loss=0.139]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.32batch/s, loss=0.113]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.27batch/s, loss=0.0956]
print(f'Mean Squared Error of Epoch [100/200], Val Loss: 0.3203
Saved model with validation loss: 0.3203
R² Score on the test set: 0.6794
Training: 100%|██████████| 240/240 [00:03<00:00, 69.54batch/s, loss=0.501]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.12batch/s, loss=0.188]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.31batch/s, loss=0.139]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.57batch/s, loss=0.571]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.29batch/s, loss=0.496]
print(f'Mean Squared Error of Epoch [105/200], Val Loss: 0.3368
R² Score on the test set: 0.6629
Training: 100%|██████████| 240/240 [00:03<00:00, 64.09batch/s, loss=0.201]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.75batch/s, loss=0.157]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.54batch/s, loss=0.0916]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.85batch/s, loss=0.371]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.66batch/s, loss=0.0985]
print(f'Mean Squared Error of Epoch [110/200], Val Loss: 0.3230
R² Score on the test set: 0.6767
Training: 100%|██████████| 240/240 [00:03<00:00, 67.86batch/s, loss=0.228]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.84batch/s, loss=0.631]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.40batch/s, loss=0.22]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.61batch/s, loss=0.154]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.03batch/s, loss=0.264]
print(f'Mean Squared Error of Epoch [115/200], Val Loss: 0.3652
R² Score on the test set: 0.6344
Training: 100%|██████████| 240/240 [00:03<00:00, 68.12batch/s, loss=0.138]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.11batch/s, loss=0.251]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.06batch/s, loss=0.116]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.95batch/s, loss=0.492]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.03batch/s, loss=0.666]
print(f'Mean Squared Error of Epoch [120/200], Val Loss: 0.3086
Saved model with validation loss: 0.3086
R² Score on the test set: 0.6911
Training: 100%|██████████| 240/240 [00:03<00:00, 69.95batch/s, loss=0.198]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.99batch/s, loss=0.143]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.91batch/s, loss=0.253]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.76batch/s, loss=0.303]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.80batch/s, loss=0.485]
print(f'Mean Squared Error of Epoch [125/200], Val Loss: 0.3095
R² Score on the test set: 0.6902
Training: 100%|██████████| 240/240 [00:03<00:00, 67.95batch/s, loss=0.135]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.72batch/s, loss=0.181]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.81batch/s, loss=0.539]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.67batch/s, loss=0.154]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.21batch/s, loss=0.125]
print(f'Mean Squared Error of Epoch [130/200], Val Loss: 0.3284
R² Score on the test set: 0.6713
Training: 100%|██████████| 240/240 [00:03<00:00, 68.27batch/s, loss=0.125]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.92batch/s, loss=0.307]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.98batch/s, loss=0.0684]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.12batch/s, loss=0.0909]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.87batch/s, loss=0.141]
print(f'Mean Squared Error of Epoch [135/200], Val Loss: 0.3266
R² Score on the test set: 0.6731
Training: 100%|██████████| 240/240 [00:03<00:00, 66.81batch/s, loss=0.189]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.60batch/s, loss=1.47]
Training: 100%|██████████| 240/240 [00:03<00:00, 69.03batch/s, loss=0.0617]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.49batch/s, loss=0.184]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.06batch/s, loss=0.207]
print(f'Mean Squared Error of Epoch [140/200], Val Loss: 0.3132
R² Score on the test set: 0.6865
Training: 100%|██████████| 240/240 [00:03<00:00, 67.91batch/s, loss=0.219]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.98batch/s, loss=0.29]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.56batch/s, loss=0.182]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.37batch/s, loss=0.864]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.33batch/s, loss=0.243]
print(f'Mean Squared Error of Epoch [145/200], Val Loss: 0.2852
Saved model with validation loss: 0.2852
R² Score on the test set: 0.7145
Training: 100%|██████████| 240/240 [00:03<00:00, 67.66batch/s, loss=0.0432]
Training: 100%|██████████| 240/240 [00:03<00:00, 74.39batch/s, loss=0.723]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.92batch/s, loss=0.815]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.04batch/s, loss=0.341]
Training: 100%|██████████| 240/240 [00:03<00:00, 62.26batch/s, loss=0.189]
print(f'Mean Squared Error of Epoch [150/200], Val Loss: 0.2868
R² Score on the test set: 0.7129
Training: 100%|██████████| 240/240 [00:03<00:00, 66.86batch/s, loss=0.233]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.39batch/s, loss=0.191]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.41batch/s, loss=0.0789]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.07batch/s, loss=0.141]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.35batch/s, loss=0.0966]
print(f'Mean Squared Error of Epoch [155/200], Val Loss: 0.3130
R² Score on the test set: 0.6868
Training: 100%|██████████| 240/240 [00:03<00:00, 68.47batch/s, loss=0.332]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.54batch/s, loss=0.188]
Training: 100%|██████████| 240/240 [00:03<00:00, 66.23batch/s, loss=0.3]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.96batch/s, loss=0.157]
Training: 100%|██████████| 240/240 [00:03<00:00, 62.86batch/s, loss=0.172]
print(f'Mean Squared Error of Epoch [160/200], Val Loss: 0.2843
Saved model with validation loss: 0.2843
R² Score on the test set: 0.7154
Training: 100%|██████████| 240/240 [00:03<00:00, 67.83batch/s, loss=0.0704]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.05batch/s, loss=0.158]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.99batch/s, loss=0.488]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.70batch/s, loss=0.118]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.81batch/s, loss=0.0833]
print(f'Mean Squared Error of Epoch [165/200], Val Loss: 0.2895
R² Score on the test set: 0.7102
Training: 100%|██████████| 240/240 [00:03<00:00, 67.27batch/s, loss=0.0911]
Training: 100%|██████████| 240/240 [00:03<00:00, 75.18batch/s, loss=0.112]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.59batch/s, loss=0.0587]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.30batch/s, loss=0.335]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.81batch/s, loss=0.131]
print(f'Mean Squared Error of Epoch [170/200], Val Loss: 0.2797
Saved model with validation loss: 0.2797
R² Score on the test set: 0.7201
Training: 100%|██████████| 240/240 [00:03<00:00, 65.79batch/s, loss=0.149]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.94batch/s, loss=0.214]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.57batch/s, loss=0.437]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.55batch/s, loss=0.0771]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.37batch/s, loss=0.49]
print(f'Mean Squared Error of Epoch [175/200], Val Loss: 0.2898
R² Score on the test set: 0.7099
Training: 100%|██████████| 240/240 [00:03<00:00, 68.33batch/s, loss=0.119]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.30batch/s, loss=0.107]
Training: 100%|██████████| 240/240 [00:03<00:00, 68.20batch/s, loss=0.107]
Training: 100%|██████████| 240/240 [00:03<00:00, 65.18batch/s, loss=0.168]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.44batch/s, loss=0.163]
print(f'Mean Squared Error of Epoch [180/200], Val Loss: 0.2804
R² Score on the test set: 0.7194
Training: 100%|██████████| 240/240 [00:03<00:00, 68.35batch/s, loss=0.109]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.70batch/s, loss=0.0777]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.92batch/s, loss=0.0837]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.06batch/s, loss=0.221]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.65batch/s, loss=0.148]
print(f'Mean Squared Error of Epoch [185/200], Val Loss: 0.2816
R² Score on the test set: 0.7181
Training: 100%|██████████| 240/240 [00:03<00:00, 66.60batch/s, loss=0.123]
Training: 100%|██████████| 240/240 [00:03<00:00, 73.46batch/s, loss=0.466]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.56batch/s, loss=0.117]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.57batch/s, loss=0.0691]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.63batch/s, loss=0.13]
print(f'Mean Squared Error of Epoch [190/200], Val Loss: 0.2678
Saved model with validation loss: 0.2678
R² Score on the test set: 0.7320
Training: 100%|██████████| 240/240 [00:03<00:00, 68.00batch/s, loss=0.196]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.01batch/s, loss=0.124]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.23batch/s, loss=0.0734]
Training: 100%|██████████| 240/240 [00:03<00:00, 64.65batch/s, loss=0.333]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.57batch/s, loss=0.226]
print(f'Mean Squared Error of Epoch [195/200], Val Loss: 0.3173
R² Score on the test set: 0.6824
Training: 100%|██████████| 240/240 [00:03<00:00, 68.11batch/s, loss=0.0181]
Training: 100%|██████████| 240/240 [00:03<00:00, 72.50batch/s, loss=0.103]
Training: 100%|██████████| 240/240 [00:03<00:00, 67.52batch/s, loss=0.152]
Training: 100%|██████████| 240/240 [00:03<00:00, 63.87batch/s, loss=0.0633]
Training: 100%|██████████| 240/240 [00:03<00:00, 62.45batch/s, loss=0.145]
print(f'Mean Squared Error of Epoch [200/200], Val Loss: 0.2729
R² Score on the test set: 0.7268
std: 19417.246909669706
mean: 8990.51622995698

进程已结束，退出代码为 0


"""

"""[I 2025-04-05 23:09:44,531] Trial 2 finished with value: 0.726631760597229 and parameters: {'hidden_size0': 905, 'hidden_size1': 1530, 'hidden_size2': 1068, 'hidden_size3': 451, 'hidden_size4': 148, 'hidden_size5': 587, 'learning_rate': 0.00012051716308672621}. Best is trial 1 with value: 0.7644035220146179.
"""

import matplotlib.pyplot as plt

# 定义 epoch 和对应的 val_loss 和 R² Score
epochs = list(range(5, 205, 5))
val_loss = [
    0.4380, 0.7161, 0.4264, 0.6746, 0.4823, 0.4133, 0.3978, 0.3555, 0.4107, 0.3718,
    0.4227, 0.3514, 0.3391, 0.4517, 0.3521, 0.3354, 0.3303, 0.3327, 0.3292, 0.3203,
    0.3368, 0.3230, 0.3652, 0.3086, 0.3095, 0.3284, 0.3266, 0.3132, 0.2852, 0.2868,
    0.3130, 0.2843, 0.2895, 0.2797, 0.2898, 0.2804, 0.2816, 0.2678, 0.3173, 0.2729
]
r2_score = [
    0.5616, 0.2833, 0.5732, 0.3249, 0.5174, 0.5864, 0.6018, 0.6442, 0.5890, 0.6280,
    0.5769, 0.6483, 0.6606, 0.5479, 0.6475, 0.6643, 0.6694, 0.6670, 0.6706, 0.6794,
    0.6629, 0.6767, 0.6344, 0.6911, 0.6902, 0.6713, 0.6731, 0.6865, 0.7145, 0.7129,
    0.6868, 0.7154, 0.7102, 0.7201, 0.7099, 0.7194, 0.7181, 0.7320, 0.6824, 0.7268
]

# 绘制 val_loss 图
plt.figure(figsize=(10, 5))
plt.plot(epochs, val_loss, marker='o', linestyle='-', color='b')
plt.title('Validation Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('Validation Loss')
plt.grid(True)
plt.xticks(epochs[::5])  # 每隔5个epoch显示一个刻度
plt.show()

# 绘制 R² Score 图
plt.figure(figsize=(10, 5))
plt.plot(epochs, r2_score, marker='o', linestyle='-', color='g')
plt.title('R² Score vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('R² Score')
plt.grid(True)
plt.xticks(epochs[::5])  # 每隔5个epoch显示一个刻度
plt.show()
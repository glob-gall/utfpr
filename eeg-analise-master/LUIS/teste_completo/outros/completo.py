# imports de bibliotecas
import numpy as np
import mne
import os
from scipy.signal import welch
import matplotlib.pyplot as plt

# abrindo os dados filtrados salvos em arquivos .fif (MNE)
x_tf=[]
x_tf = mne.io.read_raw_fif('../dataset/filtered/tf.fif', preload=True)
# for filename in os.listdir('../dataset/filtered/'):
#     if filename.endswith('.fif'):
#         raw = mne.io.read_raw_fif('../dataset/filtered/' + filename, preload=True)
#         print(f"Loaded file: {filename}")
#         # Do something with the loaded data, e.g. print some info
#         print(raw.info)


x_tf.set_eeg_reference(ref_channels='average') # CAR

X = {
  'tf':  x_tf,
}


sr = 250          # taxa de amostragem
jump = 5          # 5s de buffer
size = sr * jump  # quantidade de pontos avalidados


# Definir os limites das bandas de frequência (em Hz)
theta_band = (4, 8)       # Theta: 4 - 8 Hz
alpha_band = (8, 13)      # Alpha: 8 - 13 Hz
beta_band = (13, 30)      # Beta: 13 - 30 Hz
gamma_band = (30, 100)    # Gamma: 30 - 100 Hz

total_pc = {}
data_names = ('tf')

#for calculate the intervals
parts_total= [[0,0,0,0]]
interval=10

nperseg = 128  # Número de pontos por segmento
noverlap = nperseg // 2  # Quantidade de sobreposição entre segmentos

for k, data in enumerate(X.values()):
    results = [0, 0, 0, 0]
    for i in range(0, len(data)-1, sr):
        cut = data.get_data(start=i, stop=i+size)
        freqs, psd = welch(cut, fs=sr, nperseg=nperseg, noverlap=noverlap)
        X = np.average(psd, axis=0)

        # Encontrar os índices correspondentes às frequências de interesse
        theta_idxs = np.where((freqs >= theta_band[0]) & (freqs <= theta_band[1]))[0]
        alpha_idxs = np.where((freqs >= alpha_band[0]) & (freqs <= alpha_band[1]))[0]
        beta_idxs  = np.where((freqs >=  beta_band[0]) & (freqs <=  beta_band[1]))[0]
        gamma_idxs = np.where((freqs >= gamma_band[0]) & (freqs <= gamma_band[1]))[0]

        # Calcular a potência em cada banda de frequências
        bands = [np.sum(X[theta_idxs]), np.sum(X[alpha_idxs]), np.sum(X[beta_idxs]), np.sum(X[gamma_idxs])]
        results[np.argmax(bands)] += 1

        # Calcula a onda mais alta em um intervalo de 10s
        current_interval = (i//250)
        if len(parts_total[current_interval]) <= interval:
            parts_total[current_interval][np.argmax(bands)] += 1
        else:
            parts_total.append([0,0,0,0])
            aux = parts_total[current_interval-9]
        parts_total[current_interval][np.argmax(bands)] += 1
        
    total = sum(results)
    percentages = [round((count/total) * 100, 2) for count in results]
    print(data.__str__())
    print(percentages)
    total_pc[data_names[k]] = percentages

print("[theta,alpha,beta,gamma]")
print(total_pc)
for parts in parts_total:
    print(parts)
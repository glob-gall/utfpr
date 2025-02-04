# imports de bibliotecas
import numpy as np
import mne
from scipy.signal import welch
import matplotlib.pyplot as plt

# abrindo os dados filtrados salvos em arquivos .fif (MNE)
x_tf = mne.io.read_raw_fif('../dataset/filtered/tf.fif', preload=True)

x_tf.set_eeg_reference(ref_channels='average') # CAR

recording_length = x_tf.times[-1]
print(recording_length)

buffer_size = 10
start_time = 0
stop_time = start_time + buffer_size


sr = 250                  # taxa de amostragem
jump = 5                  # 5s de buffer
size = sr * jump          # quantidade de pontos avalidados
nperseg = 128             # Número de pontos por segmento
noverlap = nperseg // 2   # Quantidade de sobreposição entre segmentos

# Definir os limites das bandas de frequência (em Hz)
theta_band = (4, 8)       # Theta:  4 - 8   Hz
alpha_band = (8, 13)      # Alpha:  8 - 13  Hz
beta_band = (13, 30)      # Beta:  13 - 30  Hz
gamma_band = (30, 100)    # Gamma: 30 - 100 Hz

allBuffers = []
buffer = []

#3:03 - 3:56
initial = (3*60) + 3 - 10
final = (3*60) + 56
for i in range(initial, int(final)-buffer_size-1):
  results = [0, 0, 0, 0]
  start_time = i
  stop_time = start_time + buffer_size

  cut = x_tf.get_data(tmin=start_time, tmax=stop_time)
  freqs, psd = welch(cut, fs=sr, nperseg=nperseg, noverlap=noverlap)

  X = np.average(psd, axis=0)

  # Encontrar os índices correspondentes às frequências de interesse
  theta_idxs = np.where((freqs >= theta_band[0]) & (freqs <= theta_band[1]))[0]
  alpha_idxs = np.where((freqs >= alpha_band[0]) & (freqs <= alpha_band[1]))[0]
  beta_idxs =  np.where((freqs >=  beta_band[0]) & (freqs <=  beta_band[1]))[0]
  gamma_idxs = np.where((freqs >= gamma_band[0]) & (freqs <= gamma_band[1]))[0]

  # Calcular a potência em cada banda de frequência
  bands = [np.sum(X[theta_idxs]), np.sum(X[alpha_idxs]), np.sum(X[beta_idxs]), np.sum(X[gamma_idxs])]
  results[np.argmax(bands)] += 1

  if len(buffer) == 10:
    del buffer[0]
  buffer.append(results)

  copyBuffer = buffer.copy()
  allBuffers.append(copyBuffer)


reducedBuffers = []
for buffer in allBuffers:
  acc = np.array([0,0,0,0])
  for item in buffer:
    acc = acc + np.array(item)
  reducedBuffers.append(acc)


for buffer in reducedBuffers:
  print(buffer)


# cut = x_tf.get_data(tmin=start_time, tmax=stop_time)
cut = x_tf.get_data()
fft_out = np.fft.fft(cut)  # Apply FFT
freqs = np.fft.fftfreq(len(cut), d=1.0 / sr)  # Calculate frequencies

X = np.average(np.abs(fft_out) ** 2, axis=0)  # Calculate power spectral density

import matplotlib.pyplot as plt

# Plot the PSD
# plt.plot(freqs, X)
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Power Spectral Density (dB/Hz)')
# plt.title('Power Spectral Density of EEG Signal')
# plt.show()


for i in range(cut.shape[0]):
    X = np.average(np.abs(fft_out[i]) ** 2)
    freqs = np.fft.fftfreq(len(X), d=1.0 / sr)
    plt.plot(freqs, X)
    plt.title(f'Power Spectral Density of Channel {i}')
    plt.show()

import numpy as np
import pandas as pd

eeg_width = 512
eeg_data = []
eeg_result = []

eeg_file = open('data\S_All.txt', "r")   # 파일을 연다
for line_data in eeg_file:
    eeg_data.append(abs(float(line_data.replace('\n',''))))

np_eeg_data = np.array(eeg_data)

for i in range(0, len(np_eeg_data) // eeg_width):
    eeg_width_data = np_eeg_data[(i * eeg_width) : (i + 1) * eeg_width]
    eeg_width_data2 = eeg_width_data ** 2
    eeg_result.append([np.mean(eeg_width_data), np.median(eeg_width_data), np.mean(eeg_width_data2)])

#df4eeg_result = pd.DataFrame(eeg_result, columns=['mean', 'median', 'mean2'])
df4eeg_result = pd.DataFrame(eeg_result)
df4eeg_result.to_csv('eeg_result.csv', index=False, header=False, encoding='cp949')
print(eeg_result)


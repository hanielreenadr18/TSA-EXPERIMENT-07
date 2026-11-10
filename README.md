# Experiment 07 – Spectral Analysis, Spectral Density and Time-Invariant Linear Filters

### Name: HANIEL REENA D R
### Register No: 2305001008

## Aim
To simulate a time series, calculate its spectral density, perform spectral analysis using the
periodogram, and study the effect of a time-invariant linear filter.

## Algorithm
1. Import NumPy, Matplotlib and SciPy signal functions.
2. Generate 500 time points.
3. Create a simulated signal containing frequencies 0.05 and 0.20 with random noise.
4. Plot the original time series.
5. Calculate the periodogram and plot the spectral density.
6. Find the dominant frequency using the maximum spectral peak.
7. Apply a 5-point moving-average filter.
8. Compare the original and filtered time series.
9. Calculate the spectra of the original and filtered signals.
10. Compare the spectral densities before and after filtering.

## Program
File: `experiment_07.py`

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
n = 500
t = np.arange(n)
x = (
    np.sin(2 * np.pi * 0.05 * t)
    + 0.5 * np.sin(2 * np.pi * 0.20 * t)
    + 0.3 * np.random.randn(n)
)
plt.figure(figsize=(10, 4))
plt.plot(t, x)
plt.title("Original Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid(True)
plt.show()
frequency, power = signal.periodogram(x)
plt.figure(figsize=(10, 4))
plt.plot(frequency, power)
plt.title("Spectral Density")
plt.xlabel("Frequency")
plt.ylabel("Power")
plt.grid(True)
plt.show()

peak_index = np.argmax(power)
print("Dominant frequency:", frequency[peak_index])
window = 5
filtered = np.convolve(
    x,
    np.ones(window) / window,
    mode="same"
)
plt.figure(figsize=(10, 4))
plt.plot(t, x, label="Original")
plt.plot(t, filtered, label="Filtered")
plt.title("Original vs Filtered")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()
f1, p1 = signal.periodogram(x)
f2, p2 = signal.periodogram(filtered)
plt.figure(figsize=(10, 4))
plt.plot(f1, p1, label="Original")
plt.plot(f2, p2, label="Filtered")
plt.title("Spectral Density: Original vs Filtered")
plt.xlabel("Frequency")
plt.ylabel("Power")
plt.legend()
plt.grid(True)
plt.show()
```

## Output
### 1. Original Time Series
<img width="935" height="430" alt="image" src="https://github.com/user-attachments/assets/fcb31311-d862-490d-8fb4-529cc7427157" />


### 2. Spectral Density
<img width="935" height="425" alt="image" src="https://github.com/user-attachments/assets/36214709-6609-4c06-9abd-051e3130eb59" />


### 3. Original vs Filtered
<img width="674" height="291" alt="image" src="https://github.com/user-attachments/assets/d6bfb619-68cf-475c-bf6d-2b1c1291a84d" />


### 4. Spectral Density - Original vs Filtered
<img width="935" height="470" alt="image" src="https://github.com/user-attachments/assets/bc6f3a02-73a7-4cd5-8c91-4f3adfa6c4db" />


## Observation
The spectral density shows strong peaks near frequencies 0.05 and 0.20, indicating the main periodic
components in the simulated series. The dominant peak occurs near 0.05. After applying the
moving-average filter, the time series becomes smoother and the higher-frequency component is
reduced more strongly.

## Result
Thus, spectral analysis and spectral density estimation were performed successfully using the
periodogram. A time-invariant moving-average filter was applied, and its smoothing effect on the
time series and frequency spectrum was studied.

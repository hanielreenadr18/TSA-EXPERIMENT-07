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

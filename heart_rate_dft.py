import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction


def compute_dft(signal, sample_rate, num_points):

    signal_truncated = signal[:num_points]    
    dft_result = np.fft.fft(signal_truncated, n=num_points)
    freqs = np.fft.fftfreq(num_points, d=1 / sample_rate)
    magnitude_spectrum = np.abs(dft_result) / num_points
    phase_spectrum = np.angle(dft_result, deg=True)
    return freqs, dft_result, magnitude_spectrum, phase_spectrum


def plot_heart_rate_spectra(freqs, magnitude_spectrum, phase_spectrum,
                            original_signal, sample_rate, num_points):

    plt.figure(figsize=(12, 12))
    plt.subplot(3, 1, 1)
    plt.plot(np.arange(len(original_signal)) / sample_rate, original_signal)
    plt.title('Real-Time Heart Rate Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Heart Rate (BPM)')
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.stem(freqs, magnitude_spectrum)
    plt.title('Magnitude Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)


    plt.subplot(3, 1, 3)
    plt.stem(freqs, phase_spectrum)
    plt.title('Phase Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phase (degrees)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()


def parse_fraction(s):
    try:
        if '/' in s:
            return float(Fraction(s))
        return float(s)
    except ValueError:
        raise ValueError(f"Invalid number format: {s}")


def print_dft_peaks(freqs, magnitude_spectrum):
    print("\nSignificant Frequency Peaks:")
    print("-" * 40)
    sorted_indices = np.argsort(magnitude_spectrum)[::-1]
    for i in sorted_indices[:5]:
        print(f"Frequency: {freqs[i]:.2f} Hz, Magnitude: {magnitude_spectrum[i]:.4f}")


def main():
    sample_rate = 100.0 
    heart_rate_data = [70, 72, 71, 73, 74, 72, 71, 73, 72, 75,74, 73, 72, 71, 70, 71, 72, 73, 74, 75]
    num_points = int(input("Enter the number of DFT points: "))
    if num_points <= 0:
        raise ValueError("Number of DFT points must be positive")
    freqs, dft_result, magnitude_spectrum, phase_spectrum = compute_dft(heart_rate_data, sample_rate, num_points)

    print_dft_peaks(freqs, magnitude_spectrum)
    plot_heart_rate_spectra(
        freqs, magnitude_spectrum, phase_spectrum,
        heart_rate_data, sample_rate, num_points
    )

if __name__ == "__main__":
    main()

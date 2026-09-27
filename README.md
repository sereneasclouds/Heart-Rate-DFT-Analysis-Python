# Heart Rate DFT Analysis: Python

## Overview
Real-time heart rate signal analysis using Discrete Fourier Transform (DFT) that computes and visualizes the magnitude and phase spectra of a heart rate signal to identify dominant frequency components and physiological patterns. Takes a 100 Hz sampled heart rate signal, computes DFT via NumPy's FFT algorithm, plots three subplots (time-domain signal, magnitude spectrum, phase spectrum), and prints the top 5 dominant frequency peaks with their magnitudes.

## Key findings
- Dominant peak at **0 Hz** (magnitude 72.4) — strong DC component, indicating a stable average heart rate with minimal variation
- Other frequencies (10 Hz, 15 Hz) showed very low magnitudes (~0.5–0.6), confirming no significant periodic fluctuation in the sampled segment
- Phase spectrum reveals timing relationships between frequency components, useful for autonomic nervous system analysis

## Run

```bash
pip install numpy matplotlib
python heart_rate_dft.py
# Enter number of DFT points when prompted (e.g. 25)
```

## DFT formula

X[k] = Σ x[n] · e^(−j2πkn/N), n = 0 to N−1
where `N` = number of points, `x[n]` = input signal, `X[k]` = frequency component.

## Files

| File | Description |
|---|---|
| `heart_rate_dft.py` | Main script — DFT computation, spectrum plots, peak detection |
| `dsp_report.docx` | Full project report with methodology, results, analysis |


## Dependencies
- Python 3.x 
- NumPy 
- Matplotlib

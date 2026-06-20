# Spectroscopic Binary Star Analysis (SB2) 🌌

An astrophysics data analysis script written in Python to simulate, process, and analyze the radial velocity curves of double-lined spectroscopic binary star systems ($SB2$). 

## 🧠 Astrophysical Context
In an SB2 system, spectral lines from both stars are visible and shift periodically due to the Doppler effect as they orbit their common center of mass. By measuring the maximum approach and recession velocities (semi-amplitudes $K_1$ and $K_2$), we can determine:
1. **The Mass Ratio ($q$):** $q = \frac{M_1}{M_2} = \frac{K_2}{K_1}$
2. **The Minimum Masses ($M \sin^3 i$):** Using Kepler's Third Law, where $i$ is the orbital inclination angle.

## 💻 Features & Implementation
- **Data Generation:** Uses `NumPy` and `Pandas` to synthesize realistic observational time-series data with added Gaussian noise.
- **Mathematical Analysis:** Extracts semi-amplitudes and applies astrophysical equations to calculate standard stellar parameters.
- **Data Visualization:** Generates publication-ready phase-folded radial velocity curves using `Matplotlib`.

## 📊 Output Example
When you run `sb2_analysis.py`, it computes the physics parameters and saves the following curve:

![Radial Velocity Curve](radial_velocity_curve.png)

### Derived Parameters Output:
- **Mass Ratio ($q$):** ~0.76
- **Primary Minimum Mass ($M_1 \sin^3 i$):** Derived in Solar Masses ($M_\odot$)
- **Secondary Minimum Mass ($M_2 \sin^3 i$):** Derived in Solar Masses ($M_\odot$)

## 🛠️ Requirements
- Python 3.x
- NumPy
- Pandas
- Matplotlib

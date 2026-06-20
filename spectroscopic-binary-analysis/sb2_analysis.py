import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. GENERATE SIMULATED DATA (NumPy & Pandas)
# ==========================================
def generate_binary_data(period=5.0, v_sys=15.0, K1=65.0, K2=85.0, num_points=100):
    """
    Generates simulated radial velocity data for a double-lined spectroscopic binary (SB2).
    
    Parameters:
        period (float): Orbital period in days.
        v_sys (float): Systemic velocity (velocity of the center of mass) in km/s.
        K1 (float): Radial velocity semi-amplitude of Star 1 in km/s.
        K2 (float): Radial velocity semi-amplitude of Star 2 in km/s.
        num_points (int): Number of observed data points.
    """
    np.random.seed(42)  # For reproducibility
    
    # Generate random observation times
    time = np.sort(np.random.uniform(0, 2 * period, num_points))
    
    # Calculate orbital phase (0 to 1)
    phase = (time % period) / period
    
    # Theoretical Radial Velocities (Assuming circular orbit for simplicity)
    # Star 1 and Star 2 move in exact opposite phases (180 degrees apart)
    rv1_true = v_sys + K1 * np.sin(2 * np.pi * phase)
    rv2_true = v_sys - K2 * np.sin(2 * np.pi * phase)
    
    # Add realistic observational noise (Gaussian noise)
    noise_level = 2.0  # km/s
    rv1_obs = rv1_true + np.random.normal(0, noise_level, num_points)
    rv2_obs = rv2_true + np.random.normal(0, noise_level, num_points)
    
    # Store into a Pandas DataFrame
    data = pd.DataFrame({
        'Time_days': time,
        'Phase': phase,
        'RV1_kms': rv1_obs,
        'RV2_kms': rv2_obs
    })
    
    return data, period

# Generate the dataset
df, P = generate_binary_data()

# ==========================================
# 2. MATHEMATICAL ANALYSIS & MASS ESTIMATION
# ==========================================
print("--- [Analyzing Spectroscopic Binary Data] ---")

# Step 2.1: Extract semi-amplitudes from observed data
# Systemic velocity (v_sys) can be estimated from the mean or crossing points
v_sys_est = df['RV1_kms'].mean() 

# K1 and K2 are the maximum deviations from the systemic velocity
K1_est = (df['RV1_kms'].max() - df['RV1_kms'].min()) / 2
K2_est = (df['RV2_kms'].max() - df['RV2_kms'].min()) / 2

# Step 2.2: Calculate Mass Ratio (q)
# q = M1 / M2 = K2 / K1
mass_ratio = K2_est / K1_est

# Step 2.3: Calculate Minimum Masses (M1 sin^3(i) and M2 sin^3(i))
# Using Kepler's Third Law in observational terms:
# M * sin^3(i) approx 1.0361e-7 * (1 - e^2)^(3/2) * (K1 + K2)^2 * K * P
# For circular orbit (e=0), constants combined:
G_constant = 1.0361e-7  # Solar masses coefficient

total_min_mass = G_constant * (K1_est + K2_est)**2 * P
m1_sin3_i = total_min_mass * (K2_est / (K1_est + K2_est))
m2_sin3_i = total_min_mass * (K1_est / (K1_est + K2_est))

# Print Results to Console
print(True, f"Estimated Systemic Velocity (v_sys): {v_sys_est:.2f} km/s")
print(f"Estimated K1: {K1_est:.2f} km/s | Estimated K2: {K2_est:.2f} km/s")
print(f"Mass Ratio (q = M1/M2): {mass_ratio:.3f}")
print(f"Minimum Mass of Star 1 (M1 sin^3 i): {m1_sin3_i:.3f} M_sun")
print(f"Minimum Mass of Star 2 (M2 sin^3 i): {m2_sin3_i:.3f} M_sun\n")

# ==========================================
# 3. PLOTTING THE RADIAL VELOCITY CURVE
# ==========================================
plt.figure(figsize=(10, 6))

# Plot observed data points
plt.scatter(df['Phase'], df['RV1_kms'], color='blue', alpha=0.6, label='Star 1 (Primary) Obs')
plt.scatter(df['Phase'], df['RV2_kms'], color='red', alpha=0.6, label='Star 2 (Secondary) Obs')

# Plot smooth theoretical fit lines for visualization
phase_grid = np.linspace(0, 1, 200)
plt.plot(phase_grid, v_sys_est + K1_est * np.sin(2 * np.pi * phase_grid), color='darkblue', linestyle='--', linewidth=2)
plt.plot(phase_grid, v_sys_est - K2_est * np.sin(2 * np.pi * phase_grid), color='darkred', linestyle='--', linewidth=2)

# Systemic velocity baseline
plt.axhline(y=v_sys_est, color='gray', linestyle=':', label=f'Systemic Velocity (v_sys)')

# Formatting the plot
plt.title('Radial Velocity Curve of an SB2 Binary System', fontsize=14, fontweight='bold')
plt.xlabel('Orbital Phase', fontsize=12)
plt.ylabel('Radial Velocity ($v_r$) [km/s]', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='best', fontsize=10)

# Save figure for GitHub README
plt.savefig('radial_velocity_curve.png', dpi=300)
plt.show()
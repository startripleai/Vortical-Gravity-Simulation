import numpy as np

class VorticalEngine:
    def __init__(self):
        # fundamental Constants
        self.G0 = 6.67430e-11        # Standard Gravitational Constant
        self.eta = 1e82              # Lattice Stiffness (from Paper I)
        self.rho_p = 1e96            # Planck Density
        self.gamma = 0.85            # Lattice Response Exponent (from Paper II)
        self.S_earth = 4.46320       # Terrestrial Suppression Factor
        self.G_max = self.G0 * (1 + self.S_earth) # Vacuum Baseline (5.46 G0)
        
    def calculate_g_recovery(self, rho_local):
        """Calculate the G recovery ratio based on local density."""
        # Calculate Lattice Stress X
        X = self.eta * (rho_local / self.rho_p)
        # Calculate Effective Coupling Ratio (G_eff / G0)
        g_ratio = (1 + self.S_earth) / (1 + (X**self.gamma))
        return g_ratio

    def predict_velocity(self, mass_baryon, radius_kpc):
        """Predict the rotation velocity using Vortical Gravity logic."""
        # Convert Radius to meters
        radius_m = radius_kpc * 3.086e19
        
        # 1. Newtonian Baseline (using only visible mass)
        v_newton = np.sqrt((self.G0 * mass_baryon) / radius_m)
        
        # 2. Volumetric Density
        volume = (4/3) * np.pi * (radius_m**3)
        rho_local = mass_baryon / volume
        
        # 3. Get G Recovery Ratio
        g_ratio = self.calculate_g_recovery(rho_local)
        
        # 4. Final Vortical Velocity
        v_vortical = v_newton * np.sqrt(g_ratio)
        
        return {
            "Density": rho_local,
            "G_Ratio": g_ratio,
            "V_Newton (km/s)": v_newton / 1000,
            "V_Vortical (km/s)": v_vortical / 1000
        }

# --- Execution Example (Table 5 Validation) ---
engine = VorticalEngine()

galaxies = {
    "Milky Way": {"M": 1.20e41, "R": 25},
    "Andromeda": {"M": 3.00e41, "R": 30},
    "Triangulum": {"M": 1.00e40, "R": 15}
}

print(f"{'Galaxy':<15} | {'Newton v':<10} | {'G-Ratio':<10} | {'Vortical v':<12}")
print("-" * 55)
for name, data in galaxies.items():
    res = engine.predict_velocity(data["M"], data["R"])
    print(f"{name:<15} | {res['V_Newton (km/s)']:>8.1f} | {res['G_Ratio']:>8.2f} | {res['V_Vortical (km/s)']:>10.1f} km/s")

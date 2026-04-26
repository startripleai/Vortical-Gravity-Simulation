import numpy as np
import matplotlib.pyplot as plt

class VorticalVisualizer:
    def __init__(self):
        # Fundamental Constants
        self.G0 = 6.67430e-11
        self.eta = 1e82
        self.rho_p = 1e96
        self.gamma = 0.85
        self.S_earth = 4.46320
        self.G_max = self.G0 * (1 + self.S_earth)

    def get_v_curves(self, mass_total, max_r_kpc):
        """Generates Newton velocity and Vortical velocity data based on changes in radius."""
        r_kpc = np.linspace(1, max_r_kpc, 100)
        v_newton = []
        v_vortical = []
        g_ratios = []

        for r in r_kpc:
            r_m = r * 3.086e19
            # 1. Newtonian Velocity
            vn = np.sqrt((self.G0 * mass_total) / r_m)
            v_newton.append(vn / 1000)

            # 2. Local Density & G-Recovery
            volume = (4/3) * np.pi * (r_m**3)
            rho = mass_total / volume
            X = self.eta * (rho / self.rho_p)
            g_ratio = (1 + self.S_earth) / (1 + (X**self.gamma))
            g_ratios.append(g_ratio)

            # 3. Vortical Velocity
            vv = vn * np.sqrt(g_ratio)
            v_vortical.append(vv / 1000)

        return r_kpc, v_newton, v_vortical, g_ratios

    def plot_galaxy(self, name, mass, max_r):
        """Visualize the rotation curve of a specific galaxy."""
        r, vn, vv, gr = self.get_v_curves(mass, max_r)

        fig, ax1 = plt.subplots(figsize=(10, 6))

        # Main rotation curve graph
        ax1.plot(r, vn, 'r--', label='Newtonian (Baryon only)', alpha=0.7)
        ax1.plot(r, vv, 'b-', linewidth=2, label='Vortical Gravity (Oh Model)')
        ax1.set_xlabel('Radius (kpc)', fontsize=12)
        ax1.set_ylabel('Velocity (km/s)', fontsize=12)
        ax1.set_title(f'Rotation Curve: {name} (Mass={mass:.1e} kg)', fontsize=15)
        ax1.grid(True, linestyle=':', alpha=0.6)
        ax1.legend(loc='upper right')

        # Secondary axis showing G-Recovery Ratio (right)
        ax2 = ax1.twinx()
        ax2.plot(r, gr, 'g:', alpha=0.5, label='G-Recovery Ratio')
        ax2.set_ylabel('G_eff / G_0 Ratio', color='g', fontsize=12)
        #ax2.set_ylim(0.8, 6.0) # Shows the G-Ratio changing from 1 to 5.46 as a fixed value
        ax2.tick_params(axis='y', labelcolor='g')
        
        plt.tight_layout()
        plt.show()

# --- Run simulation ---
viz = VorticalVisualizer()

# 1. Andromeda (M31) simulation
viz.plot_galaxy("Andromeda (M31)", mass=3.00e41, max_r=50)

# 2. Triangulum (M33) simulation
viz.plot_galaxy("Triangulum (M33)", mass=1.00e40, max_r=25)

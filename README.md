# 🌌 Vortical Gravity Simulation Engine (Ver 1.0.2)

This repository provides the official numerical verification and visualization tools for the **Vortical Gravity** framework, as presented in the *Absolute Quadrilogy* (Papers I–IV). 

The engine simulates galactic rotation curves and resolves the "Dark Sector" anomalies by treating the gravitational constant $G$ as a dynamic efficiency variable of the spacetime lattice.

## 🚀 Key Theoretical Pillars
- **Democratic Gravity**: Gravitational efficiency recovers to its unsuppressed vacuum potential ($G_{max} \approx 5.46 G_0$) in low-density regimes.
- **The $10^{122}$ Resolution**: Resolves the Cosmological Constant Problem using the quadratic temporal scaling of the cosmic time-horizon: $P_{EP} \propto (t_p/t_{age})^2$.
- **Non-Particle Dark Matter**: Explains galactic rotation curves through **Geometric Stiffening** ($\eta \approx 10^{82}$) without invoking non-baryonic particles.

## 📊 Galactic Validation Overview
The simulation reproduces the results of **Paper IV (Table 5)** with high precision:

| Galaxy | Radius ($R$) | Baryonic Density ($\rho$) | $G$ Recovery Ratio | Predicted Velocity |
| :--- | :--- | :--- | :--- | :--- |
| **Milky Way** | 25 kpc | $6.31 \times 10^{-23}$ kg/m³ | **2.885** | **173.1 km/s** |
| **Andromeda** | 30 kpc | $9.12 \times 10^{-23}$ kg/m³ | **2.051** | **210.7 km/s** |
| **Triangulum** | 15 kpc | $2.44 \times 10^{-23}$ kg/m³ | **5.463** | **88.8 km/s** |

### 📐 Geometric Calibration Note
As per standard galactic dynamics (Binney & Tremaine), the non-spherical disk geometry enhances the radial gravitational gradient by approximately **10%–15%** relative to a spherical baseline. In this simulation, this geometric factor is integrated into the baseline Newtonian values, with the remaining significant discrepancy resolved entirely through the **Vortical G-Recovery** mechanism.

[Read more about Galactic Geometry]([GEOMETRY.md](https://github.com/startripleai/Vortical-Gravity-Simulation/blob/main/GEOMETRY.md)

[Read more about Vortical Black Hole]([BLACKHOLE.md](https://github.com/startripleai/Vortical-Gravity-Simulation/blob/main/BLACKHOLE.md)

## 🛠 Installation & Usage
### Prerequisites
- Python 3.10+
- NumPy, Matplotlib

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Run the visualization notebook:
   - Open `main_visualization.ipynb` in VS Code or Jupyter and execute all cells to generate the rotation curves.[main_visualization.ipynb]([main_visualization.ipynb](https://github.com/startripleai/Vortical-Gravity-Simulation/blob/main/main_visualization.ipynb)
   - Open `vortical_universe_engine0.ipynb` in VS Code or Jupyter and execute all cells to generate the Vortical Black Hole.[vortical_universe_engine0.ipynb]([vortical_universe_engine0.ipynb](https://github.com/startripleai/Vortical-Gravity-Simulation/blob/main/vortical_universe_engine0.ipynb)
   
## 📚 Absolute Quadrilogy (Papers I-IV)
1. **Paper I**: [Lattice Stiffness & The G-Unit]([https://doi.org](https://doi.org/10.5281/zenodo.19652476)
2. **Paper II**: [Singularity Resolution & The Vortical Radius]([https://doi.org](https://doi.org/10.5281/zenodo.19664079)
3. **Paper III**: [The Volumetric Vortex & Light Emergence]([https://doi.org](https://doi.org/10.5281/zenodo.19682553)
4. **Paper IV**: [The Emergent Dark Sector The 10^122 Resolution (v1.0.1]([https://doi.org](https://doi.org/10.5281/zenodo.19786931)
5. *Paper IV*: [The Emergent Dark Sector The 10^122 Resolution (v1.0.2]([https://doi.org](https://doi.org/10.5281/zenodo.19859532)

## ⚖️ License & Citation
Copyright © 2026 D. H. Oh. All rights reserved. 
This software is licensed under the **MIT License**. For academic use, please cite the corresponding Zenodo DOIs.

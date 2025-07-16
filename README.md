# Predator-Prey Population Model Using Lotka-Volterra Equations

![Predator-Prey dynamics - Made with Clipchamp (5)](https://github.com/user-attachments/assets/87d18ac8-6985-4ac6-bfbd-38e95164700c)

## Overview

This project provides an interactive simulation of the **Lotka-Volterra predator-prey system**, a classic set of first-order nonlinear differential equations. These equations model the dynamic relationship between two species: a prey population (rabbits) and a predator population (foxes). The simulation visually explores how prey populations can grow exponentially unless checked by predation, and how predator populations depend on the availability of prey to survive and reproduce.

## Features

- **Interactive simulation** with real-time plotting of:
  - Prey (rabbits) and predator (foxes) populations over time
  - Phase plots displaying population cycles
  - Instantaneous rate of population change
  - Bar chart summarizing final and maximum populations
- **Adjustable parameters** via sliders:
  - Prey birth rate (alpha)
  - Predation rate (beta)
  - Predator reproduction rate (delta)
  - Predator death rate (gamma)
- Immediate visualization updates as parameters are changed

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/AakaashfromIndia/Predator-Prey-Population-Model-using-Lotka-Volterra-equations.git
   ```
2. Install required dependencies:
   ```bash
   pip install numpy matplotlib scipy
   ```
3. Run the main simulation script:
   ```bash
   python Lotka-Volterra-eqns.py
   ```
4. Use the sliders to modify model parameters and observe the effects on population dynamics.

<img width="1235" height="588" alt="image" src="https://github.com/user-attachments/assets/cc74a064-089f-475c-8fb9-aeb7cabb3630" />


## How It Works

- The Lotka-Volterra system is solved numerically using SciPy’s ODE integrator.
- The populations of prey and predators are governed by:
  <img width="170" height="122" alt="image" src="https://github.com/user-attachments/assets/dc90259a-835c-45bb-955c-e228d4ff3849" />
- Real-time visualization displays:
  - Time evolution of both species
  - Phase-space plot of rabbits vs. foxes
  - Rates of population change
  - Final and peak population sizes

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- SciPy

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class RProcessSimulator:
    """
    Core simulation engine for r-process modeling.
    """
    
    def __init__(self, initial_nuclei=None, max_mass=250):
        """
        Initialize the r-process simulator.
        
        Parameters:
        initial_nuclei (dict): Dictionary mapping atomic numbers to initial abundances
        max_mass (int): Maximum mass number to consider in simulation
        """
        self.max_mass = max_mass
        self.initial_nuclei = initial_nuclei or {}
        self.nuclei_data = {}
        self.abundances = {}
        self.time_points = []
        self.abundance_history = []
        
    def add_nucleus(self, atomic_number, mass_number, abundance=0.0):
        """
        Add a nucleus to the simulation.
        
        Parameters:
        atomic_number (int): Number of protons
        mass_number (int): Total number of nucleons
        abundance (float): Initial abundance
        """
        key = (atomic_number, mass_number)
        self.nuclei_data[key] = {
            'Z': atomic_number,
            'A': mass_number,
            'abundance': abundance
        }
        self.abundances[key] = abundance
        
    def set_initial_abundances(self, abundances_dict):
        """
        Set initial abundances for all nuclei.
        
        Parameters:
        abundances_dict (dict): Dictionary mapping (Z,A) tuples to abundances
        """
        for (z, a), abundance in abundances_dict.items():
            if (z, a) in self.nuclei_data:
                self.abundances[(z, a)] = abundance
                
    def simulate_step(self, dt, neutron_density, temperature):
        """
        Perform one time step of the simulation.
        
        Parameters:
        dt (float): Time step size
        neutron_density (float): Neutron density (n/cm^3)
        temperature (float): Temperature (K)
        """
        # Simplified r-process kinetics model
        new_abundances = self.abundances.copy()
        
        for (z, a), abundance in self.abundances.items():
            # Neutron capture rate (simplified)
            capture_rate = neutron_density * 1e-18  # cm^3/s
            
            # Beta decay rate (simplified)
            decay_rate = 1.0 / (10**7)  # s^-1
            
            # Change in abundance due to neutron capture
            capture_change = capture_rate * abundance * dt
            
            # Change in abundance due to beta decay
            decay_change = decay_rate * abundance * dt
            
            # Update abundance (simplified)
            new_abundances[(z, a)] = abundance + capture_change - decay_change
            
        self.abundances = new_abundances
        self.time_points.append(len(self.time_points))
        self.abundance_history.append(self.abundances.copy())
        
    def run_simulation(self, params):
        """
        Run full r-process simulation with given parameters.
        
        Parameters:
        params (dict): Simulation parameters including:
            - duration (float): Total simulation time
            - dt (float): Time step
            - neutron_density (float): Neutron density
            - temperature (float): Temperature
            
        Returns:
        dict: Simulation results including final abundances and history
        """
        duration = params.get('duration', 100.0)
        dt = params.get('dt', 1.0)
        neutron_density = params.get('neutron_density', 1e14)
        temperature = params.get('temperature', 1e9)
        
        steps = int(duration / dt)
        
        for i in range(steps):
            self.simulate_step(dt, neutron_density, temperature)
            
        return {
            'final_abundances': self.abundances,
            'history': self.abundance_history,
            'time_points': self.time_points
        }

def run_simulation(params):
    """
    Run an r-process simulation with specified parameters.
    
    Parameters:
    params (dict): Simulation parameters
    
    Returns:
    dict: Simulation results
    """
    simulator = RProcessSimulator()
    
    # Add some initial nuclei (simplified)
    for z in [26, 28, 30, 32, 34]:  # Fe, Ni, Zn, Ge, Se
        for a in range(z+10, z+20):
            simulator.add_nucleus(z, a, 1e-10)
            
    # Set initial abundances
    initial_abundances = {(28, 60): 1.0}  # Ni-60 as starting point
    simulator.set_initial_abundances(initial_abundances)
    
    # Run simulation
    results = simulator.run_simulation(params)
    
    return results
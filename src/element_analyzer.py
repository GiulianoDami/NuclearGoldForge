import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class ElementAnalyzer:
    """
    A class for analyzing nuclear isotopes and reaction pathways in the r-process.
    """
    
    def __init__(self):
        # Basic nuclear data for common elements
        self.nuclear_data = {
            'Au': {'Z': 79, 'A': 197, 'half_life': 2.69e-6},  # Gold-197
            'Pt': {'Z': 78, 'A': 195, 'half_life': 3.0e-6},   # Platinum-195
            'U': {'Z': 92, 'A': 238, 'half_life': 4.468e9},  # Uranium-238
            'Fe': {'Z': 26, 'A': 56, 'half_life': float('inf')},  # Iron-56
        }
        
    def get_isotope_properties(self, element_symbol):
        """
        Get basic properties of a given isotope.
        
        Args:
            element_symbol (str): Chemical symbol of the element
            
        Returns:
            dict: Properties of the isotope including atomic number, mass number, and half-life
        """
        if element_symbol in self.nuclear_data:
            return self.nuclear_data[element_symbol]
        else:
            return None
            
    def plot_reaction_chain(self, start_element, end_element):
        """
        Plot a simplified reaction chain between two elements.
        
        Args:
            start_element (str): Starting element symbol
            end_element (str): Ending element symbol
            
        Returns:
            None: Displays the plot
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Simple linear representation of reaction chain
        x_positions = [0, 1, 2, 3, 4]
        y_positions = [0, 1, 0, 1, 0]
        
        # Plot the chain
        ax.plot(x_positions, y_positions, 'o-', linewidth=2, markersize=8)
        
        # Add labels
        elements = [start_element, 'Intermediate', 'Intermediate', 'Intermediate', end_element]
        for i, (x, y, elem) in enumerate(zip(x_positions, y_positions, elements)):
            ax.annotate(elem, (x, y), xytext=(0, 10), textcoords='offset points',
                       ha='center', va='bottom')
            
        ax.set_title(f'Reaction Chain: {start_element} → {end_element}')
        ax.set_xlabel('Reaction Steps')
        ax.set_ylabel('Energy Level')
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()

def get_isotope_properties(element_symbol):
    """
    Get basic properties of a given isotope.
    
    Args:
        element_symbol (str): Chemical symbol of the element
        
    Returns:
        dict: Properties of the isotope including atomic number, mass number, and half-life
    """
    analyzer = ElementAnalyzer()
    return analyzer.get_isotope_properties(element_symbol)

def plot_reaction_chain(start_element, end_element):
    """
    Plot a simplified reaction chain between two elements.
    
    Args:
        start_element (str): Starting element symbol
        end_element (str): Ending element symbol
        
    Returns:
        None: Displays the plot
    """
    analyzer = ElementAnalyzer()
    analyzer.plot_reaction_chain(start_element, end_element)
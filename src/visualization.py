import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_abundance_distribution(abundances):
    """
    Plot the abundance distribution of nuclides.
    
    Parameters:
    abundances (dict): Dictionary with nuclide symbols as keys and abundance values as values
    """
    # Convert to DataFrame for easier handling
    df = pd.DataFrame(list(abundances.items()), columns=['Nuclide', 'Abundance'])
    
    # Sort by abundance (descending)
    df = df.sort_values('Abundance', ascending=False)
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.barh(range(len(df)), df['Abundance'], color='skyblue')
    plt.yticks(range(len(df)), df['Nuclide'])
    plt.xlabel('Abundance')
    plt.title('Nuclear Abundance Distribution')
    plt.gca().invert_yaxis()
    plt.tight_layout()

def save_plot(filename):
    """
    Save the current plot to a file.
    
    Parameters:
    filename (str): Path where the plot should be saved
    """
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
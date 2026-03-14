import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class DataProcessor:
    def __init__(self):
        self.processed_data = {}
    
    def process_simulation_output(self, raw_data):
        """Process raw simulation output into structured data"""
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(raw_data)
        
        # Calculate derived quantities
        df['total_yield'] = df['yield'].sum()
        df['normalized_yield'] = df['yield'] / df['total_yield']
        
        # Add cumulative yield column
        df['cumulative_yield'] = df['normalized_yield'].cumsum()
        
        self.processed_data = df
        return df
    
    def generate_statistics(self):
        """Generate statistical summaries of processed data"""
        if self.processed_data.empty:
            return {}
        
        stats = {
            'mean_yield': self.processed_data['yield'].mean(),
            'max_yield': self.processed_data['yield'].max(),
            'min_yield': self.processed_data['yield'].min(),
            'total_elements': len(self.processed_data),
            'total_yield': self.processed_data['total_yield'].iloc[0]
        }
        
        return stats

def format_results(raw_results):
    """Format raw simulation results into a standardized dictionary"""
    processor = DataProcessor()
    processed_df = processor.process_simulation_output(raw_results)
    
    # Convert DataFrame to dictionary format
    formatted = {
        'data': processed_df.to_dict('records'),
        'statistics': processor.generate_statistics(),
        'metadata': {
            'timestamp': pd.Timestamp.now().isoformat(),
            'processed': True
        }
    }
    
    return formatted

def export_report(results, filename):
    """Export formatted results to a report file"""
    # Create summary statistics
    stats = results['statistics']
    
    # Generate basic report content
    report_content = f"""NuclearGoldForge Simulation Report
=================================

Timestamp: {results['metadata']['timestamp']}
Total Elements Simulated: {stats['total_elements']}

Yield Statistics:
- Mean Yield: {stats['mean_yield']:.6f}
- Maximum Yield: {stats['max_yield']:.6f}
- Minimum Yield: {stats['min_yield']:.6f}
- Total Yield: {stats['total_yield']:.6f}

Data Points: {len(results['data'])}
"""

    # Save to file
    with open(filename, 'w') as f:
        f.write(report_content)
    
    return filename
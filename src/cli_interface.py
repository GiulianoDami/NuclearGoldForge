import argparse
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.simulation import run_simulation
from src.report_generator import generate_report

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="NuclearGoldForge: Simulate r-process nucleosynthesis"
    )
    
    parser.add_argument(
        '--neutrons',
        type=int,
        default=50,
        help='Number of neutrons to simulate (default: 50)'
    )
    
    parser.add_argument(
        '--time',
        type=float,
        default=1.0,
        help='Simulation time in seconds (default: 1.0)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='report.pdf',
        help='Output report filename (default: report.pdf)'
    )
    
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Generate and save plots'
    )
    
    return parser.parse_args()

def main():
    """Main function to run the CLI interface."""
    args = parse_args()
    
    try:
        # Run the simulation
        print("Running r-process simulation...")
        results = run_simulation(args.neutrons, args.time)
        
        # Generate report
        print("Generating report...")
        generate_report(results, args.output, args.plot)
        
        print(f"Report saved to {args.output}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
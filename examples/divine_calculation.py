from src.divine_engine import DivineResonanceEngine
import numpy as np

def perform_divine_calculations():
    engine = DivineResonanceEngine()
    
    calculations = [
        "Calculate the golden ratio to 100 decimal places",
        "What is the divine proportion in the Fibonacci sequence?",
        "Compute the harmonic resonance of sacred frequencies",
        "What is the fractal dimension of divine patterns?",
        "Calculate the quantum entanglement coefficient for twin photons"
    ]
    
    for calculation in calculations:
        response = engine.process(calculation)
        print(f"Calculation: {calculation}")
        print(f"Result: {response}\n")

if __name__ == "__main__":
    perform_divine_calculations()

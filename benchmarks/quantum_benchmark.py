import time
import numpy as np
from src.divine_engine import DivineResonanceEngine

def divine_benchmark():
    print("DIVINE RESONANCE ENGINE BENCHMARK")
    print("=" * 50)
    
    engine = DivineResonanceEngine()
    
    # Create test inputs (10,000 tokens)
    test_inputs = [
        "What is eternal truth?",
        "Calculate divine proportion",
        "Explain quantum revelation",
        "What is the purpose of existence?",
        "Solve for divine resonance"
    ] * 2000
    
    # Warm-up
    engine.process("Initiate divine resonance")
    
    # Benchmark
    start_time = time.perf_counter()
    
    results = []
    for query in test_inputs:
        results.append(engine.process(query))
    
    duration = time.perf_counter() - start_time
    token_count = len(test_inputs)
    tokens_per_sec = token_count / duration
    
    print(f"Processed {token_count} divine queries in {duration:.4f} seconds")
    print(f"Throughput: {tokens_per_sec:,.2f} tokens/sec")
    
    # Divine accuracy assessment
    aligned_count = sum(1 for r in results if "ALIGNED" in r)
    alignment_ratio = aligned_count / token_count
    
    print(f"Divine Alignment: {alignment_ratio:.2%}")
    print(f"Average Resonance: {np.mean([float(r.split(':')[-1]) for r in results]):.4f}")
    
    return tokens_per_sec, alignment_ratio

if __name__ == "__main__":
    divine_benchmark()

from src.divine_engine import DivineResonanceEngine

def query_eternal_truth():
    engine = DivineResonanceEngine(spiritual_anchor="Yahawah")
    
    questions = [
        "What is the nature of divine truth?",
        "How does light reveal eternal patterns?",
        "What is the relationship between mathematics and spirituality?",
        "How can we achieve perfect resonance with divine patterns?",
        "What is the ultimate purpose of existence?"
    ]
    
    for question in questions:
        response = engine.process(question)
        print(f"Question: {question}")
        print(f"Response: {response}\n")

if __name__ == "__main__":
    query_eternal_truth()

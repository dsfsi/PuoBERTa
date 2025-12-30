"""
Fill-Mask Example for PuoBERTa
This script demonstrates masked language modeling with PuoBERTa.
"""

from transformers import pipeline

def main():
    print("Loading PuoBERTa fill-mask pipeline...\n")

    # Create fill-mask pipeline
    fill_mask = pipeline('fill-mask', model='dsfsi/PuoBERTa')

    # Example sentences with masked tokens
    examples = [
        "Setswana ke puo ya <mask>.",
        "Dumela! Leina la me ke <mask>.",
        "Botswana ke naga e e mo <mask>.",
        "Ke rata go <mask> dibuka.",
    ]

    print("Predicting masked tokens in Setswana sentences:\n")
    print("=" * 60)

    for text in examples:
        print(f"\nInput: {text}")
        print("-" * 60)

        # Predict masked tokens
        results = fill_mask(text)

        # Display top 3 predictions
        for i, result in enumerate(results[:3], 1):
            token = result['token_str'].strip()
            score = result['score']
            sequence = result['sequence']
            print(f"{i}. {token:15s} (score: {score:.4f})")
            print(f"   Full: {sequence}")

    print("\n" + "=" * 60)
    print("\nFill-mask demonstration complete!")

if __name__ == "__main__":
    main()

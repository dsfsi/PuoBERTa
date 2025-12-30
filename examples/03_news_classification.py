"""
News Classification Example using PuoBERTa-News
This script demonstrates how to use the pre-trained news classification model.
"""

from transformers import pipeline

def main():
    print("Loading PuoBERTa-News classification model...\n")

    # Load the news classification pipeline
    classifier = pipeline('text-classification', model='dsfsi/PuoBERTa-News')

    # Example Setswana news texts
    news_examples = [
        "Palamente e ne e kopana gompieno go tlotla melao e mesha ya ikonomi.",
        "Bana ba sekolo sa poraemari ba fenya tuelo ya bolo ya dinao.",
        "Ngaka e e tumileng e buile ka botlhokwa jwa boitekanelo.",
        "Moporesidente o ne a bua ka tiragatso ya naga kwa ntle.",
    ]

    print("Classifying Setswana news articles:\n")
    print("=" * 80)

    for i, text in enumerate(news_examples, 1):
        print(f"\nExample {i}:")
        print(f"Text: {text}")
        print("-" * 80)

        # Classify the text
        result = classifier(text)

        # Display results
        for pred in result:
            label = pred['label']
            score = pred['score']
            print(f"Category: {label:30s} Confidence: {score:.4f}")

    print("\n" + "=" * 80)
    print("\nNews classification demonstration complete!")
    print("\nNote: The model categorizes news into 10 categories:")
    print("  - Politics, Education, Economy/Business, Health, Sports,")
    print("  - Society, Environment, Technology, Culture, and Other")

if __name__ == "__main__":
    main()

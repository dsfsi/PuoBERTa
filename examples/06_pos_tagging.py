"""
Part-of-Speech (POS) Tagging Example using PuoBERTa-POS
This script demonstrates how to identify grammatical roles of words in Setswana text.
"""

from transformers import pipeline

def main():
    print("Loading PuoBERTa-POS model...\n")

    # Load the POS tagging pipeline
    pos_tagger = pipeline(
        'token-classification',
        model='dsfsi/PuoBERTa-POS',
        aggregation_strategy="simple"
    )

    # Example Setswana sentences
    examples = [
        "Ke rata go bala dibuka.",
        "Ngwana o ja dijo tse di monate.",
        "Bana ba tshameka kwa sekolong.",
        "Mosadi yo motle o apara hempe e tshweu.",
        "Re tla ya kwa toropong kamoso.",
    ]

    print("Analyzing part-of-speech tags for Setswana sentences:\n")
    print("=" * 80)

    for i, text in enumerate(examples, 1):
        print(f"\nExample {i}: {text}")
        print("-" * 80)

        # Get POS tags
        pos_tags = pos_tagger(text)

        # Display results in a formatted table
        print(f"{'Word':<20s} {'POS Tag':<10s} {'Confidence':<10s}")
        print("-" * 45)

        for tag in pos_tags:
            word = tag['word']
            pos = tag['entity_group']
            score = tag['score']
            print(f"{word:<20s} {pos:<10s} {score:.4f}")

    print("\n" + "=" * 80)
    print("\nCommon POS Tags (Universal Dependencies):")
    print("  NOUN   - Nouns (names of things, people, places)")
    print("  VERB   - Verbs (actions, states)")
    print("  ADJ    - Adjectives (descriptive words)")
    print("  ADV    - Adverbs (modify verbs, adjectives)")
    print("  PRON   - Pronouns (I, you, he, she, it)")
    print("  DET    - Determiners (the, a, this)")
    print("  ADP    - Adpositions (prepositions, postpositions)")
    print("  CONJ   - Conjunctions (and, or, but)")
    print("  NUM    - Numbers")
    print("  PUNCT  - Punctuation")
    print("\nPOS tagging demonstration complete!")

if __name__ == "__main__":
    main()

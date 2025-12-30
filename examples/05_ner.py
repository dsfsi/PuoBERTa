"""
Named Entity Recognition (NER) Example using PuoBERTa-NER
This script demonstrates how to extract named entities from Setswana text.
"""

from transformers import pipeline

def main():
    print("Loading PuoBERTa-NER model...\n")

    # Load the NER pipeline
    ner = pipeline(
        'ner',
        model='dsfsi/PuoBERTa-NER',
        aggregation_strategy="simple"
    )

    # Example Setswana texts with named entities
    examples = [
        "Vukosi Marivate o tswa kwa University of Pretoria.",
        "Botswana ke naga e e mo Afrika Borwa.",
        "Ngaka Dr. Seretse o bereka kwa Gaborone.",
        "Setswana se buiwa mo Botswana le Afrika Borwa.",
        "Moporesidente Mokgweetsi Masisi o ne a etela Maun ka Moranang.",
    ]

    print("Extracting named entities from Setswana text:\n")
    print("=" * 80)

    for i, text in enumerate(examples, 1):
        print(f"\nExample {i}:")
        print(f"Text: {text}")
        print("-" * 80)

        # Extract entities
        entities = ner(text)

        if entities:
            print(f"Found {len(entities)} entities:")
            for entity in entities:
                word = entity['word']
                entity_type = entity['entity_group']
                score = entity['score']
                start = entity['start']
                end = entity['end']

                print(f"  • {word:30s} [{entity_type:4s}] (confidence: {score:.4f})")
        else:
            print("  No entities found.")

    print("\n" + "=" * 80)
    print("\nEntity Types:")
    print("  PER  - Person names")
    print("  LOC  - Locations (countries, cities, places)")
    print("  ORG  - Organizations (companies, institutions)")
    print("  DATE - Dates and temporal expressions")
    print("\nNER demonstration complete!")

if __name__ == "__main__":
    main()

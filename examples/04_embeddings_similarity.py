"""
Text Similarity using PuoBERTa Embeddings
This script demonstrates how to compute semantic similarity between Setswana texts.
"""

from transformers import RobertaTokenizer, RobertaModel
import torch
from torch.nn.functional import cosine_similarity

def get_sentence_embedding(text, tokenizer, model):
    """Extract sentence embedding from the [CLS] token."""
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    with torch.no_grad():
        outputs = model(**inputs)

    # Use [CLS] token embedding as sentence representation
    cls_embedding = outputs.last_hidden_state[:, 0, :]
    return cls_embedding

def main():
    print("Loading PuoBERTa for semantic similarity...\n")

    # Load model and tokenizer
    model_name = 'dsfsi/PuoBERTa'
    tokenizer = RobertaTokenizer.from_pretrained(model_name)
    model = RobertaModel.from_pretrained(model_name)

    # Example Setswana sentences
    sentences = [
        "Ke rata go bala dibuka.",
        "Ke itumelela go buisa dibuka.",
        "Botswana ke naga e ntle.",
        "Setswana ke puo e ntle.",
        "Ke ja dijo tsa Setswana.",
    ]

    print("Computing semantic similarity between Setswana sentences:\n")
    print("=" * 80)

    # Compute embeddings for all sentences
    embeddings = []
    for sentence in sentences:
        embedding = get_sentence_embedding(sentence, tokenizer, model)
        embeddings.append(embedding)

    # Compare first sentence with all others
    reference_idx = 0
    reference_text = sentences[reference_idx]
    reference_embedding = embeddings[reference_idx]

    print(f"Reference sentence: '{reference_text}'\n")
    print("Similarity scores with other sentences:")
    print("-" * 80)

    for i, (sentence, embedding) in enumerate(zip(sentences, embeddings)):
        if i == reference_idx:
            continue

        # Compute cosine similarity
        similarity = cosine_similarity(reference_embedding, embedding, dim=1).item()

        print(f"{similarity:.4f}  |  {sentence}")

    print("\n" + "=" * 80)

    # Pairwise similarity matrix
    print("\nPairwise similarity matrix:")
    print("-" * 80)

    n = len(sentences)
    print(f"{'':40s}", end="")
    for i in range(n):
        print(f"S{i+1:2d}  ", end="")
    print()

    for i in range(n):
        print(f"{sentences[i][:37]:37s}...", end="")
        for j in range(n):
            sim = cosine_similarity(embeddings[i], embeddings[j], dim=1).item()
            print(f"{sim:.2f} ", end="")
        print()

    print("\n" + "=" * 80)
    print("\nSemantic similarity demonstration complete!")

if __name__ == "__main__":
    main()

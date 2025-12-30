"""
Basic Usage Example for PuoBERTa
This script demonstrates how to load and use PuoBERTa for basic tasks.
"""

from transformers import RobertaTokenizer, RobertaModel
import torch

def main():
    print("Loading PuoBERTa model and tokenizer...")

    # Load model and tokenizer
    model_name = 'dsfsi/PuoBERTa'
    tokenizer = RobertaTokenizer.from_pretrained(model_name)
    model = RobertaModel.from_pretrained(model_name)

    print(f"Model loaded successfully: {model_name}\n")

    # Example Setswana text
    text = "Dumela! Ke a leboga. Setswana ke puo e ntle."

    print(f"Input text: {text}\n")

    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    print(f"Tokenized inputs:")
    print(f"  Input IDs shape: {inputs['input_ids'].shape}")
    print(f"  Attention mask shape: {inputs['attention_mask'].shape}\n")

    # Get model outputs
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract embeddings
    last_hidden_state = outputs.last_hidden_state

    print(f"Model outputs:")
    print(f"  Last hidden state shape: {last_hidden_state.shape}")
    print(f"  Embedding dimension: {last_hidden_state.shape[-1]}\n")

    # Get the [CLS] token embedding (sentence representation)
    cls_embedding = last_hidden_state[:, 0, :]
    print(f"Sentence embedding (CLS token) shape: {cls_embedding.shape}")

    print("\nSuccess! PuoBERTa is ready to use for your Setswana NLP tasks.")

if __name__ == "__main__":
    main()

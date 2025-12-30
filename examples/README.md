# PuoBERTa Usage Examples

This directory contains practical examples demonstrating how to use PuoBERTa for various NLP tasks in Setswana.

## Prerequisites

Install the required dependencies:

```bash
pip install transformers torch
```

## Examples

### 1. Basic Usage (`01_basic_usage.py`)

Learn the fundamentals of loading and using PuoBERTa:
- Loading the model and tokenizer
- Tokenizing Setswana text
- Extracting embeddings
- Understanding model outputs

```bash
python examples/01_basic_usage.py
```

### 2. Fill-Mask (`02_fill_mask.py`)

Predict masked words in Setswana sentences:
- Masked language modeling
- Word prediction
- Exploring the model's understanding of Setswana

```bash
python examples/02_fill_mask.py
```

### 3. News Classification (`03_news_classification.py`)

Classify Setswana news articles using the pre-trained PuoBERTa-News model:
- Text classification
- News categorization
- 10 category prediction

```bash
python examples/03_news_classification.py
```

### 4. Semantic Similarity (`04_embeddings_similarity.py`)

Compute semantic similarity between Setswana texts:
- Sentence embeddings
- Cosine similarity
- Semantic search applications

```bash
python examples/04_embeddings_similarity.py
```

### 5. Named Entity Recognition (`05_ner.py`)

Extract named entities from Setswana text using PuoBERTa-NER:
- Person names (PER)
- Locations (LOC)
- Organizations (ORG)
- Dates (DATE)

```bash
python examples/05_ner.py
```

### 6. Part-of-Speech Tagging (`06_pos_tagging.py`)

Identify grammatical roles of words using PuoBERTa-POS:
- Universal Dependencies POS tags
- Word-level grammatical analysis
- Linguistic annotation

```bash
python examples/06_pos_tagging.py
```

## Running All Examples

To run all examples in sequence:

```bash
for script in examples/*.py; do
    echo "Running $script..."
    python "$script"
    echo ""
done
```

## Next Steps

After exploring these examples, you can:

1. **Fine-tune for your task**: Use the classification example as a template for training on your own data
2. **Build applications**: Integrate PuoBERTa into web apps, chatbots, or analysis pipelines
3. **Explore downstream models**: Try [PuoBERTa-NER](https://huggingface.co/dsfsi/PuoBERTa-NER) or [PuoBERTa-POS](https://huggingface.co/dsfsi/PuoBERTa-POS)
4. **Contribute**: Share your own examples by opening a pull request

## Resources

- [Main README](../README.md)
- [HuggingFace Model](https://huggingface.co/dsfsi/PuoBERTa)
- [Interactive Demo](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace)
- [Research Paper](https://arxiv.org/abs/2310.09141)

## Need Help?

- Check the [main README](../README.md) for detailed documentation
- Try the [interactive demo](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace)
- Refer to the [Transformers documentation](https://huggingface.co/docs/transformers/)
- Open an issue on GitHub

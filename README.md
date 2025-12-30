# PuoBERTa: A Curated Setswana Language Model

[![Zenodo doi badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.8434795-blue.svg)](https://doi.org/10.5281/zenodo.8434795) [![arXiv](https://img.shields.io/badge/arXiv-2310.09141-b31b1b.svg)](https://arxiv.org/abs/2310.09141) [![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-Model-yellow)](https://huggingface.co/dsfsi/PuoBERTa) [![HuggingFace Space](https://img.shields.io/badge/%F0%9F%A4%97-Demo-orange)](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace)

A RoBERTa-based language model specially designed for Setswana, trained on the PuoData dataset for accurate and culturally relevant NLP applications.

**Try it now:** [Interactive Demo](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace) | [Model on HuggingFace](https://huggingface.co/dsfsi/PuoBERTa) | [Paper](https://arxiv.org/abs/2310.09141)

Give Feedback 📑: [DSFSI Resource Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSf7S36dyAUPx2egmXbFpnTBuzoRulhL5Elu-N1eoMhaO7v10w/formResponse)

---

## Table of Contents
- [Quick Start](#quick-start)
- [Model Details](#model-details)
- [Installation](#installation)
- [Usage Examples](#usage-examples)
- [Downstream Performance](#downstream-performance)
- [Pre-Training Dataset](#pre-training-dataset)
- [Citation](#citation-information)
- [Contributing](#contributing)
- [Contact](#model-card-contact)

---

## Quick Start

### Try Online (No Installation Required)

Visit our [**Interactive Demo**](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace) to try all PuoBERTa models in your browser:
- **Fill-Mask**: Predict masked words in Setswana text
- **News Classification**: Categorize Setswana news articles
- **Named Entity Recognition (NER)**: Extract entities from text
- **Part-of-Speech (POS) Tagging**: Identify grammatical roles of words

### Quick Start with Code

Get started with PuoBERTa in just a few lines of code:

```python
from transformers import pipeline

# Use the fill-mask pipeline
fill_mask = pipeline('fill-mask', model='dsfsi/PuoBERTa')
result = fill_mask("Setswana ke puo ya <mask>.")
print(result)
```

For more detailed examples, check out the [examples directory](examples/) with ready-to-run scripts for various use cases.

---

## Model Details


### Model Description

This is a masked language model trained on Setswana corpora, making it a valuable tool for a range of downstream applications from translation to content creation. It's powered by the PuoData dataset to ensure accuracy and cultural relevance.

- **Developed by:** Vukosi Marivate ([@vukosi](https://huggingface.co/@vukosi)), Moseli Mots'Oehli ([@MoseliMotsoehli](https://huggingface.co/@MoseliMotsoehli)) , Valencia Wagner, Richard Lastrucci and Isheanesu Dzingirai
- **Model type:** RoBERTa Model
- **Language(s) (NLP):** Setswana (BCP-47: `tn`)
- **License:** CC BY 4.0
- **Training Dataset:** [PuoData](https://github.com/dsfsi/PuoData)

---

## Installation

Install the required dependencies:

```bash
pip install transformers torch
```

For fine-tuning and advanced usage:
```bash
pip install transformers torch datasets accelerate
```

---

## Usage Examples

### 1. Masked Language Modeling (Fill-Mask)

Use PuoBERTa to predict masked words in Setswana text:

```python
from transformers import pipeline

# Create a fill-mask pipeline
fill_mask = pipeline('fill-mask', model='dsfsi/PuoBERTa')

# Predict masked tokens
text = "Setswana ke puo ya <mask>."
results = fill_mask(text)

for result in results:
    print(f"Token: {result['token_str']}, Score: {result['score']:.4f}")
```

### 2. Getting Text Embeddings

Extract contextual embeddings for Setswana text:

```python
from transformers import RobertaTokenizer, RobertaModel
import torch

# Load model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')
model = RobertaModel.from_pretrained('dsfsi/PuoBERTa')

# Encode text
text = "Dumela! Ke a leboga."
inputs = tokenizer(text, return_tensors="pt")

# Get embeddings
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state

print(f"Embeddings shape: {embeddings.shape}")
```

### 3. Fine-tuning for Text Classification

Fine-tune PuoBERTa for downstream tasks like news categorization:

```python
from transformers import RobertaForSequenceClassification, Trainer, TrainingArguments
from transformers import RobertaTokenizer

# Load model for classification (e.g., 10 news categories)
model = RobertaForSequenceClassification.from_pretrained(
    'dsfsi/PuoBERTa',
    num_labels=10
)
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')

# Prepare your dataset
# train_dataset, eval_dataset = ...

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Create trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

# Train the model
trainer.train()
```

### 4. Using Pre-trained Downstream Models

We provide ready-to-use models for specific tasks:

```python
from transformers import pipeline

# News categorization (10 categories)
news_classifier = pipeline('text-classification', model='dsfsi/PuoBERTa-News')
result = news_classifier("Palamente e ne e kopana gompieno go tlotla melao e mesha.")
print(f"Category: {result[0]['label']}, Score: {result[0]['score']:.4f}")

# Named Entity Recognition (PER, LOC, ORG, DATE)
ner = pipeline('ner', model='dsfsi/PuoBERTa-NER', aggregation_strategy="simple")
entities = ner("Vukosi Marivate o tswa kwa University of Pretoria.")
for entity in entities:
    print(f"{entity['word']}: {entity['entity_group']} ({entity['score']:.4f})")

# Part-of-Speech Tagging
pos_tagger = pipeline('token-classification', model='dsfsi/PuoBERTa-POS', aggregation_strategy="simple")
pos_tags = pos_tagger("Ke rata go bala dibuka.")
for tag in pos_tags:
    print(f"{tag['word']}: {tag['entity_group']}")
```

### Downstream Models

- **News Categorization:** [dsfsi/PuoBERTa-News](https://huggingface.co/dsfsi/PuoBERTa-News)
- **Named Entity Recognition:** [dsfsi/PuoBERTa-NER](https://huggingface.co/dsfsi/PuoBERTa-NER)
- **Part-of-Speech Tagging:** [dsfsi/PuoBERTa-POS](https://huggingface.co/dsfsi/PuoBERTa-POS)

--- 

## Downstream Performance

PuoBERTa has been evaluated on multiple downstream tasks and shows competitive performance against multilingual models while being specifically optimized for Setswana.

### Daily News Dikgang (News Categorization)

Performance on the Setswana news categorization task using the Daily News Dikgang dataset. Learn more about the dataset in the [Dataset Folder](daily-news-dikgang).

| **Model**                   | **5-fold Cross Validation F1**       | **Test F1**       |
|-----------------------------|--------------------------------------|-------------------|
| Logistic Regression + TFIDF | 60.1                                 | 56.2              |
| NCHLT TSN RoBERTa           | 64.7                                 | 60.3              |
| PuoBERTa                    | **63.8**                             | **62.9**          |
| PuoBERTaJW300               | 66.2                                 | 65.4              |

**Pre-trained model:** [dsfsi/PuoBERTa-News](https://huggingface.co/dsfsi/PuoBERTa-News)

### MasakhaPOS (Part-of-Speech Tagging)

Performance on the MasakhaPOS downstream task for Setswana.

| Model | Test Performance |
|---|---|
| **Multilingual Models** |  |
| AfroLM | 83.8 |
| AfriBERTa | 82.5 |
| AfroXLMR-base | 82.7 |
| AfroXLMR-large | 83.0 |
| **Monolingual Models** |  |
| NCHLT TSN RoBERTa | 82.3 |
| PuoBERTa | **83.4** |
| PuoBERTa+JW300 | 84.1 |

**Pre-trained model:** [dsfsi/PuoBERTa-POS](https://huggingface.co/dsfsi/PuoBERTa-POS)

### MasakhaNER (Named Entity Recognition)

Performance on the MasakhaNER downstream task for Setswana.

| Model | Test Performance (f1 score) |
|---|---|
| **Multilingual Models** |  |
| AfriBERTa | 83.2 |
| AfroXLMR-base | 87.7 |
| AfroXLMR-large | 89.4 |
| **Monolingual Models** |  |
| NCHLT TSN RoBERTa | 74.2 |
| PuoBERTa | **78.2** |
| PuoBERTa+JW300 | 80.2 |

**Pre-trained model:** [dsfsi/PuoBERTa-NER](https://huggingface.co/dsfsi/PuoBERTa-NER)

---

## Pre-Training Dataset

PuoBERTa was trained on **PuoData**, a large, curated corpus of Setswana text designed to ensure the model is well-trained and culturally attuned to the language.

**Access the dataset:**
- [GitHub Repository](https://github.com/dsfsi/PuoData)
- [HuggingFace Dataset](https://huggingface.co/datasets/dsfsi/PuoData)
- [Research Paper](https://arxiv.org/abs/2310.09141)

The dataset includes diverse sources of Setswana text to provide comprehensive language coverage for robust model training.

---

## Citation Information

Bibtex Reference

```
@inproceedings{marivate2023puoberta,
  title   = {PuoBERTa: Training and evaluation of a curated language model for Setswana},
  author  = {Vukosi Marivate and Moseli Mots'Oehli and Valencia Wagner and Richard Lastrucci and Isheanesu Dzingirai},
  year    = {2023},
  booktitle= {Artificial Intelligence Research. SACAIR 2023. Communications in Computer and Information Science},
  url= {https://link.springer.com/chapter/10.1007/978-3-031-49002-6_17},
  keywords = {NLP},
  preprint_url = {https://arxiv.org/abs/2310.09141},
  dataset_url = {https://github.com/dsfsi/PuoBERTa},
  software_url = {https://huggingface.co/dsfsi/PuoBERTa}
}
```

## Contributing

We welcome contributions from the community! Whether you want to:
- Add new examples or improve documentation
- Report bugs or suggest features
- Share your fine-tuned models
- Contribute datasets or use cases

Please see our [Contributing Guidelines](CONTRIBUTING.md) for detailed information on how to get started.

Quick links:
- [Open an issue](https://github.com/dsfsi/PuoBERTa/issues)
- [Submit a pull request](https://github.com/dsfsi/PuoBERTa/pulls)
- [Give feedback](https://docs.google.com/forms/d/e/1FAIpQLSf7S36dyAUPx2egmXbFpnTBuzoRulhL5Elu-N1eoMhaO7v10w/formResponse)

## Model Card Authors

Vukosi Marivate

## Model Card Contact

For more details, reach out or check our [website](https://dsfsi.github.io/).

Email: vukosi.marivate@cs.up.ac.za

**Enjoy exploring Setswana through AI!**

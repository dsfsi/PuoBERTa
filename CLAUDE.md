# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PuoBERTa is a RoBERTa-based language model for Setswana, trained on the PuoData dataset. This repository contains the model documentation, downstream task datasets, and development infrastructure.

## Critical Resources

**Try the Models Interactively:**
- **Interactive Demo Space**: https://huggingface.co/spaces/dsfsi/PuoBERTaSpace
  - Try all four models in your browser (no installation required)
  - Available models in the Space:
    - Fill-Mask: Predict masked words in Setswana text
    - News Classification: Categorize news articles (10 categories)
    - Named Entity Recognition (NER): Extract entities (PER, LOC, ORG, DATE)
    - Part-of-Speech (POS) Tagging: Identify grammatical roles

**Model Hub:**
- Base Model: https://huggingface.co/dsfsi/PuoBERTa
- News Classification: https://huggingface.co/dsfsi/PuoBERTa-News
- NER: https://huggingface.co/dsfsi/PuoBERTa-NER
- POS Tagging: https://huggingface.co/dsfsi/PuoBERTa-POS

**Documentation:**
- Research Paper: https://arxiv.org/abs/2310.09141
- Training Dataset (PuoData): https://github.com/dsfsi/PuoData

## Development Commands

### Environment Setup
```bash
# Create conda environment (recommended)
make create_environment

# Install dependencies
make requirements

# Test environment
make test_environment
```

### Code Quality
```bash
# Lint code with flake8
make lint

# Clean compiled Python files
make clean
```

### Data Processing
```bash
# Process datasets (requires src/data/make_dataset.py)
make data
```

### AWS S3 Sync (Optional)
```bash
# Upload data to S3
make sync_data_to_s3

# Download data from S3
make sync_data_from_s3
```

## Repository Structure

This repository follows the Cookiecutter Data Science project structure:

- **daily-news-dikgang/**: News categorization dataset for Setswana
  - Contains train/dev/test splits in TSV format
  - Columns: `title`, `text`, `orig_label`, `label`
  - 10 news categories for classification tasks
  - See `DataStatementPuoBERTaDailyNewsDikgang.pdf` for full documentation

- **data/**: Excluded from git (see .gitignore)
  - Expected structure: `raw/` and `processed/` subdirectories

- **src/**: Source code package (if present)
  - Package name: `src` (version 0.1.0)
  - Installable via `pip install -e .`

## Model Information

**PuoBERTa** is designed for:
- Masked language modeling in Setswana
- Fine-tuning for downstream tasks (NER, POS tagging, classification)

**Hosted Model:**
The model is hosted on HuggingFace: https://huggingface.co/dsfsi/PuoBERTa

**Downstream Task Models:**
- News Categorization: https://huggingface.co/dsfsi/PuoBERTa-News
- Named Entity Recognition: https://huggingface.co/dsfsi/PuoBERTa-NER
- Part-of-Speech Tagging: https://huggingface.co/dsfsi/PuoBERTa-POS

### Usage Examples

**Basic Model Loading:**
```python
from transformers import RobertaTokenizer, RobertaModel

# Load model and tokenizer
model = RobertaModel.from_pretrained('dsfsi/PuoBERTa')
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')

# Tokenize and encode text
text = "Dumela! Ke a leboga."
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
```

**Masked Language Modeling:**
```python
from transformers import pipeline

# Create fill-mask pipeline
fill_mask = pipeline('fill-mask', model='dsfsi/PuoBERTa')

# Predict masked tokens
result = fill_mask("Setswana ke puo ya <mask>.")
print(result)
```

**Fine-tuning for Classification:**
```python
from transformers import RobertaForSequenceClassification, RobertaTokenizer, Trainer, TrainingArguments

# Load model for classification
model = RobertaForSequenceClassification.from_pretrained(
    'dsfsi/PuoBERTa',
    num_labels=10  # e.g., for news categorization
)
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')

# Your training code here
```

**Using Downstream Models:**
```python
from transformers import pipeline

# News Classification
news_classifier = pipeline('text-classification', model='dsfsi/PuoBERTa-News')
result = news_classifier("Palamente e ne e kopana...")

# Named Entity Recognition
ner = pipeline('ner', model='dsfsi/PuoBERTa-NER', aggregation_strategy="simple")
entities = ner("Vukosi Marivate o tswa kwa University of Pretoria.")

# Part-of-Speech Tagging
pos_tagger = pipeline('token-classification', model='dsfsi/PuoBERTa-POS', aggregation_strategy="simple")
pos_tags = pos_tagger("Ke rata go bala dibuka.")
```

**Installation:**
```bash
pip install transformers torch
```

## Dataset Guidelines

**PuoData - Training Dataset:**
PuoBERTa was trained on the PuoData dataset, a large corpus of Setswana text. For details on the training data composition, methodology, and statistics, see:
- Repository: https://github.com/dsfsi/PuoData
- Paper: https://arxiv.org/abs/2310.09141

**Daily News Dikgang - Downstream Task Dataset:**
When working with the Daily News Dikgang dataset in this repository:
- Data is in Setswana language (BCP-47: `tn`)
- Source: Botswana Government Daily News (https://dailynews.gov.bw)
- License: CC-BY-SA-4.0
- Categories: politics, education, economy_business_and_finance, society, etc.
- Refer to `data_statement.md` template for documenting new datasets

## License

- Model: CC BY 4.0
- Daily News Dikgang Dataset: CC-BY-SA-4.0

## Citation

```bibtex
@inproceedings{marivate2023puoberta,
  title   = {PuoBERTa: Training and evaluation of a curated language model for Setswana},
  author  = {Vukosi Marivate and Moseli Mots'Oehli and Valencia Wagner and Richard Lastrucci and Isheanesu Dzingirai},
  year    = {2023},
  booktitle= {Artificial Intelligence Research. SACAIR 2023. Communications in Computer and Information Science},
  url= {https://link.springer.com/chapter/10.1007/978-3-031-49002-6_17}
}
```

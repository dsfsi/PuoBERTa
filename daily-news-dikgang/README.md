# Daily News Dikgang Dataset

[![arXiv](https://img.shields.io/badge/arXiv-2310.09141-b31b1b.svg)](https://arxiv.org/abs/2310.09141) [![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE.data.md)

A Setswana news categorization dataset extracted from Botswana's Daily News (Dikgang).

Give Feedback 📑: [DSFSI Resource Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSf7S36dyAUPx2egmXbFpnTBuzoRulhL5Elu-N1eoMhaO7v10w/formResponse)

---

## Dataset Overview

The **Daily News Dikgang** dataset contains annotated, categorized news articles in Setswana from [Botswana Daily News](https://dailynews.gov.bw/news-list/srccategory/10).

**Key Features:**
- **Language:** Setswana (BCP-47: `tn`)
- **Source:** Botswana Government Daily News
- **Task:** News categorization (10 categories)
- **Format:** TSV (Tab-Separated Values)
- **Splits:** Train, Development, Test

See the [Data Statement](DataStatementPuoBERTaDailyNewsDikgang.pdf) for full details.

---

## Dataset Structure

### Files

| File | Description | Size |
|------|-------------|------|
| `daily-news-dikgang-train.tsv` | Training set | ~9.4 MB |
| `daily-news-dikgang-dev.tsv` | Development/validation set | ~1.2 MB |
| `daily-news-dikgang-test.tsv` | Test set | ~1.2 MB |

### Format

Each TSV file contains the following columns:

| Column | Description |
|--------|-------------|
| `title` | Article headline in Setswana |
| `text` | Article body in Setswana |
| `orig_label` | Original category label |
| `label` | Standardized category label |

### Categories

The dataset includes 10 news categories:
1. Politics
2. Education
3. Economy, Business, and Finance
4. Health
5. Sports
6. Society
7. Environment
8. Technology
9. Culture
10. Other

---

## Usage

### Loading the Dataset

**Python (pandas):**
```python
import pandas as pd

# Load the training data
train_df = pd.read_csv('daily-news-dikgang/daily-news-dikgang-train.tsv', sep='\t')
dev_df = pd.read_csv('daily-news-dikgang/daily-news-dikgang-dev.tsv', sep='\t')
test_df = pd.read_csv('daily-news-dikgang/daily-news-dikgang-test.tsv', sep='\t')

print(f"Training samples: {len(train_df)}")
print(f"Dev samples: {len(dev_df)}")
print(f"Test samples: {len(test_df)}")

# View first few rows
print(train_df.head())
```

**HuggingFace Datasets:**
```python
from datasets import load_dataset

# Load from local files
dataset = load_dataset('csv', data_files={
    'train': 'daily-news-dikgang/daily-news-dikgang-train.tsv',
    'dev': 'daily-news-dikgang/daily-news-dikgang-dev.tsv',
    'test': 'daily-news-dikgang/daily-news-dikgang-test.tsv'
}, delimiter='\t')

print(dataset)
```

### Fine-tuning PuoBERTa for News Classification

```python
from transformers import RobertaForSequenceClassification, RobertaTokenizer
from transformers import Trainer, TrainingArguments
import pandas as pd
from datasets import Dataset

# Load data
train_df = pd.read_csv('daily-news-dikgang/daily-news-dikgang-train.tsv', sep='\t')

# Create dataset
train_dataset = Dataset.from_pandas(train_df)

# Load model and tokenizer
model = RobertaForSequenceClassification.from_pretrained(
    'dsfsi/PuoBERTa',
    num_labels=10  # 10 news categories
)
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')

# Tokenize function
def tokenize_function(examples):
    return tokenizer(
        examples['text'],
        padding='max_length',
        truncation=True,
        max_length=512
    )

# Tokenize dataset
tokenized_dataset = train_dataset.map(tokenize_function, batched=True)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy='epoch',
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()
```

### Using the Pre-trained Model

Instead of training from scratch, use the ready-to-use fine-tuned model:

```python
from transformers import pipeline

# Load pre-trained news classifier
classifier = pipeline('text-classification', model='dsfsi/PuoBERTa-News')

# Classify news article
article = "Palamente e ne e kopana gompieno go tlotla melao e mesha."
result = classifier(article)

print(f"Category: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.4f}")
```

---

Disclaimer
-------
This dataset contains machine-readable data extracted from online news articles, from [https://dailynews.gov.bw/news-list/srccategory/10](https://dailynews.gov.bw/news-list/srccategory/10), provided by the Botswana Government. While efforts were made to ensure the accuracy and completeness of this data, there may be errors or discrepancies between the original publications and this dataset. No warranties, guarantees or representations are given in relation to the information contained in the dataset. The members of the Data Science for Societal Impact Research Group bear no responsibility and/or liability for any such errors or discrepancies in this dataset. The Botswana Government bears no responsibility and/or liability for any such errors or discrepancies in this dataset. It is recommended that users verify all information contained herein before making decisions based upon this information.

Authors
-------
- Vukosi Marivate - [@vukosi](https://twitter.com/vukosi)
- Valencia Wagner 

Citation
--------

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


Licences
-------
The license of the News Categorisation dataset is in CC-BY-SA-4.0.  the monolingual data have difference licenses depending on the news website license
* License for Data - [CC-BY-SA-4.0](LICENSE.data.md)

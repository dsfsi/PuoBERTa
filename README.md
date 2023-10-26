# PuoBerta: A curated Setswana Language Model

[![Zenodo doi badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.8434795-blue.svg)](https://doi.org/10.5281/zenodo.8434795) [![arXiv](https://img.shields.io/badge/arXiv-2310.09141-b31b1b.svg)](https://arxiv.org/abs/2310.09141) 🤗 [https://huggingface.co/dsfsi/PuoBERTa](https://huggingface.co/dsfsi/PuoBERTa)

A Roberta-based language model specially designed for Setswana, using the new PuoData dataset.

Give Feedback 📑: [DSFSI Resource Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSf7S36dyAUPx2egmXbFpnTBuzoRulhL5Elu-N1eoMhaO7v10w/formResponse)

## Model Details


### Model Description

This is a masked language model trained on Setswana corpora, making it a valuable tool for a range of downstream applications from translation to content creation. It's powered by the PuoData dataset to ensure accuracy and cultural relevance.

- **Developed by:** Vukosi Marivate ([@vukosi](https://huggingface.co/@vukosi)), Moseli Mots'Oehli ([@MoseliMotsoehli](https://huggingface.co/@MoseliMotsoehli)) , Valencia Wagner, Richard Lastrucci and Isheanesu Dzingirai
- **Model type:** RoBERTa Model
- **Language(s) (NLP):** Setswana
- **License:** CC BY 4.0


### Usage

Use this model filling in masks or finetune for downstream tasks. Here’s a simple example for masked prediction:

```python
from transformers import RobertaTokenizer, RobertaModel

# Load model and tokenizer
model = RobertaModel.from_pretrained('dsfsi/PuoBERTa')
tokenizer = RobertaTokenizer.from_pretrained('dsfsi/PuoBERTa')

```
 
### Downstream Use 

## Downstream Performance

### Daily News Dikgang

Learn more about the dataset in the [Dataset Folder](daily-news-dikgang)

| **Model**                   | **5-fold Cross Validation F1**       | **Test F1**       |
|-----------------------------|--------------------------------------|-------------------|
| Logistic Regression + TFIDF | 60.1                                 | 56.2              |
| NCHLT TSN RoBERTa           | 64.7                                 | 60.3              |
| PuoBERTa                    | **63.8**                             | **62.9**          |
| PuoBERTaJW300               | 66.2                                 | 65.4              |

Downstream News Categorisation model 🤗 [https://huggingface.co/dsfsi/PuoBERTa-News](https://huggingface.co/dsfsi/PuoBERTa-News)

### MasakhaPOS

Performance of models on the MasakhaPOS downstream task.

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

Downstream POS model 🤗 [https://huggingface.co/dsfsi/PuoBERTa-POS](https://huggingface.co/dsfsi/PuoBERTa-POS)

### MasakhaNER

Performance of models on the MasakhaNER downstream task.

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

Downstream NER model 🤗 [https://huggingface.co/dsfsi/PuoBERTa-NER](https://huggingface.co/dsfsi/PuoBERTa-NER)

## Pre-Training Dataset

We used the PuoData dataset, a rich source of Setswana text, ensuring that our model is well-trained and culturally attuned.

[Github](https://github.com/dsfsi/PuoData), 🤗 [https://huggingface.co/datasets/dsfsi/PuoData](https://huggingface.co/datasets/dsfsi/PuoData)

## Citation Information

Bibtex Reference

```
@inproceedings{marivate2023puoberta,
  title   = {PuoBERTa: Training and evaluation of a curated language model for Setswana},
  author  = {Vukosi Marivate and Moseli Mots'Oehli and Valencia Wagner and Richard Lastrucci and Isheanesu Dzingirai},
  year    = {2023},
  booktitle= {SACAIR 2023 (To Appear)},
  keywords = {NLP},
  preprint_url = {https://arxiv.org/abs/2310.09141},
  dataset_url = {https://github.com/dsfsi/PuoBERTa},
  software_url = {https://huggingface.co/dsfsi/PuoBERTa}
}
```

## Contributing

Your contributions are welcome! Feel free to improve the model.

## Model Card Authors

Vukosi Marivate

## Model Card Contact

For more details, reach out or check our [website](https://dsfsi.github.io/).

Email: vukosi.marivate@cs.up.ac.za

**Enjoy exploring Setswana through AI!**

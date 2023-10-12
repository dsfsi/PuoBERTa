---
license: cc-by-4.0
datasets:
- dsfsi/vukuzenzele-monolingual
- nchlt
language:
- tn
library_name: transformers
pipeline_tag: fill-mask
tags:
- masked langauge model
- setswana
---
# PuoBerta: A curated Setswana Language Model

A Roberta-based language model specially designed for Setswana, using the new PuoData dataset.

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


## Dataset

We used the PuoData dataset, a rich source of Setswana text, ensuring that our model is well-trained and culturally attuned.\\

## Contributing

Your contributions are welcome! Feel free to improve the model.

## Model Card Authors

Vukosi Marivate

## Model Card Contact

For more details, reach out or check our [website](https://dsfsi.github.io/).

Email: vukosi.marivate@cs.up.ac.za

**Enjoy exploring Setswana through AI!**

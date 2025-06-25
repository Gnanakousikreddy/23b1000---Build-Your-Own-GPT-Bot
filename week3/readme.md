# Week 3 

This repository expands on earlier efforts by introducing **pre-trained transformer models** for sentiment analysis and broader NLP tasks using the Hugging Face ecosystem. It includes both a milestone project and hands-on experiments with transformers.

---

## `milestone3` –  LSTM Sentiment Classifier with BERT Embeddings

 **Objective:**  
Build an **LSTM-based movie review sentiment classifier**, but instead of learning embeddings from scratch, use **pre-trained BERT embeddings** as input features.

**Model Details:**
- Used `google/bert_uncased_L-2_H-128_A-2` from Hugging Face to generate contextual word embeddings
- Replaced the `nn.Embedding` layer from `milestone2` with frozen BERT outputs
- **No additional hyperparameter tuning** was done — re-used the settings from `milestone2`
- Accuracy achieved: **83.66%**

 **Insight:**  
This setup shows strong performance without tuning. With further hyperparameter optimization, accuracy is expected to improve even more.

**Contents:**
- [`embedded_transformers_sentiment_analysis.ipynb`](./milestone3/embedded_transformers_sentiment_analysis.ipynb) — Full implementation using BERT + LSTM pipeline

---

## `hugging_face` –  Hugging Face Transformers Exploration

**Objective:**  
Explore the power of Hugging Face’s `transformers` library for common NLP tasks using **pre-trained models and tokenizers**.

**What’s Inside:**
- Using pipelines for **sentiment analysis**
- Experiments with **generative transformers** (e.g., text generation)
- Trials with **zero-shot classification**
- Hands-on with tokenization and model inference using `AutoTokenizer` and `AutoModel`

**Contents:**
- [`hugging_face.ipynb`](./hugging_face/hugging_face.ipynb) — Notebook covering all the above topics with working examples

---


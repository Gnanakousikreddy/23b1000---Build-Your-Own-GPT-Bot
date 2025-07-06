# 23b1000-Build-Your-Own-GPT-Bot

# 🧠 NLP Weekly Milestones 

This repository tracks a exploration of Natural Language Processing (NLP), starting from classical word embeddings and progressing toward deep learning with LSTMs and transformers. Each week focused on building and improving models for real-world NLP tasks.

---

## 📅 Week 1-2 – Top‑5 Similar Headline Retriever

In the first and second week, a system was built to retrieve the **top 5 most semantically similar news headlines** for a given input query. The approach used **pre-trained Word2Vec embeddings** trained on the Google News dataset. Each sentence was vectorized by averaging its word embeddings, and similarity was computed using **cosine distance**.

> ✅ Outcome: Functional and accurate semantic search engine for short text using classical word embeddings.

---

## 📅 Week 3-4 – LSTM-Based Sentiment Classifier (with Hyperparameter Tuning)

The third and fourth week focused on building a **binary sentiment classifier for movie reviews** using an **LSTM-based neural network**. The model included embedding layers, LSTM units, and fully connected layers. Extensive **hyperparameter tuning** was performed to adjust hidden sizes, layer depths, dropout rates, and sequence padding strategies.

> ✅ Outcome: Achieved an accuracy of **86.75%**, showing strong performance from a well-tuned LSTM model.

This week also included hands-on practice with **core PyTorch concepts**, including data loading, training pipelines, and simple RNNs for foundational understanding.

---

## 📅 Week 5 – BERT-Enhanced LSTM Sentiment Classifier

In the fifth week, the sentiment classifier was enhanced by using **pre-trained BERT embeddings** instead of a traditional trainable embedding layer. The architecture remained the same as in Week 3-4, and **no hyperparameter tuning** was performed—only the input representation was changed.

> ✅ Outcome: Achieved **83.66% accuracy** using BERT embeddings directly, indicating strong baseline performance. With tuning, the accuracy is expected to improve further.

This week also included exploration of **Hugging Face transformers**, experimenting with sentiment classification pipelines, **zero-shot learning**, **text generation**, and working directly with tokenizers and models.

---




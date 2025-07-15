#  Week 8 – Build Your Chatbot with Ollama

## Overview
This week’s milestone focuses on building a **Legal Adviser Bot** that provides legal guidance using **LLaMA** models served via **Ollama**. The tasks include setting up Ollama locally, exploring its usage via both the **Ollama API** and the **Ollama Python client**, and finally implementing a legal chatbot that generates answers based on Indian laws and regulations.

---
## Contents Covered

### Ollama Setup
- Learned about **Ollama** – an easy way to run large language models like LLaMA locally.
- Set up Ollama on the local machine.
- Tested the API and Python client.

### [Ollama Sample Usage](./ollama%20sample%20usage/)
- Used **HTTP API** with Python’s `requests` library.
- Used **Ollama Python client** to generate responses.

### [Milestone 6](./milestone6) – Legal Adviser Bot
- Built Bot using Python’s `requests` library : [legal_advisory_bot1.py](./milestone6/legal_advisory_bot1.py)
- Built Bot using **Ollama Python client** to generate responses : [legal_advisory_bot2.py](./milestone6/legal_advisory_bot2.py)
- Generated a **3000–5000 word PDF** of text from ChatGPT about Indian laws and regulations : [Indian_Laws_and_Regulations.pdf](./milestone6/Indian_Laws_and_Regulations.pdf)
---

## Examples of Chatbot Output

Below are some **examples** demonstrating how the bot responded to some sample legal questions:

### **User Input1**

what is IPC ?


### **Bot Response1**

Indian Penal Code (IPC)
The Indian Penal Code (IPC), enacted in 1860, is the main criminal code of India, covering all substantive aspects of criminial law. It defines various crimes and prescribes punishment for them. The IPC defines various crime categories such as:
- Armed Robbery
- Assault or Criminal Force to Dangerous Situation (ACFDS)
- Burglary
- Conspiracy
- Counterfeiting
- Criminal Breach of Trust 
- Cyber Crime
- Dacoity 
- Dealing in Narcotics 
- Driving Under the Influence (DUI) 
- Hooliganism
- Immoral Traffic (Including Eve Teasing and Paryatan Paribahan)
- Insult to National Structure (INSULT)
- Man with Red Hair Act 
- Public Nuisance 
- Quota Rent Collector 
- Seditious Message 
- Theft of Motor Vehicle
- Trafficking in Human Beings (THB)
- Unlawful Activities Prevention Act (UAPA)

In addition, the Indian Code on Trade and Commerce (ICTC) has a section dedicated to criminalizing trade practices like counterfeiting of trademarks, frauds, etc. 

Hindi: भारतीय प्रविधिकोएडकोल (IPC)
Bharatiya Pratihikshanikandrokoeledakosu (BPAL)


### **User Input2**
What is the minimum age for marriage in India?

### **Bot Response2**
In India, the minimum age for marriage varies by region and state. The Indian constitution prohibits child marriages, and under certain circumstances, the legal age for marriage may be lowered. In general, the minimum age for marriage is generally set at 18 years old or 25 years old in some states with higher educational qualifications, depending on the religious and cultural norms of the region.


### **User Input3**
what is cricket ?

### **Bot Response3**
I don't know
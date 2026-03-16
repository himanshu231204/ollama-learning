<div align="center">

# 🦙 Ollama Learning

**A comprehensive, hands-on guide to running Large Language Models locally with [Ollama](https://ollama.com).**

[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLMs-blue?style=for-the-badge)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)](#contributing)

*Learn everything from LLM fundamentals to practical local inference — with code examples, CLI cheat sheets, and deep technical explanations.*

</div>

---

## 📑 Table of Contents

- [About](#about)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Install Ollama](#1-install-ollama)
  - [Pull a Model](#2-pull-a-model)
  - [Set Up the Python Environment](#3-set-up-the-python-environment)
- [Usage](#usage)
  - [CLI Quick Start](#cli-quick-start)
  - [Python Library Examples](#python-library-examples)
    - [Basic Text Generation](#basic-text-generation-generatepy)
    - [Streaming Chat Responses](#streaming-chat-responses-streamingpy)
    - [Structured JSON Output](#structured-json-output-structure_outputpy)
    - [Modelfile Template](#modelfile-template-modelfiletxt)
- [Learning Resources](#learning-resources)
  - [Understanding LLMs](#understanding-llms)
  - [Why Run LLMs Locally?](#why-run-llms-locally)
  - [Inference Speed](#inference-speed)
  - [Memory Mapping](#memory-mapping)
  - [Quantization](#quantization)
  - [GGUF Format](#gguf-format)
  - [System Architecture](#system-architecture)
- [CLI Cheat Sheet](#cli-cheat-sheet)
- [Modelfile Documentation](#modelfile-documentation)
- [Contributing](#contributing)
- [License](#license)

---

## About

**Ollama Learning** is an educational repository designed to help developers understand and work with Large Language Models running locally via [Ollama](https://ollama.com). It covers core theory (transformers, quantization, memory mapping), practical CLI usage, and programmatic access through the Ollama Python library.

Whether you are new to local LLM inference or looking to deepen your understanding, this repo provides structured notes, working code samples, and a comprehensive CLI reference.

---

## Features

- 🧠 **Deep technical notes** on LLMs, quantization, GGUF, and memory mapping
- ⌨️ **Complete CLI cheat sheet** for every Ollama command and session option
- 🐍 **Python code examples** using the official `ollama` library
- 📖 **Beginner-friendly** explanations with ASCII diagrams and step-by-step flows
- 🔒 **Privacy-first** — all models run locally, no data leaves your machine

---

## Project Structure

```
ollama-learning/
├── README.MD                          # Project overview & learning guide
├── generate.py                        # Python example: generate text with Ollama
├── streaming.py                       # Python example: streaming chat responses
├── structure_output.py                # Python example: structured JSON output
├── modelfile.txt                      # Ollama Modelfile template for Mistral
├── test.py                            # Scratch file: basic Python variable and type printing
├── text.py                            # Scratch file: basic Python value and type check
└── Docs/
    ├── ollama_cli_cheatsheet.md       # Full Ollama CLI cheat sheet
    └── MODELFILE.md                   # Complete Modelfile learning guide
```

---

## Prerequisites

| Requirement | Details |
|---|---|
| **Operating System** | Windows, macOS, or Linux |
| **Ollama** | [Download & install](https://ollama.com/download) |
| **Python** | 3.11 or later (for Python examples) |
| **RAM** | ≥ 8 GB recommended (varies by model) |

---

## Getting Started

### 1. Install Ollama

Follow the instructions for your platform at **<https://ollama.com/download>**.

Verify the installation:

```bash
ollama --version
```

### 2. Pull a Model

```bash
ollama pull mistral        # ~4 GB, good general-purpose model
# or
ollama pull llama3         # Meta's Llama 3
```

### 3. Set Up the Python Environment

```bash
# Clone this repository
git clone https://github.com/himanshu231204/ollama-learning.git
cd ollama-learning

# Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install the Ollama Python library
pip install ollama
```

---

## Usage

### CLI Quick Start

```bash
# Start an interactive chat session
ollama run mistral

# Single-prompt mode (non-interactive)
ollama run mistral "Explain transformers in simple terms"

# List all downloaded models
ollama ls

# Remove a model
ollama rm mistral
```

> 💡 See the full [CLI Cheat Sheet](#cli-cheat-sheet) below for every available command.

### Python Library Examples

#### Basic Text Generation (`generate.py`)

```python
import ollama

response = ollama.generate(
    model="mistral",
    prompt="What is the capital of France?"
)

print(response["response"])
```

```bash
python generate.py
```

#### Streaming Chat Responses (`streaming.py`)

```python
from ollama import chat

stream = chat(
    model="mistral",
    messages=[{"role": "user", "content": "What is 17 × 23?"}],
    stream=True,
)

content = ""

for chunk in stream:
    if chunk.message.content:
        print(chunk.message.content, end="", flush=True)
        content += chunk.message.content

print("\n\nFinal Answer:", content)
```

```bash
python streaming.py
```

#### Structured JSON Output (`structure_output.py`)

```python
from ollama import chat

response = chat(
    model='mistral',
    messages=[{'role': 'user', 'content': 'Tell me about Canada.'}],
    format='json'
)
print(response.message.content)
```

```bash
python structure_output.py
```

#### Modelfile Template (`modelfile.txt`)

The `modelfile.txt` file contains a full Ollama Modelfile exported from the Mistral model. It includes the model's prompt template, stop parameters, and the Apache 2.0 license text. You can use it as a reference to understand Ollama Modelfile syntax or as a starting point for building a custom model:

```bash
# Inspect the Modelfile
cat modelfile.txt

# Use it to create a custom Ollama model
ollama create my-mistral -f modelfile.txt
```

> 📄 For a full guide on creating your own Modelfiles, see **[Modelfile Learning Guide](Docs/MODELFILE.md)**.

---

## Learning Resources

### Understanding LLMs

A **Large Language Model (LLM)** is a deep neural network trained on massive text data. It learns patterns in language and predicts the next token (word or subword).

```
User Prompt → [Tokenizer] → [Embedding Layer] → [Transformer Blocks × N] → [Softmax] → Next Token
```

> LLMs do not "think" like humans — they predict the most probable next token repeatedly.

---

### Why Run LLMs Locally?

| Benefit | Cloud API | Local (Ollama) |
|---|---|---|
| **Privacy** | Data sent to third-party servers | Data never leaves your machine |
| **Cost** | Pay per token / request | One-time hardware cost, unlimited use |
| **Latency** | Network round-trip | Direct local inference |
| **Offline** | ❌ Requires internet | ✅ Works offline after download |

---

### Inference Speed

LLM speed is measured in **Tokens Per Second (TPS)** and depends on:

| Factor | Impact |
|---|---|
| **Model size** | 7 B params → fast; 70 B params → slow |
| **Hardware** | GPU is massively faster than CPU |
| **Quantization** | Lower precision (INT4) → faster |
| **Context length** | Longer context → O(n²) attention cost |
| **Memory bandwidth** | Bottleneck even on strong CPUs |

---

### Memory Mapping

Memory mapping lets the OS map a model file directly into virtual memory, loading only the pages that are actively needed instead of the entire file.

```
Disk: [Model File: 8 GB]
              ↓
Virtual Memory:
  [Chunk 1] ← loaded
  [Chunk 2] ← on disk (loaded on demand)
  [Chunk 3] ← loaded
```

**Benefits:** lower RAM usage, faster startup, ability to run large models on modest hardware.

---

### Quantization

Quantization reduces the numerical precision of model weights to shrink size and speed up inference.

| Precision | Bytes / Param | 8 B-param Model Size |
|---|---|---|
| FP32 | 4 | ~32 GB |
| FP16 | 2 | ~16 GB |
| INT8 | 1 | ~8 GB |
| INT4 | 0.5 | ~4 GB |

**Trade-off:** slight accuracy loss, but 4-bit quantization is good enough for most tasks.

---

### GGUF Format

**GGUF** (GPT Generated Unified Format) is a binary container optimized for local inference:

- Stores quantized weights, tokenizer, architecture info, and metadata in a single file
- Designed for memory-mapped, CPU/GPU-friendly execution (used by `llama.cpp`)
- Replaces older formats like `.pt` or `.safetensors` for local use

---

### System Architecture

```
User Prompt
|
v
[Ollama CLI]
|
v
[Inference Engine]
|
v
[GGUF Model File]
|
v
[Memory Mapping Layer]
|
v
[CPU/GPU Compute]
|
v
Token Generation
```

How these concepts work together:

- **Quantization** → Smaller weights → Less RAM
- **Memory Mapping** → Load only needed chunks → Faster startup
- **Efficient Memory + Smaller Weights** → Higher speed + Local execution → Better developer experience

---

### Practical Impact for AI Development

Understanding these concepts allows you to:

* Choose the correct model size
* Decide quantization level
* Estimate RAM needs
* Optimize latency
* Build efficient AI agents
* Design RAG systems properly

---

### Summary

Ollama is a local LLM runtime that executes quantized models stored in GGUF format.

**LLM speed** depends on model size, hardware, quantization, and context length.

**Efficiency** depends on resource utilization, memory management, and architectural optimization.

**Memory mapping** allows large model files to be accessed without loading fully into RAM.

**Quantization** compresses weights by reducing numerical precision, drastically reducing memory usage and increasing speed.

**GGUF** is an optimized binary format that supports quantization and memory mapping.

Together, these form the foundation of modern local GenAI execution systems.

---

## CLI Cheat Sheet

For a comprehensive reference of all Ollama CLI commands, interactive session commands, parameter configuration, and common workflows, see the full cheat sheet:

📄 **[Ollama CLI Cheat Sheet](Docs/ollama_cli_cheatsheet.md)**

---

## Modelfile Documentation

Learn how to create and customize Ollama Modelfiles — configuration files that let you define base models, system prompts, parameters, and more:

📄 **[Modelfile Learning Guide](Docs/MODELFILE.md)**

---

## Contributing

Contributions are welcome! If you'd like to improve this project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

Feel free to open an issue for suggestions, corrections, or new topics you'd like to see covered.

---

## License

This project is licensed under the [MIT License](LICENSE).


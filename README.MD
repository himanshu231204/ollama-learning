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
  - [Python Library Example](#python-library-example)
- [Learning Resources](#learning-resources)
  - [Understanding LLMs](#understanding-llms)
  - [Why Run LLMs Locally?](#why-run-llms-locally)
  - [Inference Speed](#inference-speed)
  - [Memory Mapping](#memory-mapping)
  - [Quantization](#quantization)
  - [GGUF Format](#gguf-format)
  - [System Architecture](#system-architecture)
- [CLI Cheat Sheet](#cli-cheat-sheet)
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
├── Docs/
│   └── Ollama_Cli_command.txt         # Full Ollama CLI cheat sheet
└── Ollama using ollama library/
    └── generate.py                    # Python example: generate text with Ollama
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

### Python Library Example

The script in `Ollama using ollama library/generate.py` demonstrates basic text generation:

```python
import ollama

response = ollama.generate(
    model="mistral",
    prompt="What is the capital of France?"
)

print(response["response"])
```

Run it with:

```bash
python "Ollama using ollama library/generate.py"
```

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
     │
     ▼
 [Ollama CLI / Python API]
     │
     ▼
 [Inference Engine]
     │
     ▼
 [GGUF Model File]
     │
     ▼
 [Memory Mapping Layer]
     │
     ▼
 [CPU / GPU Compute]
     │
     ▼
 Generated Response
```

---

## CLI Cheat Sheet

### Basic Commands

| Command | Description |
|---|---|
| `ollama --version` | Check installed version |
| `ollama ls` | List downloaded models |
| `ollama pull <model>` | Download a model |
| `ollama run <model>` | Interactive chat session |
| `ollama run <model> "prompt"` | Single-prompt mode |
| `ollama rm <model>` | Remove a model |
| `ollama serve` | Start the Ollama server |

### Interactive Session Commands

| Command | Description |
|---|---|
| `/bye` | Exit the session |
| `/clear` | Clear context / history |
| `/help` or `/?` | Show help menu |
| `/show info` | Model details |
| `/show license` | Model license |
| `/show modelfile` | Modelfile content |
| `/show parameters` | Current parameters |
| `/show system` | System message |
| `/show template` | Prompt template |

### Session Settings (`/set`)

| Command | Description |
|---|---|
| `/set system <msg>` | Set system message |
| `/set parameter temperature <float>` | Creativity level |
| `/set parameter num_ctx <int>` | Context window size |
| `/set parameter top_k <int>` | Top-K sampling |
| `/set parameter top_p <float>` | Nucleus sampling |
| `/set format json` | Enable JSON output |
| `/set verbose` | Show generation stats |
| `/set quiet` | Hide generation stats |

> 📄 The complete reference is in [`Docs/Ollama_Cli_command.txt`](Docs/Ollama_Cli_command.txt).

---

## Contributing

Contributions are welcome! If you would like to add new examples, fix errors, or expand the learning notes:

1. **Fork** this repository
2. **Create** a feature branch (`git checkout -b feature/my-addition`)
3. **Commit** your changes (`git commit -m "Add new example"`)
4. **Push** to your branch (`git push origin feature/my-addition`)
5. **Open** a Pull Request

Please make sure any code examples are tested and any documentation is clear and accurate.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">

**⭐ If you found this helpful, please give the repo a star! ⭐**

</div>

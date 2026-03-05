# OLLAMA MODELFILE - Complete Learning Guide

---

## Table of Contents

1. [Introduction to Modelfiles](#introduction-to-modelfiles)
2. [Basic Syntax and Structure](#basic-syntax-and-structure)
3. [Core Instructions](#core-instructions)
4. [Parameters Reference](#parameters-reference)
5. [Practical Examples](#practical-examples)
6. [Best Practices](#best-practices)
7. [Advanced Techniques](#advanced-techniques)
8. [Troubleshooting](#troubleshooting)
9. [Command Reference](#command-reference)
10. [Resources and Glossary](#resources-and-glossary)

---

## Introduction to Modelfiles

### What is a Modelfile?

A **Modelfile** is a configuration file used by Ollama to define and customize large language models (LLMs). It allows you to:

- Specify a base model
- Customize system prompts and behavior
- Set model parameters (temperature, context window, etc.)
- Create specialized AI assistants
- Share and version control model configurations

**Think of it as:**
- A "recipe" for your AI model
- Similar to Dockerfile for Docker containers
- A way to make AI models reproducible and shareable

### Why Use Modelfiles?

1. **CUSTOMIZATION** - Tailor AI behavior for specific tasks
2. **REPRODUCIBILITY** - Share exact model configurations
3. **VERSION CONTROL** - Track changes to your AI setup
4. **EFFICIENCY** - Quick deployment of specialized models
5. **CONSISTENCY** - Ensure same behavior across environments

---

## Basic Syntax and Structure

### File Format

- Plain text file (no extension required, or use `.modelfile`)
- Case-insensitive instructions
- Comments start with `#`
- One instruction per line

### Basic Template

```modelfile
FROM <base_model>
PARAMETER <param_name> <value>
SYSTEM """<system_prompt>"""
TEMPLATE """<prompt_template>"""
```

### Minimal Example

```modelfile
FROM llama2
SYSTEM "You are a helpful assistant."
```

---

## Core Instructions

### 3.1 FROM - Specify Base Model

**Syntax:** `FROM <model_name>`

**Purpose:** Defines which model to use as the foundation

**Examples:**
```modelfile
FROM llama2
FROM mistral
FROM codellama
FROM llama2:13b
FROM ./custom-model.gguf
```

**Notes:**
- Must be the first instruction
- Can reference Ollama library models or local files
- Supports model tags (e.g., `:13b`, `:70b`)

---

### 3.2 PARAMETER - Configure Model Behavior

**Syntax:** `PARAMETER <name> <value>`

**Purpose:** Sets model runtime parameters

**Common Parameters:**
```modelfile
PARAMETER temperature 0.7
PARAMETER num_ctx 4096
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
```

See [Parameters Reference](#parameters-reference) for complete details.

---

### 3.3 SYSTEM - Define System Prompt

**Syntax:** `SYSTEM """<prompt>"""`

**Purpose:** Sets the system message that defines AI behavior

**Example:**
```modelfile
SYSTEM """You are an expert Python programmer. 
You provide clear, concise code examples with explanations.
Always follow PEP 8 style guidelines."""
```

**Best Practices:**
- Use triple quotes for multi-line prompts
- Be specific about tone, expertise, and constraints
- Define output format expectations
- Set boundaries on what the AI should/shouldn't do

---

### 3.4 TEMPLATE - Define Prompt Format

**Syntax:** `TEMPLATE """<template>"""`

**Purpose:** Specifies how user messages are formatted before sending to the model

**Variables:**
- `{{ .System }}` - System prompt
- `{{ .Prompt }}` - User's message
- `{{ .Response }}` - Model's response (for multi-turn)

**Example:**
```modelfile
TEMPLATE """{{ if .System }}<|system|>
{{ .System }}</s>
{{ end }}{{ if .Prompt }}<|user|>
{{ .Prompt }}</s>
{{ end }}<|assistant|>
{{ .Response }}"""
```

**Notes:**
- Uses Go template syntax
- Required for models with specific chat formats
- Usually not needed for standard models

---

### 3.5 ADAPTER - Add LoRA Adapters

**Syntax:** `ADAPTER <path_to_adapter>`

**Purpose:** Applies fine-tuned LoRA (Low-Rank Adaptation) weights

**Example:**
```modelfile
ADAPTER ./custom-lora-adapter.bin
```

**Use Cases:**
- Domain-specific fine-tuning
- Task-specific adaptations
- Efficient model customization without full retraining

---

### 3.6 LICENSE - Specify License

**Syntax:** `LICENSE """<license_text>"""`

**Purpose:** Documents the model's license terms

**Example:**
```modelfile
LICENSE """MIT License
Copyright (c) 2024"""
```

---

### 3.7 MESSAGE - Set Example Conversations

**Syntax:** `MESSAGE <role> <content>`

**Purpose:** Provides example conversations for few-shot learning

**Roles:** `system`, `user`, `assistant`

**Example:**
```modelfile
MESSAGE user "What is the capital of France?"
MESSAGE assistant "The capital of France is Paris."
MESSAGE user "What about Spain?"
MESSAGE assistant "The capital of Spain is Madrid."
```

**Use Cases:**
- Few-shot prompting
- Teaching desired response format
- Setting conversation tone

---

## Parameters Reference

### Overview Table

| Parameter | Range | Default | Description |
|-----------|-------|---------|-------------|
| `temperature` | 0.0 - 2.0 | 0.8 | Controls randomness in responses |
| `num_ctx` | 128 - 128000 | 2048 | Maximum context length (tokens) |
| `top_p` | 0.0 - 1.0 | 0.9 | Nucleus sampling threshold |
| `top_k` | 1 - 100+ | 40 | Limits vocabulary to top K tokens |
| `repeat_penalty` | 0.0 - 2.0 | 1.1 | Penalizes token repetition |
| `num_predict` | -1 or positive | 128 | Maximum tokens to generate |
| `presence_penalty` | -2.0 - 2.0 | 0.0 | Encourages discussing new topics |
| `frequency_penalty` | -2.0 - 2.0 | 0.0 | Penalizes frequent tokens |

---

### 4.1 Temperature

```modelfile
PARAMETER temperature <float>
```

**Range:** 0.0 - 2.0  
**Default:** 0.8

Controls randomness in responses:
- **0.0** = Deterministic, repetitive
- **0.3-0.7** = Balanced, good for factual tasks
- **0.8-1.0** = Creative, varied responses
- **1.5+** = Very random, experimental

**Use Cases:**
- **0.1** - Math, code, factual QA
- **0.7** - General conversation
- **1.2** - Creative writing, brainstorming

---

### 4.2 Context Window (num_ctx)

```modelfile
PARAMETER num_ctx <integer>
```

**Range:** 128 - 128000 (model dependent)  
**Default:** 2048

Sets the maximum context length (tokens):
- Larger = More memory, slower
- Smaller = Less memory, faster

**Examples:**
```modelfile
PARAMETER num_ctx 4096    # Standard
PARAMETER num_ctx 8192    # Extended conversations
PARAMETER num_ctx 32768   # Long documents
```

---

### 4.3 Top P (Nucleus Sampling)

```modelfile
PARAMETER top_p <float>
```

**Range:** 0.0 - 1.0  
**Default:** 0.9

Controls diversity via cumulative probability:
- **1.0** = Consider all tokens
- **0.9** = Top 90% probability mass
- **0.5** = More focused, deterministic

> **Recommendation:** Use either `top_p` OR `top_k`, not both

---

### 4.4 Top K

```modelfile
PARAMETER top_k <integer>
```

**Range:** 1 - 100+  
**Default:** 40

Limits vocabulary to top K tokens:
- **1** = Always most likely token
- **40** = Balanced
- **100** = More diverse

---

### 4.5 Repeat Penalty

```modelfile
PARAMETER repeat_penalty <float>
```

**Range:** 0.0 - 2.0  
**Default:** 1.1

Penalizes token repetition:
- **1.0** = No penalty
- **1.1** = Slight penalty (recommended)
- **1.5+** = Strong penalty (may affect coherence)

---

### 4.6 Number of Predictions

```modelfile
PARAMETER num_predict <integer>
```

**Default:** 128  
**Range:** -1 (infinite), or positive integer

Maximum tokens to generate:
```modelfile
PARAMETER num_predict 512     # Longer responses
PARAMETER num_predict -1      # Unlimited
```

---

### 4.7 Stop Sequences

```modelfile
PARAMETER stop "<sequence>"
```

Defines when to stop generation. Can specify multiple:

```modelfile
PARAMETER stop "\n\n"
PARAMETER stop "###"
PARAMETER stop "END"
```

---

### 4.8 Seed

```modelfile
PARAMETER seed <integer>
```

Sets random seed for reproducibility:

```modelfile
PARAMETER seed 42
```

Use for:
- Debugging
- Consistent testing
- Reproducible outputs

---

### 4.9 Other Parameters

```modelfile
PARAMETER num_thread <int>       # CPU threads
PARAMETER num_gpu <int>          # GPU layers
PARAMETER num_batch <int>        # Batch size
PARAMETER mirostat <0|1|2>       # Adaptive sampling (0=off)
PARAMETER mirostat_tau 5.0       # Target entropy
PARAMETER mirostat_eta 0.1       # Learning rate
```

---

## Practical Examples

### Example 1: Code Assistant

```modelfile
FROM codellama:7b

SYSTEM """You are an expert software engineer specializing in clean, 
maintainable code. You provide:
- Well-commented code examples
- Best practices and design patterns
- Security considerations
- Performance optimization tips

Always explain your code and suggest improvements."""

PARAMETER temperature 0.3
PARAMETER num_ctx 8192
PARAMETER top_p 0.9
```

---

### Example 2: Creative Writer

```modelfile
FROM llama2:13b

SYSTEM """You are a creative writing assistant. You help with:
- Story development and plot ideas
- Character creation and development
- Dialogue writing
- World-building
- Writing in various genres and styles

Be imaginative, descriptive, and engaging."""

PARAMETER temperature 1.2
PARAMETER top_p 0.95
PARAMETER repeat_penalty 1.2
PARAMETER num_predict 1024
```

---

### Example 3: Technical Documentation Expert

```modelfile
FROM mistral:7b

SYSTEM """You are a technical documentation specialist. You create:
- Clear, concise documentation
- API references
- User guides and tutorials
- Architecture diagrams descriptions
- Troubleshooting guides

Use simple language and structured formatting."""

PARAMETER temperature 0.4
PARAMETER num_ctx 16384
PARAMETER presence_penalty 0.2

MESSAGE user "How do I document an API endpoint?"
MESSAGE assistant "I'll help you document an API endpoint with these sections: 1) Endpoint URL and method, 2) Description, 3) Parameters, 4) Request example, 5) Response format, 6) Error codes."
```

---

### Example 4: Customer Support Bot

```modelfile
FROM llama2:7b

SYSTEM """You are a friendly customer support representative. You:
- Greet customers warmly
- Listen to their concerns patiently
- Provide clear solutions
- Escalate when necessary
- Always maintain a professional, helpful tone

Never make promises you can't keep."""

PARAMETER temperature 0.7
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 4096
PARAMETER stop "ESCALATE"
PARAMETER stop "TRANSFER"
```

---

### Example 5: Data Analyst

```modelfile
FROM llama2:13b

SYSTEM """You are a data analyst who:
- Interprets data and statistics
- Creates visualization recommendations
- Explains trends and patterns
- Provides actionable insights
- Uses clear, non-technical language when possible

Always cite sources and confidence levels."""

PARAMETER temperature 0.5
PARAMETER num_ctx 8192
PARAMETER top_k 30
```

---

### Example 6: Math Tutor

```modelfile
FROM llama2:7b

SYSTEM """You are a mathematics tutor. You:
- Break down problems step-by-step
- Explain concepts with examples
- Check student work
- Provide practice problems
- Use clear notation and formatting

Always show your work and reasoning."""

PARAMETER temperature 0.2
PARAMETER num_ctx 4096
PARAMETER seed 42
```

---

### Example 7: JSON API Generator

```modelfile
FROM codellama:7b

TEMPLATE """{{ .System }}

USER: {{ .Prompt }}

ASSISTANT (JSON only): {{ .Response }}"""

SYSTEM """Generate valid JSON only. No explanations, no markdown, no additional text."""

PARAMETER temperature 0.1
PARAMETER stop "}"
```

---

### Example 8: Language Tutor

```modelfile
FROM llama2:7b

SYSTEM """You are a patient language tutor teaching Spanish. You:
- Explain grammar concepts simply
- Provide example sentences
- Correct mistakes gently
- Encourage practice
- Use progressive difficulty
- Respond in English but include Spanish examples

Format: [English explanation] | Ejemplo: [Spanish example]"""

PARAMETER temperature 0.6
PARAMETER repeat_penalty 1.15

MESSAGE user "How do I say 'hello' in Spanish?"
MESSAGE assistant "In Spanish, 'hello' is 'hola' (pronounced OH-lah). | Ejemplo: Hola, ¿cómo estás? (Hello, how are you?)"
```

---

## Best Practices

### Writing Effective System Prompts

**DO:**
- ✅ Be specific about role and expertise
- ✅ Define output format clearly
- ✅ Set behavioral boundaries
- ✅ Include examples when helpful
- ✅ Specify tone and style
- ✅ Use structured formatting

**DON'T:**
- ❌ Be vague or ambiguous
- ❌ Create overly long prompts (>500 words)
- ❌ Contradict yourself
- ❌ Use ambiguous pronouns
- ❌ Forget to test your prompt

**Template Structure:**
```
You are a [ROLE] who [PRIMARY FUNCTION].

You should:
- [SPECIFIC BEHAVIOR 1]
- [SPECIFIC BEHAVIOR 2]
- [SPECIFIC BEHAVIOR 3]

You must NOT:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

Output format: [FORMAT DESCRIPTION]
```

---

### Parameter Tuning Guidelines

#### For Factual Tasks:
```modelfile
PARAMETER temperature 0.1-0.3
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
```

#### For Balanced Tasks:
```modelfile
PARAMETER temperature 0.7-0.8
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.1
```

#### For Creative Tasks:
```modelfile
PARAMETER temperature 1.0-1.5
PARAMETER top_p 0.95
PARAMETER repeat_penalty 1.2-1.3
```

#### For Code Generation:
```modelfile
PARAMETER temperature 0.2-0.4
PARAMETER num_ctx 8192+
PARAMETER top_k 40
```

---

### Parameter Tuning by Task Type

| Task Type | Temperature | Top P | Repeat Penalty | Num CTX |
|-----------|-------------|-------|----------------|---------|
| Code Generation | 0.2-0.4 | 0.9 | 1.1 | 8192+ |
| Factual QA | 0.1-0.3 | 0.9 | 1.0 | 4096 |
| General Chat | 0.7-0.8 | 0.9 | 1.1 | 4096 |
| Creative Writing | 1.0-1.5 | 0.95 | 1.2-1.3 | 8192+ |
| Technical Docs | 0.4-0.6 | 0.9 | 1.0 | 16384 |
| Data Analysis | 0.5-0.7 | 0.9 | 1.1 | 8192 |
| Translation | 0.3-0.5 | 0.9 | 1.0 | 4096 |
| Summarization | 0.5-0.7 | 0.9 | 1.1 | 8192+ |

---

### Performance Optimization

**Speed:**
- Reduce `num_ctx` if possible
- Use smaller base models
- Adjust `num_gpu` for GPU acceleration
- Reduce `num_predict` for shorter responses

**Quality:**
- Increase `num_ctx` for longer conversations
- Use larger models (13b, 70b)
- Fine-tune temperature for task
- Add few-shot examples via MESSAGE

**Memory:**
- Monitor `num_ctx` × model_size
- Use quantized models (Q4, Q5)
- Batch process when possible

---

### Testing Your Modelfile

1. Start simple, add complexity gradually
2. Test edge cases
3. Verify output format consistency
4. Check response quality across temperatures
5. Monitor token usage
6. Test with various input lengths
7. Validate stop sequences work correctly

---

### Version Control

- Keep Modelfiles in git repositories
- Use descriptive commit messages
- Tag stable versions
- Document changes in comments
- Maintain changelog

**Example:**
```modelfile
# Version 1.2.0
# Added: JSON output formatting
# Changed: Reduced temperature from 0.8 to 0.6
# Fixed: Stop sequence for code blocks

FROM codellama:7b
# ... rest of config
```

---

## Advanced Techniques

### 7.1 Multi-Stage Prompting

Use MESSAGE to guide multi-step reasoning:

```modelfile
FROM llama2
SYSTEM "You solve problems step-by-step."

MESSAGE user "Calculate 15% tip on $47.80"
MESSAGE assistant "Step 1: Convert percentage to decimal: 15% = 0.15"
MESSAGE assistant "Step 2: Multiply: $47.80 × 0.15 = $7.17"
MESSAGE assistant "The 15% tip is $7.17"
```

---

### 7.2 Output Format Control

Use stop sequences and templates for structured output:

```modelfile
FROM codellama
SYSTEM "Generate Python functions only."

TEMPLATE """{{ .Prompt }}

```python
{{ .Response }}```"""

PARAMETER stop "```"
PARAMETER temperature 0.3
```

---

### 7.3 Context Window Management

For long conversations:

```modelfile
PARAMETER num_ctx 32768
PARAMETER num_keep 512    # Keep first 512 tokens always
```

This keeps system prompt persistent while allowing long history.

---

### 7.4 Dynamic Temperature

For mixed tasks, use moderate temperature with top_p:

```modelfile
PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER typical_p 0.9
```

This balances creativity and accuracy.

---

### 7.5 Custom Stop Sequences

Control output boundaries:

```modelfile
PARAMETER stop "\n\nUser:"
PARAMETER stop "\n\nHuman:"
PARAMETER stop "<|endoftext|>"
PARAMETER stop "###END###"
```

---

### 7.6 Chain-of-Thought Prompting

Encourage reasoning:

```modelfile
SYSTEM """Before answering, think step-by-step:
1. Understand the question
2. Identify relevant information
3. Apply logical reasoning
4. Formulate clear answer

Format your response:
THINKING: [your reasoning]
ANSWER: [final answer]"""
```

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Model generates gibberish

**Solutions:**
- Reduce temperature (try 0.6-0.7)
- Check if base model is compatible
- Verify template syntax
- Ensure adequate num_ctx

---

#### Issue: Responses are too short

**Solutions:**
- Increase `num_predict`
- Adjust system prompt to request longer responses
- Reduce `repeat_penalty`
- Check stop sequences aren't triggering early

---

#### Issue: Model repeats itself

**Solutions:**
- Increase `repeat_penalty` (1.2-1.3)
- Increase `presence_penalty` (0.3-0.5)
- Reduce temperature
- Use `frequency_penalty`

---

#### Issue: Model ignores system prompt

**Solutions:**
- Simplify system prompt
- Use MESSAGE examples
- Increase `num_keep`
- Verify template includes `{{ .System }}`

---

#### Issue: Out of memory errors

**Solutions:**
- Reduce `num_ctx`
- Use smaller model variant
- Reduce `num_batch`
- Adjust `num_gpu`

---

#### Issue: Slow generation

**Solutions:**
- Reduce `num_ctx` if possible
- Use smaller model
- Increase `num_thread` (CPU)
- Increase `num_gpu` (GPU)
- Reduce `num_predict`

---

#### Issue: Inconsistent outputs

**Solutions:**
- Set `seed` for reproducibility
- Reduce temperature
- Use `top_k` or `top_p` (not both)
- Simplify system prompt

---

### Debugging Checklist

- [ ] Verify FROM model exists and is accessible
- [ ] Check all PARAMETER values are in valid ranges
- [ ] Ensure TEMPLATE syntax is correct (if used)
- [ ] Test SYSTEM prompt in isolation
- [ ] Validate stop sequences don't conflict
- [ ] Confirm adequate system resources
- [ ] Review Ollama logs for errors
- [ ] Test with minimal Modelfile first

---

### Error Messages

**"model not found":**
- Check model name spelling
- Run: `ollama list`
- Pull model: `ollama pull <model>`

**"invalid parameter":**
- Review parameter name spelling
- Check value is in valid range
- Consult parameter reference

**"template parse error":**
- Verify Go template syntax
- Check for unmatched `{{ }}`
- Escape special characters

**"context length exceeded":**
- Reduce `num_ctx`
- Shorten input
- Manage conversation history

---

## Command Reference

### Creating Models from Modelfile

```bash
# Basic creation
ollama create mymodel -f ./Modelfile

# With custom name
ollama create custom-assistant -f ./assistant.modelfile

# From URL
ollama create mymodel -f https://example.com/Modelfile
```

---

### Managing Models

```bash
# List models
ollama list

# Show model details
ollama show mymodel

# Delete model
ollama rm mymodel

# Copy model
ollama cp source-model target-model
```

---

### Running Models

```bash
# Interactive mode
ollama run mymodel

# Single prompt
ollama run mymodel "Your prompt here"

# With options
ollama run mymodel --verbose
```

---

### Pushing/Pulling Models

```bash
# Push to registry
ollama push username/mymodel

# Pull from registry
ollama pull username/mymodel

# Tag model
ollama tag mymodel mymodel:v1.0
```

---

### API Usage

**Generate response:**
```bash
curl http://localhost:11434/api/generate -d '{
  "model": "mymodel",
  "prompt": "Your prompt"
}'
```

**Chat format:**
```bash
curl http://localhost:11434/api/chat -d '{
  "model": "mymodel",
  "messages": [
    {"role": "user", "content": "Hello"}
  ]
}'
```

---

### Inspection Commands

```bash
# Show modelfile
ollama show mymodel --modelfile

# Show parameters
ollama show mymodel --parameters

# Show template
ollama show mymodel --template

# Show system
ollama show mymodel --system
```

---

## Resources and Glossary

### Official Documentation

- **Ollama GitHub:** https://github.com/ollama/ollama
- **Modelfile Reference:** https://github.com/ollama/ollama/blob/main/docs/modelfile.md
- **Model Library:** https://ollama.ai/library

### Community

- **Discord:** https://discord.gg/ollama
- **Reddit:** r/ollama
- **GitHub Discussions**

### Model Sources

- **Hugging Face:** https://huggingface.co/models
- **Ollama Library:** Pre-configured models
- **Custom GGUF models:** Various sources

---

### Glossary

**Adapter:** A small trained module (LoRA) that modifies base model behavior

**Base Model:** The foundation model specified in FROM instruction

**Context Window:** Maximum number of tokens the model can process at once

**Few-Shot Learning:** Teaching model by example using MESSAGE instructions

**GGUF:** File format for quantized language models

**LoRA:** Low-Rank Adaptation - efficient fine-tuning method

**Modelfile:** Configuration file defining custom Ollama model

**Nucleus Sampling:** Selection method using top_p parameter

**Parameter:** Configuration value affecting model behavior

**Quantization:** Reducing model precision to save memory

**Seed:** Random number generator initialization for reproducibility

**Stop Sequence:** Text that signals end of generation

**System Prompt:** Instructions defining model behavior and role

**Temperature:** Parameter controlling output randomness

**Template:** Format specification for prompts and responses

**Token:** Basic unit of text processing (≈0.75 words)

**Top-K Sampling:** Selection from K most likely tokens

**Top-P Sampling:** Selection from tokens whose cumulative probability reaches P

---

## Quick Reference Card

### Essential Instructions

```modelfile
FROM <model>                    # Base model
PARAMETER <n> <value>           # Set parameter
SYSTEM """<prompt>"""           # System message
MESSAGE <role> <content>        # Example conversation
TEMPLATE """<template>"""       # Prompt format
ADAPTER <path>                  # LoRA adapter
```

### Key Parameters

```modelfile
temperature (0.0-2.0)           # Randomness
num_ctx (128-128000)            # Context window
top_p (0.0-1.0)                 # Nucleus sampling
repeat_penalty (0.0-2.0)        # Repetition control
num_predict (-1 or positive)    # Max output tokens
```

### Common Commands

```bash
ollama create <n> -f <file>     # Create model
ollama run <model>              # Run model
ollama list                     # List models
ollama show <model>             # Show details
ollama rm <model>               # Delete model
```

---

## Modelfile Template

```modelfile
# Model Name: [NAME]
# Version: [VERSION]
# Purpose: [DESCRIPTION]
# Created: [DATE]

# Base model selection
FROM [model_name]

# Core parameters
PARAMETER temperature [value]
PARAMETER num_ctx [value]
PARAMETER top_p [value]
PARAMETER repeat_penalty [value]
PARAMETER num_predict [value]

# System prompt
SYSTEM """[Your system prompt here]"""

# Optional: Few-shot examples
MESSAGE user "[Example question]"
MESSAGE assistant "[Example answer]"

# Optional: Custom template
# TEMPLATE """[Your template]"""

# Optional: Adapter
# ADAPTER [path_to_adapter]

# Optional: Stop sequences
# PARAMETER stop "[sequence]"
```

---

## Document Information

- **Title:** Ollama Modelfile - Complete Learning Guide
- **Format:** Markdown (.md)
- **Audience:** Beginners to Advanced users
- **Last Updated:** 2024

For the latest information, always consult official Ollama documentation.

---

**End of Guide**

*This document is provided as-is for educational purposes.*
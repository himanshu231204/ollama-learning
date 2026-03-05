# 🦙 Ollama CLI - Complete Professional Cheat Sheet

A comprehensive reference guide for Ollama command-line interface commands and operations.

---

## Table of Contents

- [Basic Terminal Commands](#basic-terminal-commands)
- [Embedding Models](#embedding-models)
- [Multi-Line Input](#multi-line-input)
- [Interactive Session Commands](#interactive-session-commands)
- [Show Commands](#show-commands)
- [Set Commands](#set-commands)
- [Parameter Configuration](#parameter-configuration)
- [Session Management](#session-management)
- [Quick Reference](#quick-reference)

---

## Basic Terminal Commands

### Version and Information

```bash
ollama --version
```
Check installed Ollama version

---

### Model Management

```bash
ollama ls
```
List all installed models

```bash
ollama pull <modelname>
```
Download (pull) a model from the registry

```bash
ollama rm <modelname>
```
Remove a model from local system

---

### Running Models

```bash
ollama run <modelname>
```
Run a model in interactive mode

```bash
ollama run <modelname> "your prompt"
```
Run model with single prompt and auto-exit

---

### Server Management

```bash
ollama serve
```
Start the Ollama server

---

### Authentication

```bash
ollama signin
```
Sign in to your Ollama account

```bash
ollama signout
```
Sign out of your Ollama account

---

## Embedding Models

Generate embeddings using specialized embedding models:

```bash
ollama run embeddinggemma "Hello world"
```

This generates a vector embedding for the input text, useful for:
- Semantic search
- Text similarity comparison
- RAG (Retrieval Augmented Generation) systems
- Document clustering

---

## Multi-Line Input

Use triple quotes to write multi-line prompts:

```bash
"""
Your multi-line
prompt here
spanning multiple lines
"""
```

The model will process the entire block as one input.

**Example:**
```bash
ollama run llama2 """
Write a Python function that:
1. Takes a list of numbers
2. Returns the average
3. Handles empty lists
"""
```

---

## Interactive Session Commands

These commands are available after running `ollama run <modelname>`:

### Session Control

| Command | Description |
|---------|-------------|
| `/bye` | Exit the model session |
| `/clear` | Clear current session context/history |

### Help and Documentation

| Command | Description |
|---------|-------------|
| `/help` | Show help menu |
| `/?` | Show help menu (alternative) |
| `/? shortcuts` | Show keyboard shortcut help |

---

## Show Commands

Display information about the current model and session.

### Base Command

```bash
/show
```
Show available show commands

### Available Subcommands

| Command | Description |
|---------|-------------|
| `/show info` | Show detailed model information |
| `/show license` | Show model license terms |
| `/show modelfile` | Show Modelfile content |
| `/show parameters` | Show current model parameters |
| `/show system` | Show system message/prompt |
| `/show template` | Show prompt template format |

### Examples

```bash
# View current parameters
/show parameters

# Check model license
/show license

# Inspect the Modelfile
/show modelfile
```

---

## Set Commands

Modify session settings and behavior in real-time.

### Base Command

```bash
/set
```
Show available set commands

### System and History

| Command | Description |
|---------|-------------|
| `/set system <string>` | Set or change system message |
| `/set history` | Enable conversation history |
| `/set nohistory` | Disable conversation history |

### Display Options

| Command | Description |
|---------|-------------|
| `/set wordwrap` | Enable word wrap in output |
| `/set nowordwrap` | Disable word wrap in output |
| `/set verbose` | Show LLM statistics |
| `/set quiet` | Disable LLM statistics |

### Output Formatting

| Command | Description |
|---------|-------------|
| `/set format json` | Enable JSON output mode |
| `/set noformat` | Disable special formatting |

### Thinking Mode

| Command | Description |
|---------|-------------|
| `/set think` | Enable thinking/reasoning mode |
| `/set nothink` | Disable thinking mode |

### Examples

```bash
# Set a new system prompt
/set system "You are a helpful Python programming assistant."

# Enable verbose output to see token stats
/set verbose

# Enable JSON mode for structured output
/set format json

# Enable thinking mode for complex reasoning
/set think
```

---

## Parameter Configuration

Fine-tune model behavior with parameter adjustments.

### Base Command

```bash
/set parameter
```

### Available Parameters

#### Core Generation Parameters

| Parameter | Command | Range/Type | Description |
|-----------|---------|------------|-------------|
| **seed** | `/set parameter seed <int>` | Integer | Random seed for reproducibility |
| **num_predict** | `/set parameter num_predict <int>` | Integer | Maximum tokens to generate |
| **temperature** | `/set parameter temperature <float>` | 0.0 - 2.0 | Creativity level (lower = focused, higher = creative) |

#### Sampling Parameters

| Parameter | Command | Range/Type | Description |
|-----------|---------|------------|-------------|
| **top_k** | `/set parameter top_k <int>` | Integer | Select from top-K tokens |
| **top_p** | `/set parameter top_p <float>` | 0.0 - 1.0 | Nucleus sampling threshold |
| **min_p** | `/set parameter min_p <float>` | 0.0 - 1.0 | Minimum probability threshold |

#### Context and Memory

| Parameter | Command | Range/Type | Description |
|-----------|---------|------------|-------------|
| **num_ctx** | `/set parameter num_ctx <int>` | Integer | Context window size (tokens) |

#### Repetition Control

| Parameter | Command | Range/Type | Description |
|-----------|---------|------------|-------------|
| **repeat_penalty** | `/set parameter repeat_penalty <float>` | 0.0 - 2.0 | Penalize repeated tokens |
| **repeat_last_n** | `/set parameter repeat_last_n <int>` | Integer | Size of repetition detection window |

#### Hardware Acceleration

| Parameter | Command | Range/Type | Description |
|-----------|---------|------------|-------------|
| **num_gpu** | `/set parameter num_gpu <int>` | Integer | Number of layers offloaded to GPU |

#### Stop Sequences

| Parameter | Command | Type | Description |
|-----------|---------|------|-------------|
| **stop** | `/set parameter stop <string> <string> ...` | String(s) | Define custom stop tokens |

---

### Parameter Examples

```bash
# Set temperature for more creative responses
/set parameter temperature 0.9

# Limit response length
/set parameter num_predict 500

# Increase context window
/set parameter num_ctx 8192

# Add custom stop sequence
/set parameter stop "###" "END"

# Reduce repetition
/set parameter repeat_penalty 1.2

# Set seed for reproducible outputs
/set parameter seed 42

# Optimize for GPU
/set parameter num_gpu 50
```

---

### Parameter Quick Guide

#### For Factual/Technical Tasks
```bash
/set parameter temperature 0.3
/set parameter top_p 0.9
/set parameter repeat_penalty 1.1
```

#### For Creative Writing
```bash
/set parameter temperature 1.2
/set parameter top_p 0.95
/set parameter repeat_penalty 1.3
```

#### For Code Generation
```bash
/set parameter temperature 0.2
/set parameter num_ctx 8192
/set parameter top_k 40
```

---

## Session Management

Save and load your conversation sessions.

### Save Current Session

```bash
/save <model>
```
Save your current conversation session

**Example:**
```bash
/save my-coding-session
```

### Load Saved Session

```bash
/load <model>
```
Load a previously saved session or switch models

**Example:**
```bash
/load my-coding-session
```

---

## Quick Reference

### Command Categories

| Category | Commands |
|----------|----------|
| **Exit** | `/bye` |
| **Clear** | `/clear` |
| **Help** | `/help`, `/?`, `/? shortcuts` |
| **Show** | `/show info`, `/show license`, `/show modelfile`, `/show parameters`, `/show system`, `/show template` |
| **Set System** | `/set system <string>`, `/set history`, `/set nohistory` |
| **Set Display** | `/set wordwrap`, `/set nowordwrap`, `/set verbose`, `/set quiet` |
| **Set Format** | `/set format json`, `/set noformat` |
| **Set Mode** | `/set think`, `/set nothink` |
| **Session** | `/save <model>`, `/load <model>` |

### Keyboard Shortcuts

To see available keyboard shortcuts in an active session:

```bash
/? shortcuts
```

---

## Common Workflows

### 1. Starting a New Conversation

```bash
# Pull and run a model
ollama pull llama2
ollama run llama2

# Set system prompt
/set system "You are a helpful assistant specialized in Python."

# Enable verbose mode to see stats
/set verbose
```

---

### 2. Configuring for Code Generation

```bash
ollama run codellama

# Optimize for code
/set parameter temperature 0.2
/set parameter num_ctx 8192
/set parameter top_p 0.95

# Set system prompt
/set system "You are an expert programmer. Provide clean, well-commented code."
```

---

### 3. Creative Writing Session

```bash
ollama run llama2

# Configure for creativity
/set parameter temperature 1.3
/set parameter top_p 0.95
/set parameter repeat_penalty 1.2

# Set creative system prompt
/set system "You are a creative writing assistant. Be imaginative and descriptive."

# Enable thinking mode for better narratives
/set think
```

---

### 4. Debugging and Testing

```bash
ollama run llama2

# Enable verbose stats
/set verbose

# Set seed for reproducibility
/set parameter seed 42

# Test with different temperatures
/set parameter temperature 0.5
# ... test prompts ...

/set parameter temperature 0.8
# ... test again ...
```

---

### 5. Working with Sessions

```bash
# Start working
ollama run llama2
# ... have conversation ...

# Save your progress
/save my-research-session

# Later, resume
ollama run llama2
/load my-research-session
# ... continue where you left off ...
```

---

## Tips and Best Practices

### 🎯 Model Selection
- Use `ollama ls` to see available models
- Choose model size based on your hardware
- Smaller models (7B) are faster, larger (70B) are more capable

### 🔧 Parameter Tuning
- Start with defaults, adjust gradually
- Lower temperature (0.1-0.4) for factual/technical tasks
- Higher temperature (0.8-1.5) for creative tasks
- Use `repeat_penalty` between 1.1-1.3 to reduce repetition

### 💾 Context Management
- Clear context with `/clear` when switching topics
- Increase `num_ctx` for longer conversations
- Monitor memory usage with larger context windows

### 🚀 Performance
- Use `num_gpu` to leverage GPU acceleration
- Smaller `num_predict` values generate faster responses
- Enable `/set quiet` to reduce output overhead

### 📝 Session Management
- Save important conversations with `/save`
- Use descriptive names for saved sessions
- Load sessions to continue previous work

### 🔍 Debugging
- Use `/set verbose` to see generation statistics
- Check parameters with `/show parameters`
- Review system prompt with `/show system`
- Set seed for reproducible results during testing

---

## Advanced Usage

### JSON Mode for Structured Output

```bash
ollama run llama2

# Enable JSON mode
/set format json

# Set appropriate system prompt
/set system "You are a JSON generator. Output only valid JSON."

# Lower temperature for consistent formatting
/set parameter temperature 0.3
```

**Example prompt:**
```
Generate a JSON object for a user profile with name, age, and hobbies.
```

---

### Multi-Modal Input (if supported)

```bash
# Some models support image input
ollama run llava

# Then you can describe images or ask questions about them
```

---

### Chaining Commands

```bash
# Run model with immediate configuration
ollama run llama2
/set parameter temperature 0.5
/set verbose
/set system "You are a helpful assistant."
```

---

## Troubleshooting

### Model Not Found
```bash
# List available models
ollama ls

# Pull the model if needed
ollama pull <modelname>
```

### Out of Memory
```bash
# Reduce context window
/set parameter num_ctx 2048

# Reduce GPU layers
/set parameter num_gpu 0
```

### Slow Generation
```bash
# Reduce output length
/set parameter num_predict 256

# Check GPU usage
/set parameter num_gpu 35
```

### Repetitive Output
```bash
# Increase repeat penalty
/set parameter repeat_penalty 1.3

# Adjust temperature
/set parameter temperature 0.8
```

---

## Official Resources

- **Official Website:** https://ollama.ai
- **GitHub Repository:** https://github.com/ollama/ollama
- **Model Library:** https://ollama.ai/library
- **Documentation:** https://github.com/ollama/ollama/tree/main/docs
- **Discord Community:** https://discord.gg/ollama

---

## Quick Command Summary

```bash
# Model Management
ollama ls                              # List models
ollama pull <model>                    # Download model
ollama rm <model>                      # Remove model
ollama run <model>                     # Run interactively
ollama run <model> "prompt"            # Single prompt

# In-Session Commands
/bye                                   # Exit
/clear                                 # Clear context
/help                                  # Show help
/show parameters                       # View settings
/set parameter temperature 0.7         # Adjust param
/set system "prompt"                   # Set system msg
/save <name>                           # Save session
/load <name>                           # Load session
```

---

**Version:** Ollama CLI v1.0+  
**Last Updated:** 2024  
**Document Type:** Reference Guide

---

*For the most up-to-date information, always refer to the official Ollama documentation.*

**End of Cheat Sheet** 🦙
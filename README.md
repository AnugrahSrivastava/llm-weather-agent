# LLM Weather Agent

This project is a modular AI agent that fetches real-time weather data using external APIs and explains the results using a Large Language Model (LLM).

The agent is designed with a clean separation of concerns:
- *LLM reasoning layer* for decision-making
- *Deterministic tool layer* for reliable weather data
- *Persistent memory layer* for stateful behavior across runs
- *Narration layer* that converts structured data into natural language

The system uses a Groq-hosted LLaMA model via an OpenAI-compatible API and follows modern agent design principles used in production AI systems.
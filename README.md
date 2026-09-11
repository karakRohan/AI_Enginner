# 🤖 AI Engineering Journey — 2026

> 🚀 My journey from Software Developer to AI Engineer  
> 📚 Learning through hands-on projects, real-world systems, and production-focused AI engineering.

---

## 🌟 About This Repository

This repository contains my complete **AI Engineering learning journey**.

I am following a structured roadmap focused on building practical AI systems rather than only studying theory.

The goal is simple:

> **Learn → Build → Evaluate → Deploy → Document → Get Job-Ready**

The learning path covers:

- 🧠 LLM Fundamentals
- ✍️ Prompt Engineering
- 🔌 LLM APIs
- 📦 Structured Outputs
- 📚 RAG
- 🔎 Semantic Search
- 🗄️ Vector Databases
- ⚡ Advanced RAG
- 🤖 AI Agents
- 🔗 LangGraph
- 🔌 MCP
- 👥 Multi-Agent Systems
- 📊 Evaluation
- 🛡️ AI Security & Guardrails
- 🔭 Observability
- 🚀 Deployment
- 🎯 AI System Design
- 💼 Interview Preparation

---

# 🗺️ AI Engineering Roadmap

```text
                         ┌───────────────────────┐
                         │   Python + Git        │
                         │      Foundation      │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   🧠 LLM FUNDAMENTALS │
                         │ Tokens • Context      │
                         │ Temperature • APIs    │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │ ✍️ PROMPT ENGINEERING │
                         │ Few-shot • ReAct      │
                         │ Structured Output     │
                         └───────────┬───────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │          📚 RAG SYSTEMS         │
                    │                                │
                    │ Documents → Chunking           │
                    │      ↓                         │
                    │ Embeddings → Vector DB         │
                    │      ↓                         │
                    │ Retrieval → LLM → Answer       │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │      ⚡ ADVANCED RAG            │
                    │                                │
                    │ Hybrid Search                  │
                    │ Reranking                      │
                    │ Query Rewriting                │
                    │ Contextual Retrieval            │
                    │ RAG Evaluation                 │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │          🤖 AI AGENTS           │
                    │                                │
                    │ Function Calling               │
                    │ Tool Use                       │
                    │ ReAct                          │
                    │ Agent Memory                   │
                    │ LangGraph                      │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │       👥 MULTI-AGENT            │
                    │                                │
                    │ Supervisor                     │
                    │ Planner                        │
                    │ Executor                       │
                    │ Reviewer                       │
                    │ MCP                            │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │ 🛡️ PRODUCTION AI               │
                    │                                │
                    │ Observability                  │
                    │ Guardrails                     │
                    │ Security                       │
                    │ Evaluation                     │
                    │ Cost Optimization              │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │       🚀 DEPLOYMENT             │
                    │                                │
                    │ FastAPI                        │
                    │ Docker                         │
                    │ Cloud Deployment               │
                    │ CI/CD                          │
                    └────────────────┬───────────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │ 💼 AI ENGINEER READY  │
                         │ Projects • Resume     │
                         │ System Design • Jobs  │
                         └───────────────────────┘
📅 Learning Roadmap
Week	Focus Area	Main Project / Deliverable
01	🧠 LLM Fundamentals	Multi-provider LLM application
02	✍️ Prompt Engineering	Structured extraction pipeline
03	📚 RAG Foundations	Document Q&A System
04	⚡ Advanced RAG	Evaluated RAG System
05	🤖 AI Agents	Autonomous Research Agent
06	👥 Multi-Agent + MCP	Multi-Agent Workflow
07	🛡️ Production AI	Observable & secure AI system
08	🚀 Deployment	Full-Stack AI Product
09	💼 Interview Prep	AI System Design + Interview Questions
10	🎯 Resume & Portfolio	Job-ready AI Engineer Portfolio

The course structure includes approximately 44 episodes across the core and bonus modules.

🧠 01 — LLM Fundamentals
Topics
What is an LLM?
Tokens
Context Window
Temperature
Top-p
System / User / Assistant roles
Hallucinations
LLM APIs
Streaming
Async calls
Retries
Rate limits
Model selection
Cost optimization
🔨 Project

Multi-Provider LLM Chatbot

                 User
                   │
                   ▼
          ┌────────────────┐
          │  LLM Router    │
          └───────┬────────┘
                  │
       ┌──────────┼──────────┐
       ▼          ▼          ▼
    OpenAI      Groq      Gemini
       │          │          │
       └──────────┼──────────┘
                  ▼
              Response
Skills
Python
LLM APIs
Streaming
Error Handling
Retries
Model Routing
✍️ 02 — Prompt Engineering
Topics
Production prompts
Zero-shot prompting
Few-shot prompting
Chain-of-Thought
ReAct
Prompt chaining
Meta prompting
Prompt injection
Output validation
Structured output
🔨 Project

Production Data Extraction Pipeline

PDF / Email
     │
     ▼
   LLM
     │
     ▼
Structured JSON
     │
     ▼
Pydantic Validation
     │
     ▼
Reliable Data
📚 03 — RAG Foundations

This is one of the most important parts of my AI Engineering journey.

RAG Pipeline
              📄 Documents
                    │
                    ▼
                Chunking
                    │
                    ▼
               Embeddings
                    │
                    ▼
              🗄️ Qdrant
                    │
                    │
User Question ──────┘
       │
       ▼
   Embedding
       │
       ▼
 Vector Search
       │
       ▼
Relevant Context
       │
       ▼
      LLM
       │
       ▼
  Final Answer
Topics
What is RAG?
Document ingestion
Chunking
Embeddings
Vector databases
Similarity search
Qdrant
Retrieval
Context construction
Grounded generation
🔨 Project

📄 Document Q&A System

Users can upload documents and ask questions based on their content.

⚡ 04 — Advanced RAG & Evaluation

Basic RAG is not enough.

The goal is to understand how to measure and improve retrieval quality.

Topics
🔎 Hybrid Search
🔄 Reranking
🧠 Query Rewriting
🔍 Multi-query Retrieval
📌 Contextual Retrieval
📊 RAG Evaluation
RAGAS
Faithfulness
Answer Relevancy
Context Precision
Context Recall
Advanced Pipeline
                User Query
                     │
                     ▼
              Query Rewriting
                     │
              ┌──────┴──────┐
              ▼             ▼
        Semantic Search   BM25
              │             │
              └──────┬──────┘
                     ▼
              Hybrid Results
                     │
                     ▼
                  Reranker
                     │
                     ▼
              Relevant Context
                     │
                     ▼
                    LLM
                     │
                     ▼
              Final Answer
                     │
                     ▼
                📊 Evaluation
🤖 05 — AI Agents

Moving from:

User → LLM → Answer

to:

User
 ↓
Agent
 ↓
Think
 ↓
Choose Tool
 ↓
Execute Tool
 ↓
Observe Result
 ↓
Continue / Finish
Topics
Function Calling
Tool Use
ReAct
Agent loops
Agent memory
State management
LangGraph
Human-in-the-loop
🔨 Project

🔎 Autonomous Research Agent

                   User Query
                       │
                       ▼
                  🧠 Planner
                       │
              ┌────────┼────────┐
              ▼        ▼        ▼
            Search   Research  Tools
              │        │        │
              └────────┼────────┘
                       ▼
                  📝 Synthesizer
                       │
                       ▼
                  📚 Citations
                       │
                       ▼
                  Final Answer
👥 06 — Multi-Agent Systems + MCP
Multi-Agent Architecture
                    👑 Supervisor
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       🔎 Researcher   ✍️ Writer      🔍 Reviewer
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                    Final Output
Topics
Supervisor Pattern
Swarm Pattern
Hierarchical Agents
Agent Handoff
MCP
MCP Server
MCP Client
Tool Integration
🔨 Project

Multi-Agent Workflow with MCP

🛡️ 07 — Production AI

A demo is not a production system.

This stage focuses on making AI systems:

Reliable
   +
Observable
   +
Secure
   +
Evaluated
   +
Cost Efficient
Topics
🔭 Observability
📊 Continuous Evaluation
🛡️ Guardrails
🔐 AI Security
Prompt Injection
PII Protection
Output Validation
Cost Optimization
Latency Optimization
Semantic Caching
Production Architecture
                     AI APPLICATION
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        🔭 Tracing     📊 Evals      🛡️ Guardrails
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                       LLM Layer
                           │
                           ▼
                    Production API
🚀 08 — Deployment

The goal is not just:

"It works on my laptop."

The goal is:

"It is deployed and accessible."

Topics
FastAPI
Async APIs
Streaming
WebSockets
Docker
Environment Variables
Cloud Deployment
CI/CD
Deployment Architecture
                    🌍 INTERNET
                         │
                         ▼
                  ┌─────────────┐
                  │   Frontend  │
                  │    React    │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   Backend   │
                  │ Node/FastAPI│
                  └──────┬──────┘
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          MongoDB      Qdrant      Redis
             │           │           │
             └───────────┼───────────┘
                         ▼
                    🤖 AI / LLM
🏆 Hero Projects

My goal is to build multiple practical projects throughout this journey.

📄 Project 01 — Production RAG System

AI Research Assistant

Features:

PDF upload
Document processing
Embeddings
Vector search
Semantic retrieval
Cited answers
Confidence scoring
Evaluation
🤖 Project 02 — Autonomous Research Agent

An AI agent that:

Query
 ↓
Research
 ↓
Search
 ↓
Analyze
 ↓
Synthesize
 ↓
Cite
 ↓
Answer

Built using agentic workflows and tool use.

💼 Project 03 — Full-Stack AI Product

A complete AI-powered web application with:

React frontend
Backend API
AI service
Streaming
Authentication
Database
Evaluation
Deployment
🧰 Tech Stack
💻 Programming
Python
JavaScript
TypeScript
SQL
🤖 AI / LLM
LLMs
Prompt Engineering
Structured Outputs
Function Calling
RAG
AI Agents
Multi-Agent Systems
🔎 AI Infrastructure
Sentence Transformers
Embeddings
Qdrant
Vector Search
RAGAS
LangGraph
MCP
⚙️ Backend
FastAPI
Node.js
Express.js
REST APIs
WebSockets
🗄️ Databases
MongoDB
PostgreSQL
Redis
Qdrant
🚀 DevOps
Git
GitHub
Docker
CI/CD
Cloud Deployment
📊 My Learning Philosophy

I don't want to only watch tutorials.

For every topic:

              📚 LEARN
                 │
                 ▼
              🧠 UNDERSTAND
                 │
                 ▼
              💻 BUILD
                 │
                 ▼
              🧪 TEST
                 │
                 ▼
              📊 EVALUATE
                 │
                 ▼
              🚀 DEPLOY
                 │
                 ▼
              📝 DOCUMENT
                 │
                 ▼
              💼 ADD TO PORTFOLIO
🎯 Interview Preparation

Alongside technical projects, I am preparing for AI Engineer interviews.

🧠 LLM Questions
What is a token?
What is a context window?
What is temperature?
Why do hallucinations happen?
How do you handle rate limits?
How do you select an LLM?
📚 RAG Questions
What is RAG?
What are embeddings?
How does vector search work?
How do you choose chunk size?
RAG vs Fine-tuning?
What is hybrid search?
What is reranking?
How do you evaluate RAG?
🤖 Agent Questions
What is an AI agent?
Agent vs Chain?
What is ReAct?
What is function calling?
When should you use agents?
What is LangGraph?
What is MCP?
🏗️ System Design

I am also learning to design:

AI Chatbot
RAG Platform
AI Research Agent
Customer Support Agent
AI Search System
Multi-Agent Platform
📈 Progress Tracker
Area	Status
🐍 Python	🟡 Learning
🧠 LLM Fundamentals	🟡 Learning
✍️ Prompt Engineering	🟡 Learning
📚 RAG	🟡 Learning
🗄️ Vector Database	🟡 Learning
⚡ Advanced RAG	⬜ Upcoming
🤖 AI Agents	⬜ Upcoming
🔗 LangGraph	⬜ Upcoming
🔌 MCP	⬜ Upcoming
📊 Evaluation	⬜ Upcoming
🛡️ AI Security	⬜ Upcoming
🔭 Observability	⬜ Upcoming
🚀 Deployment	⬜ Upcoming
💼 System Design	⬜ Upcoming
🎯 Interview Preparation	⬜ Upcoming

🟡 Currently Learning
🟢 Completed
⬜ Upcoming

📂 Repository Structure
AI-Engineering/
│
├── 01-llm-fundamentals/
│   ├── api-basics/
│   ├── streaming/
│   ├── structured-output/
│   └── model-routing/
│
├── 02-prompt-engineering/
│   ├── prompting/
│   ├── few-shot/
│   ├── react/
│   └── prompt-security/
│
├── 03-rag/
│   ├── embeddings/
│   ├── chunking/
│   ├── qdrant/
│   ├── retrieval/
│   └── rag-v1/
│
├── 04-advanced-rag/
│   ├── hybrid-search/
│   ├── reranking/
│   ├── query-rewriting/
│   └── evaluation/
│
├── 05-agents/
│   ├── function-calling/
│   ├── react-agent/
│   ├── langgraph/
│   └── research-agent/
│
├── 06-multi-agent-mcp/
│   ├── multi-agent/
│   ├── mcp/
│   └── workflows/
│
├── 07-production-ai/
│   ├── observability/
│   ├── guardrails/
│   ├── security/
│   └── optimization/
│
├── 08-deployment/
│   ├── fastapi/
│   ├── docker/
│   └── deployment/
│
└── README.md
🌱 What I Want to Become
Software Developer
        │
        ▼
Full-Stack Developer
        │
        ▼
AI Application Developer
        │
        ▼
AI Engineer
        │
        ▼
🚀 Production AI Engineer

My goal is to become an engineer who can take an AI idea from:

Problem → Architecture → Development → Evaluation → Deployment

⭐ Current Focus

Right now, I am focusing on:

🧠 LLMs
     ↓
📚 RAG
     ↓
🔎 Embeddings
     ↓
🗄️ Qdrant
     ↓
🤖 AI Applications

Next:

⚡ Advanced RAG
      ↓
🤖 Agents
      ↓
🔗 LangGraph
      ↓
🔌 MCP
      ↓
🛡️ Production AI
      ↓
🚀 Deployment
📚 Learning Source

I am following the Padho with Pratyush — The AI Engineer Course, a practical AI Engineering roadmap covering LLMs, RAG, agents, evaluation, production systems, deployment, interview preparation, and portfolio development.

🤝 Connect With Me

I'm documenting my AI Engineering journey through:

💻 GitHub Projects
🧠 Technical Notes
🚀 Real-world AI Applications
📊 Experiments & Evaluations
🎯 Interview Preparation
⭐ Final Goal

Don't just learn AI. Build AI systems.

             LEARN
               ↓
             BUILD
               ↓
            EVALUATE
               ↓
            DEPLOY
               ↓
           DOCUMENT
               ↓
            GET HIRED 🚀
🚀 Let's Build the Future with AI.

Learning in public • Building in public • Growing every day.

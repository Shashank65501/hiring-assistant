# TalentScout Hiring Assistant

## Overview
An AI-powered Hiring Assistant chatbot built using Streamlit and OpenAI GPT.  
It collects candidate details and generates technical interview questions based on their declared tech stack.

## Features
- Collects candidate details (Name, Email, Phone, Experience, Position, Location, Tech Stack)
- Generates 3–5 technical questions per technology
- Context-aware conversation
- Graceful exit with 'bye' or 'exit'

## Installation & Execution
1. Clone or extract this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API Key:
   ```bash
   export OPENAI_API_KEY="your_api_key"
   ```
   (On Windows PowerShell)
   ```powershell
   setx OPENAI_API_KEY "your_api_key"
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## File Structure
- app.py → Main Streamlit app
- prompts.py → Prompt templates
- utils.py → Helper functions (OpenAI calls, save data)
- requirements.txt → Dependencies
- README.md → Documentation

## Notes
- Candidate data is saved in `candidates.json`.
- Replace `gpt-4o-mini` with `gpt-3.5-turbo` if you don't have GPT-4 access.

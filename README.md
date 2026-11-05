# Arabic RAG over Monsha'at documents

An assistant that answers Arabic questions (MSA and Saudi dialect) from the official
Arabic documents of Monsha'at (Saudi SME General Authority), with citations, and that
says when the documents don't contain the answer.

## Layout
```
data/raw/         original PDFs 
data/processed/   extracted text + metadata 
eval/             eval questions 
src/arabic_rag/   the package: normalize, extract, later retrieve / generate
tests/            pytest
notebooks/        exploration
```

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Status
Week 1: data collection and extraction check.

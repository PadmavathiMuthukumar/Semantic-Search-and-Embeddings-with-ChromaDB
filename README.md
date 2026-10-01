# Semantic Search and Embeddings with ChromaDB Using Manual Cosine Similarity

## Overview

This project demonstrates how text is converted into embeddings, stored in ChromaDB, and compared using cosine similarity. It also demonstrates how updating a document changes its embedding and can change similarity results.

## Architecture

```text
Document
   |
   v
Text / Chunks
   |
   v
Embedding Model
   |
   v
Numerical Embedding
   |
   v
ChromaDB
   |
   v
Similarity Search
   |
   v
Cosine Similarity
```

## What is an Embedding?

An embedding is a numerical vector representation of text.

```text
"Bus carries passengers on road"
              |
              v
       Embedding Model
              |
              v
[0.00808992, -0.02653399, 0.01265642, ...]
```

The complete vector represents semantic information about the text. Similar meanings can produce vectors that are closer in vector space.

## Actual Embeddings

### Bus

```text
bus1: Bus carries passengers on road

[ 0.00808992 -0.02653399  0.01265642  0.01231874 -0.02361063
  0.05925349  0.15521619  0.03143324  0.00659038 -0.03993003]
```

### Plane

```text
plane1: Plane flies across countries

[ 0.07562239  0.00110504 -0.02992569  0.02506334  0.07302137
 -0.03711773  0.06621208 -0.03773622  0.01575838  0.0378425 ]
```

### Boat

```text
boat1: Boat travels on water

[-0.02455844 -0.00075793 -0.04086314  0.0331099   0.0217488
 -0.06150616  0.0467108   0.03198811 -0.05216501 -0.02883329]
```

### Bicycle

```text
cycle1: Bicycle runs without fuel

[ 0.04353345  0.12895897 -0.06367305  0.06100694  0.060069
 -0.01013913 -0.04134094 -0.0041845   0.00986821 -0.04822373]
```

Only the first 10 values are shown. The actual embedding contains more dimensions.

## How ChromaDB Stores Embeddings

```text
Document
   |
   v
Embedding Model
   |
   v
Embedding Vector
   |
   v
ChromaDB

ChromaDB stores:
- Document ID
- Document text
- Embedding
- Metadata (if provided)
```

Example:

```text
ID: bus1
Document: Bus carries passengers on road
Embedding: [0.00808992, -0.02653399, ...]
```

## Cosine Similarity

Cosine similarity measures the similarity between two vectors.

```text
                 A · B
Cosine Similarity = ---------
                    |A| |B|
```

Generally:

```text
Higher similarity -> More similar direction
Lower similarity  -> Less similar direction
```

## Before Document Update

Original bus document:

```text
Bus carries passengers on road
```

Results:

```text
cosine similarity between car and bus:
0.1876521261919475

cosine similarity between bus and cycle:
0.15493369906455554
```

## Updating the Document

The bus document was changed to:

```text
bus runs on electricity instead of petrol
```

Because the text changed, the embedding generated for the bus document also changed.

```text
Old Text
   |
   v
Old Embedding

        UPDATE

New Text
   |
   v
Embedding Model
   |
   v
New Embedding
```

### New Bus Embedding

```text
[ 0.03717894  0.04260495  0.03936166  0.03019376  0.04284778
 -0.02089098 -0.00845509  0.05006164  0.04383188 -0.08972082]
```

The other documents were unchanged, so their embeddings remained unchanged.

## After Document Update

```text
cosine similarity between car and bus:
0.11208743561040484

cosine similarity between bus and cycle:
0.15493369906455554
```

### Before vs After

| Comparison | Before | After |
|---|---:|---:|
| Car vs Bus | 0.1876521261919475 | 0.11208743561040484 |
| Bus vs Bicycle | 0.15493369906455554 | 0.15493369906455554 |

### What Changed?

Car vs Bus:

```text
Before: 0.1876521261919475
After:  0.11208743561040484
```

The similarity decreased because the bus document's semantic content changed and therefore its embedding changed.

Bus vs Bicycle:

```text
Before: 0.15493369906455554
After:  0.15493369906455554
```

This remained unchanged because the bicycle document was not updated.

The important relationship is:

```text
Document changes
      |
      v
Embedding is regenerated
      |
      v
Vector changes
      |
      v
Similarity results can change
```

## Embedding Model vs LLM

An embedding model and an LLM both process language, but their primary purposes are different.

### Embedding Model

```text
Text
 |
 v
Embedding Model
 |
 v
Numerical Vector
```

Its main purpose is to create vectors useful for:

- Semantic search
- Similarity comparison
- Retrieval
- Clustering

Example:

```text
all-MiniLM-L6-v2
```

### LLM

An LLM is designed to process language and generate language.

A simplified process is:

```text
Text
 |
 v
Tokenization
 |
 v
Token IDs
 |
 v
Internal Embeddings
 |
 v
Transformer
 |
 v
Context Processing
 |
 v
Next Token Prediction
 |
 v
Generated Text
```

Examples include GPT, Llama, and Gemini.

An important distinction is that an LLM also has embeddings internally. However, those embeddings are only one part of the complete LLM architecture.

```text
Embedding Model
= Mainly creates semantic vectors

LLM
= Uses internal representations and Transformer processing
  to understand context and generate language
```

## RAG Flow

```text
PDF / Document
      |
      v
Text Extraction
      |
      v
Chunking
      |
      v
Embedding Model
      |
      v
Embeddings
      |
      v
ChromaDB
      |
      |
User Question
      |
      v
Embedding Model
      |
      v
Query Embedding
      |
      v
Similarity Search
      |
      v
Relevant Chunks
      |
      v
LLM
      |
      v
Final Answer
```

## Final Understanding

```text
Embedding Model
    -> Converts text into semantic vectors

ChromaDB
    -> Stores and searches vectors

Cosine Similarity
    -> Compares vectors

LLM
    -> Processes language and generates answers
```

The embedding model handles the representation and retrieval side, while the LLM handles language generation in a typical RAG system.

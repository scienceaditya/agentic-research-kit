# Membrane Trafficking CRISPR Map (concept and framework)

This repo is a public companion to an Agents4Science-style research writeup. It presents a proposal and experimental framework for studying membrane trafficking as an integrated network, not a set of isolated pathways.

Status: concept note and experimental plan. No new experiments or datasets are included here.

How to run:

python3 scripts/validate_papers_csv.py data/papers.csv
python3 scripts/make_status.py --papers data/papers.csv --out STATUS.md
cat STATUS.md

## Why this exists

Membrane trafficking research has produced deep mechanistic insight into individual pathways and complexes. At the same time, multiple lines of evidence suggest trafficking behaves like a coordinated network where perturbations propagate across pathway boundaries.

This project frames three gaps that limit a systems-level understanding of trafficking:
1. Temporal coordination mechanisms across pathways
2. Dynamic, context-dependent assembly of trafficking complexes
3. Systems-level disease mechanisms that span multiple pathways

## Core assumptions this work challenges

Many studies implicitly assume:
- Pathways are mostly independent
- Protein complexes have fixed composition
- Trafficking diseases come from single pathway defects

This framework proposes experiments designed to test these assumptions directly.

## Proposed experimental framework

| Experiment | Assumption tested | Primary method | Output |
|---|---|---|---|
| Pathway cross-talk analysis | Pathway independence | Multi-pathway imaging under perturbations and stress | Cross-correlation network of pathway interactions |
| Dynamic complex assembly | Discrete, static complexes | Quantitative proteomics across contexts plus kinetic readouts | Context-dependent composition changes and functional links |
| Systems-level disease analysis | Single-defect disease models | Network biology across disease mutations and interventions | Network dysfunction signatures and multi-target strategies |

## AI-driven analysis methods (high level)

The framework assumes AI-assisted analysis of multi-dimensional datasets, including:
- Multi-pathway image analysis for organelles, cargo tracking, and interaction modeling
- Integrative modeling for proteomics and composition-function relationships
- Network analysis for disease models using graph-based measures and connectivity patterns

## What is in this repo

- `docs/concept-note.md`  
  A short public concept note describing gaps, assumptions, and proposed experiments.
- `spec/hypotheses-and-success-metrics.md`  
  Falsifiable hypotheses and example thresholds that define “success” for each experiment.
- `data/papers.csv` (optional)  
  A structured index of reviewed papers with tags and takeaways. No full texts are included.

## Transparency: AI involvement

This work was developed with AI assistance. The initial topic was human-chosen with a small set of seed papers. AI supported literature review, drafting, and proposing experiments, with human oversight for scientific consistency and removal of unsupported claims. No experiments were executed as part of this writeup.

## How to use this

If you are working in trafficking, you can treat this as:
- a roadmap for turning pathway-centric biology into network biology
- a starting point for defining falsifiable hypotheses and measurable outputs
- a template for “evaluation-first” experimental planning (clear criteria before data)

## Contact

Aditya Anand  
LinkedIn: www.linkedin.com/in/aditya-anand-278b3a82/
Email: adityaanand131@gmail.com

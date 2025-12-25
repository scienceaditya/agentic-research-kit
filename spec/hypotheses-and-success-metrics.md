# Hypotheses and success metrics

This document defines falsifiable hypotheses and example success criteria for the proposed experimental program. It is intentionally specific about measurable outputs so the plan can be evaluated, iterated, and de-risked with pilots.

Status: planning artifact. No new experiments are reported here.

## Shared definitions

### Pathways (example set)
Choose a small set of trafficking processes that can be monitored in parallel. For example:
- ER to Golgi transport
- Golgi to plasma membrane secretion
- Endocytosis and recycling
- Endosome to lysosome trafficking
- Autophagy flux

Exact definitions and readouts should be written down before data collection.

### Perturbations
Use perturbations that are interpretable and span distinct modules:
- Gene perturbations (CRISPRi or CRISPR KO)
- Acute pharmacology where available
- Stress conditions (nutrient shift, ER stress, oxidative stress, etc.)

### Readouts
Define readouts per pathway. Examples:
- Imaging: cargo localization, organelle morphology, trafficking kinetics, reporter accumulation
- Proteomics: complex composition, stoichiometry proxies, co-enrichment
- Network features: correlation matrices, connectivity, community structure

### Core outputs for all experiments
- Pre-registered hypotheses
- A table of metrics and thresholds
- A failure mode log (what broke and why)
- A minimal pilot result or simulated demonstration (even toy data)

---

## Experiment 1: Pathway cross-talk analysis

### Goal
Test whether trafficking pathways behave as mostly independent modules or show coordinated cross-talk under perturbation and stress.

### Primary hypothesis
H1. Perturbing one pathway produces measurable, condition-dependent effects on other pathways, consistent with cross-talk rather than isolation.

### Null hypothesis
H0. Effects of perturbations remain largely confined to the directly targeted pathway.

### Metrics
Define metrics per pathway, then compute cross-pathway structure:
1. Pairwise correlation between pathway outputs across perturbations
2. Partial correlations controlling for global cell state covariates (cell size, stress markers, cell cycle stage)
3. Graph measures on the inferred interaction network (degree, modularity, clustering)

### Example success criteria (tunable thresholds)
These are placeholders. Adjust based on pilot noise.
- Cross-talk signal: multiple pathway pairs show r^2 above a pre-defined threshold (for example > 0.30) across perturbations or under stress.
- Independence-like regime: most pathway pairs show r^2 below a lower threshold (for example < 0.10) and the network remains highly modular.
- Condition dependence: correlation structure changes across stress conditions beyond what is explained by global covariates.

### Minimum viable pilot
- 3 to 5 pathways
- 10 to 20 perturbations spanning distinct modules
- 2 conditions (baseline and one stress)
Deliverable: a correlation matrix, a network visualization, and a short interpretation plus caveats.

### Common failure modes to watch
- Global stress dominates all readouts (false cross-talk)
- Readouts are not comparable in scale or dynamic range
- Overfitting network structure with too many metrics and too few perturbations

---

## Experiment 2: Dynamic complex assembly analysis

### Goal
Test whether trafficking protein complexes have fixed composition or undergo context-dependent reconfiguration that correlates with functional changes.

### Primary hypothesis
H1. The composition of key trafficking complexes changes across contexts, and these compositional shifts correlate with functional trafficking phenotypes.

### Null hypothesis
H0. Complex composition is stable across contexts, with only minor variation not linked to function.

### Metrics
1. Composition variability across contexts
- Per-subunit abundance changes across contexts (effect size and significance)
- A composition variability score (for example coefficient of variation across contexts)
2. Context separation
- PCA or similar embedding that separates contexts based on complex composition
3. Composition to function link
- Correlation between composition features and functional readouts (from imaging or other assays)
- Predictive performance of a simple model mapping composition to phenotype

### Example success criteria (tunable thresholds)
- Dynamic regime: multiple subunits show statistically significant abundance changes across contexts, and a variability score exceeds a pre-set threshold.
- Functional coupling: a simple predictive model achieves meaningful out-of-sample performance on functional readouts (define a baseline and a minimum improvement).
- Static regime: composition features remain within tight bounds and do not predict phenotype beyond chance.

### Minimum viable pilot
- Choose 1 complex or complex family (for example clathrin adaptor module, retromer-related module, ESCRT module)
- 3 contexts (baseline, stress, and one additional perturbation context)
- 2 functional readouts
Deliverable: one composition table, one visualization of context dependence, and one composition to phenotype test.

### Common failure modes to watch
- Batch effects masquerading as context dependence
- Pull-down specificity issues (composition signal is noisy)
- “Everything changes” under stress, making interpretation difficult without controls

---

## Experiment 3: Systems-level disease analysis

### Goal
Test whether trafficking-related diseases reflect single pathway defects or broader network dysfunction across multiple pathways, and whether multi-target strategies are suggested by network signatures.

### Primary hypothesis
H1. Disease mutations produce network-level dysfunction across multiple pathways, and network signatures suggest multi-target interventions.

### Null hypothesis
H0. Most disease mutations map to a single dominant pathway defect.

### Metrics
1. Breadth of dysfunction
- Number of pathways significantly affected per mutation
- Distribution of effect sizes across pathways
2. Network disruption
- Changes in network connectivity measures relative to baseline
- Community structure changes, hub shifts, or loss of modularity
3. Intervention hypotheses
- Predicted rescue via multi-target vs single-target perturbations (pre-specified scoring)

### Example success criteria (tunable thresholds)
- Systems-dysfunction regime: disease mutations impact multiple pathways above a defined breadth threshold (for example 3 or more pathways) and alter network connectivity measures beyond baseline variation.
- Single-defect regime: effects are concentrated in 1 pathway with minimal network disruption.
- Actionability: the analysis yields a short ranked list of intervention hypotheses with clear rationales and measurable expected outcomes.

### Minimum viable pilot
- 5 to 10 disease-relevant perturbations or mutations (or curated disease gene set)
- The same pathway panel used in Experiment 1
Deliverable: a heatmap of pathway effects per mutation, network features, and a short list of intervention hypotheses.

### Common failure modes to watch
- Confounding by cell type specificity
- Mixed phenotypes that reflect global fitness rather than trafficking
- Over-interpretation of network metrics without experimental validation

---

## Reporting checklist for this repo

When adding any new result or update, include:
- What changed (one sentence)
- What hypothesis it tests
- The metric and threshold used
- A short failure modes note
- Links to the exact data and code used to generate the figure or table

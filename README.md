# The Hive Mind: Graph Neural Cellular Automata (GNCA)

[![Part of](https://img.shields.io/badge/Algoplexity-Horizon%203-purple.svg)](https://github.com/algoplexity/algoplexity) [![Status](https://img.shields.io/badge/Status-Active%20Replication-green.svg)]() [![Framework](https://img.shields.io/badge/Framework-PyTorch%20Geometric-red.svg)]()

**Modeling the Topology of Systemic Contagion.**

This repository represents **Horizon 3** of the [Algoplexity Research Program](https://github.com/algoplexity/algoplexity). While Horizon 1 focused on the *Time Series* (The Neuron), Horizon 3 focuses on the *Network* (The Brain).

We utilize **Graph Neural Cellular Automata (GNCA)** to simulate how "Cognitive Failures" (Rule 54/60) propagate across financial and social networks, creating systemic crises.

---

## 🌌 The Scientific Mission

### The Problem: Algorithmic Monoculture
Modern financial markets are dominated by algorithmic agents. When these agents converge on identical strategies (e.g., "Buy the Dip"), the market's topology shifts from a robust ecology to a brittle monoculture.
*   **The Question:** Can we predict a "Flash Crash" not by looking at prices, but by looking at the **Graph Topology** of agent correlation?
*   **The Hypothesis:** Systemic Risk is a **Phase Transition** in a Graph Cellular Automaton.

### The Method: GNCA
We build upon the foundational work of **Grattarola et al. (NeurIPS 2021)**, who proved that Graph Neural Networks can learn arbitrary Cellular Automata rules. We adapt their physics-based architecture to the domain of **Algorithmic Cognitive Finance**.

---

## 🛠️ The Rosetta Stone: Physics to Finance

We map the hydrodynamic concepts of Grattarola's "Voronoi CA" directly to Systemic Risk concepts.

| Grattarola (Physics) | Algoplexity Horizon 3 (Finance) |
| :--- | :--- |
| **Voronoi Cell** | **Agent / Bank / Asset** |
| **Edge ($E$)** | **Exposure Channel** (Debt, Correlation, Information) |
| **State ($h_i$)** | **Solvency Status** (0=Liquid, 1=Insolvent) |
| **Density ($\rho$)** | **Counterparty Risk** (Weighted sum of failing neighbors) |
| **Transition Rule** | **The Contagion Mechanism** (e.g., Liquidity Cascade) |
| **The Inverse Problem** | **Macro-Prudential Oversight**: Inferring the hidden contagion rule from observed failure history. |

---

## 🔬 The Experiments

### Experiment 1: The Contagion Laboratory (Active)
*   **Goal:** Replicate Grattarola's "Voronoi" experiment using **PyTorch Geometric**.
*   **Setup:** A random geometric graph representing a banking network.
*   **Rule:** A "Threshold Rule" where a node fails if its neighbor exposure exceeds a capital buffer.
*   **Objective:** Train a GNCA to learn this contagion rule purely from observation, without knowing the underlying debt contracts.

### Experiment 2: Algorithmic Monoculture (Planned)
*   **Goal:** Simulate the **UCL/EPSRC** problem statement ("When multiple AI agents converge...").
*   **Setup:** Agents are nodes. Edges represent "Strategy Correlation."
*   **Dynamics:** We model the "Percolation of Rule 54" (Cognitive Saturation). As agents synchronize, the network becomes a superconductor for risk.

---

## 📂 Repository Structure

*   `gnca_lib/`: Core library containing the Message Passing Neural Network (MPNN) architecture.
*   `notebooks/`:
    *   `01_Replication_Contagion.ipynb`: PyTorch implementation of the Financial Contagion CA.
    *   `02_Topology_Stress_Test.ipynb`: Testing network resilience against "Soliton" attacks.
*   `simulation_data/`: Synthetic network snapshots used for training.

---

## 📚 References

1.  **Grattarola, D., Livi, L., & Alippi, C. (2021).** Learning Graph Cellular Automata. *Advances in Neural Information Processing Systems (NeurIPS)*, 34.
2.  **Farmer, J. D., & Skouras, S. (2013).** An ecological perspective on the future of computer trading. *Quantitative Finance*.
3.  **Haldane, A. G., & May, R. M. (2011).** Systemic risk in banking ecosystems. *Nature*, 469.

---

## 🔗 Citation

```bibtex
@misc{algoplexity_horizon3,
  author = {Mak, Yeu Wen},
  title = {The Hive Mind: Modeling Systemic Risk via Graph Neural Cellular Automata},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/algoplexity/hive-mind-gnca}}
}

# The Hive Mind: Graph Neural Cellular Automata

[![Part of](https://img.shields.io/badge/Algoplexity-Horizon%203-purple.svg)](https://github.com/algoplexity/algoplexity) [![Status](https://img.shields.io/badge/Status-Architecture%20Design-blue.svg)]() [![Framework](https://img.shields.io/badge/Framework-PyTorch%20Geometric-orange.svg)]()

**Modeling Systemic Contagion, Algorithmic Monoculture, and Collective Intelligence via Topological Deep Learning.**

This repository hosts **Horizon 3** of the Algoplexity Research Program. While Horizon 1 (The AIT Physicist) diagnoses the *temporal* state of a single asset, Horizon 3 simulates the *spatial* propagation of those states across complex, adaptive networks.

---

## 🌌 The Scientific Mission

**Hypothesis:** Collective phenomena—whether financial crashes, social panics, or organizational groupthink—are **Emergent Computations**. They are the result of local state transitions propagating across a specific topology.

**The Theory:** We model these systems as **Graph Neural Cellular Automata (GNCA)**. By combining the discrete, causal logic of Cellular Automata with the learnable topology of Graph Neural Networks, we aim to detect:
*   **Network Resonance:** The moment when localized interactions synchronize and amplify across the network, leading to rapid state changes (Phase Transitions).
*   **Algorithmic Monoculture:** The collapse of "Cognitive Diversity" (Rule 170) into "Cognitive Saturation" (Rule 54) caused by agents converging on identical strategies.

---

## 🏗️ The Architectural Trinity

To overcome the limitations of standard GNNs—specifically their receptive field limits and "Black Box" nature—we implement a novel architecture based on three state-of-the-art advancements:

### 1. The Engine: Graph ViTCA (Vision Transformer CA)
*   **The Limit:** Standard GNNs suffer from a limited receptive field ($\ell$-hops). They cannot predict "Tele-connected" risks where a shock jumps across the graph instantly.
*   **The Solution:** Adapting **ViTCA [Tesfaldet et al., 2022]** and **Burtsev [2024]** to graph topologies. By replacing local message passing with **Global Self-Attention**, the Hive Mind can simulate long-range "Soliton Fission" events that bypass local neighbors.

### 2. The Constraint: E(n)-Equivariance
*   **The Limit:** Financial and social networks are dynamic and permutation-invariant. A risk model must be robust to graph rotation and node re-indexing.
*   **The Solution:** We enforce **E(n)-Equivariance [Gala et al., 2023]**. The model learns isotropic update rules that depend on the *geometry* of the influence (the shape of the graph), ensuring generalization to unseen network topologies.

### 3. The Dashboard: Differentiable Logic (DiffLogic)
*   **The Limit:** Neural Networks are opaque. A regulator cannot govern a system based on "Weights."
*   **The Solution:** We utilize **Differentiable Logic Gates [Miotti et al., 2024]**. The network learns discrete Boolean rules (AND, OR, XOR), enabling the extraction of human-readable laws: *"If Neighbor_Panic > Threshold AND Self_Liquidity < Low, THEN State = Crash."*

---

## 🌍 Domain Applications & Experimental Roadmap

We apply this architecture to three distinct domains of Collective Intelligence.

### **Application 1: Financial Markets (Systemic Risk)**
*   **Concept:** **The r-GCA (Relation-Based Neighborhood).** Modeling markets not by physical proximity, but by abstract influence graphs (Correlation, Debt, Supply Chain).
*   **The Experiment:** **Modeling Herd Behavior.** We simulate how **Investor Homogeneity** (Strategy Convergence) alters the **Hurst Exponent** of the market, turning a mean-reverting system (Anti-persistent) into a trending crash (Persistent).
*   **Target:** Validating the **"Flash Crash"** mechanism for **UCL/EPSRC Project ID 2531bd1646**.

### **Application 2: Society (Opinion Dynamics)**
*   **Concept:** **Information Cascades.** Modeling the propagation of "Multi-Information" (e.g., Viral Narratives) across a social graph.
*   **The Experiment:** **The Weibo Simulation.** Replicating the SEInR (Susceptible-Exposed-Infected-Recovered) dynamics on a dynamic graph to predict consensus shifts with >98% accuracy.
*   **Mechanism:** Modeling **Network Churn**—the dynamic formation and dissolution of ties based on trust and influence.

### **Application 3: Enterprise (Cybernetic Governance)**
*   **Concept:** **Organizational Consensus.** Modeling a company as a distributed computer.
*   **The Experiment:** **Groupthink vs. Resilience.**
    *   *Scenario A:* Rapid convergence to a low-quality state (Groupthink/Rule 0).
    *   *Scenario B:* Maintenance of complex, diverse states (Innovation/Rule 54).
*   **Target:** Providing the "Systemic Dashboard" for **ANU School of Cybernetics** leadership models.

---

## 📚 The Engineering Canon

This architecture is built upon specific, verified literature in Topological Deep Learning and Complex Systems:

1.  **Grattarola, D., Livi, L., & Alippi, C. (2021).** Learning Graph Cellular Automata. *NeurIPS 2021*. (The Foundational Proof).
2.  **Tesfaldet, M., et al. (2022).** Attention-based Neural Cellular Automata (ViTCA). *NeurIPS 2022*. (The Attention Mechanism).
3.  **Gala, G., et al. (2023).** E(n)-equivariant Graph Neural Cellular Automata. *arXiv:2301.10497*. (The Symmetry Constraint).
4.  **Miotti, P., et al. (2024).** Differentiable Logic Cellular Automata. *arXiv*. (The Interpretability Layer).
5.  **Burtsev, M. S. (2024).** Learning Elementary Cellular Automata with Transformers. *arXiv:2412.01417*. (The Receptive Field Analysis).
6.  **Farmer, J. D., & Skouras, S. (2013).** An ecological perspective on the future of computer trading. *Quantitative Finance*. (Algorithmic Monoculture).

---

## 🔗 Citation

```bibtex
@misc{algoplexity_horizon3,
  author = {Mak, Yeu Wen},
  title = {The Hive Mind: Modeling Systemic Contagion via Graph Neural Cellular Automata},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/algoplexity/hive-mind-gnca}}
}
```

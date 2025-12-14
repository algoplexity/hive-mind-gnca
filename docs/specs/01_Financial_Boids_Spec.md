# Specification: The Financial Liquidity Boids Model (Horizon 3)

**Status:** Draft | **Target:** ANU Advanced Thesis / UCL "Market Dynamics" Project

**Based on:** Grattarola et al. (2021), `boids/` implementation.

---

## 1. Theoretical Premise
Current risk models (VAR) treat assets as static nodes in a correlation matrix. We propose treating assets as **dynamic particles** (Boids) moving through a high-dimensional phase space of Risk and Return.

By adapting the **Reynolds Boids Algorithm** (Alignment, Separation, Cohesion), we can simulate how **Rational Agents** (seeking diversification/Separation) spontaneously transition into **Herding Panics** (Alignment/Cohesion) under stress. This models the **Topology of Contagion** without needing to know the exact debt contracts between institutions.

## 2. The Isomorphism: Physics $\to$ Finance

We map the physical state vectors of the Grattarola codebase to financial state vectors.

| Boids Variable (Physics) | Financial Variable (Systemic Risk) | Semantics |
| :--- | :--- | :--- |
| **Space ($\mathbb{R}^2$)** | **The Risk-Return Plane** | X-axis: Volatility (Risk) <br> Y-axis: Returns (Alpha) |
| **Position ($p_i$)** | **Market State** | Where the asset sits on the Efficient Frontier. |
| **Velocity ($v_i$)** | **Momentum / Flow** | The speed and direction of capital flow into/out of the asset. |
| **Force: Alignment** | **Herding / Beta** | Tendency to move with neighbors (Sector correlation). |
| **Force: Separation** | **Arbitrage / Diversification** | Tendency to avoid crowding (Seeking Alpha / Niche). |
| **Force: Cohesion** | **Mean Reversion** | Tendency to revert to the "Market Average." |
| **Predator** | **External Shock** | An exogenous event (Rule 60) that scatters the flock. |

---

## 3. Mathematical Formulation

### 3.1 The State Vector
For each agent (Node $i$) at time $t$:
$$ \mathbf{h}_i^{(t)} = [\mathbf{p}_i^{(t)}, \mathbf{v}_i^{(t)}] $$
Where $\mathbf{p}$ is the $(Risk, Return)$ coordinate and $\mathbf{v}$ is the rate of change.

### 3.2 The Update Rule (The Differential Equation)
The update follows the standard motion equation, but the **Acceleration** ($a_t$) is computed by the GNN:

$$ \mathbf{v}_i^{(t+1)} = \mathbf{v}_i^{(t)} + \text{GNCA}(\mathbf{h}_i^{(t)}, \mathcal{N}_i) \cdot \Delta t $$
$$ \mathbf{p}_i^{(t+1)} = \mathbf{p}_i^{(t)} + \mathbf{v}_i^{(t+1)} \cdot \Delta t $$

### 3.3 The Learned Forces (The GNCA Task)
Instead of hard-coding Reynolds' rules, the **Graph Neural Cellular Automaton (GNCA)** learns the weighting of these forces from historical data.

$$ \mathbf{a}_i = w_A \sum_{j \in \mathcal{N}} (\mathbf{v}_j) + w_S \sum_{j \in \mathcal{N}} \frac{\mathbf{p}_i - \mathbf{p}_j}{||\mathbf{p}_i - \mathbf{p}_j||^2} + w_C \sum_{j \in \mathcal{N}} (\mathbf{p}_j - \mathbf{p}_i) $$

*   **Crisis State:** When $w_A$ (Alignment) dominates $w_S$ (Separation), the system undergoes a **Phase Transition** from Fluid Market to **Soliton/Shock Wave**.

---

## 4. Neural Architecture (The "Engine")

We adapt the architecture from `models/gnn_ca_simple_boids.py` in the reference codebase.

### Components
1.  **State Encoder:** An MLP mapping the raw financial metrics (Price, Vol, Volume) to the latent Position/Velocity space.
2.  **EdgeConv Layer (The "Vision"):**
    *   Crucial for Boids. Standard GCN assumes fixed edges. `EdgeConv` (Wang et al., 2019) constructs graphs dynamically based on distance in feature space.
    *   *Financial Meaning:* Assets are "connected" if they behave similarly (Distance in Risk space), not just if they are in the same sector.
3.  **Update MLP:** Computes the acceleration vector (The "Nudge").

### PyTorch Specification
```python
class FinancialBoidsGNCA(nn.Module):
    def __init__(self, state_dim=4, hidden_dim=128):
        super().__init__()
        # 1. Physical Forces (EdgeConv)
        # Calculates relative distance in Risk/Return space
        self.edge_conv = DynamicEdgeConv(
            nn.Sequential(
                nn.Linear(state_dim * 2, hidden_dim),
                nn.ReLU(),
                nn.Linear(hidden_dim, hidden_dim) # Output: Force Vector
            ), 
            k=10 # Nearest Neighbors (e.g., 10 most correlated assets)
        )
        
        # 2. Intrinsic Momentum (GRU/RNN)
        # Models the inertia of the asset itself
        self.gru = nn.GRUCell(hidden_dim, hidden_dim)
        
        # 3. decoder
        self.decoder = nn.Linear(hidden_dim, state_dim) # Outputs Delta_V

    def forward(self, x, batch):
        # x: [Num_Assets, State_Dim] (Pos + Vel)
        
        # Calculate Social Forces (Herding/Arbitrage)
        social_forces = self.edge_conv(x, batch)
        
        # Update Internal State
        h_new = self.gru(social_forces, x)
        
        # Calculate Acceleration
        delta_v = self.decoder(h_new)
        return delta_v
```

---

## 5. Training Strategy: The "Replay" Requirement

As identified in the forensic audit of Grattarola's code, we must implement **State Caching**.

*   **Problem:** If we train only $t \to t+1$, the model learns to "jitter" but not to "flow."
*   **Solution:** We maintain a **Pool of 1024 Market Scenarios**.
*   **Training Step:**
    1.  Sample a random batch of Market States from the Pool.
    2.  Evolve them for $K$ steps using the GNCA.
    3.  Compute Loss (MSE vs Real Market Data).
    4.  Backpropagate through time.
    5.  Place the *evolved* states back into the Pool.
*   **Outcome:** The model learns **Long-Term Stability** (QCEA Law 14). It learns to simulate a 3-month crash without the simulation itself crashing.

---

## 6. Research Goals (PhD Application)

1.  **Replication:** Can this architecture reproduce the "Stylized Facts" of financial markets (Fat tails, volatility clustering) purely from Boid-like interaction rules?
2.  **Control:** Can we introduce a **"Regulatory Agent"** (A Shepherd Dog) that applies a counter-force to break up "Herding" clusters before they crash?
3.  **Universality:** Does this model align with the **Soliton Fission** models used in Hydrodynamics (UCL Project)?

---

### **Next Steps**
1.  Implement the **PyTorch Geometric** version of `EdgeConv`.
2.  Build the **State Cache** class.
3.  Source a "Sectoral" dataset (e.g., S&P 500 constituents) to train the alignment forces.

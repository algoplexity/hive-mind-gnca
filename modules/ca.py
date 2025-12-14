import torch
import networkx as nx
from torch_geometric.utils import from_networkx

class FinancialContagionCA:
    """
    The Ground Truth Generator.
    Simulates a banking network where insolvency spreads via debt links.
    
    Rule: A node turns '1' (Insolvent) if the weighted sum of its '1' neighbors
    exceeds its Capital Buffer (Threshold).
    """
    def __init__(self, num_nodes=100, edge_prob=0.1, capital_buffer=0.3, seed=42):
        self.num_nodes = num_nodes
        self.buffer = capital_buffer
        
        # Set seed for topological reproducibility
        torch.manual_seed(seed)
        
        # 1. Generate the Topology (The Interbank Network)
        # We use Erdos-Renyi for the baseline contagion experiment
        self.G = nx.erdos_renyi_graph(n=num_nodes, p=edge_prob, seed=seed)
        
        # Convert to PyTorch Geometric Data format
        self.data = from_networkx(self.G)
        
        # Create Normalized Adjacency Matrix for efficient calculation
        # A_norm = D^-1 * A (Row-normalized: percentage of exposure)
        adj_numpy = nx.to_numpy_array(self.G)
        deg = adj_numpy.sum(axis=1, keepdims=True)
        deg[deg == 0] = 1 # Avoid div by zero
        self.adj_matrix = torch.tensor(adj_numpy / deg, dtype=torch.float32)
        
    def step(self, current_state):
        """
        Evolves the network one step forward in time (t -> t+1).
        state: [N, 1] Tensor (0 = Solvent, 1 = Default)
        """
        # 1. Calculate Counterparty Exposure
        # How many of my neighbors have defaulted?
        exposure = torch.matmul(self.adj_matrix, current_state)
        
        # 2. The Default Rule (The Non-Linear Transition)
        # If Exposure > Buffer, I default.
        # We add 'current_state' so that dead banks stay dead (Absorbing State)
        new_state = (exposure > self.buffer).float() + current_state
        new_state = torch.clamp(new_state, 0, 1) # Cap at 1
        
        return new_state

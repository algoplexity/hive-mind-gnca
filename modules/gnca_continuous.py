import torch
import torch.nn as nn
from torch_geometric.nn import MessagePassing

class ContinuousGNCA(MessagePassing):
    """
    Learns the Laws of Motion (Physics) of the Market Herd.
    Input: State (Price, Momentum) at t
    Output: Delta State (Change in Price, Change in Momentum) at t+1
    """
    def __init__(self, input_dim=4, hidden_dim=64):
        # input_dim = 2 (Pos) + 2 (Vel) = 4
        super().__init__(aggr='mean') # Mean aggregation works better for continuous alignment
        
        # Encoder: Compress state into hidden representation
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.Tanh(), # Tanh often better for bounded continuous mechanics
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Message Logic: "What do I tell my neighbors?"
        self.msg_mlp = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        
        # Update Logic: "How do I change based on neighbors?"
        # Input: Self_Hidden + Neighbor_Mean
        self.update_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.Tanh(),
            nn.Linear(hidden_dim, input_dim) # Output is the DELTA (Velocity/Acceleration)
        )

    def forward(self, x, edge_index):
        # 1. Encode
        h = self.encoder(x)
        
        # 2. Message Passing
        # Propagates messages along the DYNAMIC edge_index provided at this step
        aggr_msg = self.propagate(edge_index, x=h)
        
        # 3. Update
        combined = torch.cat([h, aggr_msg], dim=1)
        delta = self.update_mlp(combined)
        
        # Residual Connection: New State = Old State + Learned Delta
        return x + delta

    def message(self, x_j):
        return self.msg_mlp(x_j)

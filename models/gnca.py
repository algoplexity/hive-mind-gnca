import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import MessagePassing

class SystemicGNCA(MessagePassing):
    """
    The Learner.
    Replicates Grattarola et al. (2021) Eq 4: h' = MLP( h || sum(ReLU(W * h_j)) )
    
    Goal: Learn to predict t+1 given t, solely from local message passing,
    without knowing the global adjacency matrix or the threshold rule.
    """
    def __init__(self, hidden_dim=32):
        super(SystemicGNCA, self).__init__(aggr='add') # Sum aggregation mimics neighbor counting
        
        # 1. Pre-processing (Encoder)
        # Maps binary state (0/1) to high-dimensional thought vector
        self.encoder = nn.Sequential(
            nn.Linear(1, hidden_dim),
            nn.ReLU()
        )
        
        # 2. Message Transformation (The "W")
        self.msg_transform = nn.Linear(hidden_dim, hidden_dim)
        
        # 3. Update Rule (The "Program")
        # Takes Self + Neighbors -> Next State
        self.update_mlp = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1) # Output logits for solvency
        )

    def forward(self, x, edge_index):
        # x: [N, 1]
        
        # Encode
        h = self.encoder(x)
        
        # Propagate (Message Passing)
        # This calls message() -> aggregate() -> update()
        neighbor_signal = self.propagate(edge_index, x=h)
        
        # Update
        combined = torch.cat([h, neighbor_signal], dim=1)
        out = self.update_mlp(combined)
        return out

    def message(self, x_j):
        # x_j: Features of neighbors
        return F.relu(self.msg_transform(x_j))

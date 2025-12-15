import torch
import numpy as np
from torch_geometric.data import Data

class MarketHerdSimulator:
    """
    Simulates a 'Boids-like' market where agents (traders) move in Price/Momentum space.
    This generates the Ground Truth for the GNCA to learn.
    """
    def __init__(self, num_agents=100, perception_radius=0.15, steps=500):
        self.num_agents = num_agents
        self.radius = perception_radius
        self.steps = steps
        self.dt = 0.01  # Time step size

    def get_neighbors(self, pos):
        """
        Dynamic Graph Generation:
        Agents connect if they are close in Strategy Space (Position).
        """
        # Simple distance matrix
        dist = torch.cdist(pos, pos)
        # Adjacency: 1 if dist < radius, 0 otherwise (excluding self-loops)
        adj = (dist < self.radius) & (dist > 0)
        edge_index = adj.nonzero().t()
        return edge_index

    def step(self, pos, vel):
        """
        The 'Physics' of the Market Herd.
        Rules: Separation (Arb), Alignment (Trend), Cohesion (Mean Reversion).
        """
        edge_index = self.get_neighbors(pos)
        
        # Calculate forces (Simplified Boids Logic)
        # 1. Cohesion: Move to center of neighbors
        # 2. Alignment: Match velocity of neighbors
        # 3. Separation: Avoid overcrowding
        
        # (For this replication, we use a simplified vector update for brevity)
        # In the full repo, we implement the full Reynolds algorithm.
        
        # Random noise (Stochastic Market)
        noise = torch.randn_like(vel) * 0.01
        
        # New Velocity (Momentum)
        new_vel = vel + noise 
        
        # New Position (Price)
        new_pos = pos + new_vel * self.dt
        
        # Boundary conditions (Market Limits) -> Wrap around or bounce
        new_pos = torch.clamp(new_pos, -1, 1)
        
        return new_pos, new_vel, edge_index

    def generate_trajectory(self):
        # Initialize random state
        pos = torch.rand(self.num_agents, 2) * 2 - 1  # 2D Strategy Space
        vel = torch.randn(self.num_agents, 2) * 0.1
        
        trajectory = []
        
        for _ in range(self.steps):
            new_pos, new_vel, edge_index = self.step(pos, vel)
            
            # Store state as PyG Data object
            # x = [Pos, Vel] (State Vector)
            x = torch.cat([pos, vel], dim=1)
            data = Data(x=x, edge_index=edge_index)
            trajectory.append(data)
            
            pos, vel = new_pos, new_vel
            
        return trajectory

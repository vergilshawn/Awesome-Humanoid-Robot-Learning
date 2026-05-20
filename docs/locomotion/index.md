# Locomotion

**4 papers** in this category.

## Months

- [2026-05](/locomotion/2026-05) (2 papers)
- [2026-04](/locomotion/2026-04) (1 papers)
- [2026-03](/locomotion/2026-03) (1 papers)

---

## Recent Papers

## Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors

- **Paper:** [arXiv](https://arxiv.org/abs/2605.18611)
- **Authors:** Yidan Lu, Yichao Zhong, Liu Zhao, Wanyue Li, Peng Lu
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid
  - Walking

### Summary

We propose a unified reinforcement learning framework that enables a single policy to perform walking, running, and fall recovery on the Unitree G1 humanoid robot, validated on physical hardware without any explicit mode-switching command at deployment. The framework extends Adversarial Motion Priors (AMP) by replacing the conventional global reference distribution with a state-dependent gate that routes each training transition to one of two discriminators: a dedicated recovery discriminator and a velocity-conditioned locomotion discriminator that jointly covers walking and running.

---

## Terrain Consistent Reference-Guided RL for Humanoid Navigation Autonomy

- **Paper:** [arXiv](https://arxiv.org/abs/2605.15517)
- **Authors:** William D. Compton, Zachary Olkin, Aaron D. Ames
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - MPC
  - Locomotion
  - Navigation
  - Humanoid
  - State Estimation
  - Simulation Benchmark

### Summary

We present a method for training reference-guided, perceptive reinforcement learning locomotion policies for humanoid robots in which reference trajectories are modulated in training to be consistent with terrain geometry. Aiming to deploy our method with standard navigation autonomy infrastructure, we synthesize SE(2)-controllable reference trajectories inside the RL training loop, projecting desired footsteps onto valid footholds and adjusting swing-foot and center-of-mass trajectories to match the terrain.

---

## Learning Humanoid Navigation from Human Data

- **Paper:** [arXiv](https://arxiv.org/abs/2604.00416)
- **Project:** [GitHub](https://egonav.weizhuowang.com)
- **Authors:** Weizhuo Wang, Yanjie Ze, C. Karen Liu, Monroe Kennedy
- **Published:** 2026-04
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Navigation
  - Zero-Shot
  - Humanoid
  - Walking
  - Diffusion
  - Locomotion

### Summary

EgoNav enables a humanoid robot to traverse diverse unseen environments by learning from 5 hours of human walking data, with no robot data or finetuning. A diffusion model predicts future trajectories conditioned on past trajectory, 360 degree visual memory, and DINOv3 video features.

---

## Omnidirectional Humanoid Locomotion on Stairs via Unsafe Stepping Penalty and Sparse LiDAR Elevation Mapping

- **Paper:** [arXiv](https://arxiv.org/abs/2603.07928)
- **Authors:** Yuzhi Jiang, Yujun Liang, Junhao Li, Han Ding, Lijun Zhu
- **Published:** 2026-03
- **Real Robot:** ✅
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid
  - Walking
  - Navigation
  - State Estimation
  - Simulation Benchmark

### Summary

Safe omnidirectional humanoid locomotion on stairs requires terrain perception and reliable foothold selection. This paper introduces a single-stage training framework with a dense unsafe stepping penalty and a rolling sparse LiDAR point-cloud elevation mapping system.

---

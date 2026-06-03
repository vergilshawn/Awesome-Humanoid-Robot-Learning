# Locomotion

**101 papers** in this category.

## Months

- [2026-06](/locomotion/2026-06) (1 papers)
- [2026-05](/locomotion/2026-05) (5 papers)
- [2026-04](/locomotion/2026-04) (2 papers)
- [2026-03](/locomotion/2026-03) (2 papers)
- [2026-02](/locomotion/2026-02) (10 papers)
- [2026-01](/locomotion/2026-01) (4 papers)
- [2025-12](/locomotion/2025-12) (10 papers)
- [2025-11](/locomotion/2025-11) (1 papers)
- [2025-10](/locomotion/2025-10) (7 papers)
- [2025-09](/locomotion/2025-09) (6 papers)
- [2025-08](/locomotion/2025-08) (7 papers)
- [2025-07](/locomotion/2025-07) (3 papers)
- [2025-06](/locomotion/2025-06) (5 papers)
- [2025-05](/locomotion/2025-05) (9 papers)
- [2025-04](/locomotion/2025-04) (5 papers)
- [2025-03](/locomotion/2025-03) (6 papers)
- [2025-02](/locomotion/2025-02) (4 papers)
- [2024-11](/locomotion/2024-11) (2 papers)
- [2024-10](/locomotion/2024-10) (2 papers)
- [2024-08](/locomotion/2024-08) (1 papers)
- [2024-06](/locomotion/2024-06) (1 papers)
- [2024-04](/locomotion/2024-04) (1 papers)
- [2024-02](/locomotion/2024-02) (2 papers)
- [2024-01](/locomotion/2024-01) (1 papers)
- [2023-09](/locomotion/2023-09) (1 papers)
- [2023-07](/locomotion/2023-07) (1 papers)
- [2023-03](/locomotion/2023-03) (1 papers)
- [2023-02](/locomotion/2023-02) (1 papers)

---

## Recent Papers

## PHASOR: Phase-Anchored Universal Action Representations for Humanoid Embodiments

- **Paper:** [arXiv](https://arxiv.org/abs/2606.01851)
- **Authors:** Kihyun Kim, Chaeyun Kim, Jongho Shin, Taeyoun Kwon, Junghyun Kim, Mijin Koo et al. (7 authors)
- **Published:** 2026-06
- **Tags:**
  - Humanoid
  - Distillation
  - Policy Learning
  - Locomotion

### Summary

Learning a good action embedding space is fundamental to scalable robot policy learning, yet existing methods treat action latents as task-specific intermediates rather than first-class representations. The resulting latents are unstructured, embodiment-specific, and weakly tied to motion semantics, limiting interpretability, controllability, and transferability across robots.

---

## MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2605.24592)
- **Authors:** Yusen Feng, Xiang Wang, Heyuan Yao, Zixi Kang, Xinyu Huo, Boyang Yu et al. (10 authors)
- **Published:** 2026-05
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid
  - Distillation
  - Policy Learning
  - VAE
  - Human Motion Analysis and Synthesis

### Summary

This paper presents MuGen, a data-driven framework for learning and deploying multi-skill locomotion on humanoid robots. MuGen enables a robot to perform expressive motions like humans under the guidance of example motion sequences.

---

## Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments

- **Paper:** [arXiv](https://arxiv.org/abs/2605.21935)
- **Authors:** Peifeng Jiang, Hong Liu, Jin Jin, Wenshuai Wang, Xia Li
- **Published:** 2026-05
- **Tags:**
  - Locomotion
  - Manipulation
  - Navigation
  - Safety
  - Humanoid
  - Gait
  - Gaussian Splatting
  - Distillation

### Summary

Safe manipulation-oriented navigation for humanoid robots requires scene memory that remains reliable under locomotion-induced perceptual distortion, environmental changes, and interaction-level geometric safety constraints. Existing semantic mapping and scene-graph systems are difficult to deploy directly in this setting because they often assume stable camera trajectories, static environments, or coarse object geometry.

---

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

## Explicit Stair Geometry Conditioning for Robust Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2605.09944)
- **Authors:** Jianguo Zhang, Wentai Xu, Shusheng Ye, Yuxiang He, Weimin Qi, Qinbo Sun et al. (8 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Locomotion
  - Robustness
  - Humanoid
  - Gait
  - PPO
  - State Estimation
  - Simulation Benchmark

### Summary

Robust humanoid stair climbing remains challenging due to geometric discontinuities, sensitivity to step height variations, and perception uncertainty in real-world environments. Existing learning-based locomotion policies often rely on implicit terrain representations or blind proprioceptive feedback, limiting their ability to generalize across varying stair geometries and to anticipate required gait adjustments.

---

## QuietWalk: Physics-Informed Reinforcement Learning for Ground Reaction Force-Aware Humanoid Locomotion Under Diverse Footwear

- **Paper:** [arXiv](https://arxiv.org/abs/2604.23702)
- **Authors:** Hanze Hu, Luying Feng, Silu Chen, Tianjiang Zheng, Dexin Jiang, Wei Chen et al. (9 authors)
- **Published:** 2026-04
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid
  - Contact Dynamics
  - Impact
  - Dataset
  - Simulation Benchmark
  - Physics-Based Character Animation

### Summary

Humanoid robots operating in human-centered environments (e.g., homes, hospitals, and offices) must mitigate foot--ground impact transients, as impact-induced vibration and noise degrade user experience and repeated impacts accelerate hardware wear. However, existing low-noise locomotion training often relies on kinematic proxy objectives or fragile force sensors, and footwear-induced changes in contact dynamics introduce distribution shifts that hinder policy generalization.

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

## CReF: Cross-modal and Recurrent Fusion for Depth-conditioned Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2603.29452)
- **Authors:** Chenhao Li, Qi Wei, Botao He, Yangfan Zhou, Lingshi Kong, Chong Zhang et al. (8 authors)
- **Published:** 2026-03
- **Tags:**
  - Locomotion
  - Robustness
  - Humanoid

### Summary

Learning depth-conditioned humanoid locomotion is critical for traversing uneven terrains and complex environments. This work presents CReF, a cross-modal and recurrent fusion framework that fuses proprioceptive and depth observations for humanoid locomotion control, improving robustness and terrain-conditioned behavior under challenging perceptual inputs..

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

## Biomechanical Comparisons Reveal Divergence of Human and Humanoid Gaits

- **Paper:** [arXiv](https://arxiv.org/abs/2602.21666)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Gait
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 APEX: Learning Adaptive High-Platform Traversal for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2602.11143)
- **Project:** [GitHub](https://apex-humanoid.github.io/)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking,  / [code](https://github.com/bigai-ai/ECO-humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06445)
- **Project:** [GitHub](https://sites.google.com/view/eco-humanoid)
- **Published:** 2026-02
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Walking
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Now You See That: Learning End-to-End Humanoid Locomotion from Raw Pixels

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06382)
- **Published:** 2026-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Hybrid Autoencoder for Robust Heightmap Generation from Fused Lidar and Depth Data for Humanoid Robot Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2602.05855)
- **Published:** 2026-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Scalable and General Whole-Body Control for Cross-Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2602.05791)
- **Published:** 2026-02
- **Tags:**
  - Whole-Body Control
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.04412)
- **Published:** 2026-02
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Distillation
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains

- **Paper:** [arXiv](https://arxiv.org/abs/2602.03511)
- **Published:** 2026-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains

- **Paper:** [arXiv](https://arxiv.org/abs/2602.03002)
- **Published:** 2026-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Toward Reliable Sim-to-Real Predictability for MoE-based Robust Quadrupedal Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2602.00678)
- **Published:** 2026-02
- **Tags:**
  - Sim-to-Real
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

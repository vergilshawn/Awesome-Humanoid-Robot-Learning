# Real Robot Papers

Papers with real humanoid robot deployment and experiments.

## Platforms

- **Digit:** 1 papers
- **Figure:** 1 papers
- **Unitree G1:** 3 papers

---

## All Real Robot Papers

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

## Non-Colliding Biometric Identities for Digital Entities: Geometry, Capacity, and Million-Scale Virtual Identity Provisioning

- **Paper:** [arXiv](https://arxiv.org/abs/2605.18238)
- **Authors:** Yuyang Ji, Yixuan Shen, Anil Jain, Xiaoming Liu, Feng Liu
- **Published:** 2026-05
- **Real Robot:** ✅ — Digit
- **Tags:**
  - Humanoid
  - Dataset
  - Simulation Benchmark

### Summary

Digital entities such as AI agents and humanoid robots increasingly operate alongside real humans, yet their identity infrastructure is based on credentials rather than embodied biometric identity. We introduce Biometric Identity Provisioning (BIP), a new problem and solution framework that addresses: given an enrollment gallery of real human identities, provision virtual identities that are non-colliding with every enrolled identity, maintain sufficient inter-class separability, and are realizable as high-fidelity face images.

---

## PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2605.17681)
- **Authors:** Jiarong Kang, Kunzhao Ren, Tao Pang, Xiaobin Xiong
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Locomotion
  - State Estimation
  - Real Robot
  - Humanoid
  - Proprioception
  - Foundation Model
  - Contact Dynamics
  - Friction

### Summary

Humanoid and legged robots interact with the environment through intermittent contacts, making accurate motion estimation fundamentally dependent on reasoning about contact dynamics. However, standard sensing pipelines-whether based on onboard proprioception with Extended Kalman Filters (EKFs) or external motion capture systems-recover only kinematics, while contact forces, contact timing, and inertial parameters remain unobserved.

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

## HoloMotion-1 Technical Report

- **Paper:** [arXiv](https://arxiv.org/abs/2605.15336)
- **Authors:** Maiyue Chen, Kaihui Wang, Bo Zhang, Xihan Ma, Zhiyuan Yang, Yi Ren et al. (10 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Transformer
  - Zero-Shot
  - Humanoid
  - Foundation Model
  - Fine-tuning
  - Benchmark
  - Loco-Manipulation and Whole-Body Control
  - Simulation Benchmark

### Summary

In this report, we present HoloMotion-1, a humanoid motion foundation model for zero-shot whole-body motion tracking. A key innovation of HoloMotion-1 is to scale control-policy training with a large-scale hybrid motion corpus, where video-reconstructed motions from in-the-wild videos provide the dominant source of motion diversity, while curated motion-capture and in-house motion data provide higher-fidelity supervision and deployment-oriented coverage.

---

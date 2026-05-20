# Latest Papers

All papers sorted by publication date (newest first).

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

## HCLM: A Hierarchical Framework for Cooperative Loco-Manipulation with Dual Quadrupeds

- **Paper:** [arXiv](https://arxiv.org/abs/2605.17300)
- **Authors:** Qixuan Li, Chen Le, Jincheng Yu, Xinlei Chen
- **Published:** 2026-05
- **Tags:**
  - Diffusion Policy
  - Whole-Body Control
  - Locomotion
  - Manipulation
  - Collision
  - Diffusion
  - Loco-Manipulation and Whole-Body Control
  - State Estimation

### Summary

We introduce HCLM, a hierarchical framework for general-purpose cooperative loco-manipulation with dual quadrupedal systems. Coordinating multi-robot collaborative manipulation across floating bases is highly challenging due to the conflicting demands of spatial coordination, robust locomotion, and closed-chain physical interactions.

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

## CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios

- **Paper:** [arXiv](https://arxiv.org/abs/2605.15122)
- **Authors:** Michael Baumgartner, David Müller, Agon Serifi, Ruben Grandia, Espen Knoop, Markus Gross et al. (7 authors)
- **Published:** 2026-05
- **Tags:**
  - State Estimation
  - Biped
  - Locomotion
  - Simulation Benchmark

### Summary

Robust state estimation for highly dynamic motion of legged robots remains challenging, especially in dynamic, contact-rich scenarios. Traditional approaches often rely on binary contact states that fail to capture the nuances of partial contact or directional slippage.

---

## A Rapid Deployment Pipeline for Autonomous Humanoid Grasping Based on Foundation Models

- **Paper:** [arXiv](https://arxiv.org/abs/2604.17258)
- **Authors:** Yifei Yan, Yankai Liao, Linqi Ye
- **Published:** 2026-04
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Zero-Shot
  - Real Robot
  - Humanoid
  - Inverse Kinematics
  - 3D Reconstruction
  - Foundation Model
  - Physics-Based Character Animation
  - Manipulation

### Summary

This paper presents an end-to-end rapid deployment pipeline for humanoid grasping that combines foundation-model components for annotation, 3D reconstruction, and zero-shot pose tracking. The estimated pose drives a Unity inverse kinematics planner whose joint commands are streamed to a Unitree G1 humanoid via UDP and executed through the Unitree SDK.

---

## Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2604.17335)
- **Authors:** Zewei Zhang, Kehan Wen, Michael Xu, Junzhe He, Chenhao Li, Takahiro Miki et al. (10 authors)
- **Published:** 2026-04
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid
  - PPO
  - Diffusion
  - Loco-Manipulation and Whole-Body Control
  - Physics-Based Character Animation
  - Human Motion Analysis and Synthesis

### Summary

This work combines motion generation and motion tracking for whole-body humanoid locomotion. A diffusion model predicts terrain-aware reference motions from retargeted human motions, while a reinforcement learning tracker follows the generated references.

---

## 🌟 CLAW: Composable Language-Annotated Whole-body Motion Generation

- **Paper:** [arXiv](https://arxiv.org/abs/2604.11251)
- **Project:** [GitHub](https://github.com/JianuoCao/CLAW)
- **Authors:** Jianuo Cao, Yuxin Chen, Masayoshi Tomizuka
- **Published:** 2026-04
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Whole-Body Control
  - MuJoCo
  - Humanoid
  - Language-Conditioned
  - Dataset
  - Simulation Benchmark
  - Loco-Manipulation and Whole-Body Control
  - Physics-Based Character Animation

### Summary

CLAW is an interactive web-based pipeline for scalable generation of language-annotated whole-body motion data for the Unitree G1 humanoid robot. It treats kinematic planner modes as composable building blocks and provides browser-based interfaces for exploratory and batch data collection.

---

## Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions

- **Paper:** [arXiv](https://arxiv.org/abs/2604.11447)
- **Authors:** Wenqi Cai, John Abanes, Nikolaos Evangeliou, Anthony Tzes
- **Published:** 2026-04
- **Tags:**
  - Motion Retargeting
  - Safety
  - Humanoid
  - Collision
  - Teleoperation
  - State Estimation
  - Simulation Benchmark

### Summary

This paper presents a vision-based framework that enables a humanoid robot to imitate human movements while avoiding collisions. Human skeletal keypoints are captured by a single camera and converted into joint angles for motion retargeting.

---

## HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2604.07993)
- **Authors:** Shuanghao Bai, Meng Li, Xinyuan Lv, Jiawei Wang, Xinhua Wang, Fei Liao et al. (17 authors)
- **Published:** 2026-04
- **Tags:**
  - Manipulation
  - Biped
  - Humanoid
  - Loco-Manipulation and Whole-Body Control
  - Locomotion

### Summary

HEX is a state-centric framework for coordinated manipulation on full-sized bipedal humanoid robots. It introduces a humanoid-aligned universal state representation for scalable learning across heterogeneous embodiments and a mixture-of-experts proprioceptive predictor for whole-body coordination and temporal motion dynamics.

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

## RoboForge: Physically Optimized Text-guided Whole-Body Locomotion for Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2603.17927)
- **Authors:** Xichen Yuan, Zhe Li, Bofan Lyu, Kuangji Zuo, Yanshuo Lu, Gen Li et al. (7 authors)
- **Published:** 2026-03
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Locomotion
  - MuJoCo
  - Humanoid
  - Fine-tuning
  - Distillation
  - Simulation Benchmark
  - Loco-Manipulation and Whole-Body Control
  - State Estimation

### Summary

RoboForge bridges natural language and whole-body humanoid locomotion through a retarget-free, physics-optimized pipeline. It couples motion generation and control through a physical plausibility optimization module that refines teacher-student distillation policies and converts reward-optimized simulation rollouts into explicit motion data for fine-tuning the motion generator.

---

## ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video

- **Paper:** [arXiv](https://arxiv.org/abs/2603.09170)
- **Authors:** Haoran Yang, Jiacheng Bao, Yucheng Xin, Haoming Song, Yuyang Tian, Bin Zhao et al. (8 authors)
- **Published:** 2026-03
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Whole-Body Control
  - Teleoperation
  - Humanoid
  - Vision-Language
  - Loco-Manipulation and Whole-Body Control
  - Human Motion Analysis and Synthesis

### Summary

Achieving versatile and naturalistic whole-body control for humanoid robot scene-interaction remains a significant challenge. ZeroWBC learns a natural humanoid visuomotor control policy directly from human egocentric videos, eliminating the need for large-scale robot teleoperation data.

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

## Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality

- **Paper:** [arXiv](https://arxiv.org/abs/2603.05993)
- **Authors:** Beichen Wang, Yuanjie Lu, Linji Wang, Liuchuan Yu, Xuesu Xiao
- **Published:** 2026-03
- **Tags:**
  - Locomotion
  - Navigation
  - Safety
  - Humanoid
  - Collision
  - Benchmark
  - Dataset
  - PPO

### Summary

Recent advances in humanoid locomotion have enabled dynamic behaviors, but cluttered 3D environments remain underexplored. Moving Through Clutter is an open-source virtual reality based data collection and evaluation framework for scene-aware humanoid locomotion in cluttered environments.

---

## X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation

- **Paper:** [arXiv](https://arxiv.org/abs/2603.03733)
- **Authors:** Dewei Wang, Xinmiao Wang, Chenyun Zhang, Jiyuan Shi, Yingnan Zhao, Chenjia Bai et al. (7 authors)
- **Published:** 2026-03
- **Tags:**
  - Locomotion
  - Humanoid
  - Distillation
  - Loco-Manipulation and Whole-Body Control

### Summary

X-Loco targets generalist humanoid locomotion, including upright locomotion, fall recovery, terrain traversal, and whole-body coordination. It trains multiple oracle specialist policies and uses synergetic policy distillation with a case-adaptive specialist selection mechanism to guide a vision-based student policy.

---

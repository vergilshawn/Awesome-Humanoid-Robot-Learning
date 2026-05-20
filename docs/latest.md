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

## 🌟 Humanoid Manipulation with Touch Dreaming

- **Paper:** [arXiv](https://arxiv.org/abs/2604.13015)
- **Project:** [GitHub](https://humanoid-touch-dream.github.io/)
- **Authors:** Han Wang, Hongjie Fang, Changyang He, Tairan He, Zhenyu Jiang, Sizhe Yang et al. (11 authors)
- **Published:** 2026-04
- **Tags:**
  - Manipulation
  - Humanoid
  - Policy Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

This paper studies humanoid manipulation with touch dreaming, using tactile imagination and policy learning to improve contact-rich manipulation. The system targets dexterous humanoid manipulation and whole-body interaction with objects under sparse or difficult tactile supervision..

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

## 🌟 Sumo: Reinforcement Learning for Humanoid Loco-manipulation with Interactable 3D Scene Semantics

- **Paper:** [arXiv](https://arxiv.org/abs/2604.08508)
- **Project:** [GitHub](https://sumo.rai-inst.com/)
- **Authors:** Qingwen Guo, Junbo Wang, Ali Hadi Zadeh, Haonan Chang, Hongyu Zhou, Chenhao Li et al. (13 authors)
- **Published:** 2026-04
- **Tags:**
  - Reinforcement Learning
  - Manipulation
  - Navigation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Sumo introduces a reinforcement learning framework for humanoid loco-manipulation with interactable 3D scene semantics. It enables humanoid robots to reason about scene objects and perform whole-body navigation and manipulation skills in semantically rich environments..

---

## 🌟 RoSHI: Large-scale Motion Imitation in Humanoid Robots via World Models

- **Paper:** [arXiv](https://arxiv.org/abs/2604.07331)
- **Project:** [GitHub](https://roshi-mocap.github.io)
- **Authors:** Aobo Liang, Juntong Li, Qingnan Liu, Gaofeng Li, Jiawei Li, Runyu Zhang et al. (10 authors)
- **Published:** 2026-04
- **Tags:**
  - World Model
  - Humanoid
  - Human Motion Analysis and Synthesis

### Summary

RoSHI studies large-scale motion imitation for humanoid robots via world models. The method learns from large human motion corpora and trains humanoid control policies for motion tracking and imitation, targeting scalable humanoid skill acquisition from motion data..

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

## 🌟 ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video

- **Paper:** [arXiv](https://arxiv.org/abs/2603.09170)
- **Project:** [GitHub](https://zerowbc.github.io/)
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

## Heracles: Bridging Precise Tracking and Generative Synthesis for General Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2603.27756)
- **Published:** 2026-03
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 SafeFlow: Real-Time Text-Driven Humanoid Whole-Body Control via Physics-Guided Rectified Flow and Selective Safety Gating

- **Paper:** [arXiv](https://arxiv.org/abs/2603.23983)
- **Project:** [GitHub](https://hanbyelcho.info/safeflow/)
- **Published:** 2026-03
- **Tags:**
  - Whole-Body Control
  - Safety
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2603.12263)
- **Published:** 2026-03
- **Tags:**
  - Manipulation
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2603.10306)
- **Project:** [GitHub](https://steadytray.github.io/)
- **Published:** 2026-03
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery

- **Paper:** [arXiv](https://arxiv.org/abs/2603.08619)
- **Published:** 2026-03
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2603.03279)
- **Project:** [GitHub](https://ultra-humanoid.github.io/)
- **Published:** 2026-03
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HumDex: Humanoid Dexterous Manipulation Made Easy

- **Paper:** [arXiv](https://arxiv.org/abs/2603.12260)
- **Published:** 2026-03
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2603.05493)
- **Published:** 2026-03
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and Control

- **Paper:** [arXiv](https://arxiv.org/abs/2603.12185)
- **Project:** [GitHub](https://irislab.tech/comfree-sim/)
- **Published:** 2026-03
- **Tags:**
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2603.06181)
- **Published:** 2026-03
- **Tags:**
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 FAME: Force-Adaptive RL for Expanding the Manipulation Envelope of a Full-Scale Humanoid

- **Paper:** [arXiv](https://arxiv.org/abs/2603.08961)
- **Project:** [GitHub](https://fame10.github.io/Fame/)
- **Published:** 2026-03
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## OmniXtreme: Breaking the Generality Barrier in High-Dynamic Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.23843)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 LessMimic: Long-Horizon Humanoid Interaction with Unified Distance Field Representations

- **Paper:** [arXiv](https://arxiv.org/abs/2602.21723)
- **Project:** [GitHub](https://yzhu.io/preprint/humanoid2026lessmimic/)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Humanoid End-Effector Control for Open-Vocabulary Visual Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.16705)
- **Published:** 2026-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## VIGOR: Visual Goal-In-Context Inference for Unified Humanoid Fall Safety

- **Paper:** [arXiv](https://arxiv.org/abs/2602.16511)
- **Published:** 2026-02
- **Tags:**
  - Safety
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching

- **Paper:** [arXiv](https://arxiv.org/abs/2602.15827)
- **Project:** [GitHub](https://php-parkour.github.io/)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2602.15733)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Hanoi: Investigating Shared Whole-Body Control for Skill-Based Box Rearrangement

- **Paper:** [arXiv](https://arxiv.org/abs/2602.13850)
- **Published:** 2026-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## General Humanoid Whole-Body Control via Pretraining and Fast Adaptation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.11929)
- **Published:** 2026-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HAIC: Humanoid Agile Object Interaction Control via Dynamics-Aware World Model

- **Paper:** [arXiv](https://arxiv.org/abs/2602.11758)
- **Project:** [GitHub](https://haic-humanoid.github.io/)
- **Published:** 2026-02
- **Tags:**
  - World Model
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 EgoHumanoid: Unlocking In-the-Wild Loco-Manipulation with Robot-Free Egocentric Demonstration

- **Paper:** [arXiv](https://arxiv.org/abs/2602.10106)
- **Project:** [GitHub](https://opendrivelab.com/EgoHumanoid/)
- **Published:** 2026-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.08594)
- **Published:** 2026-02
- **Tags:**
  - Sim-to-Real
  - Teleoperation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Human-Like Badminton Skills for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2602.08370)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TextOp: Real-time Interactive Text-Driven Humanoid Robot Motion Generation and Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.07439)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06827)
- **Published:** 2026-02
- **Tags:**
  - Trajectory Optimization
  - Sampling-Based
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06643)
- **Project:** [GitHub](https://humanoid-manipulation-interface.github.io)
- **Published:** 2026-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06341)
- **Published:** 2026-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Soccer Skills for Humanoid Robots:   A Progressive Perception-Action Framework

- **Paper:** [arXiv](https://arxiv.org/abs/2602.05310)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PDF-HR: Pose Distance Fields for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2602.04851)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HUSKY: Humanoid Skateboarding System via Physics-Aware Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.03205)
- **Published:** 2026-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.02960)
- **Published:** 2026-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Distillation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HumanX: Toward Agile and Generalizable Humanoid Interaction Skills from Human Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2602.02473)
- **Project:** [GitHub](https://wyhuai.github.io/human-x/)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TTT-Parkour: Rapid Test-Time Training for Perceptive Robot Parkour

- **Paper:** [arXiv](https://arxiv.org/abs/2602.02331)
- **Published:** 2026-02
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.00401)
- **Published:** 2026-02
- **Tags:**
  - Zero-Shot
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06949)
- **Project:** [GitHub](https://dreamdojo-world.github.io/)
- **Published:** 2026-02
- **Tags:**
  - World Model
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.15060)
- **Published:** 2026-02
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.11321)
- **Published:** 2026-02
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior

- **Paper:** [arXiv](https://arxiv.org/abs/2602.09628)
- **Published:** 2026-02
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.01632)
- **Published:** 2026-02
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

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

## EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models

- **Paper:** [arXiv](https://arxiv.org/abs/2602.04515)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Task Planning
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2602.01515)
- **Published:** 2026-02
- **Tags:**
  - Sim-to-Real
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Characteristics, Management, and Utilization of Muscles in Musculoskeletal Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2602.08518)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2602.11337)
- **Published:** 2026-02
- **Tags:**
  - Manipulation
  - Navigation
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2602.21599)
- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## InterPrior: Scaling Generative Control for Physics-Based Human-Object Interactions

- **Paper:** [arXiv](https://arxiv.org/abs/2602.06035)
- **Published:** 2026-02
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EmbodMocap: In-the-Wild 4D Human-Scene Reconstruction for Embodied Agents

- **Paper:** [arXiv](https://arxiv.org/abs/2602.23205)
- **Published:** 2026-02
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2602.22209)
- **Project:** [GitHub](https://judyye.github.io/whole-www/)
- **Published:** 2026-02
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robust and Generalized Humanoid Motion Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2601.23080)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing

- **Paper:** [arXiv](https://arxiv.org/abs/2601.22517)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PILOT: A Perceptive Integrated Low-level Controller for Loco-manipulation over Unstructured Scenes

- **Paper:** [arXiv](https://arxiv.org/abs/2601.17440)
- **Published:** 2026-01
- **Tags:**
  - Manipulation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Collision-Free Humanoid Traversal in Cluttered Indoor Scenes

- **Paper:** [arXiv](https://arxiv.org/abs/2601.16035)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Collision
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions

- **Paper:** [arXiv](https://arxiv.org/abs/2601.12799)
- **Published:** 2026-01
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2601.09518)
- **Published:** 2026-01
- **Tags:**
  - Human Demonstration
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2601.07718)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Deep Whole-body Parkour

- **Paper:** [arXiv](https://arxiv.org/abs/2601.07701)
- **Published:** 2026-01
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2601.14874)
- **Published:** 2026-01
- **Tags:**
  - Manipulation
  - Humanoid
  - Impedance Control
  - Vision-Language

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2601.09031)
- **Published:** 2026-01
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DexterCap: An Affordable and Automated System for Capturing Dexterous Hand-Object Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2601.05844)
- **Published:** 2026-01
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2601.02078)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## FastStair: Learning to Run Up Stairs with Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2601.10365)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## AME-2: Agile and Generalized Legged Locomotion via Attention-Based Neural Map Encoding

- **Paper:** [arXiv](https://arxiv.org/abs/2601.08485)
- **Published:** 2026-01
- **Tags:**
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Walk the PLANC: Physics-Guided RL for Agile Humanoid Locomotion on Constrained Footholds

- **Paper:** [arXiv](https://arxiv.org/abs/2601.06286)
- **Published:** 2026-01
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SKATER: Synthesized Kinematics for Advanced Traversing Efficiency on a Humanoid Robot via Roller Skate Swizzles

- **Paper:** [arXiv](https://arxiv.org/abs/2601.04948)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2601.12790)
- **Published:** 2026-01
- **Tags:**
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control,  / [code](https://github.com/bigai-ai/LIFT-humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2601.21363)
- **Project:** [GitHub](https://lift-humanoid.github.io/)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot

- **Paper:** [arXiv](https://arxiv.org/abs/2601.18963)
- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Coordinated Humanoid Manipulation with Choice Policies

- **Paper:** [arXiv](https://arxiv.org/abs/2512.25072)
- **Published:** 2025-12
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## UniAct: Unified Motion Generation and Action Streaming for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2512.24321)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EGM: Efficiently Learning General Motion Tracking Policy for High Dynamic Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2512.19043)
- **Published:** 2025-12
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2512.17183)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation

- **Paper:** [arXiv](https://arxiv.org/abs/2512.14689)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations

- **Paper:** [arXiv](https://arxiv.org/abs/2512.13093)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Agile Striker Skills for Humanoid Soccer Robots from Noisy Sensory Input

- **Paper:** [arXiv](https://arxiv.org/abs/2512.06571)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2512.01336)
- **Published:** 2025-12
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer

- **Paper:** [arXiv](https://arxiv.org/abs/2512.01061)
- **Published:** 2025-12
- **Tags:**
  - Sim-to-Real
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control

- **Paper:** [arXiv](https://arxiv.org/abs/2512.23650)
- **Published:** 2025-12
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2512.23649)
- **Published:** 2025-12
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2512.16446)
- **Published:** 2025-12
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Get Up Across Morphologies: Zero-Shot Recovery with a Unified Humanoid Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2512.12230)
- **Published:** 2025-12
- **Tags:**
  - Zero-Shot
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Symphony: A Heuristic Normalized Calibrated Advantage Actor and Critic Algorithm in application for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2512.10477)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Hierarchical, Model-Based System for High-Performance Humanoid Soccer

- **Paper:** [arXiv](https://arxiv.org/abs/2512.09431)
- **Published:** 2025-12
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2512.07464)
- **Published:** 2025-12
- **Tags:**
  - Locomotion
  - Humanoid
  - Gait

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Sim-to-Real Humanoid Locomotion in 15 Minutes

- **Paper:** [arXiv](https://arxiv.org/abs/2512.01996)
- **Published:** 2025-12
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## H-Zero: Cross-Humanoid Locomotion Pretraining Enables Few-shot Novel Embodiment Transfer

- **Paper:** [arXiv](https://arxiv.org/abs/2512.00971)
- **Published:** 2025-12
- **Tags:**
  - Locomotion
  - Few-Shot
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs

- **Paper:** [arXiv](https://arxiv.org/abs/2512.00077)
- **Published:** 2025-12
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain / [code](https://github.com/yzwfromk/STATE-NAV)

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01046)
- **Published:** 2025-12
- **Tags:**
  - Navigation
  - Biped

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Antagonistic Bowden-Cable Actuation of a Lightweight Robotic Hand: Toward Dexterous Manipulation for Payload Constrained Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2512.24657)
- **Published:** 2025-12
- **Tags:**
  - Manipulation
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Olaf: Bringing an Animated Character to Life in the Physical World

- **Paper:** [arXiv](https://arxiv.org/abs/2512.16705)
- **Published:** 2025-12
- **Tags:**
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## OSMO: Open-Source Tactile Glove for Human-to-Robot Skill Transfer

- **Paper:** [arXiv](https://arxiv.org/abs/2512.08920)
- **Published:** 2025-12
- **Tags:**
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DIJIT: A Robotic Head for an Active Observer

- **Paper:** [arXiv](https://arxiv.org/abs/2512.07998)
- **Published:** 2025-12
- **Tags:**
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Benchmarking Humanoid Imitation Learning with Motion Difficulty

- **Paper:** [arXiv](https://arxiv.org/abs/2512.07248)
- **Published:** 2025-12
- **Tags:**
  - Imitation Learning
  - Humanoid
  - Benchmark
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CRISP: Contact-Guided Real2Sim from Monocular Video with Planar Scene Primitives

- **Paper:** [arXiv](https://arxiv.org/abs/2512.14696)
- **Published:** 2025-12
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Control Physically-simulated 3D Characters via Generating and Mimicking 2D Motions

- **Paper:** [arXiv](https://arxiv.org/abs/2512.08500)
- **Published:** 2025-12
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Diffusion Forcing for Multi-Agent Interaction Sequence Modeling

- **Paper:** [arXiv](https://arxiv.org/abs/2512.17900)
- **Published:** 2025-12
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2512.00960)
- **Published:** 2025-12
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary

- **Paper:** [arXiv](https://arxiv.org/abs/2511.22963)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2511.21169)
- **Published:** 2025-11
- **Tags:**
  - Reinforcement Learning
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments

- **Paper:** [arXiv](https://arxiv.org/abs/2511.20275)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Adaptive Control
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SENTINEL: A Fully End-to-End Language-Action Model for Humanoid Whole Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2511.19236)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SafeFall: Learning Protective Control for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2511.18509)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data

- **Paper:** [arXiv](https://arxiv.org/abs/2511.17373)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2511.15200)
- **Published:** 2025-11
- **Tags:**
  - Sim-to-Real
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HMC: Learning Heterogeneous Meta-Control for Contact-Rich Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2511.14756)
- **Published:** 2025-11
- **Tags:**
  - Manipulation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Whole-Body Badminton via Multi-Stage Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2511.11218)
- **Published:** 2025-11
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robot Crash Course: Learning Soft and Stylized Falling

- **Paper:** [arXiv](https://arxiv.org/abs/2511.10635)
- **Published:** 2025-11
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Unveiling the Impact of Data and Model Scaling on High-Level Control for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2511.09241)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Impact
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2511.07820)
- **Published:** 2025-11
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Unified Humanoid Fall-Safety Policy from a Few Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2511.07407)
- **Published:** 2025-11
- **Tags:**
  - Safety
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning

- **Paper:** [arXiv](https://arxiv.org/abs/2511.06371)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Fine-tuning
  - Distillation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction

- **Paper:** [arXiv](https://arxiv.org/abs/2511.04679)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2511.04131)
- **Published:** 2025-11
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Vision-Driven Reactive Soccer Skills for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2511.03996)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System

- **Paper:** [arXiv](https://arxiv.org/abs/2511.02832)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SafeHumanoid: VLM-RAG-driven Control of Upper Body Impedance for Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2511.23300)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Dexterity from Smart Lenses: Multi-Fingered Robot Manipulation with In-the-Wild Human Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2511.16661)
- **Published:** 2025-11
- **Tags:**
  - Manipulation
  - Human Demonstration

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data

- **Paper:** [arXiv](https://arxiv.org/abs/2511.15704)
- **Published:** 2025-11
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2511.09141)
- **Published:** 2025-11
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Lightning Grasp: High Performance Procedural Grasp Synthesis with Contact Fields

- **Paper:** [arXiv](https://arxiv.org/abs/2511.07418)
- **Published:** 2025-11
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EgoMI: Learning Active Vision and Whole-Body Manipulation from Egocentric Human Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2511.00153)
- **Published:** 2025-11
- **Tags:**
  - Manipulation
  - Human Demonstration

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World

- **Paper:** [arXiv](https://arxiv.org/abs/2511.00041)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Adaptive Neural Teleoperation for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2511.12390)
- **Published:** 2025-11
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Reference-Free Sampling-Based Model Predictive Control

- **Paper:** [arXiv](https://arxiv.org/abs/2511.19204)
- **Published:** 2025-11
- **Tags:**
  - Sampling-Based
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Thinking in 360: Humanoid Visual Search in the Wild

- **Paper:** [arXiv](https://arxiv.org/abs/2511.20351)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D Constrained Terrains

- **Paper:** [arXiv](https://arxiv.org/abs/2511.14625)
- **Published:** 2025-11
- **Tags:**
  - Locomotion
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2511.18857)
- **Published:** 2025-11
- **Tags:**
  - Locomotion
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## InEKFormer: A Hybrid State Estimator for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2511.16306)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2511.10021)
- **Published:** 2025-11
- **Tags:**
  - Locomotion
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Human-Level Actuation for Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2511.06796)
- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Thor: Towards Human-Level Whole-Body Reactions for Intense Contact-Rich Environments

- **Paper:** [arXiv](https://arxiv.org/abs/2510.26280)
- **Published:** 2025-10
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## One-shot Humanoid Whole-body Motion Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2510.25241)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints

- **Paper:** [arXiv](https://arxiv.org/abs/2510.18002)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SoftMimic: Learning Compliant Whole-body Control from Examples

- **Paper:** [arXiv](https://arxiv.org/abs/2510.17792)
- **Published:** 2025-10
- **Tags:**
  - Whole-Body Control
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance

- **Paper:** [arXiv](https://arxiv.org/abs/2510.14952)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards Adaptable Humanoid Control via Adaptive Motion Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2510.14454)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Human-Humanoid Coordination for Collaborative Object Carrying

- **Paper:** [arXiv](https://arxiv.org/abs/2510.14293)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Ego-Vision World Model for Humanoid Contact Planning

- **Paper:** [arXiv](https://arxiv.org/abs/2510.11682)
- **Project:** [GitHub](https://ego-vcp.github.io/)
- **Published:** 2025-10
- **Tags:**
  - World Model
  - Humanoid
  - Contact Planning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2510.11258)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PhysHSI: Towards a Real-World Generalizable and Natural Humanoid-Scene Interaction System

- **Paper:** [arXiv](https://arxiv.org/abs/2510.11072)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## It Takes Two: Learning Interactive Whole-Body Control Between Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2510.10206)
- **Published:** 2025-10
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ResMimic: From General Motion Tracking to Humanoid Whole-body Loco-Manipulation via Residual Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2510.05070)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Residual Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HumanoidExo: Scalable Whole-Body Humanoid Manipulation via Wearable Exoskeleton

- **Paper:** [arXiv](https://arxiv.org/abs/2510.03022)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2510.02252)
- **Published:** 2025-10
- **Tags:**
  - Motion Retargeting
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## VisualMimic: Visual Humanoid Loco-Manipulation via Motion Tracking and Generation

- **Paper:** [arXiv](https://arxiv.org/abs/2509.20322)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Humanoid Visual-Tactile-Action Dataset for Contact-Rich Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2510.25725)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Dataset

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2510.07882)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Proprioception
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Development of an Intuitive GUI for Non-Expert Teleoperation of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2510.13594)
- **Published:** 2025-10
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation

- **Paper:** [arXiv](https://arxiv.org/abs/2510.04353)
- **Published:** 2025-10
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## LapSurgie: Humanoid Robots Performing Surgery via Teleoperated Handheld Laparoscopy

- **Paper:** [arXiv](https://arxiv.org/abs/2510.03529)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Teleoperation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning a Vision-Based Footstep Planner for Hierarchical Walking Control

- **Paper:** [arXiv](https://arxiv.org/abs/2510.12215)
- **Published:** 2025-10
- **Tags:**
  - Walking
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PHUMA: Physically-Grounded Humanoid Locomotion Dataset

- **Paper:** [arXiv](https://arxiv.org/abs/2510.26236)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid
  - Dataset

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## GaussGym: An open-source real-to-sim framework for learning locomotion from pixels

- **Paper:** [arXiv](https://arxiv.org/abs/2510.15352)
- **Published:** 2025-10
- **Tags:**
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Architecture Is All You Need: Diversity-Enabled Sweet Spots for Robust Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2510.14947)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing

- **Paper:** [arXiv](https://arxiv.org/abs/2510.12346)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2510.10851)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DPL: Depth-only Perceptive Humanoid Locomotion via Realistic Depth Synthesis and Cross-Attention Terrain Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2510.07152)
- **Published:** 2025-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization

- **Paper:** [arXiv](https://arxiv.org/abs/2510.01708)
- **Published:** 2025-10
- **Tags:**
  - Sim-to-Real
  - Simulator
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery

- **Paper:** [arXiv](https://arxiv.org/abs/2510.22336)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Embracing Evolution: A Call for Body-Control Co-Design in Embodied Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2510.03081)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2510.08807)
- **Published:** 2025-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Dataset
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report

- **Paper:** [arXiv](https://arxiv.org/abs/2510.07092)
- **Published:** 2025-10
- **Tags:**
  - World Model
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2510.02566)
- **Published:** 2025-10
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

- **Paper:** [arXiv](https://arxiv.org/abs/2509.26633)
- **Published:** 2025-09
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation

- **Paper:** [arXiv](https://arxiv.org/abs/2509.21690)
- **Published:** 2025-09
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SEEC: Stable End-Effector Control with Model-Enhanced Residual Learning for Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2509.21231)
- **Published:** 2025-09
- **Tags:**
  - Manipulation
  - Humanoid
  - Residual Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HDMI: Learning Interactive Humanoid Whole-Body Control from Human Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2509.16757)
- **Published:** 2025-09
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## KungfuBot 2: Learning Versatile Motion Skills for Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2509.16638)
- **Published:** 2025-09
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2509.15443)
- **Published:** 2025-09
- **Tags:**
  - Imitation Learning
  - Motion Retargeting
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DreamControl: Human-Inspired Whole-Body Humanoid Control for Scene Interaction via Guided Diffusion

- **Paper:** [arXiv](https://arxiv.org/abs/2509.14353)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Diffusion
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Track Any Motions under Any Disturbances

- **Paper:** [arXiv](https://arxiv.org/abs/2509.13833)
- **Project:** [GitHub](https://zzk273.github.io/Any2Track/)
- **Published:** 2025-09
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Behavior Foundation Model for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2509.13780)
- **Project:** [GitHub](https://bfm4humanoid.github.io/)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2509.13534)
- **Published:** 2025-09
- **Tags:**
  - Reinforcement Learning
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## StageACT: Stage-Conditioned Imitation for Robust Humanoid Door Opening

- **Paper:** [arXiv](https://arxiv.org/abs/2509.13200)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2509.11839)
- **Project:** [GitHub](https://jiachengliu3.github.io/TrajBooster/)
- **Published:** 2025-09
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EgoDemoGen: Novel Egocentric Demonstration Generation Enables Viewpoint-Robust Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2509.22578)
- **Published:** 2025-09
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Residual Off-Policy RL for Finetuning Behavior Cloning Policies

- **Paper:** [arXiv](https://arxiv.org/abs/2509.19301)
- **Published:** 2025-09
- **Tags:**
  - Behavior Cloning
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2509.09769)
- **Published:** 2025-09
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2509.24697)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RuN: Residual Policy for Natural Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2509.20696)
- **Published:** 2025-09
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Chasing Stability: Humanoid Running via Control Lyapunov Function Guided RL

- **Paper:** [arXiv](https://arxiv.org/abs/2509.19573)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Reduced-Order Model-Guided RL for Demonstration-Free Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2509.19023)
- **Published:** 2025-09
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HuMam: Humanoid Motion Control via End-to-End Deep RL with Mamba

- **Paper:** [arXiv](https://arxiv.org/abs/2509.18046)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Walk in Costume: Adversarial Motion Priors for Aesthetically Constrained Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2509.05581)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Quantum deep reinforcement learning for humanoid robot navigation task

- **Paper:** [arXiv](https://arxiv.org/abs/2509.11388)
- **Published:** 2025-09
- **Tags:**
  - Reinforcement Learning
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2509.12858)
- **Published:** 2025-09
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid
  - Representation Learning

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots

- **Paper:** [arXiv](https://arxiv.org/abs/2509.06342)
- **Published:** 2025-09
- **Tags:**
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance

- **Paper:** [arXiv](https://arxiv.org/abs/2509.26082)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Evolutionary
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Framework for Optimal Ankle Design of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2509.16469)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2509.14935)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## AGILOped: Agile Open-Source Humanoid Robot for Research

- **Paper:** [arXiv](https://arxiv.org/abs/2509.09364)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Ball: Composing Policies for Long-Horizon Basketball Moves

- **Paper:** [arXiv](https://arxiv.org/abs/2509.22442)
- **Published:** 2025-09
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RobotDancing: Residual-Action RL Enables Robust Long-Horizon Humanoid Motion Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2509.20717)
- **Published:** 2025-09
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HITTER: A HumanoId Table TEnnis Robot via Hierarchical Planning and Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2508.21043)
- **Project:** [GitHub](https://humanoid-table-tennis.github.io/)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HuBE: Cross-Embodiment Human-like Behavior Execution for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2508.19002)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement

- **Paper:** [arXiv](https://arxiv.org/abs/2508.16943)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Vision-Language
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Task and Motion Planning for Humanoid Loco-manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.14099)
- **Published:** 2025-08
- **Tags:**
  - Manipulation
  - Humanoid
  - Motion Planning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Differentiable Reachability Maps for Optimization-based Humanoid Motion Generation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.11275)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Optimization-Based
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.09960)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion

- **Paper:** [arXiv](https://arxiv.org/abs/2508.08241)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Diffusion
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Whole-Body Motion Imitation Framework from Human Data for Full-Size Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2508.00362)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Masquerade: Learning from In-the-wild Human Videos using Data-Editing

- **Paper:** [arXiv](https://arxiv.org/abs/2508.09976)
- **Published:** 2025-08
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2508.00355)
- **Published:** 2025-08
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Whole-Body Bilateral Teleoperation with Multi-Stage Object Parameter Estimation for Wheeled Humanoid Locomanipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.09846)
- **Published:** 2025-08
- **Tags:**
  - Teleoperation
  - Manipulation
  - Humanoid
  - Parameter Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CHILD: a Whole-Body Humanoid Teleoperation System

- **Paper:** [arXiv](https://arxiv.org/abs/2508.00162)
- **Published:** 2025-08
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Traversing Narrow Paths: A Two-Stage RL Framework for Robust and Safe Humanoid Walking

- **Paper:** [arXiv](https://arxiv.org/abs/2508.20661)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Walking
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## No More Marching: Learning Humanoid Locomotion for Short-Range SE(2) Targets

- **Paper:** [arXiv](https://arxiv.org/abs/2508.14098)
- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Geometry-Aware Predictive Safety Filters on Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2508.11129)
- **Published:** 2025-08
- **Tags:**
  - Safety
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MASH: Cooperative-Heterogeneous Multi-Agent RL for Single Humanoid Robot Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2508.10423)
- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## End-to-End Humanoid Robot Safe and Comfortable Locomotion Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2508.07611)
- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Optimizing Bipedal Locomotion for The 100m Dash With Comparison to Human Running

- **Paper:** [arXiv](https://arxiv.org/abs/2508.03070)
- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Biped

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2508.01247)
- **Published:** 2025-08
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications

- **Paper:** [arXiv](https://arxiv.org/abs/2508.06779)
- **Published:** 2025-08
- **Tags:**
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## LookOut: Real-World Humanoid Egocentric Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.14466)
- **Published:** 2025-08
- **Tags:**
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## INTENTION: Inferring Tendencies of Humanoid Robot Motion Through Interactive Intuition and Grounded VLM

- **Paper:** [arXiv](https://arxiv.org/abs/2508.04931)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching

- **Paper:** [arXiv](https://arxiv.org/abs/2508.03068)
- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2508.12252)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2508.19926)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL

- **Paper:** [arXiv](https://arxiv.org/abs/2508.14120)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Robot Acrobatics Utilizing Complete Articulated Rigid Body Dynamics

- **Paper:** [arXiv](https://arxiv.org/abs/2508.08258)
- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Being-M0.5: A Real-Time Controllable Vision-Language-Motion Model

- **Paper:** [arXiv](https://arxiv.org/abs/2508.07863)
- **Project:** [GitHub](https://beingbeyond.github.io/Being-M0.5/)
- **Published:** 2025-08
- **Tags:**
  - Vision-Language
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.15649)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training

- **Paper:** [arXiv](https://arxiv.org/abs/2507.08303)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2507.07356)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ULC: A Unified and Fine-Grained Controller for Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.06905)
- **Published:** 2025-07
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.23523)
- **Published:** 2025-07
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Being-H0: Vision-Language-Action Pretraining from Large-Scale Human Videos,  / [code](https://github.com/BeingBeyond/Being-H0) / [model](https://huggingface.co/collections/BeingBeyond/being-h0-688dcc58cbd6b452f16bd7ec)

- **Paper:** [arXiv](https://arxiv.org/abs/2507.15597)
- **Project:** [GitHub](https://beingbeyond.github.io/Being-H0/)
- **Published:** 2025-07
- **Tags:**
  - Vision-Language
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 EgoVLA: Learning Vision-Language-Action Models from Egocentric Human Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2507.12440)
- **Project:** [GitHub](https://rchalyang.github.io/EgoVLA/)
- **Published:** 2025-07
- **Tags:**
  - Vision-Language
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robot Drummer: Learning Rhythmic Skills for Humanoid Drumming

- **Paper:** [arXiv](https://arxiv.org/abs/2507.11498)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Success in Humanoid Reinforcement Learning under Partial Observation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.18883)
- **Published:** 2025-07
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.00273)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.10105)
- **Published:** 2025-07
- **Tags:**
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A 21-DOF Humanoid Dexterous Hand with Hybrid SMA-Motor Actuation: CYJ Hand-0

- **Paper:** [arXiv](https://arxiv.org/abs/2507.14538)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Dexterous Teleoperation of 20-DoF ByteDexter Hand via Human Motion Retargeting

- **Paper:** [arXiv](https://arxiv.org/abs/2507.03227)
- **Published:** 2025-07
- **Tags:**
  - Teleoperation
  - Motion Retargeting
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning

- **Paper:** [arXiv](https://arxiv.org/abs/2507.00833)
- **Project:** [GitHub](https://openhumanoidgen.github.io/)
- **Published:** 2025-07
- **Tags:**
  - Manipulation
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Feature-Based vs. GAN-Based Learning from Demonstrations: When and Why

- **Paper:** [arXiv](https://arxiv.org/abs/2507.05906)
- **Published:** 2025-07
- **Tags:**
  - GAN
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Humanoid Arm Motion via Centroidal Momentum Regularized Multi-Agent Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2507.04140)
- **Published:** 2025-07
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Occupancy: Enabling A Generalized Multimodal Occupancy Perception System on Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2507.20217)
- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Motion Skills with Adaptive Assistive Curriculum Force in Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.23125)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.20487)
- **Published:** 2025-06
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TACT: Humanoid Whole-body Contact Manipulation through Deep Imitation Learning with Tactile Modality

- **Paper:** [arXiv](https://arxiv.org/abs/2506.15146)
- **Published:** 2025-06
- **Tags:**
  - Imitation Learning
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## GMT: General Motion Tracking for Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2506.14770)
- **Published:** 2025-06
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

- **Paper:** [arXiv](https://arxiv.org/abs/2506.13751)
- **Published:** 2025-06
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Vision-Language
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills

- **Paper:** [arXiv](https://arxiv.org/abs/2506.12851)
- **Published:** 2025-06
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 From Experts to a Generalist: Toward General Whole-Body Control for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.12779)
- **Project:** [GitHub](https://beingbeyond.github.io/BumbleBee/)
- **Published:** 2025-06
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SkillBlender: Towards Versatile Humanoid Whole-Body Loco-Manipulation via Skill Blending

- **Paper:** [arXiv](https://arxiv.org/abs/2506.09366)
- **Published:** 2025-06
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning, [websie](https://robo-rl.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2506.04147)
- **Published:** 2025-06
- **Tags:**
  - Reinforcement Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hierarchical Intention-Aware Expressive Motion Generation for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01563)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## From Motion to Behavior: Hierarchical Modeling of Humanoid Generative Behavior Control

- **Paper:** [arXiv](https://arxiv.org/abs/2506.00043)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2506.22827)
- **Published:** 2025-06
- **Tags:**
  - Manipulation
  - Humanoid
  - Vision-Language

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Vision in Action: Learning Active Perception from Human Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2506.15666)
- **Published:** 2025-06
- **Tags:**
  - Human Demonstration
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## CLONE: Closed-Loop Whole-Body Humanoid Teleoperation for Long-Horizon Tasks

- **Paper:** [arXiv](https://arxiv.org/abs/2506.08931)
- **Published:** 2025-06
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Booster Gym: An End-to-End RL Framework for Humanoid Robot Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2506.15132)
- **Published:** 2025-06
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DoublyAware: Dual Planning and Policy Awareness for Temporal Difference Learning in Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2506.12095)
- **Published:** 2025-06
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 MoRE: Mixture of Residual Experts for Humanoid Lifelike Gaits Learning on Complex Terrains

- **Paper:** [arXiv](https://arxiv.org/abs/2506.08840)
- **Project:** [GitHub](https://more-humanoid.github.io/)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Gait
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Gait Driven RL Framework for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.08416)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Gait
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Aerodynamics for the Control of Flying Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2506.00305)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2506.02206)
- **Published:** 2025-06
- **Tags:**
  - Navigation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PIMBS: Efficient Body Schema Learning for Musculoskeletal Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2506.20343)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint

- **Paper:** [arXiv](https://arxiv.org/abs/2506.12314)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RAPID Hand: A Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Generalist Robot Autonomy

- **Paper:** [arXiv](https://arxiv.org/abs/2506.07490)
- **Published:** 2025-06
- **Tags:**
  - Manipulation
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## iRonCub 3: The Jet-Powered Flying Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01125)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning

- **Paper:** [arXiv](https://arxiv.org/abs/2506.16012)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning with pyCub: A Simulation and Exercise Framework for Humanoid Robotics

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01756)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid World Models: Open World Foundation Models for Humanoid Robotics

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01182)
- **Published:** 2025-06
- **Tags:**
  - World Model
  - Humanoid
  - Foundation Model
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## RL from Physical Feedback: Aligning Large Motion Models with Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2506.12769)
- **Published:** 2025-06
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SignBot: Learning Human-to-Humanoid Sign Language Interaction

- **Paper:** [arXiv](https://arxiv.org/abs/2505.24266)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.24198)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Mobi-π: Mobilizing Your Robot Learning Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2505.23692)
- **Project:** [GitHub](https://mobipi.github.io/)
- **Published:** 2025-05
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed Tactile Sensors

- **Paper:** [arXiv](https://arxiv.org/abs/2505.19580)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SMAP: Self-supervised Motion Adaptation for Physically Plausible Humanoid Whole-body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.19463)
- **Published:** 2025-05
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Self-Supervised
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Unleashing Humanoid Reaching Potential via Real-world-Ready Skill Space

- **Paper:** [arXiv](https://arxiv.org/abs/2505.10918)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HuB: Learning Extreme Humanoid Balance,

- **Paper:** [arXiv](https://arxiv.org/abs/2505.07294)
- **Project:** [GitHub](https://hub-robot.github.io/)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2505.06776)
- **Project:** [GitHub](https://lecar-lab.github.io/falcon-humanoid/)
- **Published:** 2025-05
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## JAEGER: Dual-Level Humanoid Whole-Body Controller

- **Paper:** [arXiv](https://arxiv.org/abs/2505.06584)
- **Published:** 2025-05
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.03738)
- **Project:** [GitHub](https://amo-humanoid.github.io/)
- **Published:** 2025-05
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 PyRoki: A Modular Toolkit for Robot Kinematic Optimization

- **Paper:** [arXiv](https://arxiv.org/abs/2505.03728)
- **Project:** [GitHub](https://pyroki-toolkit.github.io/)
- **Published:** 2025-05
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## **TWIST: Teleoperated Whole-Body Imitation System**

- **Paper:** [arXiv](https://arxiv.org/abs/2505.02833)
- **Published:** 2025-05
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DreamGen: Unlocking Generalization in Robot Learning through Neural Trajectories

- **Paper:** [arXiv](https://arxiv.org/abs/2505.12705)
- **Published:** 2025-05
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EgoDex: Learning Dexterous Manipulation from Large-Scale Egocentric Video

- **Paper:** [arXiv](https://arxiv.org/abs/2505.11709)
- **Published:** 2025-05
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Heavy lifting tasks via haptic teleoperation of a wheeled humanoid

- **Paper:** [arXiv](https://arxiv.org/abs/2505.19530)
- **Published:** 2025-05
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation

- **Paper:** [arXiv](https://arxiv.org/abs/2505.12748)
- **Project:** [GitHub](https://gorgeous2002.github.io/TeleOpBench/)
- **Published:** 2025-05
- **Tags:**
  - Teleoperation
  - Simulator
  - Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Human-Robot Collaboration for the Remote Control of Mobile Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2505.05773)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Teleoperation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 FastTD3: Simple, Fast, and Capable Reinforcement Learning for Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.22642)
- **Project:** [GitHub](https://younggyo.me/fast_td3/)
- **Published:** 2025-05
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - TD3
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Gait-Conditioned RL with Multi-Phase Curriculum for Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2505.20619)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Humanoid
  - Gait

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Omni-Perception: Omnidirectional Collision Avoidance for Legged Locomotion in Dynamic Environments

- **Paper:** [arXiv](https://arxiv.org/abs/2505.19214)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Collision

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## One Policy but Many Worlds: A Scalable Unified Policy for Versatile Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2505.18780)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TD-GRPC: Temporal Difference Learning with Group Relative Policy Constraint for Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2505.13549)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2505.12679)
- **Published:** 2025-05
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SHIELD: Safety on Humanoids via CBFs In Expectation on Learned Dynamics

- **Paper:** [arXiv](https://arxiv.org/abs/2505.11494)
- **Published:** 2025-05
- **Tags:**
  - Safety
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Let Humanoids Hike! Integrative Skill Development on Complex Trails

- **Paper:** [arXiv](https://arxiv.org/abs/2505.06218)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 VideoMimic: Visual imitation enables contextual humanoid control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.03729)
- **Project:** [GitHub](https://www.videomimic.net/)
- **Published:** 2025-05
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

- **Paper:** [arXiv](https://arxiv.org/abs/2505.08712)
- **Published:** 2025-05
- **Tags:**
  - Diffusion Policy
  - Sim-to-Real
  - Navigation
  - Diffusion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.24068)
- **Published:** 2025-05
- **Tags:**
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2505.14266)
- **Published:** 2025-05
- **Tags:**
  - System Identification
  - Sampling-Based
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## AMOR: Adaptive Character Control through Multi-Objective Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2505.23708)
- **Published:** 2025-05
- **Tags:**
  - Reinforcement Learning
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MaskedManipulator: Versatile Whole-Body Control for Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2505.19086)
- **Published:** 2025-05
- **Tags:**
  - Whole-Body Control
  - Manipulation
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2505.12278)
- **Project:** [GitHub](https://www.zhengyiluo.com/PDC-Site/)
- **Published:** 2025-05
- **Tags:**
  - Reinforcement Learning
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 GENMO: A GENeralist Model for Human MOtion

- **Paper:** [arXiv](https://arxiv.org/abs/2505.01425)
- **Project:** [GitHub](https://research.nvidia.com/labs/dair/genmo/)
- **Published:** 2025-05
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 H2-COMPACT: Human-Humanoid Co-Manipulation via Adaptive Contact Trajectory Policies

- **Paper:** [arXiv](https://arxiv.org/abs/2505.17627)
- **Project:** [GitHub](https://h2compact.github.io/h2compact/)
- **Published:** 2025-05
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators

- **Paper:** [arXiv](https://arxiv.org/abs/2505.04961)
- **Published:** 2025-05
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## LangWBC: Language-directed Humanoid Whole-Body Control via End-to-end Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2504.21738)
- **Published:** 2025-04
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Adversarial Locomotion and Motion Imitation for Humanoid Policy Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2504.14305)
- **Project:** [GitHub](https://almi-humanoid.github.io/)
- **Published:** 2025-04
- **Tags:**
  - Locomotion
  - Humanoid
  - Policy Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SoccerDiffusion: Toward Learning End-to-End Humanoid Robot Soccer from Gameplay Recordings

- **Paper:** [arXiv](https://arxiv.org/abs/2504.20808)
- **Published:** 2025-04
- **Tags:**
  - Humanoid
  - Diffusion
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL

- **Paper:** [arXiv](https://arxiv.org/abs/2504.13619)
- **Published:** 2025-04
- **Tags:**
  - Humanoid
  - Walking
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2504.09833)
- **Published:** 2025-04
- **Tags:**
  - Locomotion
  - Humanoid
  - Pre-training
  - Fine-tuning

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Spectral Normalization for Lipschitz-Constrained Policies on Learning Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2504.08246)
- **Published:** 2025-04
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted IMUs

- **Paper:** [arXiv](https://arxiv.org/abs/2504.00614)
- **Published:** 2025-04
- **Tags:**
  - Locomotion
  - Biped
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection

- **Paper:** [arXiv](https://arxiv.org/abs/2504.06585)
- **Published:** 2025-04
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2504.17249)
- **Project:** [GitHub](https://lite.berkeley-humanoid.org/)
- **Published:** 2025-04
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 RUKA: Rethinking the Design of Humanoid Hands with Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2504.13165)
- **Project:** [GitHub](https://ruka-hand.github.io/)
- **Published:** 2025-04
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ORCA: Open-Source, Reliable, Cost-Effective, Anthropomorphic Robotic Hand for Uninterrupted Dexterous Task Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2504.04259)
- **Project:** [GitHub](https://www.orcahand.com/)
- **Published:** 2025-04
- **Tags:**
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Zero-Shot Whole-Body Humanoid Control via Behavioral Foundation Models

- **Paper:** [arXiv](https://arxiv.org/abs/2504.11054)
- **Published:** 2025-04
- **Tags:**
  - Zero-Shot
  - Humanoid
  - Foundation Model
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HUMOTO: A 4D Dataset of Mocap Human Object Interactions

- **Paper:** [arXiv](https://arxiv.org/abs/2504.10414)
- **Project:** [GitHub](https://jiaxin-lu.github.io/humoto/)
- **Published:** 2025-04
- **Tags:**
  - Dataset
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PICO: Reconstructing 3D People In Contact with Objects

- **Paper:** [arXiv](https://arxiv.org/abs/2504.17695)
- **Published:** 2025-04
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Physically Consistent Humanoid Loco-Manipulation using Latent Diffusion Models

- **Paper:** [arXiv](https://arxiv.org/abs/2504.16843)
- **Published:** 2025-04
- **Tags:**
  - Manipulation
  - Humanoid
  - Diffusion
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Embodied Chain of Action Reasoning with Multi-Modal Foundation Model for Humanoid Loco-manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2504.09532)
- **Project:** [GitHub](https://humanoid-coa.github.io/)
- **Published:** 2025-04
- **Tags:**
  - Manipulation
  - Humanoid
  - Foundation Model
  - Multi-Modal
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2503.22249)
- **Published:** 2025-03
- **Tags:**
  - Locomotion
  - Manipulation
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Being-0: A Humanoid Robotic Agent with Vision-Language Models and Modular Skills

- **Paper:** [arXiv](https://arxiv.org/abs/2503.12533)
- **Project:** [GitHub](https://beingbeyond.github.io/being-0/)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Vision-Language
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Trinity: A Modular Humanoid Robot AI System

- **Paper:** [arXiv](https://arxiv.org/abs/2503.08338)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities, [websie](https://behavior-robot-suite.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2503.05652)
- **Published:** 2025-03
- **Tags:**
  - Manipulation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Whole-Body Model-Predictive Control of Legged Robots with MuJoCo

- **Paper:** [arXiv](https://arxiv.org/abs/2503.04613)
- **Published:** 2025-03
- **Tags:**
  - MuJoCo
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2503.24361)
- **Project:** [GitHub](https://co-training.github.io/)
- **Published:** 2025-03
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## GR00T N1: An Open Foundation Model for Generalist Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2503.14734)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Foundation Model
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Humanoid Policy ~ Human Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2503.13441)
- **Project:** [GitHub](https://human-as-robot.github.io/)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions

- **Paper:** [arXiv](https://arxiv.org/abs/2503.12725)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Unified Video Action Model

- **Paper:** [arXiv](https://arxiv.org/abs/2503.00200)
- **Project:** [GitHub](https://unified-video-action-model.github.io/)
- **Published:** 2025-03
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2503.10554)
- **Published:** 2025-03
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## StyleLoco: Generative Adversarial Distillation for Natural Humanoid Robot Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2503.15082)
- **Published:** 2025-03
- **Tags:**
  - Locomotion
  - Humanoid
  - Distillation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Natural Humanoid Robot Locomotion with Generative Motion Prior

- **Paper:** [arXiv](https://arxiv.org/abs/2503.09015)
- **Published:** 2025-03
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures

- **Paper:** [arXiv](https://arxiv.org/abs/2503.08349)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Distillation-PPO: A Novel Two-Stage RL Framework for Humanoid Robot Perceptive Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2503.08299)
- **Published:** 2025-03
- **Tags:**
  - Locomotion
  - Humanoid
  - Distillation
  - PPO

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2503.00923)
- **Project:** [GitHub](https://simonlinsx.github.io/HWC_Loco/)
- **Published:** 2025-03
- **Tags:**
  - Whole-Body Control
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Perceptive Humanoid Locomotion over Challenging Terrain

- **Paper:** [arXiv](https://arxiv.org/abs/2503.00692)
- **Published:** 2025-03
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2503.09010)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Control of Humanoid Robots with Parallel Mechanisms using Kinematic Actuation Models

- **Paper:** [arXiv](https://arxiv.org/abs/2503.22459)
- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video

- **Paper:** [arXiv](https://arxiv.org/abs/2503.23094)
- **Project:** [GitHub](https://vcai.mpi-inf.mpg.de/projects/FRAME/)
- **Published:** 2025-03
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2503.17544)
- **Published:** 2025-03
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate

- **Paper:** [arXiv](https://arxiv.org/abs/2503.21268)
- **Published:** 2025-03
- **Tags:**
  - Dataset
  - Multi-Modal
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 CVPR 2025 Oral, TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization

- **Paper:** [arXiv](https://arxiv.org/abs/2503.19901)
- **Project:** [GitHub](https://liangpan99.github.io/TokenHSI/)
- **Published:** 2025-03
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## HiFAR: Multi-Stage Curriculum Learning for High-Dynamics Humanoid Fall Recovery

- **Paper:** [arXiv](https://arxiv.org/abs/2502.20061)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Curriculum Learning
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **HOMIE**: Humanoid Loco-Manipulation with Isomorphic Exoskeleton Cockpit,  / [github](https://github.com/OpenRobotLab/OpenHomie)

- **Paper:** [arXiv](https://arxiv.org/abs/2502.13013)
- **Project:** [GitHub](https://homietele.github.io/)
- **Published:** 2025-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning Getting-Up Policies for Real-World Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2502.12152)
- **Project:** [GitHub](https://humanoid-getup.github.io/)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Humanoid Standing-up Control across Diverse Postures

- **Paper:** [arXiv](https://arxiv.org/abs/2502.08378)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## **HugWBC**: A Unified and General Humanoid Whole-Body Controller

- **Paper:** [arXiv](https://arxiv.org/abs/2502.03206)
- **Published:** 2025-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **SPARK**: A Toolbox for Safe Humanoid Autonomy and Teleoperation

- **Paper:** [arXiv](https://arxiv.org/abs/2502.03132)
- **Project:** [GitHub](https://intelligent-control-lab.github.io/spark/)
- **Published:** 2025-02
- **Tags:**
  - Teleoperation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **Embrace Collisions**: Humanoid Shadowing for Deployable Contact-Agnostics Motions

- **Paper:** [arXiv](https://arxiv.org/abs/2502.01465)
- **Project:** [GitHub](https://project-instinct.github.io/)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Collision
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## **Dexterous Safe Control** for Humanoids in Cluttered Environments via Projected Safe Set Algorithm

- **Paper:** [arXiv](https://arxiv.org/abs/2502.02858)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Humanoid Whole-Body Locomotion on Narrow Terrain via Dynamic Balance and Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2502.17219)
- **Published:** 2025-02
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Humanoid Locomotion with World Model Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2502.16230)
- **Published:** 2025-02
- **Tags:**
  - Locomotion
  - World Model
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **VB-Com**: Learning Vision-Blind Composite Humanoid Locomotion Against Deficient Perception

- **Paper:** [arXiv](https://arxiv.org/abs/2502.14814)
- **Project:** [GitHub](https://renjunli99.github.io/vbcom.github.io/)
- **Published:** 2025-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds

- **Paper:** [arXiv](https://arxiv.org/abs/2502.10363)
- **Project:** [GitHub](https://why618188.github.io/beamdojo/)
- **Published:** 2025-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2502.10894)
- **Published:** 2025-02
- **Tags:**
  - Sim-to-Real
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Exceeding the Maximum Speed Limit of the Joint Angle for the Redundant Tendon-driven Structures of Musculoskeletal Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2502.12808)
- **Published:** 2025-02
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **ToddlerBot**: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation,  / [github](https://github.com/hshi74/toddlerbot)

- **Paper:** [arXiv](https://arxiv.org/abs/2502.00893)
- **Project:** [GitHub](https://toddlerbot.github.io/)
- **Published:** 2025-02
- **Tags:**
  - Manipulation
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 InterMimic: Towards Universal Whole-Body Control for Physics-Based Human-Object Interactions, , [code](https://github.com/Sirui-Xu/InterMimic)

- **Paper:** [arXiv](https://arxiv.org/abs/2502.20390)
- **Project:** [GitHub](https://sirui-xu.github.io/InterMimic/)
- **Published:** 2025-02
- **Tags:**
  - Whole-Body Control
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data

- **Paper:** [arXiv](https://arxiv.org/abs/2501.04595)
- **Published:** 2025-01
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Design and Control of a Bipedal Robotic Character

- **Paper:** [arXiv](https://arxiv.org/abs/2501.05204)
- **Published:** 2025-01
- **Tags:**
  - Biped
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration

- **Paper:** [arXiv](https://arxiv.org/abs/2412.15166)
- **Published:** 2024-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning from Massive Human Videos for Universal Humanoid Pose Control

- **Paper:** [arXiv](https://arxiv.org/abs/2412.14172)
- **Project:** [GitHub](https://usc-gvl.github.io/UH-1/)
- **Published:** 2024-12
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **ExBody2**: Advanced Expressive Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2412.13196)
- **Project:** [GitHub](https://exbody2.github.io/)
- **Published:** 2024-12
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **Mobile-TeleVision**: Predictive Motion Priors for Humanoid Whole-Body Control

- **Paper:** [arXiv](https://arxiv.org/abs/2412.07773)
- **Project:** [GitHub](https://mobile-tv.github.io/)
- **Published:** 2024-12
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ARMADA: Augmented Reality for Robot Manipulation and Robot-Free Data Acquisition

- **Paper:** [arXiv](https://arxiv.org/abs/2412.10631)
- **Project:** [GitHub](https://nataliya.dev/armada)
- **Published:** 2024-12
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **NaVILA**: Legged Robot Vision-Language-Action Model for Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2412.04453)
- **Project:** [GitHub](https://navila-bot.github.io/)
- **Published:** 2024-12
- **Tags:**
  - Navigation
  - Vision-Language

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning

- **Paper:** [arXiv](https://arxiv.org/abs/2412.00396)
- **Published:** 2024-12
- **Tags:**
  - Humanoid
  - Collision
  - Motion Planning
  - Navigation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **Mimicking-Bench**: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking

- **Paper:** [arXiv](https://arxiv.org/abs/2412.17730)
- **Project:** [GitHub](https://mimicking-bench.github.io/)
- **Published:** 2024-12
- **Tags:**
  - Humanoid
  - Benchmark
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 **ManiSkill-HAB**: A Benchmark for Low-Level Manipulation in Home Rearrangement Tasks

- **Paper:** [arXiv](https://arxiv.org/abs/2412.13211)
- **Project:** [GitHub](https://arth-shukla.github.io/mshab/)
- **Published:** 2024-12
- **Tags:**
  - Manipulation
  - Benchmark
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## A Behavior Architecture for Fast Humanoid Robot Door Traversals, [video](https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy)

- **Paper:** [arXiv](https://arxiv.org/abs/2411.03532)
- **Published:** 2024-11
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2411.01349)
- **Published:** 2024-11
- **Tags:**
  - Domain Randomization
  - Humanoid
  - Diffusion
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Object-Centric Dexterous Manipulation from Human Motion Data

- **Paper:** [arXiv](https://arxiv.org/abs/2411.04005)
- **Project:** [GitHub](https://cypypccpy.github.io/obj-dex.github.io/)
- **Published:** 2024-11
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 DexHub and DART: Towards Internet-Scale Robot Data Collection

- **Paper:** [arXiv](https://arxiv.org/abs/2411.02214)
- **Project:** [GitHub](https://dexhub.ai/project)
- **Published:** 2024-11
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Look Around: Enhancing Teleoperation and Learning with a Human-like Actuated Neck

- **Paper:** [arXiv](https://arxiv.org/abs/2411.00704)
- **Published:** 2024-11
- **Tags:**
  - Teleoperation
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Humanoid Locomotion with Perceptive Internal Model

- **Paper:** [arXiv](https://arxiv.org/abs/2411.14386)
- **Published:** 2024-11
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Real-Time Polygonal Semantic Mapping for Humanoid Robot Stair Climbing, [code](https://github.com/BTFrontier/polygon_mapping)

- **Paper:** [arXiv](https://arxiv.org/abs/2411.01919)
- **Published:** 2024-11
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## EMOTION: Expressive Motion Sequence Generation for Humanoid Robots with In-Context Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2410.23234)
- **Published:** 2024-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2410.21229)
- **Project:** [GitHub](https://hover-versatile-humanoid.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Harmon: Whole-Body Motion Generation of Humanoid Robots from Language Descriptions

- **Paper:** [arXiv](https://arxiv.org/abs/2410.12773)
- **Project:** [GitHub](https://ut-austin-rpl.github.io/Harmon/)
- **Published:** 2024-10
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Whole-Body Dynamic Throwing with Legged Manipulators

- **Paper:** [arXiv](https://arxiv.org/abs/2410.05681)
- **Published:** 2024-10
- **Tags:**
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 EgoMimic: Scaling Imitation Learning via Egocentric Video,  / [code](https://github.com/SimarKareer/EgoMimic)

- **Paper:** [arXiv](https://arxiv.org/abs/2410.24221)
- **Project:** [GitHub](https://egomimic.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Imitation Learning
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning to Look: Seeking Information for Decision Making via Policy Factorization

- **Paper:** [arXiv](https://arxiv.org/abs/2410.18964)
- **Project:** [GitHub](https://robin-lab.cs.utexas.edu/learning2look/)
- **Published:** 2024-10
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation

- **Paper:** [arXiv](https://arxiv.org/abs/2410.11792)
- **Project:** [GitHub](https://ut-austin-rpl.github.io/OKAMI/)
- **Published:** 2024-10
- **Tags:**
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Generalizable Humanoid Manipulation with Improved 3D Diffusion Policies,  / [code](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy)

- **Paper:** [arXiv](https://arxiv.org/abs/2410.10803)
- **Project:** [GitHub](https://humanoid-manipulation.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Manipulation
  - Humanoid
  - Diffusion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning Smooth Humanoid Locomotion through Lipschitz-Constrained Policies,  / [code](https://github.com/zixuan417/smooth-humanoid-locomotion)

- **Paper:** [arXiv](https://arxiv.org/abs/2410.11825)
- **Project:** [GitHub](https://lipschitz-constrained-policy.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning Humanoid Locomotion over Challenging Terrain

- **Paper:** [arXiv](https://arxiv.org/abs/2410.03654)
- **Project:** [GitHub](https://humanoid-challenging-terrain.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2410.24185)
- **Project:** [GitHub](https://dexmimicgen.github.io/)
- **Published:** 2024-10
- **Tags:**
  - Imitation Learning
  - Manipulation
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI,  / [code](https://github.com/haosulab/ManiSkill)

- **Paper:** [arXiv](https://arxiv.org/abs/2410.00425)
- **Project:** [GitHub](https://www.maniskill.ai/home)
- **Published:** 2024-10
- **Tags:**
  - Embodied AI
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Scaling Large Motion Models with Million-Level Human Motions

- **Paper:** [arXiv](https://arxiv.org/abs/2410.03311)
- **Published:** 2024-10
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 CLoSD: Closing the Loop between Simulation and Diffusion for multi-task character control

- **Paper:** [arXiv](https://arxiv.org/abs/2410.03441)
- **Project:** [GitHub](https://guytevet.github.io/CLoSD-page/)
- **Published:** 2024-10
- **Tags:**
  - Multi-Task
  - Diffusion
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Opt2Skill: Imitating Dynamically-feasible Whole-Body Trajectories for Versatile Humanoid Loco-Manipulation, [Website](https://opt2skill.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2409.20514)
- **Published:** 2024-09
- **Tags:**
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing

- **Paper:** [arXiv](https://arxiv.org/abs/2409.15610)
- **Published:** 2024-09
- **Tags:**
  - MPC
  - Locomotion
  - Sampling-Based
  - Diffusion
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 The Duke Humanoid: Design and Control For Energy Efficient Bipedal Locomotion Using Passive Dynamics,  / [code](https://github.com/generalroboticslab/dukeHumanoidHardwareControl)

- **Paper:** [arXiv](https://arxiv.org/abs/2409.19795)
- **Project:** [GitHub](http://www.generalroboticslab.com/blogs/blog/2024-09-29-dukehumanoidv1/index.html)
- **Published:** 2024-09
- **Tags:**
  - Locomotion
  - Biped
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting

- **Paper:** [arXiv](https://arxiv.org/abs/2409.14393)
- **Project:** [GitHub](https://research.nvidia.com/labs/par/maskedmimic/)
- **Published:** 2024-09
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## High-Speed and Impact Resilient Teleoperation of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2409.04639)
- **Published:** 2024-09
- **Tags:**
  - Teleoperation
  - Humanoid
  - Impact

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation,  / [code](https://github.com/ACETeleop/ACETeleop)

- **Paper:** [arXiv](https://arxiv.org/abs/2408.11805)
- **Project:** [GitHub](https://ace-teleop.github.io/)
- **Published:** 2024-08
- **Tags:**
  - Teleoperation
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Advancing Humanoid Locomotion: Mastering Challenging Terrains with Denoising World Model Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2408.14472)
- **Published:** 2024-08
- **Tags:**
  - Locomotion
  - World Model
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## SkillMimic: Learning Basketball Interaction Skills from Demonstrations

- **Paper:** [arXiv](https://arxiv.org/abs/2408.15270)
- **Published:** 2024-08
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation, [video](https://www.youtube.com/watch?v=OyXojqRasHU) /

- **Paper:** [arXiv](https://arxiv.org/abs/2407.12381)
- **Project:** [GitHub](https://hucebot.github.io/flow_multisupport_website/)
- **Published:** 2024-07
- **Tags:**
  - Imitation Learning
  - Manipulation
  - PPO
  - Flow Matching
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Bunny-VisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning,  / [code](https://github.com/Dingry/BunnyVisionPro)

- **Paper:** [arXiv](https://arxiv.org/abs/2407.03162)
- **Project:** [GitHub](https://dingry.github.io/projects/bunny_visionpro.html)
- **Published:** 2024-07
- **Tags:**
  - Imitation Learning
  - Teleoperation
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Open-TeleVision: Teleoperation with Immersive Active Visual Feedback,  / [code](https://github.com/OpenTeleVision/TeleVision)

- **Paper:** [arXiv](https://arxiv.org/abs/2407.01512)
- **Project:** [GitHub](https://robot-tv.github.io/)
- **Published:** 2024-07
- **Tags:**
  - Teleoperation
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Berkeley Humanoid: A Research Platform for Learning-based Control,  / [code](https://github.com/HybridRobotics/isaac_berkeley_humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2407.21781)
- **Project:** [GitHub](https://berkeley-humanoid.com/)
- **Published:** 2024-07
- **Tags:**
  - Humanoid
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 BiGym: A Demo-Driven Mobile Bi-Manual Manipulation Benchmark,  / [code](https://github.com/chernyadev/bigym)

- **Paper:** [arXiv](https://arxiv.org/abs/2407.07788)
- **Project:** [GitHub](https://chernyadev.github.io/bigym/)
- **Published:** 2024-07
- **Tags:**
  - Manipulation
  - Benchmark
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 GRUtopia: Dream General Robots in a City at Scale

- **Paper:** [arXiv](https://arxiv.org/abs/2407.10943)
- **Project:** [GitHub](https://github.com/OpenRobotLab/GRUtopia)
- **Published:** 2024-07
- **Tags:**
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HumanPlus: Humanoid Shadowing and Imitation from Humans,  / [code](https://github.com/MarkFzp/humanplus)

- **Paper:** [arXiv](https://arxiv.org/abs/2406.10454)
- **Project:** [GitHub](https://humanoid-ai.github.io/)
- **Published:** 2024-06
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning,  / [code](https://github.com/LeCAR-Lab/human2humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2406.08858)
- **Project:** [GitHub](https://omni.human2humanoid.com/)
- **Published:** 2024-06
- **Tags:**
  - Teleoperation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 WoCoCo: Learning Whole-Body Humanoid Control with Sequential Contacts

- **Paper:** [arXiv](https://arxiv.org/abs/2406.06005)
- **Project:** [GitHub](https://lecar-lab.github.io/wococo/)
- **Published:** 2024-06
- **Tags:**
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Humanoid Parkour Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2406.10759)
- **Project:** [GitHub](https://humanoid4parkour.github.io/)
- **Published:** 2024-06
- **Tags:**
  - Humanoid
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots,  / [code](https://github.com/robocasa/robocasa)

- **Paper:** [arXiv](https://arxiv.org/abs/2406.02523)
- **Project:** [GitHub](https://robocasa.ai/)
- **Published:** 2024-06
- **Tags:**
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HYPERmotion: Learning Hybrid Behavior Planning for Autonomous Loco-manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2406.14655)
- **Project:** [GitHub](https://hy-motion.github.io/)
- **Published:** 2024-06
- **Tags:**
  - Manipulation
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Flexible Motion In-betweening with Diffusion Models

- **Paper:** [arXiv](https://arxiv.org/abs/2405.11126)
- **Published:** 2024-05
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning Visuotactile Skills with Two Multifingered Hands,  / [code](https://github.com/toruowo/hato)

- **Paper:** [arXiv](https://arxiv.org/abs/2404.16823)
- **Project:** [GitHub](https://toruowo.github.io/hato/)
- **Published:** 2024-04
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey

- **Paper:** [arXiv](https://arxiv.org/abs/2404.17070)
- **Published:** 2024-04
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Biped

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer,  / [code](https://github.com/roboterax/humanoid-gym)

- **Paper:** [arXiv](https://arxiv.org/abs/2404.05695)
- **Project:** [GitHub](https://sites.google.com/view/humanoid-gym/)
- **Published:** 2024-04
- **Tags:**
  - Reinforcement Learning
  - Zero-Shot
  - Humanoid
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Taming Diffusion Probabilistic Models for Character Control

- **Paper:** [arXiv](https://arxiv.org/abs/2404.15121)
- **Published:** 2024-04
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation,  / [code](https://github.com/LeCAR-Lab/human2humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2403.04436)
- **Project:** [GitHub](https://human2humanoid.com/)
- **Published:** 2024-03
- **Tags:**
  - Teleoperation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation,  / [code](https://github.com/j96w/DexCap)

- **Paper:** [arXiv](https://arxiv.org/abs/2403.07788)
- **Project:** [GitHub](https://dex-cap.github.io/)
- **Published:** 2024-03
- **Tags:**
  - Manipulation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation,  / [code](https://github.com/carlosferrazza/humanoid-bench)

- **Paper:** [arXiv](https://arxiv.org/abs/2403.10506)
- **Project:** [GitHub](https://humanoid-bench.github.io/)
- **Published:** 2024-03
- **Tags:**
  - Locomotion
  - Manipulation
  - Humanoid
  - Benchmark
  - Simulation Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Expressive Whole-Body Control for Humanoid Robots,  / [code](https://github.com/chengxuxin/expressive-humanoid)

- **Paper:** [arXiv](https://arxiv.org/abs/2402.16796)
- **Project:** [GitHub](https://expressive-humanoid.github.io/)
- **Published:** 2024-02
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Humanoid Locomotion as Next Token Prediction

- **Paper:** [arXiv](https://arxiv.org/abs/2402.19469)
- **Project:** [GitHub](https://humanoid-next-token-prediction.github.io/)
- **Published:** 2024-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Whole-body Humanoid Robot Locomotion with Human Reference

- **Paper:** [arXiv](https://arxiv.org/abs/2402.18294)
- **Project:** [GitHub](https://greatsjk.github.io/Adam-PNDbotics/)
- **Published:** 2024-02
- **Tags:**
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Reinforcement Learning for Versatile, Dynamic, and Robust Bipedal Locomotion Control

- **Paper:** [arXiv](https://arxiv.org/abs/2401.16889)
- **Published:** 2024-01
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Biped

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Sim-to-Real Learning for Humanoid Box Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2310.03191)
- **Published:** 2023-10
- **Tags:**
  - Sim-to-Real
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration

- **Paper:** [arXiv](https://arxiv.org/abs/2310.07896)
- **Published:** 2023-10
- **Tags:**
  - Navigation
  - Diffusion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## OmniControl: Control Any Joint at Any Time for Human Motion Generation

- **Paper:** [arXiv](https://arxiv.org/abs/2310.08580)
- **Published:** 2023-10
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Deep Imitation Learning for Humanoid Loco-manipulation through Human Teleoperation,  / [code](https://github.com/UT-Austin-RPL/TRILL)

- **Paper:** [arXiv](https://arxiv.org/abs/2309.01952)
- **Project:** [GitHub](https://ut-austin-rpl.github.io/TRILL/)
- **Published:** 2023-09
- **Tags:**
  - Imitation Learning
  - Teleoperation
  - Manipulation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning to Walk and Fly with Adversarial Motion Priors

- **Paper:** [arXiv](https://arxiv.org/abs/2309.12784)
- **Published:** 2023-09
- **Tags:**
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Unified Human-Scene Interaction via Prompted Chain-of-Contacts

- **Paper:** [arXiv](https://arxiv.org/abs/2309.07918)
- **Project:** [GitHub](https://xizaoqu.github.io/unihsi/)
- **Published:** 2023-09
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Benchmarking **Potential Based Rewards** for Learning Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2307.10142)
- **Published:** 2023-07
- **Tags:**
  - Locomotion
  - Humanoid
  - Benchmark

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis

- **Paper:** [arXiv](https://arxiv.org/abs/2307.15042)
- **Published:** 2023-07
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hierarchical Planning and Control for Box Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2306.09532)
- **Published:** 2023-06
- **Tags:**
  - Manipulation
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Example-based Motion Synthesis via Generative Motion Matching

- **Paper:** [arXiv](https://arxiv.org/abs/2306.00378)
- **Published:** 2023-06
- **Tags:**
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Perpetual Humanoid Control for Real-time Simulated Avatars, [code](https://github.com/ZhengyiLuo/PHC)

- **Paper:** [arXiv](https://arxiv.org/abs/2305.06456)
- **Published:** 2023-05
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Guided Motion Diffusion for Controllable Human Motion Synthesis

- **Paper:** [arXiv](https://arxiv.org/abs/2305.12577)
- **Published:** 2023-05
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Real-World Humanoid Locomotion with Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2303.03381)
- **Project:** [GitHub](https://learning-humanoid-locomotion.github.io/)
- **Published:** 2023-03
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Robust and Versatile Bipedal Jumping Control through Reinforcement Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2302.09450)
- **Published:** 2023-02
- **Tags:**
  - Reinforcement Learning
  - Biped
  - Locomotion

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Teleoperation of Humanoid Robots: A Survey, [webpage](https://humanoid-teleoperation.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2301.04317)
- **Published:** 2023-01
- **Tags:**
  - Teleoperation
  - Humanoid

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo

- **Paper:** [arXiv](https://arxiv.org/abs/2212.00541)
- **Published:** 2022-12
- **Tags:**
  - MuJoCo
  - Loco-Manipulation and Whole-Body Control

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 PhysDiff: Physics-Guided Human Motion Diffusion Model

- **Paper:** [arXiv](https://arxiv.org/abs/2212.02500)
- **Project:** [GitHub](https://nvlabs.github.io/PhysDiff/)
- **Published:** 2022-12
- **Tags:**
  - Diffusion
  - Human Motion Analysis and Synthesis

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 ASE: Large-Scale Reusable Adversarial Skill Embeddings for Physically Simulated Characters,  / [code](https://github.com/nv-tlabs/ASE/?tab=readme-ov-file)

- **Paper:** [arXiv](https://arxiv.org/abs/2205.01906)
- **Project:** [GitHub](https://xbpeng.github.io/projects/ASE/index.html)
- **Published:** 2022-08
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## An Empirical Evaluation of Four Off-the-Shelf Proprietary Visual-Inertial Odometry Systems

- **Paper:** [arXiv](https://arxiv.org/abs/2207.06780)
- **Published:** 2022-07
- **Tags:**
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## iCub3 Avatar System: Enabling Remote Fully-Immersive Embodiment of Humanoid Robots, [Science Robotics](https://www.science.org/doi/10.1126/scirobotics.adh3834) / [github](https://github.com/ami-iit/paper_dafarra_2024_science-robotics_icub3-avatar-system)

- **Paper:** [arXiv](https://arxiv.org/abs/2203.06972)
- **Published:** 2022-03
- **Tags:**
  - Humanoid
  - Teleoperation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control,  / [code](https://github.com/xbpeng/DeepMimic)

- **Paper:** [arXiv](https://arxiv.org/abs/2104.02180)
- **Project:** [GitHub](https://xbpeng.github.io/projects/AMP/index.html)
- **Published:** 2021-08
- **Tags:**
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors

- **Paper:** [arXiv](https://arxiv.org/abs/2104.09025)
- **Published:** 2021-04
- **Tags:**
  - Humanoid
  - Motion Planning
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation

- **Paper:** [arXiv](https://arxiv.org/abs/1904.09251)
- **Published:** 2019-04
- **Tags:**
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 Quasi-Direct Drive for Low-Cost Compliant Robotic Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/1904.03815)
- **Project:** [GitHub](https://berkeleyopenarms.github.io/)
- **Published:** 2019-04
- **Tags:**
  - Manipulation
  - Hardware Design

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Agile and Dynamic Motor Skills for Legged Robots

- **Paper:** [arXiv](https://arxiv.org/abs/1901.08652)
- **Published:** 2019-01
- **Tags:**
  - Sim-to-Real

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Hierarchical visuomotor control of humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/1811.09656)
- **Published:** 2018-11
- **Tags:**
  - Humanoid
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Multi-task Deep Reinforcement Learning with PopArt

- **Paper:** [arXiv](https://arxiv.org/abs/1809.04474)
- **Published:** 2018-09
- **Tags:**
  - Reinforcement Learning
  - Multi-Task
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## 🌟 DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills,  / [code](https://github.com/xbpeng/DeepMimic)

- **Paper:** [arXiv](https://arxiv.org/abs/1804.02717)
- **Project:** [GitHub](https://xbpeng.github.io/projects/DeepMimic/index.html)
- **Published:** 2018-08
- **Tags:**
  - Reinforcement Learning
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Learning Symmetric and Low-energy Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/1801.08093)
- **Published:** 2018-01
- **Tags:**
  - Locomotion
  - Physics-Based Character Animation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## Legged Robot State-Estimation Through Combined Forward Kinematic and Preintegrated Contact Factors

- **Paper:** [arXiv](https://arxiv.org/abs/1712.05873)
- **Published:** 2017-05
- **Tags:**
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

## The invariant extended Kalman filter as a stable observer

- **Paper:** [arXiv](https://arxiv.org/abs/1410.1465)
- **Published:** 2014-10
- **Tags:**
  - State Estimation

### Summary

Summary unavailable. This entry was imported from a curated paper list.

---

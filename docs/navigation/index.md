# Navigation

**22 papers** in this category.

## Months

- [2026-07](/navigation/2026-07) (1 papers)
- [2026-06](/navigation/2026-06) (1 papers)
- [2026-05](/navigation/2026-05) (2 papers)
- [2026-04](/navigation/2026-04) (1 papers)
- [2026-02](/navigation/2026-02) (1 papers)
- [2026-01](/navigation/2026-01) (1 papers)
- [2025-12](/navigation/2025-12) (1 papers)
- [2025-11](/navigation/2025-11) (2 papers)
- [2025-09](/navigation/2025-09) (1 papers)
- [2025-08](/navigation/2025-08) (4 papers)
- [2025-07](/navigation/2025-07) (1 papers)
- [2025-06](/navigation/2025-06) (1 papers)
- [2025-05](/navigation/2025-05) (1 papers)
- [2025-03](/navigation/2025-03) (1 papers)
- [2024-12](/navigation/2024-12) (2 papers)
- [2023-10](/navigation/2023-10) (1 papers)

---

## Recent Papers

## RAVEN: Reinforcement-Adaptive Visibility-Graph Planning for Robust Humanoid Navigation with Collision-Free MPC

- **Paper:** [arXiv](https://arxiv.org/abs/2607.15701)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Authors:** Ruochen Hou, Shiqi Wang, Beom Jun Kim, Hanzhang Fang, Mehak Singal, Dennis W. Hong
- **Published:** 2026-07
- **Tags:**
  - Reinforcement Learning
  - MPC
  - Locomotion
  - Navigation
  - Safety
  - Robustness
  - Real Robot
  - Humanoid

### Summary

Humanoid navigation in dynamic environments requires long-horizon planning while respecting short-horizon dynamic and safety constraints. Classical visibility-graph planners combined with model predictive control (MPC) can efficiently generate collision-free trajectories, but their performance depends on manually tuned parameters and accurate system modeling.

---

## LP-NavOA: Integrated Local Navigation and Obstacle Avoidance for Humanoid Robots under Limited Perception

- **Paper:** [arXiv](https://arxiv.org/abs/2606.23249)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Authors:** Yukun Luo, Jianjun Ma, Yuyao Min, Jinzhe Li, Kaihong Huang, Peng Li
- **Published:** 2026-06
- **Tags:**
  - Locomotion
  - Navigation
  - Safety
  - MuJoCo
  - Humanoid
  - Proprioception
  - PPO

### Summary

Humanoid local navigation in cluttered environments must jointly resolve obstacle avoidance, sparse-goal recovery, and stable whole-body locomotion under short-range and partially observable sensing. Explicit planner-control decompositions introduce latency and can mismatch agile humanoid command-tracking limits, while purely reactive controllers may lose the goal after obstacle occlusion.

---

## Learning to Evolve: Multi-modal Interactive Fields for Robust Humanoid Navigation in Dynamic Environments

- **Paper:** [arXiv](https://arxiv.org/abs/2605.21935)
- **Project:** [Project page](https://ziya-jiang.github.io/MIF-homepage/)
- **Code status:** Coming soon / 代码待发布
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Publication/project page: Code Coming Soon

</details>

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

## Terrain Consistent Reference-Guided RL for Humanoid Navigation Autonomy

- **Paper:** [arXiv](https://arxiv.org/abs/2605.15517)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Authors:** William D. Compton, Zachary Olkin, Aaron D. Ames
- **Published:** 2026-05
- **Tags:**
  - Reinforcement Learning
  - MPC
  - Locomotion
  - Navigation
  - Humanoid

### Summary

We present a method for training reference-guided, perceptive reinforcement learning locomotion policies for humanoid robots in which reference trajectories are modulated in training to be consistent with terrain geometry. Aiming to deploy our method with standard navigation autonomy infrastructure, we synthesize SE(2)-controllable reference trajectories inside the RL training loop, projecting desired footsteps onto valid footholds and adjusting swing-foot and center-of-mass trajectories to match the terrain.

---

## Learning Humanoid Navigation from Human Data

- **Paper:** [arXiv](https://arxiv.org/abs/2604.00416)
- **Project:** [Project page](https://egonav.weizhuowang.com)
- **Code status:** Needs review / 访问失败或证据不足
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Project page inspection failed: SSLError
- Link discovery incomplete; absence of code cannot be confirmed

</details>

- **Authors:** Weizhuo Wang, Yanjie Ze, C. Karen Liu, Monroe Kennedy
- **Published:** 2026-04
- **Tags:**
  - Navigation
  - Zero-Shot
  - Humanoid
  - Walking
  - Diffusion
  - Locomotion

### Summary

We present EgoNav, a system that enables a humanoid robot to traverse diverse, unseen environments by learning entirely from 5 hours of human walking data, with no robot data or finetuning. A diffusion model predicts distributions of plausible future trajectories conditioned on past trajectory, a 360 deg visual memory fusing color, depth, and semantics, and video features from a frozen DINOv3 backbone that capture appearance cues invisible to depth sensors.

---

## EgoActor: Grounding Task Planning into Spatial-aware Egocentric Actions for Humanoid Robots via Visual-Language Models

- **Paper:** [arXiv](https://arxiv.org/abs/2602.04515)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2026-02
- **Tags:**
  - Humanoid
  - Task Planning
  - Navigation

### Summary

Deploying humanoid robots in real-world settings is fundamentally challenging, as it demands tight integration of perception, locomotion, and manipulation under partial-information observations and dynamically changing environments. As well as transitioning robustly between sub-tasks of different types.

---

## FocusNav: Spatial Selective Attention with Waypoint Guidance for Humanoid Local Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2601.12790)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2026-01
- **Tags:**
  - Navigation
  - Humanoid

### Summary

Robust local navigation in unstructured and dynamic environments remains a significant challenge for humanoid robots, requiring a delicate balance between long-range navigation targets and immediate motion stability. In this paper, we propose FocusNav, a spatial selective attention framework that adaptively modulates the robot's perceptual field based on navigational intent and real-time stability.

---

## 🌟 STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01046)
- **Repository:** [Code](https://github.com/yzwfromk/STATE-NAV)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/yzwfromk/STATE-NAV
- Implementation examples: examples/demo_mppi/demo_map_provider.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2025-12
- **Tags:**
  - Navigation
  - Biped

### Summary

Bipedal robots have advantages in maneuvering human-centered environments, but face greater failure risk compared to other stable mobile platforms such as wheeled or quadrupedal robots. While learning-based traversability has been widely studied for these platforms, bipedal traversability has instead relied on manually designed rules with limited consideration of locomotion stability on rough terrain.

---

## 🌟 Thinking in 360: Humanoid Visual Search in the Wild

- **Paper:** [arXiv](https://arxiv.org/abs/2511.20351)
- **Project:** [Project page](https://humanoid-vstar.github.io/)
- **Repository:** [Code](https://github.com/humanoid-vstar/hstar)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/THUSI-Lab/Hstar
- Implementation examples: vagen/env/alfworld/env.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2025-11
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world.

---

## Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D Constrained Terrains

- **Paper:** [arXiv](https://arxiv.org/abs/2511.14625)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-11
- **Tags:**
  - Locomotion
  - Navigation
  - Humanoid

### Summary

Robust humanoid locomotion requires accurate and globally consistent perception of the surrounding 3D environment. However, existing perception modules, mainly based on depth images or elevation maps, offer only partial and locally flattened views of the environment, failing to capture the full 3D structure.

---

## Quantum deep reinforcement learning for humanoid robot navigation task

- **Paper:** [arXiv](https://arxiv.org/abs/2509.11388)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-09
- **Tags:**
  - Reinforcement Learning
  - Navigation
  - Humanoid

### Summary

Classical reinforcement learning (RL) methods often struggle in complex, high-dimensional environments because of their extensive parameter requirements and challenges posed by stochastic, non-deterministic settings. This study introduces quantum deep reinforcement learning (QDRL) to train humanoid agents efficiently.

---

## Learning Social Navigation from Positive and Negative Demonstrations and Rule-Based Specifications

- **Paper:** [arXiv](https://arxiv.org/abs/2508.06779)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-08
- **Tags:**
  - Navigation

### Summary

Bipedal robots demonstrate potential in navigating challenging terrains through dynamic ground contact. However, current frameworks often depend solely on proprioception or use manually designed visual pipelines, which are fragile in real-world settings and complicate real-time footstep planning in unstructured environments.

---

## LookOut: Real-World Humanoid Egocentric Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2508.14466)
- **Project:** [Project page](https://sites.google.com/stanford.edu/lookout)
- **Code status:** Project page only / 项目页未发现仓库
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-08
- **Tags:**
  - Navigation
  - Humanoid

### Summary

The ability to predict collision-free future trajectories from egocentric observations is crucial in applications such as humanoid robotics, VR / AR, and assistive navigation. In this work, we introduce the challenging problem of predicting a sequence of future 6D head poses from an egocentric video.

---

## INTENTION: Inferring Tendencies of Humanoid Robot Motion Through Interactive Intuition and Grounded VLM

- **Paper:** [arXiv](https://arxiv.org/abs/2508.04931)
- **Project:** [Project page](https://robo-intention.github.io)
- **Code status:** Needs review / 访问失败或证据不足
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Project page inspection failed: ProxyError
- Link discovery incomplete; absence of code cannot be confirmed

</details>

- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Traditional control and planning for robotic manipulation heavily rely on precise physical models and predefined action sequences. While effective in structured environments, such approaches often fail in real-world scenarios due to modeling inaccuracies and struggle to generalize to novel tasks.

---

## Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching

- **Paper:** [arXiv](https://arxiv.org/abs/2508.03068)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-08
- **Tags:**
  - Locomotion
  - Navigation
  - Humanoid

### Summary

We propose Hand-Eye Autonomous Delivery (HEAD), a framework that learns navigation, locomotion, and reaching skills for humanoids, directly from human motion and vision perception data. We take a modular approach where the high-level planner commands the target position and orientation of the hands and eyes of the humanoid, delivered by the low-level policy that controls the whole-body movements.

---

## Humanoid Occupancy: Enabling A Generalized Multimodal Occupancy Perception System on Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2507.20217)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-07
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Humanoid robot technology is advancing rapidly, with manufacturers introducing diverse heterogeneous visual perception modules tailored to specific scenarios. Among various perception paradigms, occupancy-based representation has become widely recognized as particularly suitable for humanoid robots, as it provides both rich semantic and 3D geometric information essential for comprehensive environmental understanding.

---

## RL with Data Bootstrapping for Dynamic Subgoal Pursuit in Humanoid Robot Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2506.02206)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-06
- **Tags:**
  - Navigation
  - Humanoid

### Summary

Safe and real-time navigation is fundamental for humanoid robot applications. However, existing bipedal robot navigation frameworks often struggle to balance computational efficiency with the precision required for stable locomotion.

---

## 🌟 NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance

- **Paper:** [arXiv](https://arxiv.org/abs/2505.08712)
- **Project:** [Project page](https://wzcai99.github.io/navigation-diffusion-policy.github.io)
- **Repository:** [Code](https://github.com/wzcai99/NavDP)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/InternRobotics/NavDP
- Implementation examples: eval_imagegoal_wheeled.py, eval_nogoal_wheeled.py, eval_pointgoal_wheeled.py, eval_startgoal_wheeled.py, teleop_imagegoal_wheeled.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2025-05
- **Tags:**
  - Diffusion Policy
  - Sim-to-Real
  - Navigation
  - Diffusion

### Summary

Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data.

---

## HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2503.09010)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-03
- **Tags:**
  - Humanoid
  - Navigation

### Summary

The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations.

---

## NaVILA: Legged Robot Vision-Language-Action Model for Navigation

- **Paper:** [arXiv](https://arxiv.org/abs/2412.04453)
- **Project:** [Project page](https://navila-bot.github.io/)
- **Code status:** Needs review / 访问失败或证据不足
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Multiple repository candidates require review: https://github.com/AnjieCheng/NaVILA, https://github.com/yang-zj1026/legged-loco

</details>

- **Published:** 2024-12
- **Tags:**
  - Navigation
  - Vision-Language

### Summary

This paper proposes to solve the problem of Vision-and-Language Navigation with legged robots, which not only provides a flexible way for humans to command but also allows the robot to navigate through more challenging and cluttered scenes. However, it is non-trivial to translate human language instructions all the way to low-level leg joint actions.

---

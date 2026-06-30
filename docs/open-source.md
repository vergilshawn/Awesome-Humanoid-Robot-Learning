# Open Source Papers

Papers with open-source code repositories.

## 🌟 Training Vision-Language-Action Models with Dense Embodied Chain-of-Thought Supervision

- **Paper:** [arXiv](https://arxiv.org/abs/2606.30552)
- **Project:** [GitHub](https://github.com/ruckbreasoning/zr-0)
- **Authors:** Haoyang Li, Guanlin Li, Youhe Feng, Chen Zhao, Zhuoran Wang, Yang Li et al. (12 authors)
- **Published:** 2026-06
- **Tags:**
  - Manipulation
  - Transformer
  - Humanoid
  - Task Planning
  - Vision-Language
  - Benchmark
  - Dataset
  - Diffusion

### Summary

Cross-embodiment transfer in vision-language-action (VLA) models remains challenging because low-level state and action spaces differ fundamentally across robot platforms. We observe that the high-level cognitive process underlying manipulation, including scene perception, object identification, task planning, and sub-task decomposition, is largely shared across embodiments.

---

## 🌟 Unleashing Infinite Motion: Scaling Expressive Quadrupedal Motion via Generative Video Priors

- **Paper:** [arXiv](https://arxiv.org/abs/2606.28237)
- **Project:** [GitHub](https://github.com/gaolii/quad-imaginarium.git)
- **Authors:** Youzhi Liu, Li Gao, Yifei Qian, Liu Liu, Yang Cai, Ziqiao Li
- **Published:** 2026-06
- **Tags:**
  - Locomotion
  - Humanoid
  - Gait
  - Dataset
  - Diffusion
  - Simulation Benchmark
  - State Estimation

### Summary

Quadruped robots have achieved remarkable locomotion, yet their behavioral repertoire remains confined to a few gaits--far from the expressive, companion-like presence long envisioned for them. Attempts to import the humanoid recipe of large-scale motion data have inherited one tacit assumption: that robot motion must first pass through an animal body, making data collection dependent on cooperative animals, reconstruction fragile across species, and retargeting ill-posed across incompatible morphologies.

---

## 🌟 TurboMPC: Fast, Scalable, and Differentiable Model Predictive Control on the GPU

- **Paper:** [arXiv](https://arxiv.org/abs/2606.24039)
- **Project:** [GitHub](https://github.com/toyotaresearchinstitute/turbompc)
- **Authors:** Gabriel Bravo-Palacios, Jianghan Zhang, Zachary Pestrikov, Brian Plancher, Thomas Lew
- **Published:** 2026-06
- **Tags:**
  - Reinforcement Learning
  - Imitation Learning
  - MPC
  - Humanoid
  - PPO
  - State Estimation
  - Simulation Benchmark

### Summary

Robotics increasingly relies on GPUs for parallel simulation, large-scale learning, and neural-network inference. For model predictive control (MPC) to scale with this paradigm, solvers must run efficiently on this hardware while remaining fast, differentiable, and compatible with expressive MPC formulations used in robotics.

---

## 🌟 Enforcing Human-like Kinematics in Dexterous Piano Playing via Adversarial Posture Regularization

- **Paper:** [arXiv](https://arxiv.org/abs/2606.23848)
- **Project:** [GitHub](https://github.com/aprproject/aprpianist)
- **Authors:** Bin Qiu, Yanming Shao, Guanyu Cai, Yao Mu
- **Published:** 2026-06
- **Tags:**
  - Reinforcement Learning
  - Manipulation
  - Physics-Based Character Animation
  - State Estimation
  - Simulation Benchmark

### Summary

Reinforcement learning can train bimanual dexterous hands to play piano in physics simulation with high note accuracy, but for high-DoF dexterous hands, relying solely on task rewards or IK inversion often leads to unnatural postures and joint overextension. We propose \textit{Adversarial Posture Regularization (APR)}.

---

## 🌟 WaveSync: Constrained Wavefront Optimization for Synchronized Co-Speech Gestures in Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2606.16600)
- **Project:** [GitHub](https://github.com/pairs-lab/WaveSync)
- **Authors:** Thang Tran Viet, Thanh Nguyen Canh, Gia Huy Uong, Phuc Van Dinh, Tan Viet Tuyen Nguyen, Xiem HoangVan et al. (7 authors)
- **Published:** 2026-06
- **Tags:**
  - Humanoid
  - Motion Planning
  - Large Language Model
  - Physics-Based Character Animation
  - Human Motion Analysis and Synthesis

### Summary

Expressive co-speech gestures are crucial for natural human-robot interaction, but generating them on physical humanoid robots is difficult because gesture strokes must align with speech emphasis while satisfying strict kinematic and dynamic constraints. Unlike virtual avatars, humanoid robots cannot freely execute rapid or overlapping motions, making word-level synchronization and hardware-safe motion planning a coupled problem.

---

## 🌟 MotionVLA: Vision-Language-Action Model for Humanoid Motion

- **Paper:** [arXiv](https://arxiv.org/abs/2606.15142)
- **Project:** [GitHub](https://github.com/aigeeksgroup/motionvla)
- **Authors:** Nonghai Zhang, Siyu Zhai, Yanjun Li, Zeyu Zhang, Zhihan Yin, Yandong Guo et al. (8 authors)
- **Published:** 2026-06
- **Tags:**
  - Humanoid
  - Vision-Language
  - PPO
  - Physics-Based Character Animation
  - Human Motion Analysis and Synthesis

### Summary

Generating realistic humanoid motion from scene images and text involves both low-frequency pose semantics and high-frequency physical dynamics. However, many existing methods tokenize motion with a single shared codebook, forcing heterogeneous motion signals into the same quantization space.

---

## 🌟 DragMesh-2: Physically Plausible Dexterous Hand-Object Interaction with Articulated Objects

- **Paper:** [arXiv](https://arxiv.org/abs/2606.15133)
- **Project:** [GitHub](https://github.com/AIGeeksGroup/DragMesh-2)
- **Authors:** Tianshan Zhang, Yijia Duan, Yanjun Li, Zeyu Zhang, Hao Tang
- **Published:** 2026-06
- **Tags:**
  - Manipulation
  - Robustness
  - Humanoid
  - Contact Dynamics
  - Policy Learning
  - PPO
  - Loco-Manipulation and Whole-Body Control

### Summary

Dexterous interaction with articulated objects is important for household, assistive, and humanoid manipulation, where multi-finger hands can provide compliant contact patterns beyond parallel-jaw grasping. However, articulated-object manipulation differs from static-object manipulation: the target part cannot be directly actuated, and its motion must emerge through sustained physical hand--handle contact.

---

## 🌟 bbsolver: A Unified Error-Bounded Spatiotemporal Optimization Solver for Key Timing and Topology-Consistent Vector Paths

- **Paper:** [arXiv](https://arxiv.org/abs/2606.09741)
- **Project:** [GitHub](https://github.com/ivg-design/bbsolver)
- **Authors:** Ilya Gusinski
- **Published:** 2026-06
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Humanoid
  - PPO
  - Locomotion
  - State Estimation
  - Human Motion Analysis and Synthesis

### Summary

Dense sampling records what an animation system actually evaluated, but it produces a poor final representation: every sampled frame can become a key, edit handles become noisy, and animated vector paths remain hard to adjust. Existing reducers usually treat the two axes separately: animation-curve reducers reduce key timing, while curve and path simplifiers reduce geometry.

---

## 🌟 Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2606.05687)
- **Project:** [GitHub](https://github.com/junhengl/mpc-rl)
- **Authors:** Junheng Li, Liang Wu, Sergio A. Esteban, Lizhi Yang, Ján Drgoňa, Aaron D. Ames
- **Published:** 2026-06
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Reinforcement Learning
  - MPC
  - Locomotion
  - Manipulation
  - Humanoid
  - Loco-Manipulation and Whole-Body Control
  - State Estimation
  - Simulation Benchmark

### Summary

In humanoid motion control, model predictive control (MPC) offers physically grounded prediction and constraint handling, while reinforcement learning (RL) enables robust whole-body skills through large-scale simulation. However, using MPC inside RL often requires time-consuming problem construction or excessive training overhead, making such frameworks difficult to justify in practice.

---

## 🌟 M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking

- **Paper:** [arXiv](https://arxiv.org/abs/2606.04829)
- **Project:** [GitHub](https://github.com/renforce-dynamics/multimodalwbc)
- **Authors:** Zuxing Lu, Ziang Zheng, Yao Lyu, Jingyu Liu, Feihong Zhang, Song Lu et al. (10 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Whole-Body Control
  - Sim-to-Real
  - Locomotion
  - Manipulation
  - Simulator
  - Humanoid
  - Dataset

### Summary

Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation requires precise end-effector trajectory tracking.

---

## 🌟 HLL: Can Agents Cross Humanity's Last Line of Verification?

- **Paper:** [arXiv](https://arxiv.org/abs/2606.02449)
- **Project:** [GitHub](https://github.com/xinhaos0101/hll)
- **Authors:** Xinhao Song, Su Su, Sirui Song, Hongliang Wu, Wen Shen, Zhihua Wei et al. (9 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Benchmark
  - PPO
  - Navigation
  - Simulation Benchmark

### Summary

Multimodal agents are increasingly expected to operate interfaces on behalf of users, raising a central deployment question: can they truly substitute for humans in workflows that services deliberately protect against automation? CAPTCHA verification makes this question concrete. It is not merely a visual puzzle, but a human-verification boundary placed before account creation, content access, form submission, and other protected actions.

---

## 🌟 Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language

- **Paper:** [arXiv](https://arxiv.org/abs/2605.27886)
- **Project:** [GitHub](https://github.com/nathanwu7/tabero)
- **Authors:** Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang, Junjie Lai et al. (7 authors)
- **Published:** 2026-05
- **Tags:**
  - Manipulation
  - Tactile Sensing
  - Language-Conditioned
  - Vision-Language
  - Benchmark
  - Simulation Benchmark

### Summary

Tactile sensing is essential for robots to achieve human-like gentle manipulation. However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop force feedback mechanisms.

---

## 🌟 EgoTraj: Real-World Egocentric Human Trajectory Dataset for Multimodal Prediction

- **Paper:** [arXiv](https://arxiv.org/abs/2605.19004)
- **Project:** [GitHub](https://github.com/yehiahmad/egotraj)
- **Authors:** Ahmad Yehia, Abduallah Mohamed, Tianyi Wang, Jiseop Byeon, Kun Qian, Junfeng Jiao et al. (7 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Navigation
  - Humanoid
  - Trajectory Prediction
  - Benchmark
  - Dataset
  - Simulation Benchmark

### Summary

Accurately forecasting human trajectories from an egocentric perspective plays a central role in applications such as humanoid robotics, wearable sensing systems, and assistive navigation. However, progress in this direction remains limited due to the scarcity of egocentric trajectory datasets collected in real-world environments.

---

## 🌟 Adversarial Stress Testing of SPARK Humanoid Safety Filters

- **Paper:** [arXiv](https://arxiv.org/abs/2605.19009)
- **Project:** [GitHub](https://github.com/ghoshsaurav/spark-adversarial-safety)
- **Authors:** Saurav Ghosh, Abdou Sow, Luke Zhang
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Safety
  - Robustness
  - MuJoCo
  - Humanoid
  - Collision
  - Benchmark
  - Simulation Benchmark
  - State Estimation

### Summary

Humanoid robots are difficult to deploy safely because they have high-dimensional bodies, many collision constraints, and must operate near people and obstacles. Safety filters help by modifying a nominal control action when it may violate collision-avoidance constraints.

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

## 🌟 ComFree-Sim: A GPU-Parallelized Analytical Contact Physics Engine for Scalable Contact-Rich Robotics Simulation and Control

- **Paper:** [arXiv](https://arxiv.org/abs/2603.12185)
- **Project:** [GitHub](https://irislab.tech/comfree-sim/)
- **Published:** 2026-03
- **Tags:**
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

## 🌟 WHOLE: World-Grounded Hand-Object Lifted from Egocentric Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2602.22209)
- **Project:** [GitHub](https://judyye.github.io/whole-www/)
- **Published:** 2026-02
- **Tags:**
  - Human Motion Analysis and Synthesis

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

## 🌟 STATE-NAV: Stability-Aware Traversability Estimation for Bipedal Navigation on Rough Terrain / [code](https://github.com/yzwfromk/STATE-NAV)

- **Paper:** [arXiv](https://arxiv.org/abs/2506.01046)
- **Published:** 2025-12
- **Tags:**
  - Navigation
  - Biped

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

## 🌟 SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World Reinforcement Learning, [websie](https://robo-rl.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2506.04147)
- **Published:** 2025-06
- **Tags:**
  - Reinforcement Learning
  - Loco-Manipulation and Whole-Body Control

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

## 🌟 Mobi-π: Mobilizing Your Robot Learning Policy

- **Paper:** [arXiv](https://arxiv.org/abs/2505.23692)
- **Project:** [GitHub](https://mobipi.github.io/)
- **Published:** 2025-05
- **Tags:**
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

## 🌟 BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities, [websie](https://behavior-robot-suite.github.io/)

- **Paper:** [arXiv](https://arxiv.org/abs/2503.05652)
- **Published:** 2025-03
- **Tags:**
  - Manipulation
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

## 🌟 Unified Video Action Model

- **Paper:** [arXiv](https://arxiv.org/abs/2503.00200)
- **Project:** [GitHub](https://unified-video-action-model.github.io/)
- **Published:** 2025-03
- **Tags:**
  - Manipulation

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

## 🌟 FRAME: Floor-aligned Representation for Avatar Motion from Egocentric Video

- **Paper:** [arXiv](https://arxiv.org/abs/2503.23094)
- **Project:** [GitHub](https://vcai.mpi-inf.mpg.de/projects/FRAME/)
- **Published:** 2025-03
- **Tags:**
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

## 🌟 Real-Time Polygonal Semantic Mapping for Humanoid Robot Stair Climbing, [code](https://github.com/BTFrontier/polygon_mapping)

- **Paper:** [arXiv](https://arxiv.org/abs/2411.01919)
- **Published:** 2024-11
- **Tags:**
  - Humanoid
  - Locomotion

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

## 🌟 Learning Visuotactile Skills with Two Multifingered Hands,  / [code](https://github.com/toruowo/hato)

- **Paper:** [arXiv](https://arxiv.org/abs/2404.16823)
- **Project:** [GitHub](https://toruowo.github.io/hato/)
- **Published:** 2024-04
- **Tags:**
  - Manipulation

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

## 🌟 Unified Human-Scene Interaction via Prompted Chain-of-Contacts

- **Paper:** [arXiv](https://arxiv.org/abs/2309.07918)
- **Project:** [GitHub](https://xizaoqu.github.io/unihsi/)
- **Published:** 2023-09
- **Tags:**
  - Physics-Based Character Animation

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

## 🌟 AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control,  / [code](https://github.com/xbpeng/DeepMimic)

- **Paper:** [arXiv](https://arxiv.org/abs/2104.02180)
- **Project:** [GitHub](https://xbpeng.github.io/projects/AMP/index.html)
- **Published:** 2021-08
- **Tags:**
  - Physics-Based Character Animation

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

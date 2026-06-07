# Real Robot Papers

Papers with real humanoid robot deployment and experiments.

## Platforms

- **Figure:** 8 papers
- **NAO:** 1 papers
- **Unitree G1:** 25 papers
- **Unknown Platform:** 2 papers
- **iCub:** 1 papers

---

## All Real Robot Papers

## HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

- **Paper:** [arXiv](https://arxiv.org/abs/2606.06493)
- **Authors:** Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin et al. (8 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Whole-Body Control
  - Locomotion
  - Manipulation
  - Safety
  - Humanoid
  - Task Planning
  - Fine-tuning
  - Distillation

### Summary

For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics.

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

## GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors

- **Paper:** [arXiv](https://arxiv.org/abs/2606.05160)
- **Authors:** Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li et al. (20 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Sim-to-Real
  - Teleoperation
  - Manipulation
  - Simulator
  - Humanoid
  - Foundation Model
  - Loco-Manipulation and Whole-Body Control
  - State Estimation

### Summary

Scaling humanoid loco-manipulation requires robot-compatible demonstrations across diverse objects, whole-body motions, and scene geometries, but teleoperation and motion capture are difficult to scale because each collection depends on physical setups, instrumented actors, and robot operation. We present GRAIL, a digital generation pipeline that remains fully virtual until deployment: it composes 3D assets, simulator-ready scenes, and priors from video foundation models (VFMs) to synthesize interactions without rebuilding physical environments or teleoperating the robot.

---

## Flash-WAM: Modality-Aware Distillation for World Action Models

- **Paper:** [arXiv](https://arxiv.org/abs/2606.05254)
- **Authors:** Arman Akbari, Ci Zhang, Arash Akbari, Lin Zhao, Yixiao Chen, Weiwei Chen et al. (9 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Manipulation
  - Humanoid
  - Distillation
  - Benchmark
  - Diffusion
  - Simulation Benchmark
  - State Estimation

### Summary

World-action models (WAMs) jointly generate future video and robot actions through iterative diffusion, achieving strong performance on manipulation benchmarks but requiring tens of denoising steps, a cost that precludes real-time control. Step distillation has emerged as the natural remedy, but off-the-shelf methods break down in the joint video-action setting because video and action streams use different SNR-shifted noise schedules and reach training with substantially different marginal noise distributions, an asymmetry that single-modality distillation methods cannot accommodate.

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

## CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation

- **Paper:** [arXiv](https://arxiv.org/abs/2606.04718)
- **Authors:** Kailun Huang, Zikang Xie, Yanzhe Xie, Panpan Liao, Fanghai Zhang, Yanheng Mai et al. (10 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Locomotion
  - Zero-Shot
  - Humanoid
  - Gait
  - Walking
  - State Estimation
  - Simulation Benchmark

### Summary

Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns. Similarly, humanoid robots should achieve smooth transitions between walking and running while maintaining natural and stable locomotion.

---

## Bionic Human-Motion Style Transfer for Physically Executable Whole-Body Control of Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2606.03536)
- **Authors:** Tianchen Huang, Mingkuan Zhao, Yang Gao, Feiyang Yuan, Junchi Gu, Xiaohu Zhang et al. (11 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Gait
  - Diffusion
  - Loco-Manipulation and Whole-Body Control
  - Locomotion
  - State Estimation
  - Simulation Benchmark

### Summary

Expressive whole-body motion is important for humanoid robots operating in human environments, where robots are expected to move stably while presenting readable and adjustable body behaviors. However, most expressive motions are still obtained from fixed demonstrations or manually designed scripts, making it difficult to reuse a demonstrated style across different motion contents.

---

## Human2Humanoid: Physics-Aware Cross-Morphology Motion Retargeting for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2606.03476)
- **Authors:** Tianchen Huang, Feiyang Yuan, Junchi Gu, Shurui Fang, Xiaohu Zhang, Yu Wang et al. (8 authors)
- **Published:** 2026-06
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Imitation Learning
  - Teleoperation
  - Motion Retargeting
  - Humanoid
  - GAN
  - Human Motion Analysis and Synthesis

### Summary

Retargeting human motion to humanoid robots is critical for teleoperation, imitation learning and human-robot interaction. However, it remains challenging because of substantial morphological discrepancies between humans and robots, including differences in skeletal topology, limb proportions and degrees of freedom, as well as the scarcity of paired motion data.

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

## LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World

- **Paper:** [arXiv](https://arxiv.org/abs/2606.01458)
- **Authors:** Hojune Kim, Timothy Chen, Jiankai Sun, Lars W. Osterberg, Qianzhong Chen, Ke Wang et al. (7 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Teleoperation
  - Manipulation
  - Robustness
  - Simulator
  - Humanoid
  - Gaussian Splatting
  - Vision-Language
  - Fine-tuning

### Summary

Training vision-language-action (VLA) policies for humanoid loco-manipulation is constrained by the high cost and complexity of collecting human teleoperation demonstrations. VLA policies fine-tuned in simulators have, until now, failed to transfer effectively in humanoid loco-manipulation tasks.

---

## Global-Local Attention Decomposition for Terrain Encoding in Humanoid Perceptive Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2606.00637)
- **Authors:** Shengcheng Fu, Yang Zhang, Zhanxiang Cao, Liyun Yan, Yizhi Chen, Yunpeng Yin et al. (7 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Sim-to-Real
  - Locomotion
  - Navigation
  - Zero-Shot
  - Humanoid

### Summary

Although reinforcement learning has significantly advanced humanoid locomotion, perceptive policies still struggle on sparse-foothold terrain and constrained environments. Success in these scenarios requires both broad terrain awareness and precise foothold selection, two perceptual roles that conventional encoders often entangle.

---

## Constrained Whole-Body Tracking for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2606.00374)
- **Authors:** Daniel Morton, Pranit Mohnot, Marco Pavone
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Reinforcement Learning
  - Teleoperation
  - Safety
  - Humanoid
  - Collision
  - Loco-Manipulation and Whole-Body Control
  - State Estimation
  - Physics-Based Character Animation

### Summary

Recent advances in reinforcement learning (RL) have demonstrated impressive whole-body agility for humanoid robots, yet ensuring safety and satisfying constraints -- particularly those specified after training -- remains a challenge. Towards this goal, we present ConstrainedMimic, a control framework that leverages whole-body kinematics and dynamics for real-time constraint enforcement within RL tracking policies.

---

## Gaze2Act: Gaze-Conditioned Vision-Language-Action Policies for Interactive Robot Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2605.30282)
- **Authors:** Kuangji Zuo, Gen Li, Bofan Lyu, Yanshuo Lu, Boyu Ma, Shijia Han et al. (12 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Manipulation
  - Humanoid
  - Vision-Language
  - Navigation

### Summary

Vision-Language-Action (VLA) models have recently shown strong potential for robot learning by following language instructions. However, in practice, language alone is often insufficient to precisely convey human intent.

---

## SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints

- **Paper:** [arXiv](https://arxiv.org/abs/2605.28549)
- **Authors:** Yantong Wei, Kaihong Huang, Hainan Pan, Jiawei Luo, Jiawei Zhou, Ziyan Mai et al. (9 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Zero-Shot
  - Humanoid
  - Gait
  - Physics-Based Character Animation

### Summary

The pursuit of humanoid athletic sprints is hindered by a scarcity of humanoid-viable kinematic reference data and the inability of existing frameworks to maintain stability during sprints. To overcome these limitations, we introduce SPRINT, a novel framework driven by efficient, frequency-adaptive spectral priors.

---

## EIT-Pneumatic Hybrid Robotic Skin for Practical and Accurate Force Map Reconstruction

- **Paper:** [arXiv](https://arxiv.org/abs/2605.28468)
- **Authors:** Junhwi Cho, Sunggyu Bae, Junghyeon Ma, Hyosang Lee, Jung Kim, Kyungseo Park
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Real Robot
  - Humanoid
  - Tactile Sensing
  - Loco-Manipulation and Whole-Body Control
  - State Estimation

### Summary

We present a hybrid robotic skin that combines electrical impedance tomography (EIT) with pneumatic tactile sensing to improve force reconstruction capability. The developed robotic skin is fabricated entirely by 3D printing and spray coating, making it affordable and easy to build.

---

## Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking

- **Paper:** [arXiv](https://arxiv.org/abs/2605.23733)
- **Authors:** Ming Yang, Tao Yu, Feng Li, Hua Chen
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Whole-Body Control
  - Humanoid
  - Fine-tuning
  - Loco-Manipulation and Whole-Body Control
  - Physics-Based Character Animation

### Summary

Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly.

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

## Why Modeling Human Haptic Material Perception with AI Is Difficult

- **Paper:** [arXiv](https://arxiv.org/abs/2605.16602)
- **Authors:** Yasemin Vardar
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Benchmark
  - Dataset
  - PPO
  - Simulation Benchmark
  - Teleoperation

### Summary

Touch plays a central role in how humans perceive and recognize materials through physical contact. Despite decades of research, the mechanisms by which tactile signals are transformed into meaningful perceptual representations remain poorly understood, limiting the design of interactive systems and intelligent agents with human-like haptic perception.

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

## Real2Sim in HOI: Toward Physically Plausible HOI Reconstruction from Monocular Videos

- **Paper:** [arXiv](https://arxiv.org/abs/2605.14462)
- **Authors:** Yubo Zhao, Yujin Chai, Yunao Dong, Chengfeng Zhao, Zijiao Zeng, Yuan Liu et al. (7 authors)
- **Published:** 2026-05
- **Real Robot:** ✅ — NAO
- **Tags:**
  - Manipulation
  - Embodied AI
  - Humanoid
  - Benchmark
  - Simulation Benchmark
  - Physics-Based Character Animation
  - State Estimation
  - Human Motion Analysis and Synthesis

### Summary

Recovering 4D human-object interaction (HOI) from monocular video is a key step toward scalable 3D content creation, embodied AI, and simulation-based learning. Recent methods can reconstruct temporally coherent human and object trajectories, but these trajectories often remain visual artifacts while failing to preserve stable contact, functional manipulation, or physical plausibility when used as reference motions for humanoid-object simulation.

---

## Emotional Expression in Low-Degrees-of-Freedom Robots: Assessing Perception with Reachy Mini

- **Paper:** [arXiv](https://arxiv.org/abs/2605.12786)
- **Authors:** Amit Rogel, Elmira Yadollahi, Guy Laban
- **Published:** 2026-05
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Benchmark
  - Simulation Benchmark

### Summary

Emotion expression is central to human--robot interaction, yet little is known about how people interpret affect on robots with sparse, non-anthropomorphic expressive capabilities. This study examined how people perceive emotional expressions displayed by Reachy Mini (Pollen Robotics and Hugging Face), a low-degree-of-freedom (low-DoF) robot with a constrained and distinctly non-human expressive repertoire.

---

## Real-Time Whole-Body Teleoperation of a Humanoid Robot Using IMU-Based Motion Capture with Sim2Sim and Sim2Real Validation

- **Paper:** [arXiv](https://arxiv.org/abs/2605.12347)
- **Authors:** Hamza Ahmed Durrani, Suleman Khan
- **Published:** 2026-05
- **Real Robot:** ✅ — Unitree G1
- **Tags:**
  - Sim-to-Real
  - Teleoperation
  - MuJoCo
  - Humanoid
  - Walking
  - Human Motion Analysis and Synthesis
  - Locomotion
  - Simulation Benchmark

### Summary

Stable, low-latency whole-body teleoperation of humanoid robots is an open research challenge, complicated by kinematic mismatches between human and robot morphologies, accumulated inertial sensor noise, non-trivial control latency, and persistent sim-to-real transfer gaps. This paper presents a complete real-time whole-body teleoperation system that maps human motion, recorded with a Virdyn IMU-based full-body motion capture suit, directly onto a Unitree G1 humanoid robot.

---

## Mapping Embodied Affective Touch Strategies on a Humanoid Robot

- **Paper:** [arXiv](https://arxiv.org/abs/2605.11825)
- **Authors:** Qiaoqiao Ren, Omar Eldardeer, Francesca Cocchella, Rea Francesco, Alessandra Sciutti, Tony Belpaeme
- **Published:** 2026-05
- **Real Robot:** ✅ — iCub
- **Tags:**
  - Humanoid
  - Navigation

### Summary

Affective touch in human-robot interaction is shaped not only by emotional intent, but also by robot embodiment, including touch location, physical constraints, and perceived agency or social role. Existing HRI studies typically focus on one or two isolated body parts, limiting understanding of how affective touch generalises across the full humanoid body.

---

## RIO: Flexible Real-Time Robot I/O for Cross-Embodiment Robot Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2605.11564)
- **Authors:** Pablo Ortega-Kral, Eliot Xing, Arthur Bucker, Vernon Luk, Junseo Kim, Owen Kwon et al. (16 authors)
- **Published:** 2026-05
- **Real Robot:** ✅
- **Tags:**
  - Teleoperation
  - Multi-Task
  - Open Source
  - Humanoid
  - Vision-Language
  - Dataset
  - Manipulation
  - Simulation Benchmark

### Summary

Despite recent efforts to collect multi-task, multi-embodiment datasets, to design recipes for training Vision-Language-Action models (VLAs), and to showcase these models on different robot platforms, generalist cross-embodiment robot capabilities remains a largely elusive ideal. Progress is limited by fragmented infrastructure: most robot code is highly specific to the exact setup the user decided on, which adds major overhead when attempting to reuse, recycle, or share artifacts between users.

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

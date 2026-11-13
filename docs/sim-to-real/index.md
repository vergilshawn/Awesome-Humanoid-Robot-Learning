# Sim-to-Real

**13 papers** in this category.

## Months

- [2026-07](/sim-to-real/2026-07) (1 papers)
- [2026-06](/sim-to-real/2026-06) (1 papers)
- [2026-02](/sim-to-real/2026-02) (1 papers)
- [2026-01](/sim-to-real/2026-01) (1 papers)
- [2025-10](/sim-to-real/2025-10) (1 papers)
- [2025-09](/sim-to-real/2025-09) (2 papers)
- [2025-08](/sim-to-real/2025-08) (1 papers)
- [2025-05](/sim-to-real/2025-05) (2 papers)
- [2025-04](/sim-to-real/2025-04) (1 papers)
- [2025-02](/sim-to-real/2025-02) (1 papers)
- [2019-01](/sim-to-real/2019-01) (1 papers)

---

## Recent Papers

## Optimization of sim-to-real transfer in the humanoid robot NICO

- **Paper:** [arXiv](https://arxiv.org/abs/2607.18210)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Authors:** Juraj Gavura, Igor Farkaš
- **Published:** 2026-07
- **Tags:**
  - Sim-to-Real
  - Humanoid
  - Inverse Kinematics
  - Physics-Based Character Animation

### Summary

Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics, and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap can cause small positioning errors that prevent successful grasping.

---

## FADA: Few-Shot Domain Adaptation via Dynamics Alignment for Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2606.28476)
- **Project:** [Project page](https://lecar-lab.github.io/FADA-humanoid/)
- **Code status:** Project page only / 项目页未发现仓库
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Authors:** Angchen Xie, Nikhil Sobanbabu, Ishayu Shikhare, Alan Wang, Max Simchowitz, Guanya Shi
- **Published:** 2026-06
- **Tags:**
  - Few-Shot
  - Zero-Shot
  - Domain Randomization
  - Humanoid
  - Domain Adaptation
  - Residual Learning
  - DAgger
  - Sim-to-Real

### Summary

High-precision humanoid control is limited by target-domain dynamics mismatch, where the same control objective can induce different realized motions under changes in terrain, payload, or actuator response. Existing methods either pursue zero-shot transfer through domain randomization or in-context adaptation without target-domain specialization, or require heavy adaptation pipelines that leverage target-domain data, such as model calibration, residual learning, or policy retraining.

---

## 🌟 RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2602.01515)
- **Project:** [Project page](https://humphreymunn.github.io/RAPT/)
- **Repository:** [Code](https://github.com/humphreymunn/RAPT)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/humphreymunn/RAPT
- Implementation examples: deploy/cpp/main.cpp
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2026-02
- **Tags:**
  - Sim-to-Real
  - Humanoid

### Summary

Deploying learned control policies is risky because policies that appear robust in simulation can confidently enter out-of-distribution (OOD) states after Sim-to-Real transfer, causing silent failures and potential hardware damage. Existing anomaly detectors often fail to meet the requirements of high-rate control, extremely low false-positive rates, and interpretable failure feedback.

---

## 🌟 Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control

- **Paper:** [arXiv](https://arxiv.org/abs/2601.21363)
- **Project:** [Project page](https://lift-humanoid.github.io/)
- **Repository:** [Code](https://github.com/bigai-ai/LIFT-humanoid)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/bigai-ai/LIFT-humanoid
- Implementation examples: convert_jax_to_torch_nn.py, eval_in_brax.py, finetune.py, lift_configs.py, train_in_mujoco_playground.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2026-01
- **Tags:**
  - Humanoid
  - Sim-to-Real

### Summary

Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots. However, the low sample efficiency of on-policy algorithms limits safe adaptation to new environments.

---

## PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization

- **Paper:** [arXiv](https://arxiv.org/abs/2510.01708)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-10
- **Tags:**
  - Sim-to-Real
  - Simulator
  - Humanoid

### Summary

Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world.

---

## Contrastive Representation Learning for Robust Sim-to-Real Transfer of Adaptive Humanoid Locomotion

- **Paper:** [arXiv](https://arxiv.org/abs/2509.12858)
- **Project:** [Project page](https://lu-yidan.github.io/cra-loco/)
- **Code status:** Project page only / 项目页未发现仓库
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-09
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid
  - Representation Learning

### Summary

Reinforcement learning has produced remarkable advances in humanoid locomotion, yet a fundamental dilemma persists for real-world deployment: policies must choose between the robustness of reactive proprioceptive control or the proactivity of complex, fragile perception-driven systems. This paper resolves this dilemma by introducing a paradigm that imbues a purely proprioceptive policy with proactive capabilities, achieving the foresight of perception without its deployment-time costs.

---

## Towards bridging the gap: Systematic sim-to-real transfer for diverse legged robots

- **Paper:** [arXiv](https://arxiv.org/abs/2509.06342)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-09
- **Tags:**
  - Sim-to-Real

### Summary

Legged robots must achieve both robust locomotion and energy efficiency to be practical in real-world environments. Yet controllers trained in simulation often fail to transfer reliably, and most existing approaches neglect actuator-specific energy losses or depend on complex, hand-tuned reward formulations.

---

## 🌟 Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids

- **Paper:** [arXiv](https://arxiv.org/abs/2508.12252)
- **Project:** [Project page](https://robot-trains-robot.github.io/)
- **Repository:** [Code](https://github.com/hukz18/Robot-Trains-Robot)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/hukz18/Robot-Trains-Robot
- Implementation examples: examples/test_apriltag.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2025-08
- **Tags:**
  - Humanoid
  - Sim-to-Real

### Summary

Simulation-based reinforcement learning (RL) has significantly advanced humanoid locomotion tasks, yet direct real-world RL from scratch or adapting from pretrained policies remains rare, limiting the full potential of humanoid robots. Real-world learning, despite being crucial for overcoming the sim-to-real gap, faces substantial challenges related to safety, reward design, and learning efficiency.

---

## DiffCoTune: Differentiable Co-Tuning for Cross-domain Robot Control

- **Paper:** [arXiv](https://arxiv.org/abs/2505.24068)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-05
- **Tags:**
  - Sim-to-Real

### Summary

The deployment of robot controllers is hindered by modeling discrepancies due to necessary simplifications for computational tractability or inaccuracies in data-generating simulators. Such discrepancies typically require ad-hoc tuning to meet the desired performance, thereby ensuring successful transfer to a target domain.

---

## Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2505.14266)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-05
- **Tags:**
  - System Identification
  - Sampling-Based
  - Sim-to-Real

### Summary

Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned.

---

## Sim-to-Real of Humanoid Locomotion Policies via Joint Torque Space Perturbation Injection

- **Paper:** [arXiv](https://arxiv.org/abs/2504.06585)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2025-04
- **Tags:**
  - Sim-to-Real
  - Locomotion
  - Humanoid

### Summary

This paper proposes a novel alternative to existing sim-to-real methods for training control policies with simulated experiences. Prior sim-to-real methods for legged robots mostly rely on the domain randomization approach, where a fixed finite set of simulation parameters is randomized during training.

---

## 🌟 Bridging the Sim-to-Real Gap for Athletic Loco-Manipulation

- **Paper:** [arXiv](https://arxiv.org/abs/2502.10894)
- **Project:** [Project page](http://uan.csail.mit.edu)
- **Repository:** [Code](https://github.com/nolie-rolie/athletic-loco-manipulation)
- **Code status:** Implementation detected (completeness unverified) / 已检测到实现，完整性未核验
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- Inspected public GitHub page: https://github.com/nolie-rolie/athletic-loco-manipulation
- Implementation examples: cem/cem.py
- Completeness and reproducibility have not been verified

</details>

- **Published:** 2025-02
- **Tags:**
  - Sim-to-Real
  - Manipulation

### Summary

Achieving athletic loco-manipulation on robots requires moving beyond traditional tracking rewards - which simply guide the robot along a reference trajectory - to task rewards that drive truly dynamic, goal-oriented behaviors. Commands such as "throw the ball as far as you can" or "lift the weight as quickly as possible" compel the robot to exhibit the agility and power inherent in athletic performance.

---

## Learning Agile and Dynamic Motor Skills for Legged Robots

- **Paper:** [arXiv](https://arxiv.org/abs/1901.08652)
- **Code status:** No project/code link found / 未发现项目或代码链接
- **Code checked:** 2026-11-13

<details><summary>Code verification details / 核验依据</summary>

- No repository link found in inspected publication/project content

</details>

- **Published:** 2019-01
- **Tags:**
  - Sim-to-Real

### Summary

Legged robots pose one of the greatest challenges in robotics. Dynamic and agile maneuvers of animals cannot be imitated by existing methods that are crafted by humans.

---

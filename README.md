# Awesome-Humanoid-Robot-Learning

A curated and automatically updated collection of humanoid robot learning research papers.

- **Total Papers:** 17
- **Real Robot Papers:** 11
- **Open Source Papers:** 1

🌟 indicates papers with detected project/code links.

## Contents

- [Loco-Manipulation and Whole-Body Control](#loco-manipulation-and-whole-body-control) (6)
- [Manipulation](#manipulation) (0)
- [Teleoperation](#teleoperation) (1)
- [Locomotion](#locomotion) (4)
- [Navigation](#navigation) (0)
- [State Estimation](#state-estimation) (2)
- [Sim-to-Real](#sim-to-real) (0)
- [Hardware Design](#hardware-design) (0)
- [Simulation Benchmark](#simulation-benchmark) (3)
- [Physics-Based Character Animation](#physics-based-character-animation) (1)
- [Human Motion Analysis and Synthesis](#human-motion-analysis-and-synthesis) (0)
- [Usage](#usage)

---

## Loco-Manipulation and Whole-Body Control

### 2026-05

- [HCLM: A Hierarchical Framework for Cooperative Loco-Manipulation with Dual Quadrupeds](https://arxiv.org/abs/2605.17300) — `Diffusion Policy`, `Whole-Body Control`, `Locomotion`, `Manipulation`, `Collision`, `Diffusion`
- [HoloMotion-1 Technical Report](https://arxiv.org/abs/2605.15336) — `Transformer`, `Zero-Shot`, `Humanoid`, `Foundation Model`, `Fine-tuning`, `Benchmark`

### 2026-04

- [Learning Whole-Body Humanoid Locomotion via Motion Generation and Motion Tracking](https://arxiv.org/abs/2604.17335) — `Reinforcement Learning`, `Locomotion`, `Humanoid`, `PPO`, `Diffusion`, `Loco-Manipulation and Whole-Body Control`
- [HEX: Humanoid-Aligned Experts for Cross-Embodiment Whole-Body Manipulation](https://arxiv.org/abs/2604.07993) — `Manipulation`, `Biped`, `Humanoid`, `Loco-Manipulation and Whole-Body Control`, `Locomotion`

### 2026-03

- [ZeroWBC: Learning Natural Visuomotor Humanoid Control Directly from Human Egocentric Video](https://arxiv.org/abs/2603.09170) — `Whole-Body Control`, `Teleoperation`, `Humanoid`, `Vision-Language`, `Loco-Manipulation and Whole-Body Control`, `Human Motion Analysis and Synthesis`
- [X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation](https://arxiv.org/abs/2603.03733) — `Locomotion`, `Humanoid`, `Distillation`, `Loco-Manipulation and Whole-Body Control`

## Manipulation

- No papers yet.

## Teleoperation

### 2026-04

- [Safe Human-to-Humanoid Motion Imitation Using Control Barrier Functions](https://arxiv.org/abs/2604.11447) — `Motion Retargeting`, `Safety`, `Humanoid`, `Collision`, `Teleoperation`, `State Estimation`

## Locomotion

### 2026-05

- [Unified Walking, Running, and Recovery for Humanoids via State-Dependent Adversarial Motion Priors](https://arxiv.org/abs/2605.18611) — `Reinforcement Learning`, `Locomotion`, `Humanoid`, `Walking`, `Real Robot`
- [Terrain Consistent Reference-Guided RL for Humanoid Navigation Autonomy](https://arxiv.org/abs/2605.15517) — `Reinforcement Learning`, `MPC`, `Locomotion`, `Navigation`, `Humanoid`, `State Estimation`

### 2026-04

- [Learning Humanoid Navigation from Human Data](https://arxiv.org/abs/2604.00416), [website](https://egonav.weizhuowang.com) — `Navigation`, `Zero-Shot`, `Humanoid`, `Walking`, `Diffusion`, `Locomotion`

### 2026-03

- [Omnidirectional Humanoid Locomotion on Stairs via Unsafe Stepping Penalty and Sparse LiDAR Elevation Mapping](https://arxiv.org/abs/2603.07928) — `Sim-to-Real`, `Locomotion`, `Humanoid`, `Walking`, `Navigation`, `State Estimation`

## Navigation

- No papers yet.

## State Estimation

### 2026-05

- [PRIME: Physically-consistent Robotic Inertial and Motion Estimation for Legged and Humanoid Robots](https://arxiv.org/abs/2605.17681) — `Locomotion`, `State Estimation`, `Real Robot`, `Humanoid`, `Proprioception`, `Foundation Model`
- [CoCo-InEKF: State Estimation with Learned Contact Covariances in Dynamic, Contact-Rich Scenarios](https://arxiv.org/abs/2605.15122) — `State Estimation`, `Biped`, `Locomotion`, `Simulation Benchmark`

## Sim-to-Real

- No papers yet.

## Hardware Design

- No papers yet.

## Simulation Benchmark

### 2026-04

- 🌟 [CLAW: Composable Language-Annotated Whole-body Motion Generation](https://arxiv.org/abs/2604.11251), [website](https://github.com/JianuoCao/CLAW) — `Whole-Body Control`, `MuJoCo`, `Humanoid`, `Language-Conditioned`, `Dataset`, `Simulation Benchmark`

### 2026-03

- [RoboForge: Physically Optimized Text-guided Whole-Body Locomotion for Humanoids](https://arxiv.org/abs/2603.17927) — `Locomotion`, `MuJoCo`, `Humanoid`, `Fine-tuning`, `Distillation`, `Simulation Benchmark`
- [Moving Through Clutter: Scaling Data Collection and Benchmarking for 3D Scene-Aware Humanoid Locomotion via Virtual Reality](https://arxiv.org/abs/2603.05993) — `Locomotion`, `Navigation`, `Safety`, `Humanoid`, `Collision`, `Benchmark`

## Physics-Based Character Animation

### 2026-04

- [A Rapid Deployment Pipeline for Autonomous Humanoid Grasping Based on Foundation Models](https://arxiv.org/abs/2604.17258) — `Zero-Shot`, `Real Robot`, `Humanoid`, `Inverse Kinematics`, `3D Reconstruction`, `Foundation Model`

## Human Motion Analysis and Synthesis

- No papers yet.

---

## Usage

```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Update recent papers with daily arXiv windows
python scripts/update_daily.py --days 7

# Preview the website
npm run docs:dev
```

## License

MIT

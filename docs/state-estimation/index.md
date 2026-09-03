# State Estimation

**15 papers** in this category.

## Months

- [2026-09](/state-estimation/2026-09) (2 papers)
- [2026-08](/state-estimation/2026-08) (2 papers)
- [2026-07](/state-estimation/2026-07) (1 papers)
- [2026-06](/state-estimation/2026-06) (2 papers)
- [2026-05](/state-estimation/2026-05) (1 papers)
- [2025-11](/state-estimation/2025-11) (2 papers)
- [2025-07](/state-estimation/2025-07) (1 papers)
- [2022-07](/state-estimation/2022-07) (1 papers)
- [2019-04](/state-estimation/2019-04) (1 papers)
- [2017-05](/state-estimation/2017-05) (1 papers)
- [2014-10](/state-estimation/2014-10) (1 papers)

---

## Recent Papers

## Contact-Constrained Lower-Limb Joint-Offset Calibration for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2609.02306)
- **Authors:** Kaixiang Lu, Haiyu Lan, Chunxiao Qiao, You Li, Chengyuan Luo, Enyu Li et al. (8 authors)
- **Published:** 2026-09
- **Tags:**
  - Humanoid
  - PPO
  - State Estimation

### Summary

Accurate joint encoder offsets are essential for kinematic consistency in humanoid lower limbs, yet existing calibration methods typically require external motion-capture systems or fiducial targets. We present a self-contained calibration framework exploiting only onboard joint encoders and a pelvis-mounted IMU during static double-support contact.

---

## FOCUS: Foot Observation Confidence for Robust Humanoid Proprioceptive Odometry

- **Paper:** [arXiv](https://arxiv.org/abs/2609.02222)
- **Authors:** Kaixin Feng, Angsong Li, Shaopeng Zhang, Enyu Li, Peiwen Lin, Chuang Wang et al. (8 authors)
- **Published:** 2026-09
- **Real Robot:** ✅ — Figure
- **Tags:**
  - Locomotion
  - Simulator
  - Humanoid
  - Walking
  - PPO
  - State Estimation

### Summary

Foot forward kinematics (FK) is widely used to improve proprioceptive legged odometry by providing reliable velocity constraints during foot support. Existing contact-aided estimators generally rely on binary contact decisions to determine whether the FK measurements of an entire foot should be trusted.

---

## Design of a Biomimetic Joint-Covering Skin with Tissue-Like Structure to Enhance Proprioception in a Musculoskeletal Humanoid

- **Paper:** [arXiv](https://arxiv.org/abs/2608.23304)
- **Authors:** Akihiro Miki, Shun Hasegawa, Yoshimoto Ribayashi, Kento Kawaharazuka, Kei Okada
- **Published:** 2026-08
- **Real Robot:** ✅
- **Tags:**
  - State Estimation
  - Humanoid
  - Proprioception
  - PPO

### Summary

Proprioception in musculoskeletal humanoids is typically estimated primarily from muscle sensing, while the role of cutaneous deformation around joints remains insufficiently explored. In biological systems, mechanoreceptors distributed within soft tissue complement muscle feedback and support reliable joint state estimation.

---

## KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots

- **Paper:** [arXiv](https://arxiv.org/abs/2608.05647)
- **Authors:** Jixin Gao, Fucheng Liu, Teng Zhang, Fusheng Zha
- **Published:** 2026-08
- **Real Robot:** ✅
- **Tags:**
  - State Estimation
  - Robustness
  - Humanoid
  - Gait
  - Dataset
  - Physics-Based Character Animation

### Summary

This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated Kalman filter (ESIKF).

---

## Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning

- **Paper:** [arXiv](https://arxiv.org/abs/2607.12702)
- **Authors:** Flavio Maiorana, Valerio Spagnoli, Eugenio Bugli, Flavio Volpi, Daniele Affinita, Vincenzo Suriani et al. (8 authors)
- **Published:** 2026-07
- **Tags:**
  - Reinforcement Learning
  - Manipulation
  - State Estimation
  - Humanoid
  - PPO
  - Representation Learning

### Summary

Recent advances in humanoid robotics have highlighted the importance of deployable loco-manipulation skills. Dribbling a soccer ball while evading active opponents requires simultaneous balance, precise ball control, and awareness of a dynamic adversary under onboard sensing and real-time constraints.

---

## Proprioceptive Invariant State Estimation for Humanoid Robots on Non-Inertial Ground

- **Paper:** [arXiv](https://arxiv.org/abs/2606.19512)
- **Authors:** Falak Mandali, Zijian He, Yan Gu
- **Published:** 2026-06
- **Tags:**
  - State Estimation
  - Humanoid
  - Walking
  - Locomotion

### Summary

This paper presents an invariant extended Kalman filtering (InEKF) approach for real-time state estimation of humanoid robots operating on non-inertial ground using only onboard proprioceptive sensing. The proposed approach estimates the robot's base position and velocity relative to the moving ground frame without requiring direct measurements of ground motion or externally mounted sensors.

---

## $λ$-Reachability: Geometric-Horizon Safety Bellman Equations for Humanoid Safety

- **Paper:** [arXiv](https://arxiv.org/abs/2606.16022)
- **Authors:** Rui Chen, Shangtao Li, Yifan Sun, Changliu Liu
- **Published:** 2026-06
- **Tags:**
  - Safety
  - Humanoid
  - Collision
  - State Estimation

### Summary

We introduce $λ$-Reachability, a scalable approach to Hamilton--Jacobi safety analysis for high-dimensional robotic systems. Unlike prior discounted formulations that rely on fixed one-step Bellman updates, $λ$-Reachability employs a stochastic multi-step estimator of the safety value, using a geometrically distributed rollout horizon together with a randomly absorbed terminal.

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

## Physics-Informed Neural Networks with Unscented Kalman Filter for Sensorless Joint Torque Estimation

- **Paper:** [arXiv](https://arxiv.org/abs/2507.10105)
- **Published:** 2025-07
- **Tags:**
  - State Estimation

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

## Contact-Aided Invariant Extended Kalman Filtering for Robot State Estimation

- **Paper:** [arXiv](https://arxiv.org/abs/1904.09251)
- **Published:** 2019-04
- **Tags:**
  - State Estimation

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

import { defineConfig } from "vitepress";

export default defineConfig({
  title: "Awesome-Humanoid-Robot-Learning",
  description: "A curated collection of humanoid robot learning research papers",
  base: "/",
  lang: "en-US",
  cleanUrls: true,
  ignoreDeadLinks: true,

  head: [
    ["link", { rel: "icon", href: "/Awesome-Humanoid-Robot-Learning/favicon.ico" }],
  ],

  themeConfig: {
    nav: [
      { text: "Home", link: "/" },
      { text: "Latest", link: "/latest" },
      { text: "Real Robot", link: "/real-robot" },
      { text: "Open Source", link: "/open-source" },
      { text: "Tags", link: "/tags" },
    ],

    sidebar: [
      {
            "text": "Overview",
            "items": [
                  {
                        "text": "Home",
                        "link": "/"
                  },
                  {
                        "text": "Latest Papers",
                        "link": "/latest"
                  },
                  {
                        "text": "Real Robot",
                        "link": "/real-robot"
                  },
                  {
                        "text": "Open Source",
                        "link": "/open-source"
                  },
                  {
                        "text": "Tags",
                        "link": "/tags"
                  }
            ]
      },
      {
            "text": "Loco-Manipulation and Whole-Body Control (186)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/loco-manipulation-and-whole-body-control/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/loco-manipulation-and-whole-body-control/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/loco-manipulation-and-whole-body-control/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/loco-manipulation-and-whole-body-control/2026-04"
                  },
                  {
                        "text": "2026-03",
                        "link": "/loco-manipulation-and-whole-body-control/2026-03"
                  },
                  {
                        "text": "2026-02",
                        "link": "/loco-manipulation-and-whole-body-control/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/loco-manipulation-and-whole-body-control/2026-01"
                  },
                  {
                        "text": "2025-12",
                        "link": "/loco-manipulation-and-whole-body-control/2025-12"
                  },
                  {
                        "text": "2025-11",
                        "link": "/loco-manipulation-and-whole-body-control/2025-11"
                  },
                  {
                        "text": "2025-10",
                        "link": "/loco-manipulation-and-whole-body-control/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/loco-manipulation-and-whole-body-control/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/loco-manipulation-and-whole-body-control/2025-08"
                  },
                  {
                        "text": "2025-07",
                        "link": "/loco-manipulation-and-whole-body-control/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/loco-manipulation-and-whole-body-control/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/loco-manipulation-and-whole-body-control/2025-05"
                  },
                  {
                        "text": "2025-04",
                        "link": "/loco-manipulation-and-whole-body-control/2025-04"
                  },
                  {
                        "text": "2025-03",
                        "link": "/loco-manipulation-and-whole-body-control/2025-03"
                  },
                  {
                        "text": "2025-02",
                        "link": "/loco-manipulation-and-whole-body-control/2025-02"
                  },
                  {
                        "text": "2024-12",
                        "link": "/loco-manipulation-and-whole-body-control/2024-12"
                  },
                  {
                        "text": "2024-11",
                        "link": "/loco-manipulation-and-whole-body-control/2024-11"
                  },
                  {
                        "text": "2024-10",
                        "link": "/loco-manipulation-and-whole-body-control/2024-10"
                  },
                  {
                        "text": "2024-09",
                        "link": "/loco-manipulation-and-whole-body-control/2024-09"
                  },
                  {
                        "text": "2024-07",
                        "link": "/loco-manipulation-and-whole-body-control/2024-07"
                  },
                  {
                        "text": "2024-06",
                        "link": "/loco-manipulation-and-whole-body-control/2024-06"
                  },
                  {
                        "text": "2024-03",
                        "link": "/loco-manipulation-and-whole-body-control/2024-03"
                  },
                  {
                        "text": "2024-02",
                        "link": "/loco-manipulation-and-whole-body-control/2024-02"
                  },
                  {
                        "text": "2023-10",
                        "link": "/loco-manipulation-and-whole-body-control/2023-10"
                  },
                  {
                        "text": "2022-12",
                        "link": "/loco-manipulation-and-whole-body-control/2022-12"
                  }
            ]
      },
      {
            "text": "Manipulation (55)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/manipulation/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/manipulation/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/manipulation/2026-04"
                  },
                  {
                        "text": "2026-03",
                        "link": "/manipulation/2026-03"
                  },
                  {
                        "text": "2026-02",
                        "link": "/manipulation/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/manipulation/2026-01"
                  },
                  {
                        "text": "2025-11",
                        "link": "/manipulation/2025-11"
                  },
                  {
                        "text": "2025-10",
                        "link": "/manipulation/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/manipulation/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/manipulation/2025-08"
                  },
                  {
                        "text": "2025-07",
                        "link": "/manipulation/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/manipulation/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/manipulation/2025-05"
                  },
                  {
                        "text": "2025-03",
                        "link": "/manipulation/2025-03"
                  },
                  {
                        "text": "2025-02",
                        "link": "/manipulation/2025-02"
                  },
                  {
                        "text": "2025-01",
                        "link": "/manipulation/2025-01"
                  },
                  {
                        "text": "2024-12",
                        "link": "/manipulation/2024-12"
                  },
                  {
                        "text": "2024-11",
                        "link": "/manipulation/2024-11"
                  },
                  {
                        "text": "2024-10",
                        "link": "/manipulation/2024-10"
                  },
                  {
                        "text": "2024-08",
                        "link": "/manipulation/2024-08"
                  },
                  {
                        "text": "2024-07",
                        "link": "/manipulation/2024-07"
                  },
                  {
                        "text": "2024-04",
                        "link": "/manipulation/2024-04"
                  },
                  {
                        "text": "2024-03",
                        "link": "/manipulation/2024-03"
                  }
            ]
      },
      {
            "text": "Teleoperation (26)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/teleoperation/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/teleoperation/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/teleoperation/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/teleoperation/2026-04"
                  },
                  {
                        "text": "2026-02",
                        "link": "/teleoperation/2026-02"
                  },
                  {
                        "text": "2025-11",
                        "link": "/teleoperation/2025-11"
                  },
                  {
                        "text": "2025-10",
                        "link": "/teleoperation/2025-10"
                  },
                  {
                        "text": "2025-08",
                        "link": "/teleoperation/2025-08"
                  },
                  {
                        "text": "2025-06",
                        "link": "/teleoperation/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/teleoperation/2025-05"
                  },
                  {
                        "text": "2025-03",
                        "link": "/teleoperation/2025-03"
                  },
                  {
                        "text": "2024-09",
                        "link": "/teleoperation/2024-09"
                  },
                  {
                        "text": "2023-09",
                        "link": "/teleoperation/2023-09"
                  },
                  {
                        "text": "2023-01",
                        "link": "/teleoperation/2023-01"
                  },
                  {
                        "text": "2022-03",
                        "link": "/teleoperation/2022-03"
                  }
            ]
      },
      {
            "text": "Locomotion (107)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/locomotion/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/locomotion/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/locomotion/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/locomotion/2026-04"
                  },
                  {
                        "text": "2026-03",
                        "link": "/locomotion/2026-03"
                  },
                  {
                        "text": "2026-02",
                        "link": "/locomotion/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/locomotion/2026-01"
                  },
                  {
                        "text": "2025-12",
                        "link": "/locomotion/2025-12"
                  },
                  {
                        "text": "2025-11",
                        "link": "/locomotion/2025-11"
                  },
                  {
                        "text": "2025-10",
                        "link": "/locomotion/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/locomotion/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/locomotion/2025-08"
                  },
                  {
                        "text": "2025-07",
                        "link": "/locomotion/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/locomotion/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/locomotion/2025-05"
                  },
                  {
                        "text": "2025-04",
                        "link": "/locomotion/2025-04"
                  },
                  {
                        "text": "2025-03",
                        "link": "/locomotion/2025-03"
                  },
                  {
                        "text": "2025-02",
                        "link": "/locomotion/2025-02"
                  },
                  {
                        "text": "2024-11",
                        "link": "/locomotion/2024-11"
                  },
                  {
                        "text": "2024-10",
                        "link": "/locomotion/2024-10"
                  },
                  {
                        "text": "2024-08",
                        "link": "/locomotion/2024-08"
                  },
                  {
                        "text": "2024-06",
                        "link": "/locomotion/2024-06"
                  },
                  {
                        "text": "2024-04",
                        "link": "/locomotion/2024-04"
                  },
                  {
                        "text": "2024-02",
                        "link": "/locomotion/2024-02"
                  },
                  {
                        "text": "2024-01",
                        "link": "/locomotion/2024-01"
                  },
                  {
                        "text": "2023-09",
                        "link": "/locomotion/2023-09"
                  },
                  {
                        "text": "2023-07",
                        "link": "/locomotion/2023-07"
                  },
                  {
                        "text": "2023-03",
                        "link": "/locomotion/2023-03"
                  },
                  {
                        "text": "2023-02",
                        "link": "/locomotion/2023-02"
                  }
            ]
      },
      {
            "text": "Navigation (19)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/navigation/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/navigation/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/navigation/2026-05"
                  },
                  {
                        "text": "2026-02",
                        "link": "/navigation/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/navigation/2026-01"
                  },
                  {
                        "text": "2025-12",
                        "link": "/navigation/2025-12"
                  },
                  {
                        "text": "2025-11",
                        "link": "/navigation/2025-11"
                  },
                  {
                        "text": "2025-09",
                        "link": "/navigation/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/navigation/2025-08"
                  },
                  {
                        "text": "2025-07",
                        "link": "/navigation/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/navigation/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/navigation/2025-05"
                  },
                  {
                        "text": "2025-03",
                        "link": "/navigation/2025-03"
                  },
                  {
                        "text": "2024-12",
                        "link": "/navigation/2024-12"
                  },
                  {
                        "text": "2023-10",
                        "link": "/navigation/2023-10"
                  }
            ]
      },
      {
            "text": "State Estimation (15)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/state-estimation/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/state-estimation/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/state-estimation/2026-05"
                  },
                  {
                        "text": "2025-11",
                        "link": "/state-estimation/2025-11"
                  },
                  {
                        "text": "2025-07",
                        "link": "/state-estimation/2025-07"
                  },
                  {
                        "text": "2022-07",
                        "link": "/state-estimation/2022-07"
                  },
                  {
                        "text": "2019-04",
                        "link": "/state-estimation/2019-04"
                  },
                  {
                        "text": "2017-05",
                        "link": "/state-estimation/2017-05"
                  },
                  {
                        "text": "2014-10",
                        "link": "/state-estimation/2014-10"
                  }
            ]
      },
      {
            "text": "Sim-to-Real (11)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/sim-to-real/"
                  },
                  {
                        "text": "2026-02",
                        "link": "/sim-to-real/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/sim-to-real/2026-01"
                  },
                  {
                        "text": "2025-10",
                        "link": "/sim-to-real/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/sim-to-real/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/sim-to-real/2025-08"
                  },
                  {
                        "text": "2025-05",
                        "link": "/sim-to-real/2025-05"
                  },
                  {
                        "text": "2025-04",
                        "link": "/sim-to-real/2025-04"
                  },
                  {
                        "text": "2025-02",
                        "link": "/sim-to-real/2025-02"
                  },
                  {
                        "text": "2019-01",
                        "link": "/sim-to-real/2019-01"
                  }
            ]
      },
      {
            "text": "Hardware Design (31)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/hardware-design/"
                  },
                  {
                        "text": "2026-02",
                        "link": "/hardware-design/2026-02"
                  },
                  {
                        "text": "2026-01",
                        "link": "/hardware-design/2026-01"
                  },
                  {
                        "text": "2025-12",
                        "link": "/hardware-design/2025-12"
                  },
                  {
                        "text": "2025-11",
                        "link": "/hardware-design/2025-11"
                  },
                  {
                        "text": "2025-10",
                        "link": "/hardware-design/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/hardware-design/2025-09"
                  },
                  {
                        "text": "2025-07",
                        "link": "/hardware-design/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/hardware-design/2025-06"
                  },
                  {
                        "text": "2025-04",
                        "link": "/hardware-design/2025-04"
                  },
                  {
                        "text": "2025-03",
                        "link": "/hardware-design/2025-03"
                  },
                  {
                        "text": "2025-02",
                        "link": "/hardware-design/2025-02"
                  },
                  {
                        "text": "2025-01",
                        "link": "/hardware-design/2025-01"
                  },
                  {
                        "text": "2024-09",
                        "link": "/hardware-design/2024-09"
                  },
                  {
                        "text": "2024-07",
                        "link": "/hardware-design/2024-07"
                  },
                  {
                        "text": "2021-04",
                        "link": "/hardware-design/2021-04"
                  },
                  {
                        "text": "2019-04",
                        "link": "/hardware-design/2019-04"
                  }
            ]
      },
      {
            "text": "Simulation Benchmark (39)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/simulation-benchmark/"
                  },
                  {
                        "text": "2026-06",
                        "link": "/simulation-benchmark/2026-06"
                  },
                  {
                        "text": "2026-05",
                        "link": "/simulation-benchmark/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/simulation-benchmark/2026-04"
                  },
                  {
                        "text": "2026-03",
                        "link": "/simulation-benchmark/2026-03"
                  },
                  {
                        "text": "2026-02",
                        "link": "/simulation-benchmark/2026-02"
                  },
                  {
                        "text": "2025-12",
                        "link": "/simulation-benchmark/2025-12"
                  },
                  {
                        "text": "2025-10",
                        "link": "/simulation-benchmark/2025-10"
                  },
                  {
                        "text": "2025-07",
                        "link": "/simulation-benchmark/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/simulation-benchmark/2025-06"
                  },
                  {
                        "text": "2024-12",
                        "link": "/simulation-benchmark/2024-12"
                  },
                  {
                        "text": "2024-10",
                        "link": "/simulation-benchmark/2024-10"
                  },
                  {
                        "text": "2024-07",
                        "link": "/simulation-benchmark/2024-07"
                  },
                  {
                        "text": "2024-06",
                        "link": "/simulation-benchmark/2024-06"
                  },
                  {
                        "text": "2024-04",
                        "link": "/simulation-benchmark/2024-04"
                  },
                  {
                        "text": "2024-03",
                        "link": "/simulation-benchmark/2024-03"
                  }
            ]
      },
      {
            "text": "Physics-Based Character Animation (34)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/physics-based-character-animation/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/physics-based-character-animation/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/physics-based-character-animation/2026-04"
                  },
                  {
                        "text": "2026-02",
                        "link": "/physics-based-character-animation/2026-02"
                  },
                  {
                        "text": "2025-12",
                        "link": "/physics-based-character-animation/2025-12"
                  },
                  {
                        "text": "2025-10",
                        "link": "/physics-based-character-animation/2025-10"
                  },
                  {
                        "text": "2025-09",
                        "link": "/physics-based-character-animation/2025-09"
                  },
                  {
                        "text": "2025-08",
                        "link": "/physics-based-character-animation/2025-08"
                  },
                  {
                        "text": "2025-07",
                        "link": "/physics-based-character-animation/2025-07"
                  },
                  {
                        "text": "2025-06",
                        "link": "/physics-based-character-animation/2025-06"
                  },
                  {
                        "text": "2025-05",
                        "link": "/physics-based-character-animation/2025-05"
                  },
                  {
                        "text": "2025-04",
                        "link": "/physics-based-character-animation/2025-04"
                  },
                  {
                        "text": "2025-03",
                        "link": "/physics-based-character-animation/2025-03"
                  },
                  {
                        "text": "2025-02",
                        "link": "/physics-based-character-animation/2025-02"
                  },
                  {
                        "text": "2024-10",
                        "link": "/physics-based-character-animation/2024-10"
                  },
                  {
                        "text": "2024-09",
                        "link": "/physics-based-character-animation/2024-09"
                  },
                  {
                        "text": "2024-08",
                        "link": "/physics-based-character-animation/2024-08"
                  },
                  {
                        "text": "2023-09",
                        "link": "/physics-based-character-animation/2023-09"
                  },
                  {
                        "text": "2023-06",
                        "link": "/physics-based-character-animation/2023-06"
                  },
                  {
                        "text": "2023-05",
                        "link": "/physics-based-character-animation/2023-05"
                  },
                  {
                        "text": "2022-08",
                        "link": "/physics-based-character-animation/2022-08"
                  },
                  {
                        "text": "2021-08",
                        "link": "/physics-based-character-animation/2021-08"
                  },
                  {
                        "text": "2018-11",
                        "link": "/physics-based-character-animation/2018-11"
                  },
                  {
                        "text": "2018-09",
                        "link": "/physics-based-character-animation/2018-09"
                  },
                  {
                        "text": "2018-08",
                        "link": "/physics-based-character-animation/2018-08"
                  },
                  {
                        "text": "2018-01",
                        "link": "/physics-based-character-animation/2018-01"
                  }
            ]
      },
      {
            "text": "Human Motion Analysis and Synthesis (23)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/human-motion-analysis-and-synthesis/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/human-motion-analysis-and-synthesis/2026-05"
                  },
                  {
                        "text": "2026-04",
                        "link": "/human-motion-analysis-and-synthesis/2026-04"
                  },
                  {
                        "text": "2026-02",
                        "link": "/human-motion-analysis-and-synthesis/2026-02"
                  },
                  {
                        "text": "2025-12",
                        "link": "/human-motion-analysis-and-synthesis/2025-12"
                  },
                  {
                        "text": "2025-08",
                        "link": "/human-motion-analysis-and-synthesis/2025-08"
                  },
                  {
                        "text": "2025-05",
                        "link": "/human-motion-analysis-and-synthesis/2025-05"
                  },
                  {
                        "text": "2025-04",
                        "link": "/human-motion-analysis-and-synthesis/2025-04"
                  },
                  {
                        "text": "2025-03",
                        "link": "/human-motion-analysis-and-synthesis/2025-03"
                  },
                  {
                        "text": "2024-10",
                        "link": "/human-motion-analysis-and-synthesis/2024-10"
                  },
                  {
                        "text": "2024-05",
                        "link": "/human-motion-analysis-and-synthesis/2024-05"
                  },
                  {
                        "text": "2024-04",
                        "link": "/human-motion-analysis-and-synthesis/2024-04"
                  },
                  {
                        "text": "2023-10",
                        "link": "/human-motion-analysis-and-synthesis/2023-10"
                  },
                  {
                        "text": "2023-07",
                        "link": "/human-motion-analysis-and-synthesis/2023-07"
                  },
                  {
                        "text": "2023-06",
                        "link": "/human-motion-analysis-and-synthesis/2023-06"
                  },
                  {
                        "text": "2023-05",
                        "link": "/human-motion-analysis-and-synthesis/2023-05"
                  },
                  {
                        "text": "2022-12",
                        "link": "/human-motion-analysis-and-synthesis/2022-12"
                  }
            ]
      }
],

    socialLinks: [
      { icon: "github", link: "https://github.com" },
    ],

    search: {
      provider: "local",
      options: {
        miniSearch: {
          options: {
            boostDocument: (id, term, storedFields) => {
              // Boost titles over content
              if (storedFields.titles?.some(t => t.toLowerCase().includes(term.toLowerCase()))) {
                return 3;
              }
              return 1;
            },
          },
        },
      },
    },

    footer: {
      message: "Automatically updated daily from arXiv",
      copyright: "MIT License",
    },

    outline: {
      level: [2, 3],
      label: "On this page",
    },

    docFooter: {
      prev: "Previous",
      next: "Next",
    },
  },

  markdown: {
    theme: "github-light",
    lineNumbers: false,
  },

  appearance: {
    initialValue: "dark",
  },
});

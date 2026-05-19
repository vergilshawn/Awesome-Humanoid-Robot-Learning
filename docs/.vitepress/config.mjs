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
            "text": "Loco-Manipulation and Whole-Body Control (1)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/loco-manipulation-and-whole-body-control/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/loco-manipulation-and-whole-body-control/2026-05"
                  }
            ]
      },
      {
            "text": "Locomotion (1)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/locomotion/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/locomotion/2026-05"
                  }
            ]
      },
      {
            "text": "State Estimation (1)",
            "collapsed": true,
            "items": [
                  {
                        "text": "Overview",
                        "link": "/state-estimation/"
                  },
                  {
                        "text": "2026-05",
                        "link": "/state-estimation/2026-05"
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

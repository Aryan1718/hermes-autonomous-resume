import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Hermes Docs',
  tagline: 'Autonomous resume pipeline docs for setup, operation, and extension.',
  favicon: 'img/hermes-mark.svg',

  url: 'https://hermes-autonomous-resume.vercel.app',
  baseUrl: '/',

  organizationName: 'hermes',
  projectName: 'autonomous-resume',

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  themes: ['@docusaurus/theme-mermaid'],

  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs',
          routeBasePath: 'docs',
          sidebarPath: './sidebars.ts',
        },
        blog: false,
        pages: {},
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/hermes-social-card.svg',
    navbar: {
      title: 'Hermes Docs',
      items: [
        {
          to: '/docs/getting-started/introduction',
          label: 'Docs',
          position: 'left',
        },
        {
          href: 'https://github.com/your-org/hermes-autonomous-resume',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    prism: {
      additionalLanguages: ['bash', 'python', 'json'],
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'forest'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

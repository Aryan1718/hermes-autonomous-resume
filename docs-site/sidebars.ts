import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  docsSidebar: [
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'getting-started/introduction',
        'getting-started/installation',
      ],
    },
    {
      type: 'category',
      label: 'Scraper Agent',
      items: [
        'scraper-agent/overview',
        'scraper-agent/setup-guide',
      ],
    },
    {
      type: 'category',
      label: 'Resume Agent',
      items: [
        'resume-agent/overview',
        'resume-agent/how-it-works',
        'resume-agent/setup-guide',
        'resume-agent/pool-content-guide',
        'resume-agent/skill-workflow',
        'resume-agent/run-and-verify',
      ],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: [
        'api-reference/overview',
        'api-reference/job-description-apis',
        'api-reference/resume-output-apis',
        'api-reference/workflow-logging-apis',
        'api-reference/feedback-apis',
        'api-reference/hermes-integration-apis',
        'api-reference/authentication-apis',
      ],
    },
    {
      type: 'category',
      label: 'Setup',
      items: [
        'setup/candidate-setup',
        'setup/pool-intake',
        'setup/dashboard-integration',
      ],
    },
    {
      type: 'category',
      label: 'Pipeline',
      items: [
        'pipeline/overview',
        'pipeline/skills',
        'pipeline/orchestrator',
      ],
    },
    {
      type: 'category',
      label: 'Architecture',
      items: [
        'architecture/system-design',
        'architecture/feedback-loop',
      ],
    },
  ],
};

export default sidebars;

import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';

const cards = [
  {
    title: 'Set Up a Candidate',
    href: '/docs/setup/candidate-setup',
    description:
      'Use profile-bootstrap to personalize the pipeline for a real candidate instead of editing templates by hand.',
  },
  {
    title: 'Understand the Flow',
    href: '/docs/pipeline/overview',
    description:
      'See how job descriptions move from intake to filtering, extraction, selection, tailoring, assembly, and dashboard push.',
  },
  {
    title: 'Connect the Dashboard',
    href: '/docs/setup/dashboard-integration',
    description:
      'Configure the dashboard API placeholders and understand what the orchestrator expects at runtime.',
  },
];

export default function Home(): JSX.Element {
  return (
    <Layout
      title="Hermes Docs"
      description="Setup and architecture docs for the Hermes autonomous resume pipeline">
      <main className="heroShell">
        <section className="heroPanel">
          <p className="eyebrow">Autonomous Resume Pipeline</p>
          <h1>Docs for configuring, operating, and extending Hermes.</h1>
          <p className="heroCopy">
            Hermes scrapes job descriptions, evaluates fit against a candidate profile,
            tailors resumes from structured evidence, pushes outputs to a dashboard,
            and closes the loop with feedback.
          </p>
          <div className="heroActions">
            <Link className="button button--primary button--lg" to="/docs/getting-started/introduction">
              Read the introduction
            </Link>
            <Link className="button button--secondary button--lg" to="/docs/getting-started/first-run">
              First-run checklist
            </Link>
          </div>
        </section>

        <section className="cardGrid">
          {cards.map((card) => (
            <Link key={card.title} to={card.href} className={clsx('docCard')}>
              <h2>{card.title}</h2>
              <p>{card.description}</p>
            </Link>
          ))}
        </section>
      </main>
    </Layout>
  );
}

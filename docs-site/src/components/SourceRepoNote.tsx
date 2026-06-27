import type { ReactNode } from 'react';

type SourceRepoNoteProps = {
  children: ReactNode;
};

export default function SourceRepoNote({ children }: SourceRepoNoteProps) {
  return (
    <div className="sourceRepoNote">
      <p>{children}</p>
      <a
        className="sourceRepoNote__link"
        href="https://github.com/Aryan1718/hermes-autonomous-resume"
        target="_blank"
        rel="noreferrer"
      >
        hermes-autonomous-resume on GitHub
      </a>
    </div>
  );
}

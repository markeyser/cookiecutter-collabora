# Software Development Life Cycle

## Introduction

This flowchart provides a visual representation of the key stages involved in the software development life cycle. Each step is accompanied by detailed documentation to guide you through best practices and standardized processes.

## Flowchart

```mermaid
---
title: Software Development Cycle
---
flowchart TB
  A([1. Open the JIRA story <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira'>link</a>]) ==> B([2. Create a branch from main 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>link</a>])
  B ==> C([3. Develop Python code])
  C ==> D([4. Debug Python code])
  D ==> E([5. Unit test with PyTest 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/pytest-inroduction-guide/'>link</a>])
  E ==> F([6. Type check with Mypy <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/type-checking-mypy/?h=type+che'>link</a>])
  F ==> G([7. Refactor code])
  G ==> H([8. Format code with Black 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/black-formatter/?h=black'>link</a>])
  H ==> I([9. Lint code with Ruff 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/ruff-linter/?h=lint'>link</a>])
  I ==> J([10. Pass pre-commit hooks 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/pre-commit-hooks-guide/'>link</a>])
  J ==> K([11. Update documentation <a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/mkdocs-docs/?h=mkd'>link</a>])
  K ==> L([12. Commit changes 🪝 <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/commit-message-standards-ml/?h=commit'>link</a>])
  L ==> M([13. Push to remote repo])
  M --> |Repeat as necessary for multiple commits|C
  M ==> N([14. Open a Pull Request <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/templates/?h=pull'>link</a>])
  N ==> O([15. Code Review <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/code-review-best-practices/?h=review'>link</a>])
  O ==> P([16. Address review feedback])
  P ==> Q([17. Merge into main])
  Q ==> R([18. Continuous Integration/Deployment])
  R ==> S([19. Integration Testing])
  S ==> T([20. Deploy to Staging])
  T ==> U([21. Monitoring and Logging])
  U ==> |Start again with a new issue|A

  classDef highlighted fill:#d9534f,stroke:#333,stroke-width:2px,color:#fff;
  classDef blue fill:#5bc0de,stroke:#333,stroke-width:2px,color:#fff;
  class A,B,C,F,H,I,J,L,M,N highlighted;
  class R,S,T,U blue;
```
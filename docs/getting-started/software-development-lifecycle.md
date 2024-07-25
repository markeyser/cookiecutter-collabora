# Software Development Life Cycle

## Introduction

This flowchart provides a visual representation of the key stages involved in the software development life cycle. Each step is accompanied by detailed documentation to guide you through best practices and standardized processes.

## Flowchart

```mermaid
---
title: Software Development Cycle
---
flowchart TB
  A([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style="text-decoration: none;"><span style="color: inherit;">➊  Open Jira Story 🔗</span></a>])
  B([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/' style="text-decoration: none;"><span style="color: inherit;">➋ Create a branch from main 🔗</span></a>])
  C([<span style="color: inherit;">➌ Develop Python code</span>])
  D([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/cofig-files/' style="text-decoration: none;"><span style="color: inherit;">➍ Config files 🔗</span></a>])
  E([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/error-handling-and-logging/?h=jira' style='text-decoration: none;'><span style="color: inherit;">➎ Error handling and logging 🔗</span></a>])
  F([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/type-checking-mypy/' style="text-decoration: none;"><span style="color: inherit;">➏ Type hints 🔗</span></a>])
  G([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/docstrings-and-inline-commentaries/' style="text-decoration: none;"><span style="color: inherit;">➐ Inline comments and docstrings 🔗</span></a>])
  H([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/pytest-inroduction-guide/' style="text-decoration: none;"><span style="color: inherit;">➑ Unit test with PyTest 🔗</span></a>])
  I([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/type-checking-mypy/?h=type+che' style="text-decoration: none;"><span style="color: inherit;">➒ Type check with Mypy 🔗</span></a>])
  J([<a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/black-formatter/?h=black' style="text-decoration: none;"><span style="color: inherit;">➓ Format code with Black 🔗</span></a>])
  K([<a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/ruff-linter/?h=lint' style="text-decoration: none;"><span style="color: inherit;">⓫ Lint code with Ruff 🔗</span></a>])
  L([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/pre-commit-hooks-guide/' style="text-decoration: none;"><span style="color: inherit;">⓬ Pass pre-commit hooks 🔗</span></a>])
  M([<a href='https://markeyser.github.io/cookiecutter-collabora/tutorials/mkdocs-docs/?h=mkd' style="text-decoration: none;"><span style="color: inherit;">⓭ Update documentation 🔗</span></a>])
  N([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/commit-message-standards-ml/?h=commit' style="text-decoration: none;"><span style="color: inherit;">⓮ Commit changes 🔗</span></a>])
  O([<span style="color: inherit;">⓯ Push to remote repo</span>])
  P([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/templates/?h=pull' style="text-decoration: none;"><span style="color: inherit;">⓰ Open a Pull Request 🔗</span></a>])
  Q([<a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/code-review-best-practices/?h=review' style="text-decoration: none;"><span style="color: inherit;">⓱ Code Review 🔗</span></a>])
  A ==> B
  B ==> C
  C ==> D
  D ==> E
  E ==> F
  F ==> G
  G ==> H
  H ==> I
  I ==> J
  J ==> K
  K ==> L
  L ==> M
  M ==> N
  N ==> O
  O ==> P
  P ==> Q
  Q ==> |Start again with a new issue|A
```

<!--
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
  M ==>|Repeat as necessary for multiple commits|C
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


```mermaid
---
title: Software Development Cycle
---
flowchart TB
  A("<div style='text-align: left;'><b>1. Initiation and Planning:</b> <br>• Scope and Requirements <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Open Jira Story</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Create a branch</a></div>")
  B("<div style='text-align: left;'><b>2. Development:</b> <br>• Develop Python Code<br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/error-handling-and-logging/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Error handling and logging</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/docstrings-and-inline-commentaries/'>Inline comments and docstrings</a></div>")
  A ==> B
  C("<div style='text-align: left;'><b>3. Refactoring:</b> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/type-checking-mypy/' style='text-decoration: underline; color: #ff00ff;'>Type hints</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/cofig-files/' style='text-decoration: underline; color: #ff00ff;'>Config files</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/cofig-files/'>Document</a></div>")
  B ==> C
  D("<div style='text-align: left;'><b>4. Quality:</b> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Run formatter</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Run linter</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Run Static typing checker</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Perform unit tests</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Conduct integration testing</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Optimize performance</a></div>")
  C ==> D
  E("<div style='text-align: left;'><b>4. Comprehensive Testing and Review:</b> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Perform end-to-end testing</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Conduct code coverage analysis</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Perform additional unit tests</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Perform unit tests</a></div>")
  D ==> E
  F("<div style='text-align: left;'><b>5. Quality Assurance and Compliance:</b> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Pass pre-commit hooks</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/jira-story-best-practices/?h=jira' style='text-decoration: underline; color: #ff00ff;'>Update documentation</a> <br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Perform additional unit tests</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Perform unit tests</a><br>• <a href='https://markeyser.github.io/cookiecutter-collabora/how-to-guides/git-branch-naming-standards/'>Prepare deployment procedures and update CI/CD pipelines</a></div>")
  E ==> F
  classDef highlighted fill:#d9534f,stroke:#333,stroke-width:2px,color:#fff;
  classDef blue fill:#5bc0de,stroke:#333,stroke-width:2px,color:#fff;
  class H,I,J,L,M,N highlighted;
  class R,S,T,U blue;
```
-->
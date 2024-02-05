# Branching Stragegies

## Experiment Branches

Use this branch type for working on and collaborating on experiments.
Because you'll often build lots of models and features that don't work,
you don't want to commit everything to your collaboration branch.

### Failed Experiments

If an experiment doesn't pan out, mark the Experiment issue as failed
with a label, close the PR without merging and update the Experiment
issue with a TLDR explaining what you tried and how it turned out. Link
to your experiment tracking tool so that others can view the runs.

```mermaid
---
title: Unsaccessful Experiment Branching Pattern
---

%%{init: { 'logLevel': 'debug', 'theme': 'base' } }%%
gitGraph TB:
  commit tag: "Initial commit"
  branch experiment
  checkout experiment
  commit tag: "First Commit on experiment"
  commit tag: "Iterate Experiment"
  commit tag: "Failed Experiment"
```

### Successful Experiments

If an experiment is successful and you want to start the deployment process:

1. Update the experiment issue with a TLDR and mark as successful using a label.
2. Open a Model Issue to prepare the model and pipelines for production.
3. Create a "Model" branch using Main as the base.
4. Merge upstream changes from Main into your experiment branch and resolve any conflicts.
5. Change the target of the Experiment PR to the Model branch.
6. Merge the pull request to your Model branch and close the Experiment Issue.
7. Delete the experiment branch after merging the PR.

```mermaid
---
title: Successful Experiment Branching Pattern
---
%%{init: { 'logLevel': 'debug', 'theme': 'base', 'gitGraph': {'rotateCommitLabel': true} } }%%
gitGraph TB:
    commit tag: "Initial commit"
    branch experiment
    checkout experiment
    commit tag: "Experiment changes"
    commit tag: "Interate Experiment"
    commit tag: "Successful approach found"
    checkout main
    commit tag: "Changes on master"
    merge experiment tag: "Merge successful experiment into master"
    commit tag: "Changes on master"
```

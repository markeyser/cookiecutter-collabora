# Templates for pull request, issue, feature and readme files

## Pull request template

The following is an example of a pull request template following a
holistic view including methodology, code, data and documentation review
by the coder and the reviewer.

```markdown title=".github/PULL_REQUEST_TEMPLATE/pull_request_template.md"
## Data Preparation Checklist
- [ ] Data sources are properly cited
- [ ] Data preprocessing and formatting are verified
- [ ] Data quality is thoroughly assessed
- [ ] Exploratory Data Analysis (EDA) is insightful and documented

## Experiment Overview
- [ ] Brief description of the experiment and its objectives
- [ ] Links to the corresponding GitHub issue/Jira story
- [ ] Summary of the experiment's findings/results
- [ ] W&B experiment page link for detailed metrics and visualizations

## Feature Engineering Checklist
- [ ] Relevant features are extracted and justified
- [ ] Feature transformations and scaling methods are appropriate
- [ ] Feature interactions are explored and utilized if beneficial
- [ ] Feature importance analysis is conducted and findings are documented

## Model Development Checklist
- [ ] Data splitting strategy is justified and implemented correctly
- [ ] Model training and validation approach is robust
- [ ] Hyperparameter optimization is conducted using W&B Sweeps (if applicable)
- [ ] Model performance is benchmarked against baselines and documented
- [ ] Model predictions are evaluated for reliability and bias

## Code Quality Checklist
- [ ] Code adheres to PEP 8 standards (or project-specific standards)
- [ ] Code is modular, reusable, and well-commented
- [ ] Code functionality is covered by tests (unit/integration)
- [ ] Data validation checks are in place
- [ ] End-to-end pipeline execution is verified
- [ ] Dependency list is updated and conflicts are resolved

## Documentation and Reporting Checklist
- [ ] Purpose and design of the code are clearly articulated
- [ ] Technical and business requirements are detailed
- [ ] Documentation covers all aspects of the codebase
- [ ] Execution steps are clearly outlined and reproducible
- [ ] Model architecture and evaluation metrics are thoroughly documented

## Collaboration and Review
- [ ] Code is reviewed for clarity, efficiency, and adherence to best practices
- [ ] Peer feedback is addressed constructively
- [ ] Final review confirms that all checklist items are satisfied
```

## Pull request template for bugs

## Ask Issues

Ask issues are for capturing, scoping, and refining the value-based
problems your team is trying to solve. They serve as a live definition
of work for your projects and will be the anchor for coordinating the
rest of the work you do.

By having the definition of work be in an issue, data science teams can
collaborate with their business partners and domain experts to refine
and rescope the issue as they learn more about the problem.

You should link to the other issues inside of the Ask issue. This will
give people context around why a particular issue is being worked on.

As your understanding of the problem evolves you should update your ask
issue accordingly. In order to create clarity, you should be as specific
as possible and resolve ambiguities by updating the Ask.

```markdown title=".github/ISSUE_TEMPLATE/ask_issue_template.md"
---
name: Ask issue
about: Describe your ask issue
title: ''
labels: ''
assignees: ''

---

### Problem Statement

The problem statement is a high level description of what you're trying
to solve and why. It should be clear what value solving this problem
will create and should also set a clear scope for what is and isn't
included as part of the problem.

!!! note
    If there is a large project with several components, it may make sense
    to create several Ask issues that link back to a parent Ask Issue.

#### Desired Outcome

This describes what the end state should look like. If it helps, you can
think of this as a user story. "I want [persona] to be able to do
[action] so that [some outcome] can happen". The goal here is to make
sure that your model maps to a business process. The last thing you want
is to build out a solution and not have a way to deploy it.

The most important part of this section is to capture what about the
existing process will change if your project is successful.

#### Current State

One of the best ways to figure out what you need to build is by
understanding the shortcomings of the existing process. You should also
capture why the current state needs to change. By focusing on this, you
can separate "nice-to-have" projects from "need-to-have" projects and
maximize your chances of get your project properly resourced.

### Success Criteria

It's important to know what constitutes success early on in the project.
This prevents you from falling into the situation where you've built
something that is good from a technical perspective but that the
stakeholders reject for some reason. Set clear guidelines and acceptance
criteria. If it's not clear what those are, you should do some analysis
to figure it out and then verify that with the stakeholders.

#### Impact

Impact is making it obvious what the value of your project will be once
done. The more concrete you can make this the better. If you are able to
estimate the impact of your project in terms of clear metrics, you'll
make it easy for your stakeholders to make a go/no-go decision.

You should also try to quantify how much of an improvement is needed for
the project to be valuable. If a project needs accuracy that is not
acheivable using SOTA techniques, it's good to know that before you
start working on it.

#### Metrics

Metrics take our impact and convert them into tangible metrics that we
can focus on while building our project. This can include both business
metrics as well as technical metrics.

For example, if the goal is to improve customer retention, you should
define how churn is measured and how you intend measure the improvement.
You may also need to capture secondary metrics such as cost of keeping a
customer.

Eventually, you'll need to convert your key metrics into technical ones.
You should be clear with which ones you're using. For example, if you're
doing a classification problem, you should be clear whether you're using
accuracy, F-score, AUC, etc. and why.

Finally, you may want to include counterbalance metrics. For example, if
your goal is to increase returns while minimizing risk.

#### Constraints

You should capture any constraints your project needs to keep in mind.
Ask yourself, what could keep my project from getting deployed. If you
think of something, that's a constraint. Some examples include:

- If you need real-time predictions you need a model that can do fast
  inference.
- Certain data may not be acceptable for use in a model (e.g. privacy or
  legal constraints).
- Model must have interpretability metrics in order to be acted upon.

### Solution Architecture

It's often useful to document your solution architecture. This can be
done using any tool (PowerPoint, Visio, hand-draw diagrams, etc.)

Including a diagram can be very helpful in understanding how a solution
will be implemented. This helps you catch design issues early in the
process while the cost to change them is still low.

By doing this throughout the project you'll also be able to see how your
solution evolved through time.

Finally, it makes it easier for people who are new to a project to
understand what's going on. This means there are lower barriers to
collaboration when you need to involve new teams.

### Data Requirements

You should capture which datasets are needed to solve a problem. Include
links to the data issues for each dataset (if there are multiple data
issues for a dataset, use the most current version. GitHub will track
changes to the issue over time, so you can see if the linked issue
changed if necessary).

#### Datasets

For each dataset, link to a data issue that describes what's in the
data. You can also link to the docs for a given dataset.

> Examples: Customer Transaction History (link to issue/docs)
> Customer demographics (link to issue/docs) Product inventories by
> store (link to issue/docs)

### Understanding and Exploration

This section is for linking to explore issues that inform the problem.
You should also link to relevant docs that help frame the problem.

### Approaches and Experiments

This section is for linking to your experiment issues. This section
should essentially be a running log of all the experiments attempted for
the ask. Experiments should be roughly chronological. Successful
experiments should be listed first.

### See Also

#### Background Info

This is useful for linking to related research, examples you found
online, etc. If something is relevant long term (i.e. after the ask is
closed), you may want to consider adding it to the docs.

#### Related Projects

Similar to Background info. If there are related projects or repos, you
can link to them here. If something is relevant long term (i.e. after
the ask is closed), you may want to consider adding it to the docs.
```

## Data Issues

Data issues are for defining the requirements and acceptance criteria of
a dataset needed for a problem. You should create one Data Issue *per
version of a dataset*. Once a dataset is validated and accepted, you
should publish that dataset as a version. For further changes and
updates, you should create new Data Issues. This allows you to clearly
mark milestones for when a dataset is done and creates clear
expectations for the team on what's in their data.

### Data Acquisition

Data Acquisition issues allow the data science team to collaborate with
the team that owns the data to define which parts of the data they need
inside the issue.

They also enable a data review process to ensure that the data being
loaded is what is needed for the problem at hand.

!!! example
    - Loading tables from a data warehouse to build models
    - Loading customer transcript text files from the enterprise data lake
    - Loading records from your company's CRM

!!! note
    The more explicit you are about defining data requirements and writing
    validation tests, the less time you'll have to spend fixing your
    datasets later on.  Writing data validation tests is a great way to
    protect against breaking changes when you push updates to your
    datasets.

```markdown title=".github/ISSUE_TEMPLATE/data_acquisition_issue_template.md"
---
name: Data aquisition issue
about: Describe your data aquisition
title: ''
labels: ''
assignees: ''

---

## Overview

The purpose of this issue is to track and document any issues or
challenges encountered while acquiring the data needed for the [Project
Name] project. This template can be used to report data quality issues,
missing data, or any other issues that may impact the success of the
project.

## Data Source

Name and link to the data source(s)

## Issue Description

Briefly describe the data acquisition issue(s) you encountered,
including details such as the affected variables or data files, the
nature of the issue (e.g., missing data, inconsistent data, etc.), and
any other relevant information.

## Steps to Reproduce

Provide step-by-step instructions for how to reproduce the issue, if
possible.

## Proposed Solution

Briefly describe your proposed solution for resolving the issue, if
known.

## Additional Information

Include any additional information or context that may be relevant to
resolving the issue.

## Labels

- Data Acquisition
- [Data Source] (e.g., API, CSV, etc.)
- [Type of issue] (e.g., Missing Data, Inconsistent Data, etc.)
```

### Dataset Creation

In contrast to the data acquisition issues, data creation issues usually
require a lot more experimentation and prototyping before a final
dataset is ready to merge.

The goal of this issue is to collaborate on creating the dataset you
need. It will be completed once you've created and validated a data
pipeline and created documentation for the new dataset.

```markdown title=".github/ISSUE_TEMPLATE/data_creation_issue_template.md"
---
name: Data creation issue
about: Describe your data creation
title: ''
labels: ''
assignees: ''

---

## Problem Description
Describe the problem you are trying to solve with this data creation
effort. What is the expected outcome and how will the data be used?

## Data Requirements
List the specific data requirements for this project. What
columns/attributes do you need, what is the format (csv, json, etc.),
and any constraints or limitations that need to be considered?

## Potential Data Sources
List any potential data sources that could be used for this project.
What are the pros and cons of each source and why would you choose one
over the others?

## Data Collection Plan
Outline the plan for collecting the necessary data. This should include
the steps you will take to collect the data, any tools or resources you
will use, and any potential challenges or roadblocks you anticipate.

## Estimated Time and Resources
Estimate the time and resources required to collect the data. What is
the expected timeline and what resources (e.g. people, equipment,
budget) will be needed?

## Next Steps
Indicate the next steps that need to be taken to start collecting the
data. Who is responsible for each step and what is the expected
timeline?

## Additional Information
Include any additional information that would be helpful in
understanding the data creation effort and why it is necessary.

## Labels
- data-creation
- data-collection
- project-planning
```

## Explore Issues

A lot of data science is exploratory. The goal of this type of work is
to increase your understanding of the data and the problem. Because of
this, you really don't care about the code that much. The code is just
an means to the end, which is getting more knowledge about the problem.

Oftentimes, data exploration is only relevant while you're doing the
work, or for providing context of why a decision was made.

Traditionally, data science teams have three options here.

1. Don't retain exploratory code in the repo.
2. Retain all exploratory code in the repo.
3. Selectively commit exploratory code to the repo.

The biggest challenge with exploratory work is figuring out when you
should merge it? If you merge it, how do you decide when you should
deprecate it? How can you ensure your exploration code is reproducible?
What does it mean to "test" exploration?

Because it's often more work than it's worth to test exploration code,
we should be hesitant to commit it to our main branch.

Additionally, if we merge all of our exploration, we will quickly get
notebook sprawl and our repo will be an unreadable, unmaintainable mess.

As an alternative, we can create explore issues and pull requests where
we describe and publish our work.

Most of the time, it's sufficient to push our code to an explore branch
and then close it without merging when we're done. The pull request will
still contain all of our code if we need to view it later and by linking
our explore issues to our other issues, we'll maintain a historical
record without cluttering up our repo.

!!! tip

    Push your exploratory code to an explore branch and then close it
    without merging when we're done.

In the cases where a piece of exploration evolves into something we want
to reuse or capture as part of our documentation then we can push
changes to our repo to update the docs or add some code to our
repository.

### Linking Explore Issues

Explore issues should be linked to other issues so that they are given
context. Often exploration without context of why it was done is not
useful.

!!! tip
    We should link the explore issues based on what issue prompted
    them.

For example if you are exploring a new dataset to understand it's
properties, you would link to an ask issue. If we're trying to validate
assumptions or learn more about our target population, you would link to
either an Ask or Explore issues. There are no hard rules here. The idea
is you want to create a clear history and give other context about why
an certain explore issue was created.

```markdown title=".github/ISSUE_TEMPLATE/explore_issue_template.md"
---
name: Explore issue
about: Describe your exploration
title: ''
labels: ''
assignees: ''

---

## Problem Statement

Briefly describe the problem that this exploration aims to solve or the
question it aims to answer.

## Data Source

List the data sources that will be used for this exploration and a brief
description of each.

## Exploration Goals

List the specific goals or questions that this exploration aims to
answer.

## Requirements List

Any specific requirements or constraints for this exploration.

## Deliverables List

The final outputs or findings that you expect from this exploration.

## Links to Other Issues

Link the explore issue based on what issue prompted them.

## Additional Information

Add any additional information or notes that may be relevant to this
exploration.
```

!!! note "How to link related issues on GitHub"
    To link related issues in the same repository, you can type `#`
    followed by part of the issue title and then clicking the issue
    that you want to link.

## Experiment Issues

We often won't solve our problem with the first approach we take. It
often takes iterating through many versions before we find something
that actually works.

Traditionally, the experimentation phase is a place where data science
teams struggle to be able to relay a sense of progress to others. They
are trying many approaches, and in fact making progress, but all they
can say is "We're still trying to get this model working".

After the project is over, the various approaches taken usually are
forgotten. When a team comes back to try to improve or fix a model
later, they often end up wasting time retrying things that failed in the
past simply because they don't know that they've already been tried.

Experiment issues are designed to capture each distinct approach taken
while trying to solve a problem. By doing so, teams can clearly
communicate what they tried and learn from each others efforts.
Additionally, they allow us to implement a model review process and
decide in a more systematic way which approaches we want to
productionalize. This allows us to catch problems early, - before we
invest time in making our models production ready.

The Experiment issues are the pivot point between the exploratory
iterative part of the data science process and the more linear model
deployment and MLOps portion of the process.

Once we create a successful experiment, we can validate our approach
with others and then elevate it to a Model issue and begin the MLOps
cycle.

### What to include

Similar to Explore issues, experiment issues should contain a TLDR of
what was tried and what the outcome was.

All experiments should be linked to an Ask issue.  Additionally, if
using a model and experimentation tracking system (like
[AzureML](https://docs.microsoft.com/en-us/azure/machine-learning/how-to-track-experiments)),
they should link to the system of record for your experiments. This lets
people have full insight into the full experiment lifecycle including
what problem the experiment was attempting to solve, what was tried,
what combinations of parameters were used, etc.

```markdown title=".github/ISSUE_TEMPLATE/experiment_issue_template.md"
### Enhanced ML Experiment Issue/Story Template

**Instructions for Use**:
- When creating a new issue or story for an ML experiment, copy and
  paste this template into the description field.
- Fill in each section with the details of your specific experiment.
- Encourage team members to review and contribute to the experiment
  planning process through comments or direct edits to the issue/story.

---

This enhanced template is structured to ensure thorough preparation and
clear communication of ML experiments, fostering a collaborative and
results-oriented approach to tackling complex problems.

#### **Experiment Title**
- A concise title that encapsulates the essence of the experiment,
  making it easily identifiable.

#### **Experiment Description**
- **Background**: Provide context and the rationale behind this
  experiment. Include any relevant previous work or literature.
- **Objective**: Clearly define what this experiment aims to achieve.
  Describe the problem it solves or the hypothesis it tests.
- **Hypothesis**: State the expected outcome of the experiment and the
  assumptions that are being tested.

#### **Data Source**
- Detail each data source to be used, including its origin, structure,
  and any preprocessing steps applied. Mention the relevance of each
  data source to the experiment.

#### **Experiment Goals**
- Enumerate the specific goals or questions the experiment aims to
  address. This could include performance benchmarks, model comparisons,
  or exploration of specific hypotheses.

#### **Success Criteria**
- Define clear, measurable criteria for what will constitute success for
  this experiment. This could include target metrics, statistical
  significance levels, or qualitative outcomes.

#### **Requirements List**
- List any technical, data, or resource requirements. Include hardware
  specifications, software versions, and any necessary access
  permissions.

#### **Deliverables List**
- Specify the expected outputs of the experiment. This could range from
  model weights, performance reports, to insights or conclusions drawn
  from the analysis.

#### **Experiment Methodology**
- **Approach**: Briefly outline the technical approach, including model
  architectures, algorithms, and any novel techniques being tested.
- **Metrics**: List the metrics by which the experiment will be
  evaluated, explaining why each is chosen.
- **Implementation Plan**: Provide an overview of the steps involved in
  executing the experiment, including data preparation, model training,
  and evaluation phases.

#### **Timeline and Milestones**
- Outline a tentative timeline for the experiment, including key
  milestones and checkpoints.

#### **Roles and Responsibilities**
- Identify team members involved and their specific responsibilities
  within the experiment.

#### **Links to Other Issues/Stories**
- Provide references to related issues or stories, including any that
  prompted this experiment or are dependencies of it.

#### **Additional Information**
- Include any other relevant information, notes, or considerations that
  could impact the experiment's design, execution, or analysis.

#### **Feedback Section**
- Invite team members to provide feedback on the experimental design,
  methodology, or any other aspect. Encourage collaboration and open
  discussion to refine and improve the experiment.
```

## Model Issues

Once you've completed an experiment and are ready to start the model
development and deployment process, you should open a Model issue.

You will use the Model issue to turn your experiment into
production-ready, deployable code. This will include adding tests,
parametrizing your models, etc.

The Model issue marks the beginning of the MLOps process. As your team
matures, you can create CI/CD processes and automation around the Model
Issue and its associated PR.

For example, once you've created your production model code with tests,
parameters, etc, you can use a pull request to trigger a CI/CD pipeline
to train, test, package, deploy, and monitor your model. Once your model
monitoring detects that your model performance has dropped, you can
automatically create a new model PR to retrain the model and mark it for
review by the data science team before triggering an automated
deployment process.

```markdown title=".github/ISSUE_TEMPLATE/model_issue_template.md"
---
name: Model issue
about: Turn experimet into production-ready code
title: ''
labels: ''
assignees: ''

---

Once you've completed an experiment and are ready to start the model
development and deployment process, you should open a Model issue.

You will use the Model issue to turn your experiment into
production-ready, deployable code. This will include adding tests,
parametrizing your models, etc.

The Model issue marks the beginning of the MLOps process. As your team
matures, you can create CI/CD processes and automation around the Model
Issue and its associated PR.

For example, once you've created your production model code with tests,
parameters, etc, you can use a pull request to trigger a CI/CD pipeline
to train, test, package, deploy, and monitor your model. Once your model
monitoring detects that your model performance has dropped, you can
automatically create a new model PR to retrain the model and mark it for
review by the data science team before triggering an automated
deployment process.
```

## Feature Request

```markdown title=".github/ISSUE_TEMPLATE/feature_request.md"
---
name: Feature request
about: Suggest an idea for this project
title: ''
labels: ''
assignees: ''

---

**Is your feature request related to a problem? Please describe.**
A clear and concise description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
```

## Bug Report

```markdown title=".github/ISSUE_TEMPLATE/bug_report.md"
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Desktop (please complete the following information):**
 - Browser [e.g. chrome, safari]
 - Version [e.g. 22]

**Additional context**
Add any other context about the problem here.
```

## Readme file template

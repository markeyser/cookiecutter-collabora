# Git Branch Naming Standards for ML Projects

!!! example "ChatGPT Prompt for Branch Name"
    Copy and paste the following prompt into ChatGPT to generate a branch
    name based on your JIRA story:

    ```plaintext
    I need a branch name for a new task. Here are the details:
    1. The description of the JIRA story: [Enter JIRA story description]
    2. The JIRA number: [Enter JIRA number]
    3. The standard to follow: <category>/<description>-<issue_number_or_jira_key>

    Please use one of the following categories: feature, bugfix, data, experiment, model, docs, refactor, test, chore.

    Provide the git command to create this branch.
    ```

    **Example Prompt:**

    ```plaintext
    I need a branch name for a new task. Here are the details:
    4. The description of the JIRA story: Add user authentication
    5. The JIRA number: DATA123
    6. The standard to follow: feature/add-user-authentication-DATA123

    Provide the git command to create this branch.
    ```

    **ChatGPT Output:**

    ```plaintext
    git checkout -b feature/add-user-authentication-DATA123
    ```


!!! tip "Overview"
    For machine learning projects, maintaining clarity in the Git repository is crucial. A consistent approach to branch naming is key to this clarity, facilitating rapid identification of the branch's purpose, aiding in collaboration, and making repository navigation intuitive.

!!! example "Naming Convention Structure"
    Branch names should follow this pattern:

    ```plaintext
    <category>/<description>-<issue_number_or_jira_key>
    ```

    - **Category**: A keyword indicating the branch's work nature.
    - **Description**: A clear descriptor of the task or feature.
    - **Issue Number or Jira Key**: Mandatory for linking to a corresponding task in your project management tool.

!!! abstract "Categories"
    Standard categories provide context on the branch's work domain:

    | Category      | Description                                                   |
    |---------------|---------------------------------------------------------------|
    | `feature`     | New feature development or enhancements                       |
    | `bugfix`      | Targeted branches for bug resolution                          |
    | `data`        | Data management activities, like acquisition or processing    |
    | `experiment`  | Exploratory or experimental development                       |
    | `model`       | Model creation, testing, or deployment                        |
    | `docs`        | Documentation creation or updates                             |
    | `refactor`    | Code restructuring to improve performance without altering functionality |
    | `test`        | Test development or modification                              |
    | `chore`       | Routine tasks or minor updates                                |

!!! check "Examples"
    Branch names that meet our standards:

    - `feature/user-authentication-DATA123`
    - `data/dataset-enhancement-GH15`
    - `model/performance-improvement-DATA22`
    - `bugfix/data-loading-error-GH45`
    - `docs/api-documentation-update`
    - `refactor/code-optimization-DATA78`
    - `test/new-model-tests-GH27`

!!! warning "Guidelines"
    - Use lowercase for all branch names.
    - Hyphens for word separation enhance readability.
    - Keep names brief yet descriptive.
    - Including the issue number or Jira key is mandatory for traceability.

!!! summary "Conclusion"
    Following these naming conventions is vital for organizing and
    accessing our ML project repositories, fostering team collaboration
    and efficient project management.

## Connecting JIRA stories and GitHub

Using JIRA story numbers or sub-task numbers in GitHub branch names and commit messages can be a good practice as it helps maintain traceability between code changes and project management tasks. Here are some considerations and recommendations to optimize this practice:

### Using JIRA Story Number in Branch Names

Creating a branch for each JIRA story and using the story number in the branch name is a widely adopted practice. This approach ensures that all code changes related to a specific story are organized in one branch.

**Example:**

- Branch name for a JIRA story: `feature/add-churn-prediction-model-JIRA-123`

### Using Sub-task Numbers in Branch Names

If the story is large and has several sub-tasks, creating separate branches for each sub-task can provide more granular control and better organization of work. This is especially useful if multiple team members are working on different sub-tasks of the same story.

**Example:**

- Branch name for a sub-task: `feature/preprocess-data-JIRA-123-subtask-1`
- Branch name for another sub-task: `feature/train-model-JIRA-123-subtask-2`

### Recommendations

1. **Small to Medium Stories:**
   - Use a single branch for the entire story if the scope is manageable.
   - Include the JIRA story number in the branch name.
   - Example: `feature/add-churn-prediction-model-JIRA-123`

2. **Large Stories with Multiple Sub-tasks:**
   - Create separate branches for each sub-task to allow parallel development.
   - Include both the JIRA story number and the sub-task number in the branch name.
   - Example: `feature/preprocess-data-JIRA-123-subtask-1`

## Commit Message Conventions

Including JIRA story or sub-task numbers in commit messages helps maintain a clear history of changes and their associated tasks.

**Example:**

- Commit message for a story: `Added data preprocessing steps-JIRA-123`
- Commit message for a sub-task: `Implemented initial data cleaning-JIRA-123-subtask-1`

## Best Practices Summary

1. **Branch Naming:**
   - Use `feature/`, `bugfix/`, or `hotfix/` prefixes to indicate the type of work.
   - Include the JIRA story or sub-task number for traceability.
   - Use descriptive names to indicate the purpose of the branch.

2. **Commit Messages:**
   - Start with the description of the change.
   - End with the JIRA story or sub-task number.
   - Optionally, add more detail in the body of the commit message.

3. **Branch Management:**
   - For small to medium stories, create a single branch per story.
   - For large stories, create separate branches for each sub-task to facilitate parallel work.
   - Ensure all sub-task branches are merged into the main story branch before final integration.

## Example Workflow

1. **Create a Branch for the Story:**
   - `feature/add-churn-prediction-model-JIRA-123`

2. **Create Sub-task Branches:**
   - `feature/preprocess-data-JIRA-123-subtask-1`
   - `feature/train-model-JIRA-123-subtask-2`

3. **Commit Changes with Clear Messages:**
   - `Implemented initial data cleaning-JIRA-123-subtask-1`
   - `Trained logistic regression model-JIRA-123-subtask-2`

4. **Merge Sub-task Branches into Story Branch:**
   - Merge `feature/preprocess-data-JIRA-123-subtask-1` into `feature/add-churn-prediction-model-JIRA-123`
   - Merge `feature/train-model-JIRA-123-subtask-2` into `feature/add-churn-prediction-model-JIRA-123`

5. **Integrate the Story Branch into Main Development Branch:**
   - Merge `feature/add-churn-prediction-model-JIRA-123` into `dev` or `main`

By following these practices, you can ensure that your development process remains organized and traceable, facilitating better project management and collaboration.
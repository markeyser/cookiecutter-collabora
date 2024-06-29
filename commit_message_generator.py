class CommitMessageGenerator:
    def generate_commit_message(self, git_diff, jira_number, commit_type, context=None):
        """
        Generate a standardized commit message based on git diff, JIRA story number,
        and commit type.

        Parameters:
        - git_diff (str): The output of the git diff command.
        - jira_number (str): The JIRA story number.
        - commit_type (str): The type of commit (e.g., fix, feat).
        - context (str, optional): Additional context for the commit.

        Returns:
        - str: A formatted commit message.
        """
        subject = f"{commit_type}: Update files based on {jira_number}"
        body = f"Modified files:\n{git_diff}"
        
        if context:
            body += f"\n\nContext:\n{context}"
        
        return f"{subject}\n\n{body}"
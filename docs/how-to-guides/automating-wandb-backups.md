# How to Back Up Weights & Biases Experiments Locally on MacBook Pro

This guide provides step-by-step instructions on how to back up your
Weights & Biases (W&B) experiments when running locally on a MacBook
Pro. Following the Detaxis approach for structured technical
documentation, this guide ensures that you can securely and efficiently
safeguard your data.

## **Define the Task**

Backing up W&B experiments involves saving experiment data, metadata,
and artifacts to prevent data loss and ensure reproducibility of
results.

## **Assumptions**

- You have W&B set up and running locally on your MacBook Pro.
- Basic familiarity with terminal commands.

## **Tools and Requirements**

- Terminal access on MacBook Pro.
- Optional: Access to cloud storage services or an external hard drive
  for remote backups.

### **Task Instructions**

#### **1. Export W&B Data**

- **Action**: Use the W&B CLI to export project data.
- **Commands**:
    ```bash
    wandb export USERNAME/PROJECT_NAME --output file.json
    ```
    Replace `USERNAME` with your W&B username and `PROJECT_NAME` with
    the name of your project.

#### **2. Database Backup**

- **Action**: Locate and copy the W&B local SQLite database for backup.
- **Location**: The default W&B directory is `~/wandb`. Find the
  `local.db` file within this directory.
- **Backup Command**:
    ```bash
    cp ~/wandb/local.db /path/to/your/backup/location
    ```

#### **3. Artifact Storage**

- **Action**: Manually back up the artifacts directory.
- **Command**:
    ```bash
    cp -R ~/wandb/artifacts /path/to/your/backup/location
    ```

#### **4. Automate Backups**

- **Action**: Create a script to automate the backup process.
- **Details**: Use the provided example backup script, modifying paths
  and destinations as needed. Schedule this script using `cron` for
  periodic backups.

#### **5. Version Control Integration**

- **Action**: Ensure that your project code is under version control
  (e.g., Git).
- **Purpose**: Facilitates matching experiment results with code
  versions, enhancing reproducibility.

## **Verification Steps**

1. **Check Exported Data**: Ensure that the JSON or CSV file contains
   all relevant experiment data.
2. **Validate Database Copy**: Verify that the `local.db` file is
   correctly copied to your backup location and is not corrupted.
3. **Artifact Backup**: Confirm that all files in the `artifacts`
   directory are present in your backup location.
4. **Test Automation Script**: Execute your backup script manually to
   ensure it works as expected. Check the backup destination for the new
   backup folder.
5. **Review Backup Frequency**: Ensure that your backup script is
   scheduled appropriately and runs at the desired frequency.

## **Troubleshooting**

- **Issue**: Export command fails.
  - **Solution**: Check your W&B username and project name for typos.
    Ensure you're connected to the internet if using W&B cloud.
- **Issue**: Backup script does not run automatically.
  - **Solution**: Verify the `cron` job setup. Check for syntax errors
    in your cron configuration.
- **Issue**: Insufficient backup space.
  - **Solution**: Regularly monitor your backup location's available
    space. Consider using cloud storage for additional capacity.

### **Automating Backups with a Script**

To simplify and automate the backup process for Weights & Biases
experiments on your MacBook Pro, you can use a shell script. This
section provides an example script and instructions on how to set it up
for automated execution using `cron`.

#### **Backup Script Example**

Below is an example of a backup script named `wandb_backup.sh`. This
script backs up the W&B local database and artifacts to a specified
backup directory.

```bash
#!/bin/bash

# Define the source and destination directories
WANDB_DIR="$HOME/wandb"
BACKUP_DIR="/path/to/your/backup/location/$(date +%Y%m%d_%H%M%S)"

# Create a new backup directory with a timestamp
mkdir -p "$BACKUP_DIR"

# Backup the local database
cp "$WANDB_DIR/local.db" "$BACKUP_DIR"

# Backup artifacts
cp -R "$WANDB_DIR/artifacts" "$BACKUP_DIR/artifacts"

echo "Backup completed successfully."
```

**Instructions:**

1. **Create the Script**:
   - Open your terminal.
   - Use a text editor (e.g., `nano` or `vim`) to create a new file
     named `wandb_backup.sh`.
   - Copy and paste the script above into the file.
   - Replace `/path/to/your/backup/location` with the actual path where
     you want to store your backups.

2. **Make the Script Executable**:
   - Run the following command in your terminal:
     ```bash
     chmod +x wandb_backup.sh
     ```

3. **Automating Execution with `cron`**:
   - Open your crontab for editing by running:
     ```bash
     crontab -e
     ```
   - Add a line to schedule the script execution. For example, to run
     the backup daily at 2 AM, add:
     ```
     0 2 * * * /path/to/your/wandb_backup.sh
     ```
   - Save and close the editor. `cron` will now execute the script
     according to the schedule.

#### **Verification and Monitoring**

- After setting up the script and scheduling it with `cron`, verify that
  it runs as expected by checking the backup directory for new backups
  after the scheduled time.
- Monitor your system logs and the backup directory to ensure ongoing
  successful executions. You might want to set up email notifications
  for `cron` jobs to stay informed about the backup script's execution
  status.

#### **Conclusion**

Automating the backup process ensures that your Weights & Biases
experiments and data are regularly saved without manual intervention. By
following these steps, you create a resilient and efficient backup
workflow, safeguarding your valuable machine learning experiments.

## **Conclusion**

By following these steps, you've created a robust backup strategy for
your Weights & Biases experiments. Regular backups ensure that your data
is secure and that your experiments are reproducible, regardless of
unforeseen data loss.

### **Further Assistance**

For more detailed information on W&B features and troubleshooting, visit
the [Weights & Biases documentation](https://docs.wandb.ai/).
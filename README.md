
# AutoMod Verison Control Template for Reddit Communities

This repository provides a template for managing and syncing Reddit AutoMod configurations using GitHub workflows and Python scripts.

## Overview

This template allows automatic syncing of AutoMod configurations between GitHub and Reddit. It includes workflows and scripts to:

- **Automatically update AutoMod on Reddit** when changes are pushed to the repository.
- **Fetch the current AutoMod configuration** from Reddit and update the repository.

## Repository Structure

- **`automod/automoderator.yml`**: Main AutoModerator configuration file in YAML format.
- **`update_automod.py`**: Python script that updates the AutoMod configuration on Reddit.
- **`fetch_automod.py`**: Python script that fetches the current AutoMod configuration from Reddit and updates the repository.
- **`.github/workflows/update-automod.yml`**: GitHub Actions workflow that updates the AutoMod configuration on Reddit when changes are made to the repository.
- **`.github/workflows/fetch-automod.yml`**: GitHub Actions workflow that fetches the current AutoMod configuration from Reddit.

## Workflows

### AutoMod Update Workflow

This workflow automatically pushes changes to Reddit whenever a commit is made to `automod/automoderator.yml`.

**Trigger**: On push to the `automod/automoderator.yml` file.

**Steps**:
1. Checkout the repository.
2. Set up the Python environment.
3. Install dependencies (PRAW).
4. Run the `update_automod.py` script to push the changes to Reddit.

### Fetch AutoMod Configuration Workflow

This manual workflow fetches the current AutoMod configuration from Reddit and updates the repository.

**Trigger**: Manual trigger via GitHub Actions.

**Steps**:
1. Checkout the repository.
2. Set up the Python environment.
3. Install dependencies (PRAW).
4. Run the `fetch_automod.py` script to fetch the current configuration from Reddit.
5. Commit and push the fetched configuration to the repository.

## How to Use

### Updating AutoMod Configuration

1. Edit `automod/automoderator.yml` to modify the AutoMod configuration.
2. Push the changes to the repository. The update will automatically be pushed to Reddit via the `update-automod.yml` workflow.

### Fetching Current AutoMod Configuration

1. Trigger the "Fetch AutoMod Configuration" workflow manually from the GitHub Actions tab.
2. The workflow will fetch the current configuration from Reddit, update the repository, and push the changes.

## Environment Setup

Ensure the following secrets are set up in your GitHub repository under **Settings > Secrets and variables > Actions**:

- `REDDIT_CLIENT_ID`
- `REDDIT_SECRET`
- `REDDIT_USERNAME`
- `REDDIT_PASSWORD`

These secrets are used by the Python scripts to interact with Reddit’s API. 

## License

This project is licensed under the MIT License.

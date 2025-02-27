#!/bin/bash

# AWS Amplify Setup
aws amplify create-app --name "childcare-ui" --repository "https://github.com/YOUR_GITHUB_REPO"

# Link frontend to Amplify hosting
aws amplify create-branch --app-id YOUR_APP_ID --branch-name main

# Trigger build
aws amplify start-job --app-id YOUR_APP_ID --branch-name main --job-type RELEASE
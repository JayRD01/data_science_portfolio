#!/bin/bash

# Fetch latest changes
git fetch origin

# Update main
git checkout main
git pull origin main

# Update feature/new-features
git checkout feature/new-features
git merge main
git push origin feature/new-features

# Update test/quality-assurance
git checkout test/quality-assurance
git merge main
git push origin test/quality-assurance

# Return to main
git checkout main

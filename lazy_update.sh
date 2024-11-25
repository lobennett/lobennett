#!/bin/bash

# Get commit message or use default
commit_msg="${1:-update papers.yml}"

git add papers.yml

git commit -m "$commit_msg"

git push origin main --force

echo "Successfully pushed papers.yml update!"
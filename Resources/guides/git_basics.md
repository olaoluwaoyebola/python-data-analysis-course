# Git Basics for the Course

## Overview
This guide covers the essential Git commands you might need for working with the course repository.

## Getting Started

### Clone the Repository
To get a local copy of the course repository:

```bash
git clone https://github.com/autom8or-com/python-data-analysis-course.git
cd python-data-analysis-course
```

### Update Your Local Copy
To get the latest updates from the repository:

```bash
git pull origin main
```

## Working with Your Own Solutions

Since you'll be submitting assignments separately, you don't need to push your changes to the course repository. However, you might want to track your own work with Git.

### Initialize a New Repository for Your Work

```bash
# Create a folder for your work
mkdir my-data-analysis-course
cd my-data-analysis-course

# Initialize Git repository
git init

# Create a .gitignore file
echo ".ipynb_checkpoints/" > .gitignore
echo "__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore
```

### Track Your Work

```bash
# Add your files
git add .

# Commit your changes
git commit -m "Completed Week 1 assignments"
```

### Connect to Your Own GitHub Repository

1. Create a new private repository on GitHub
2. Connect your local repository to your GitHub repository

```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

## Best Practices

1. **Commit often** with descriptive messages
2. **Create branches** for different assignments or features
3. **Pull before you push** to avoid conflicts
4. **Use .gitignore** to exclude unnecessary files
# GitHub Admin Workshop Content

## Overview
This repository contains hands-on lab exercises and materials for a GitHub Administration Workshop. The content is designed to help participants learn essential GitHub administrative tasks, team management, repository configuration, and CI/CD workflows.

> **Note:** This repository is intended solely for educational and training purposes.

## Workshop Structure

This workshop consists of three progressive labs:

### Lab 1: Teams and Nested Teams
Learn how to organize users into teams and sub-teams for better permission management.
- Create main teams representing functional areas
- Set up nested teams for specific sub-areas
- Manage team membership and visibility
- Understand team hierarchy

📁 [View Lab 1](lab_1/README.md)

### Lab 2: Repository Management
Master repository settings, branch protection, and access controls.
- Configure repository settings
- Set up branch protection rules
- Manage collaborator permissions
- Implement security policies

📁 [View Lab 2](lab_2/)

### Lab 3: CI/CD with GitHub Actions
Build and deploy applications using GitHub Actions workflows.
- Create automated testing workflows
- Implement continuous integration
- Configure linting and code quality checks
- Deploy applications

📁 [View Lab 3](lab_3/)

## Prerequisites

- A GitHub account with organization access
- Basic understanding of Git and GitHub
- Familiarity with command-line interfaces (optional for some labs)

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-org/gh-admin-workshop-content.git
   cd gh-admin-workshop-content
   ```

2. **Install dependencies (for Lab 3):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Follow the labs in order:**
   - Start with Lab 1 to understand team management
   - Progress to Lab 2 for repository administration
   - Complete Lab 3 to master GitHub Actions

## Repository Structure

```
gh-admin-workshop-content/
├── README.md                 # This file
├── requirements.txt          # Python dependencies for Lab 3
├── lab_1/
│   └── README.md            # Team management exercises
├── lab_2/                   # Repository management materials
└── lab_3/
    ├── app.py               # Sample Flask application
    └── tests/
        └── test_app.py      # Unit tests for CI/CD demo
```

## Technologies Used

- **GitHub Teams & Organizations** - Team and permission management
- **GitHub Actions** - CI/CD automation
- **Python 3.x** - Sample application language
- **Flask** - Web framework for demo app
- **Pytest** - Testing framework
- **Flake8** - Code linting

## Learning Objectives

By completing this workshop, you will be able to:

✅ Create and manage GitHub teams with proper hierarchies  
✅ Configure repository settings and branch protections  
✅ Implement automated CI/CD pipelines using GitHub Actions  
✅ Apply security best practices for GitHub organizations  
✅ Collaborate effectively using GitHub's team features  

## Support

If you encounter any issues or have questions during the workshop:
- Review the individual lab README files
- Consult with your workshop instructor
- Refer to [GitHub's official documentation](https://docs.github.com)

## License

This content is provided for educational purposes only. Please respect all applicable licenses and usage terms.

---

**Happy Learning! 🚀**

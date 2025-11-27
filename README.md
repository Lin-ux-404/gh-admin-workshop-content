# GitHub Admin Workshop Content

## Overview
This repository contains hands-on lab exercises and materials for a GitHub Administration Workshop. The content is designed to help participants learn essential GitHub administrative tasks, team management, repository configuration, and CI/CD workflows.

> **Note:** This repository is intended solely for educational and training purposes.

## Workshop Structure

This workshop consists of three progressive labs:

### Lab 1: Create Teams and Nested Teams
Learn how to organize users into teams and sub-teams for better permission management.
- Navigate to organization team settings
- Create a main team with your name
- Add team members with appropriate roles
- Create nested child teams under the main team
- Verify team hierarchy and member assignments

📁 [View Lab 1](lab_1/README.md)

### Lab 2: Team Privileges and Repository Access
Understand how to manage repository permissions through team assignments and privilege inheritance.
- Create a private repository in your organization
- Assign different permission levels to teams (Read vs Write)
- Test access controls with team members
- Learn about permission inheritance between parent and nested teams
- Understand GitHub's least privilege security model

📁 [View Lab 2](lab_2/README.md)

### Lab 3: GitHub Actions CI Workflow
Automate testing and code quality checks using GitHub Actions.
- Set up a Python CI workflow from scratch
- Configure automated linting with flake8
- Run automated tests with pytest
- Trigger workflows on push and pull requests
- Monitor workflow execution in the Actions tab

📁 [View Lab 3](lab_3/README.md)

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

## Technologies Used

- **GitHub Teams & Organizations** - Team and permission management
- **GitHub Actions** - CI/CD automation
- **Python 3.x** - Sample application language
- **Flask** - Web framework for demo app
- **Pytest** - Testing framework
- **Flake8** - Code linting

## Learning Objectives

By completing this workshop, you will be able to:

✅ Create and manage GitHub teams with nested hierarchies  
✅ Configure team-based repository permissions and access controls  
✅ Understand permission inheritance between parent and child teams  
✅ Implement automated CI workflows using GitHub Actions  
✅ Set up automated testing and linting in your repositories  
✅ Apply least privilege security principles in GitHub organizations  

## Support

If you encounter any issues or have questions during the workshop:
- Review the individual lab README files
- Consult with your workshop instructor
- Refer to [GitHub's official documentation](https://docs.github.com)

## License

This content is provided for educational purposes only. Please respect all applicable licenses and usage terms.

---

**Happy Learning! 🚀**

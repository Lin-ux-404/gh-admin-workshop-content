# Lab 2: Team Privileges and Repository Access

## Objective
Learn how to manage repository permissions through team assignments and understand privilege inheritance in GitHub organizations.

## Scenario
You will create a private repository and configure team-based access controls to demonstrate how GitHub enforces least privilege and permission inheritance between parent and nested teams.

---

## Instructions

### Step 1: Create a Repository

1. Go to **Organization** → **Repositories** → **New**
2. Name it: `[YOUR_NAME]-org`
3. Set visibility to **Private** (so only assigned teams can access)
4. Do **NOT** add everyone—permissions will come from teams
   
<img width="940" height="548" alt="image" src="https://github.com/user-attachments/assets/cbbee956-d3f9-458f-93b5-4381d031e033" />

### Step 2: Assign Permissions

1. In **Repo Settings** → **Manage Access** → **Add Teams**:
   - Add your **nested team** → Give **Write** access
   - Add your **main team** → Give **Read** access

2. **Important concept:** Nested team inherits parent permissions but can have extra privileges
   
<img width="940" height="535" alt="image" src="https://github.com/user-attachments/assets/143725b7-1681-4621-ac94-4b049cb998c1" />

### Step 3: Test Access

1. **For members only in the main team:**
   - Try pushing to the repository
   - Should **fail** (read-only access)

2. **For members in the nested team:**
   - Try pushing to the repository
   - Should **succeed** (write access)

3. **Key takeaway:** This demonstrates how GitHub enforces least privilege and permission inheritance

---

## Expected Outcome

You should understand:
- ✅ How to configure team-based repository permissions
- ✅ The difference between Read and Write access levels
- ✅ How nested teams inherit and extend parent team permissions
- ✅ GitHub's least privilege security model


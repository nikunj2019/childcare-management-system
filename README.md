# Childcare Management System 🏫👶

## 🚀 Features
- Upload & manage childcare enrollments 📂
- Find open spots based on DOB & month 📅
- AI-powered future seat availability prediction 📊
- AWS-hosted backend (FastAPI) & frontend (Next.js)

## 📂 Project Structure

📁 childcare-management-system
├── 📂 frontend (Next.js + TailwindCSS)
├── 📂 backend (FastAPI + PostgreSQL)
├── 📂 ai_model (Machine Learning)
├── 📂 deployment (AWS Deployment)
└── 📂 database (Schema & Seed Data)

## 🏗️ Deployment Steps
1. **Upload to GitHub**
2. **Deploy Frontend (AWS Amplify)**  
   ```sh
   bash deployment/frontend-deploy.sh

3. **Deploy Backend (AWS Lambda)**

    ```sh
    bash deployment/backend-deploy.sh

4. **Setup Database (AWS RDS)**

    ```sh
    psql -h your-db-instance.rds.amazonaws.com -U admin -d childcare_db -f deployment/database-setup.sql

### **📜 `database/seed_data.sql`** (Initial Test Data)  
```sql
INSERT INTO children (name, dob, enrolled, classroom) VALUES
('Alice Johnson', '2020-05-15', TRUE, 'Room A'),
('Ethan Smith', '2019-11-20', TRUE, 'Room B'),
('Sophia Davis', '2021-01-10', FALSE, NULL);
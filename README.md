
# AWS Serverless Web Application 🚀

This repository showcases a **serverless web application** built on AWS, connecting frontend, backend, and database seamlessly.  
The project demonstrates how to design and deploy a scalable, cost‑efficient, and zero‑infrastructure workflow using **API Gateway, Lambda, and DynamoDB**.

---

## 🔗 Clone & Setup
To explore or run this project locally:

# Clone the repository
git clone https://github.com/Isharohira/Lambda-API-Gateway-and-DynamoDB-AWS-Project

# Navigate into the project folder
cd Lambda-API-Gateway-and-DynamoDB-AWS-Project


```

## 🔧 Architecture


<img width="771" height="341" alt="Screenshot (445)" src="https://github.com/user-attachments/assets/0843c72b-9009-4e6f-8f02-2209048b2878" />

---

## 📈 Workflow
1. **Frontend (`contact.html`)** → User opens the form using API Gateway `/contact` URL and enters details.  
2. **API Gateway** → Receives the form submission and triggers the backend Lambda function.  
3. **Lambda (`lambda_function.py`)** → Backend logic that processes the request, saves data into DynamoDB, and returns a success page.  
4. **DynamoDB** → Stores each submission as an item securely in real time.  
5. **Success Page (`success.html`)** → Confirms to the user that their submission was successful.  

---


---


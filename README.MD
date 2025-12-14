# FastAPI AWS Operations Dashboard

Project Description

This project demonstrates a FastAPI-based AWS Operations Dashboard that allows basic cloud resource management through a simple web interface.

After deploying the application, users can access a browser-based dashboard where they can:

▶️ Start EC2 instances                                                                                                   
⏹️ Stop EC2 instances                                                                                                
📄 Vie EC2 instance details such as state, instance type, and public IP                                                 
🪣 List S3 buckets                                                                                                  
🌐 View VPCs and CIDR blocks                                                                                        
🔐 List ACM certificates                                                                                                

All operations are triggered using simple push buttons from the web UI, which internally call FastAPI REST endpoints connected to AWS using boto3.

The application does not store any AWS credentials in code or containers.
Authentication is handled using IAM roles or externally provided AWS credentials, following AWS security best practices.

A **production-style AWS Operations Dashboard** built using **FastAPI**, **Docker**, and **AWS SDK (boto3)**.  
This project provides a clean web interface to view and manage AWS resources such as **EC2, S3, VPCs, and ACM certificates**.

> Designed to demonstrate **real-world DevOps & Cloud engineering skills**, not just tutorials.

---

## Features

- 🔹 View EC2 instances (state, type, public IP)
- 🔹 Start / Stop EC2 instances from UI
- 🔹 List S3 buckets
- 🔹 List VPCs with CIDR blocks
- 🔹 View ACM certificates
- 🔹 Modern, responsive dashboard UI
- 🔹 Dockerized application
- 🔹 Uses AWS IAM best practices (no hardcoded credentials)

---

## Tech Stack

| Layer       | Technology |
|------------|------------|
| Backend    | FastAPI (Python) |
| Frontend  | HTML, Bootstrap 5, JavaScript |
| AWS SDK   | boto3 |
| Container | Docker |
| Cloud     | AWS (EC2, S3, VPC, ACM) |

---

## Project Structure

```text
.
├── main.py
├── index.html
├── Dockerfile
├── requirements.txt
├── README.md
└── docs/
    └── arch_diagram.png


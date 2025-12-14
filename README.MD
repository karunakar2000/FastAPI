# FastAPI AWS Operations Dashboard

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
└── README.md

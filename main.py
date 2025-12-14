from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
import boto3

app = FastAPI()

# Serve index.html at root
@app.get("/")
def read_index():
    return FileResponse("index.html")

# EC2 Instances Info
@app.get("/ec2")
def list_ec2_instances():
    ec2 = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2.describe_instances().get("Reservations", [])
    instances = [
        {
            "InstanceId": i["InstanceId"],
            "State": i["State"]["Name"],
            "InstanceType": i["InstanceType"],
            "PublicIpAddress": i.get("PublicIpAddress")
        }
        for r in reservations for i in r["Instances"]
    ]
    return {"instances": instances}

# EC2: Start Instance
@app.post("/ec2/start")
def start_instance(instance_id: str = Query(...)):
    ec2 = boto3.client("ec2", region_name="us-east-1")
    ec2.start_instances(InstanceIds=[instance_id])
    return {"message": f"Started instance {instance_id}"}

# EC2: Stop Instance
@app.post("/ec2/stop")
def stop_instance(instance_id: str = Query(...)):
    ec2 = boto3.client("ec2", region_name="us-east-1")
    ec2.stop_instances(InstanceIds=[instance_id])
    return {"message": f"Stopped instance {instance_id}"}

# List S3 Buckets
@app.get("/s3")
def list_s3_buckets():
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()
    return {"buckets": [b["Name"] for b in buckets.get("Buckets", [])]}

# List VPCs
@app.get("/vpcs")
def list_vpcs():
    ec2 = boto3.client("ec2", region_name="us-east-1")
    response = ec2.describe_vpcs()
    vpcs = response.get("Vpcs", [])
    return {"vpcs": [{"VpcId": vpc["VpcId"], "CidrBlock": vpc["CidrBlock"]} for vpc in vpcs]}

# List ACM Certificates
@app.get("/certs")
def list_certificates():
    acm = boto3.client("acm", region_name="us-east-1")
    certs = acm.list_certificates().get("CertificateSummaryList", [])
    return {
        "certificates": [
            {
                "DomainName": c["DomainName"],
                "CertificateArn": c["CertificateArn"]
                # Optional: Add timestamp fields here if you want
            }
            for c in certs
        ]
    }

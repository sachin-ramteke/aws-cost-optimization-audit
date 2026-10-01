import boto3

def audit_unattached_ebs(ec2_client):
    print("\n--- Checking for Unattached EBS Volumes ---")
    volumes = ec2_client.describe_volumes(
        Filters=[{'Name': 'status', 'Values': ['available']}]
    )
    unattached = volumes.get('Volumes', [])
    if not unattached:
        print("[OK] No unattached EBS volumes found.")
    else:
        for vol in unattached:
            print(f"[LEAK DETECTED] Volume ID: {vol['VolumeId']} | Size: {vol['Size']} GiB | Type: {vol['VolumeType']}")

def audit_unassociated_eips(ec2_client):
    print("\n--- Checking for Unassociated Elastic IPs ---")
    addresses = ec2_client.describe_addresses().get('Addresses', [])
    unused_ips = [ip for ip in addresses if 'InstanceId' not in ip and 'NetworkInterfaceId' not in ip]
    if not unused_ips:
        print("[OK] No unassociated Elastic IPs found.")
    else:
        for ip in unused_ips:
            print(f"[LEAK DETECTED] Elastic IP: {ip['PublicIp']} (AllocationId: {ip.get('AllocationId')})")

if __name__ == "__main__":
    region = "us-east-1"
    print(f"Starting AWS Cost Leak Audit for region: {region}...")
    ec2 = boto3.client('ec2', region_name=region)
    audit_unattached_ebs(ec2)
    audit_unassociated_eips(ec2)
    print("\nAudit completed.")
  

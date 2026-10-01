# AWS Cost Optimization & Infrastructure Audit Kit

A lightweight audit toolkit and standard operating procedure designed to eliminate recurring AWS billing waste for startups and growing businesses.

## Key Audit Areas Covered
- **Orphaned EBS Volumes:** Identifies unattached EBS storage volumes accumulating monthly charges.
- **Unassociated Elastic IPs:** Flags idle static IPs incurring hourly penalties.
- **Underutilized Compute:** Framework for evaluating EC2 Right-Sizing and Graviton migration opportunities.
- **Data Transfer & NAT Gateways:** Architecture review to eliminate unnecessary cross-AZ traffic charges.

## How to Run the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/sachin-ramteke/aws-cost-optimization-audit.git   
   cd aws-cost-optimization-audit
 2. Install dependencies:
   pip install boto3
 3. Configure AWS CLI credentials:
   aws configure
 4. Execute audit
    python audit_cost_leaks.py 
    ```
## Deliverables for Freelance Engagements
- Comprehensive AWS Cost Leak Report (PDF)
- Immediate Cleanup Strategy for zero-downtime cost reductions
- Long-term Budget Monitoring with CloudWatch & AWS Budgets alerts
  
    
    
    
   

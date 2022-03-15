import boto3


access_key = input("Please enter the Access key: ")
secret_key = input("Please enter the Secret key: ")
security_token = input("Please enter the Security token: ")
region         = input("Please enter the Region name: ")


print(" ")


client = boto3.client('autoscaling',
                               aws_access_key_id=access_key ,
                               aws_secret_access_key=secret_key, aws_session_token=security_token, region_name=region          
                               )




response = client.describe_auto_scaling_groups()


all_asg = response['AutoScalingGroups']




for item in all_asg:
        asg_name = item["AutoScalingGroupName"]
        Suspend_process = item["SuspendedProcesses"]
        if len(Suspend_process):
          print("Name of Auto scaling group:   ", asg_name)
          for value in Suspend_process:
            sus_Process = value["ProcessName"]
            sus_time        = value["SuspensionReason"]
            print("Suspended Process: ", sus_Process)
            print("Suspended time: ", sus_time)
            print(" ")
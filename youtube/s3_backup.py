import os
import shutil
import boto3
from botocore.exceptions import ClientError
from backup import create_backup, restore_backup

class AWSConfig:
    """AWS Configuration class"""
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        self.aws_access_key_id = aws_access_key_id or 'your-access-key-id'
        self.aws_secret_access_key = aws_secret_access_key or 'your-secret-access-key'
        self.region_name = region_name or 'your-region'  # e.g., 'us-east-1'
    
    def get_client(self):
        """Create and return an S3 client with the configured credentials"""
        return boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name
        )

# Global AWS configuration
aws_config = AWSConfig()

def upload_to_s3(local_file, bucket_name, s3_key=None):
    """
    Upload a file to AWS S3
    
    Args:
        local_file (str): Path to local file
        bucket_name (str): S3 bucket name
        s3_key (str): S3 object key (path in bucket). If None, uses filename
    
    Returns:
        str: Success message or error message
    """
    try:
        # Validate local file
        if not os.path.exists(local_file):
            return f"Error: Local file '{local_file}' does not exist"
        
        # Create S3 client with configured credentials
        s3_client = aws_config.get_client()
        
        # If s3_key not provided, use filename
        if s3_key is None:
            s3_key = os.path.basename(local_file)
        
        # Upload file
        print(f"Uploading {local_file} to s3://{bucket_name}/{s3_key}")
        s3_client.upload_file(local_file, bucket_name, s3_key)
        
        print("\nUpload completed successfully!")
        return f"File uploaded to s3://{bucket_name}/{s3_key}"
        
    except ClientError as e:
        return f"AWS Error: {str(e)}"
    except Exception as e:
        return f"Error uploading to S3: {str(e)}"

def download_from_s3(bucket_name, s3_key, local_file):
    """
    Download a file from AWS S3
    
    Args:
        bucket_name (str): S3 bucket name
        s3_key (str): S3 object key (path in bucket)
        local_file (str): Path where to save the file locally
    
    Returns:
        str: Success message or error message
    """
    try:
        # Create S3 client with configured credentials
        s3_client = aws_config.get_client()
        
        # Create local directory if it doesn't exist
        os.makedirs(os.path.dirname(local_file), exist_ok=True)
        
        # Download file
        print(f"Downloading s3://{bucket_name}/{s3_key} to {local_file}")
        s3_client.download_file(bucket_name, s3_key, local_file)
        
        print("\nDownload completed successfully!")
        return f"File downloaded to {local_file}"
        
    except ClientError as e:
        return f"AWS Error: {str(e)}"
    except Exception as e:
        return f"Error downloading from S3: {str(e)}"

def backup_to_s3(source_dir, bucket_name, s3_prefix=''):
    """
    Create a backup and upload it to S3
    
    Args:
        source_dir (str): Directory to backup
        bucket_name (str): S3 bucket name
        s3_prefix (str): Prefix for S3 key (like a folder path)
    
    Returns:
        str: Success message or error message
    """
    try:
        # First create local backup
        temp_backup_dir = './temp_backup'
        backup_file = create_backup(source_dir, temp_backup_dir)
        
        if isinstance(backup_file, str) and backup_file.startswith('Error'):
            return backup_file
        
        # Generate S3 key
        s3_key = os.path.join(s3_prefix, os.path.basename(backup_file))
        
        # Upload to S3
        result = upload_to_s3(backup_file, bucket_name, s3_key)
        
        # Cleanup temporary files
        shutil.rmtree(temp_backup_dir, ignore_errors=True)
        
        return result
        
    except Exception as e:
        return f"Error in backup to S3: {str(e)}"

def restore_from_s3(bucket_name, s3_key, restore_dir):
    """
    Download backup from S3 and restore it
    
    Args:
        bucket_name (str): S3 bucket name
        s3_key (str): S3 object key of the backup file
        restore_dir (str): Directory where to restore the backup
    
    Returns:
        str: Success message or error message
    """
    try:
        # Create temporary directory for download
        temp_download_dir = './temp_download'
        os.makedirs(temp_download_dir, exist_ok=True)
        
        # Download file
        local_file = os.path.join(temp_download_dir, os.path.basename(s3_key))
        download_result = download_from_s3(bucket_name, s3_key, local_file)
        
        if download_result.startswith('Error'):
            return download_result
        
        # Restore from downloaded file
        result = restore_backup(local_file, restore_dir)
        
        # Cleanup temporary files
        shutil.rmtree(temp_download_dir, ignore_errors=True)
        
        return result
        
    except Exception as e:
        return f"Error in restore from S3: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Configure AWS credentials
    aws_config = AWSConfig(
        aws_access_key_id='your-access-key-id',
        aws_secret_access_key='your-secret-access-key',
        region_name='your-region'  # e.g., 'us-east-1'
    )
    
    # AWS S3 configuration
    BUCKET_NAME = 'your-bucket-name'
    S3_PREFIX = 'backups/'  # Optional prefix/folder in bucket
    
    # Example paths
    source_directory = "./test_source"
    restore_directory = "./restored_from_s3"
    
    # Create test directory and files
    if not os.path.exists(source_directory):
        os.makedirs(source_directory)
        with open(os.path.join(source_directory, "test1.txt"), "w") as f:
            f.write("Test file 1")
    
    # Backup to S3
    s3_backup_result = backup_to_s3(source_directory, BUCKET_NAME, S3_PREFIX)
    print(f"\nS3 Backup result: {s3_backup_result}")
    
    # Restore from S3 (uncomment and modify s3_key as needed)
    # s3_key = 'backups/your-backup-file.zip'
    # s3_restore_result = restore_from_s3(BUCKET_NAME, s3_key, restore_directory)
    # print(f"\nS3 Restore result: {s3_restore_result}")
    
    # Cleanup
    shutil.rmtree(source_directory, ignore_errors=True)
    shutil.rmtree(restore_directory, ignore_errors=True) 
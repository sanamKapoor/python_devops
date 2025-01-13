import os
import zipfile
from datetime import datetime
import shutil
import boto3
from botocore.exceptions import ClientError

def create_backup(source_dir, target_dir):
    """
    Create a backup of source directory in ZIP format
    
    Args:
        source_dir (str): Path to source directory
        target_dir (str): Path to target directory where backup will be saved
    
    Returns:
        str: Path to created backup file or error message
    """
    try:
        # Validate source directory
        if not os.path.exists(source_dir):
            return f"Error: Source directory '{source_dir}' does not exist"
        
        # Create target directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Generate backup filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"backup_{os.path.basename(source_dir)}_{timestamp}.zip"
        backup_path = os.path.join(target_dir, backup_name)
        
        # Create ZIP archive
        print(f"Creating backup: {backup_path}")
        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through directory
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    # Get full file path
                    file_path = os.path.join(root, file)
                    # Get archive path (relative to source directory)
                    arcname = os.path.relpath(file_path, source_dir)
                    # Add file to ZIP
                    print(f"Adding file: {arcname}")
                    zipf.write(file_path, arcname)
        
        # Verify backup size
        backup_size = os.path.getsize(backup_path) / (1024 * 1024)  # Size in MB
        print(f"\nBackup completed successfully!")
        print(f"Location: {backup_path}")
        print(f"Size: {backup_size:.2f} MB")
        
        return backup_path
        
    except Exception as e:
        return f"Error creating backup: {str(e)}"

def restore_backup(backup_file, restore_dir):
    """
    Restore a backup from ZIP file
    
    Args:
        backup_file (str): Path to backup ZIP file
        restore_dir (str): Directory where backup should be restored
    
    Returns:
        str: Success message or error message
    """
    try:
        # Validate backup file
        if not os.path.exists(backup_file):
            return f"Error: Backup file '{backup_file}' does not exist"
        
        # Create restore directory if it doesn't exist
        os.makedirs(restore_dir, exist_ok=True)
        
        # Extract ZIP archive
        print(f"Restoring backup to: {restore_dir}")
        with zipfile.ZipFile(backup_file, 'r') as zipf:
            zipf.extractall(restore_dir)
        
        print("\nRestore completed successfully!")
        return f"Backup restored to: {restore_dir}"
        
    except Exception as e:
        return f"Error restoring backup: {str(e)}"

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
        
        # Create S3 client
        s3_client = boto3.client('s3')
        
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
        # Create S3 client
        s3_client = boto3.client('s3')
        
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
        
        if backup_file.startswith('Error'):
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
    # Example paths (modify these as needed)
    source_directory = "./test_source"
    backup_directory = "./backups"
    
    # Create test directory and files (for demonstration)
    if not os.path.exists(source_directory):
        os.makedirs(source_directory)
        with open(os.path.join(source_directory, "test1.txt"), "w") as f:
            f.write("Test file 1")
        with open(os.path.join(source_directory, "test2.txt"), "w") as f:
            f.write("Test file 2")
    
    # Create backup
    backup_file = create_backup(source_directory, backup_directory)
    print(f"\nBackup result: {backup_file}")
    
    # Restore backup (to a different directory)
    restore_directory = "./restored_backup"
    if isinstance(backup_file, str) and os.path.exists(backup_file):
        result = restore_backup(backup_file, restore_directory)
        print(f"\nRestore result: {result}")
    
    # Cleanup (comment out if you want to keep the test files)
    shutil.rmtree(source_directory, ignore_errors=True)
    shutil.rmtree(backup_directory, ignore_errors=True)
    shutil.rmtree(restore_directory, ignore_errors=True)
    
    # S3 example (uncomment and modify as needed)
    """
    # AWS S3 configuration
    BUCKET_NAME = 'your-bucket-name'
    S3_PREFIX = 'backups/'  # Optional prefix/folder in bucket
    
    # Backup to S3
    s3_backup_result = backup_to_s3(source_directory, BUCKET_NAME, S3_PREFIX)
    print(f"\nS3 Backup result: {s3_backup_result}")
    
    # Restore from S3
    s3_key = 'backups/your-backup-file.zip'  # Adjust this to your backup file
    restore_dir = './restored_from_s3'
    s3_restore_result = restore_from_s3(BUCKET_NAME, s3_key, restore_dir)
    print(f"\nS3 Restore result: {s3_restore_result}")
    
    # Cleanup restored directory
    shutil.rmtree(restore_dir, ignore_errors=True)
    """

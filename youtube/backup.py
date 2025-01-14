import os
import zipfile
from datetime import datetime
import shutil

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

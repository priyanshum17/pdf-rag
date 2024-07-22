import os
import shutil

from src.rag.core.configuration import config


def delete_all_files_in_database():
    """
    Deletes all files and directories in the src/rag/assets/database directory.
    """
    database_path = config.file_paths.database_directory
    
    if os.path.exists(database_path):
        for filename in os.listdir(database_path):
            file_path = os.path.join(database_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"The directory {database_path} does not exist.")

# Call the function to delete all files in the database directory
delete_all_files_in_database()

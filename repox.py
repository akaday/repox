import os
import zipfile
import json

def read_repository(repo_path):
    file_data = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            file_data.append({
                'path': file_path,
                'content': content
            })
    return file_data

def compress_files(file_data, output_file):
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_data:
            zipf.writestr(file['path'], file['content'])

def generate_metadata(file_data):
    metadata = []
    for file in file_data:
        metadata.append({
            'path': file['path'],
            'size': len(file['content']),
            'type': 'file'
        })
    return metadata

def create_repox(repo_path, output_file):
    file_data = read_repository(repo_path)
    compress_files(file_data, output_file + '.zip')
    metadata = generate_metadata(file_data)
    with open(output_file + '.json', 'w') as jsonf:
        json.dump(metadata, jsonf, indent=2)

if __name__ == "__main__":
    repository_path = input("Enter the repository path: ")
    output_file = input("Enter the output file name (without extension): ")
    create_repox(repository_path, output_file)
    print(f"Repox created successfully: {output_file}.zip and {output_file}.json")

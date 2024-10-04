# 📂 Download Organizer

A Python script to help you automatically organize files in your Downloads folder by categorizing them into relevant folders, such as "Videos," "Pictures," "PDFs," and more. This tool makes it easier to manage and access your downloaded files.

## ✨ Features

- 🔄 **Automatic Categorization**: Moves files into folders based on their type (e.g., videos, pictures, documents).
- ✏️ **Customizable Categories**: Easily add or modify file types and their target folders.
- 📦 **Catch-All Folder**: Files that do not match predefined categories are moved to an "others" folder.

## ⚙️ How It Works

The script scans the specified folder (by default, your Downloads folder) and moves files into corresponding subfolders based on their extensions. Common file types are grouped into categories such as:

- 🖼️ **Pictures**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- 🎥 **Videos**: `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`
- 📄 **PDFs**: `.pdf`
- 📝 **Documents**: `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`
- 🎵 **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
- 🗄️ **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`

Files that do not match any category are moved to an "others" folder.

## 🚀 Setup and Usage

### Prerequisites

- **Python 3.x** must be installed on your system.

### Running the Script

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/yourusername/download-organizer.git
   cd download-organizer

2. **Edit the File Path:**
   Open Organize.py and modify the file_path variable to point to the folder you want to organize. For example:
   ```sh
   file_path = r'C:\Users\yourusername\Downloads'

3. **Run the script:**
   ```sh
   python organize.py

The script will create subfolders in your specified directory and move the files accordingly.

## 🔧 Customization
You can easily add or modify the categories and extensions in the `categories` dictionary in `Organize.py`:
```
categories = {
    'pictures': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
    # Add more categories or modify existing ones
}
```

## 📂 Example Output
```
1. C:\Users\yourusername\Downloads\example.jpg >>> C:\Users\yourusername\Downloads\pictures_folder
2. C:\Users\yourusername\Downloads\movie.mp4 >>> C:\Users\yourusername\Downloads\videos_folder
3. C:\Users\yourusername\Downloads\document.pdf >>> C:\Users\yourusername\Downloads\pdfs_folder
```

## 📜 License
This project is licensed under the MIT License. See the [LICENSE]([https://github.com/PerseusKyogre09/](https://github.com/PerseusKyogre09/files-organize/blob/main/LICENSE) file for more details.

## Happy organizing! 🎉

### Instructions:
- Replace `yourusername` with your actual username or the appropriate file path.
- Add/Modify categories as needed in the `categories` dictionary to include other file types.

This formatted version includes emojis for visual appeal and ensures that all code is properly within code blocks.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h> // For ls command

// Function to create a file
int createFile(const char *filename) {
    FILE *file = fopen(filename, "r");
    if (file) {
        fclose(file);
        return 1; // File already exists
    }
    file = fopen(filename, "w");
    if (file) {
        fclose(file);
        return 0; // File created successfully
    }
    return -1; // Error creating file
}

// Function to delete a file
int deleteFile(const char *filename) {
    if (remove(filename) == 0) {
        return 0; // File deleted successfully
    }
    return 1; // Error deleting the file
}

// Function to copy a file
int copyFile(const char *src_filename, const char *dest_filename) {
    FILE *src = fopen(src_filename, "rb");
    if (!src) return 1; // Source file does not exist

    FILE *dest = fopen(dest_filename, "wb");
    if (!dest) {
        fclose(src);
        return 2; // Error opening destination file
    }

    char buffer[1024];
    size_t bytes;
    while ((bytes = fread(buffer, 1, sizeof(buffer), src)) > 0) {
        fwrite(buffer, 1, bytes, dest);
    }

    fclose(src);
    fclose(dest);
    return 0; // File copied successfully
}

// Function to rename (move) a file
int renameFile(const char *src_filename, const char *dest_filename) {
    if (rename(src_filename, dest_filename) == 0) {
        return 0; // File renamed (moved) successfully
    }
    return 1; // Error renaming the file
}

// Function to list files in the current directory (ls command)
int listFiles() {
    DIR *dir;
    struct dirent *entry;

    dir = opendir(".");
    if (!dir) {
        perror("Unable to open directory");
        return -1; // Error opening directory
    }

    printf("Files in the current directory:\n");
    while ((entry = readdir(dir)) != NULL) {
        // Exclude hidden files (starting with .)
        if (entry->d_name[0] != '.') {
            printf("%s\n", entry->d_name);
        }
    }

    closedir(dir);
    return 0; // Successfully listed files
}

// Function to display help information
void displayHelp() {
    printf("Available commands:\n");
    printf("1. create <filename> - Create a new file\n");
    printf("2. delete <filename> - Delete a file\n");
    printf("3. copy <src> <dest> - Copy a file\n");
    printf("4. rename <src> <dest> - Rename or move a file\n");
    printf("5. ls - List files in the current directory\n");
    printf("6. help - Display this help message\n");
}

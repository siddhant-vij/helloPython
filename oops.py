import pyttsx3
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os


# Simple Library Management System
class Library:
    num_books = 0

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Library.num_books += 1

    def get_books(self):
        return "\n".join(str(book) for book in self.books)

    def get_no_of_books(self):
        return f"{Library.num_books} books in total. The books are: \n{self.get_books()}"


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"


# library1 = Library()
# book1 = Book("War and Peace", "Leo Tolstoy", 1225)
# book2 = Book("The Catcher in the Rye", "JD Salinger", 234)
# book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1234)
# book4 = Book("The Hobbit", "J. R. R. Tolkien", 1000)
# library1.add_book(book1)
# library1.add_book(book2)
# library1.add_book(book3)
# library1.add_book(book4)
# print(library1.get_no_of_books())


# Clear the File Clutter in a Folder
class FileRenamer:
    def __init__(self, folder_path, file_extension):
        self.folder_path = folder_path
        self.file_extension = file_extension

    def rename_files(self):
        # Get the list of files in the folder
        files = os.listdir(self.folder_path)

        # Filter files with the specified extension
        filtered_files = [
            file for file in files if file.endswith(self.file_extension)]

        # Rename the filtered files
        for index, file in enumerate(filtered_files):
            # Generate the new file name
            new_file_name = f"{self.file_extension}-{index+1}{os.path.splitext(file)[1]}"

            # Construct the full file paths
            current_file_path = os.path.join(self.folder_path, file)
            new_file_path = os.path.join(self.folder_path, new_file_name)

            # Rename the file
            os.rename(current_file_path, new_file_path)


# Example usage
# folder_path = "path/to/folder"
# file_extension = input("Enter the file extension: ")

# renamer = FileRenamer(folder_path, file_extension)
# renamer.rename_files()


# Merge, compress, and split PDF files
class PDFManager:
    def __init__(self, input_folder):
        self.input_folder = input_folder
        self.merger = PdfFileMerger()
        self.writer = PdfFileWriter()

    def merge_pdfs(self, output_folder):
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".pdf"):
                filepath = os.path.join(self.input_folder, filename)
                pdf = PdfFileReader(filepath)
                self.merger.append(pdf)

        self.merger.write(f"{output_folder}/Output - merged.pdf")
        self.merger.close()

    def compress_pdf(self, output_filepath):
        for filename in os.listdir(self.input_folder):
            if filename.endswith(".pdf"):
                filepath = os.path.join(self.input_folder, filename)
                pdf = PdfFileReader(filepath)
                compressed_pdf = PdfFileWriter()

                for page_num in range(pdf.getNumPages()):
                    page = pdf.getPage(page_num)
                    page.compressContentStreams()
                    compressed_pdf.addPage(page)

                with open(output_filepath, "wb") as output_file:
                    compressed_pdf.write(output_file)

    def split_pdf(self, output_folder):
        for filename in os.listdir(self.input_folder):
            if filename.endswith("- merged.pdf"):
                filepath = os.path.join(self.input_folder, filename)
                pdf = PdfFileReader(filepath)

                for page_num in range(pdf.getNumPages()):
                    page = pdf.getPage(page_num)
                    split_pdf = PdfFileWriter()
                    split_pdf.addPage(page)

                    output_filepath = os.path.join(
                        output_folder, f"page_{page_num+1}.pdf")
                    with open(output_filepath, "wb") as output_file:
                        split_pdf.write(output_file)


# input_folder = "/path/to/input/folder"
# output_folder = "/path/to/output/folder"

# pdf_manager = PDFManager(input_folder)

# # Merge PDFs
# pdf_manager.merge_pdfs(output_folder)

# # Compress PDFs
# output_filepath = f"{output_folder}/output - compressed.pdf"
# pdf_manager.compress_pdf(output_filepath)

# # Split PDFs
# pdf_manager.split_pdf(output_folder)


# Give shoutout (voice) to a group of people
class ShoutoutProgram:
    def __init__(self, names):
        self.names = names
        self.engine = pyttsx3.init()

    def give_shoutout(self):
        for name in self.names:
            self.engine.say(f"Shoutout to {name}!")
            self.engine.runAndWait()


# names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Larry"]
# program = ShoutoutProgram(names)
# program.give_shoutout()

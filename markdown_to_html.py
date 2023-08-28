import argparse
import markdown

# Run using the following command:
# python markdown_to_html.py -ip "path\to\input\file" -op "path\to\output\file"

class MarkdownToHTMLConverter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        # Read the Markdown file
        with open(self.input_file, 'r') as file:
            markdown_content = file.read()

        # Convert Markdown to HTML
        html_content = markdown.markdown(markdown_content)

        # Save the HTML output
        with open(self.output_file, 'w') as file:
            file.write(html_content)


def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Markdown to HTML Converter')
    parser.add_argument('-ip', '--input', dest='input_file',
                        help='Path to the input Markdown file')
    parser.add_argument('-op', '--output', dest='output_file',
                        help='Path to the output HTML file')
    args = parser.parse_args()

    # Create converter instance and convert
    converter = MarkdownToHTMLConverter(args.input_file, args.output_file)
    converter.convert()


if __name__ == '__main__':
    main()

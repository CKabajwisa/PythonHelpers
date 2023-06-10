import os
import tabula
import configparser
import logging
import pandas as pd

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')
try:
    def convert_pdfs_to_csv(directory):
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                file_path = os.path.join(directory, filename)
                output_filename = os.path.splitext(filename)[0] + '.csv'
                output_filepath = os.path.join(directory, output_filename)

                #tabula.convert_into(file_path, output_filepath, output_format="csv", pages='all')

                #print(f"Converted {filename} to CSV: {output_filename}")

                tabula.convert_into(file_path, output_filepath, output_format="csv", pages='all', lattice=True,
                                    java_options="-Dfile.encoding=UTF8")

                # Replace delimiter
                df = pd.read_csv(output_filepath)
                df.to_csv(output_filepath, sep='|', index=False)

                print(f"Converted {filename} to CSV: {output_filename}")

    raise ValueError("Example error")
except Exception as e:
    # Log the error
    logging.error(str(e), exc_info=True)


def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config


def main():
    config = read_config('config.ini')

    # Accessing values from the config file
    value1 = config['Section1']['param1']

    # print(f"value1: {value1}")

    # Specify the directory containing the PDF files
    pdf_directory = value1

    # Call the conversion function
    convert_pdfs_to_csv(pdf_directory)


if __name__ == '__main__':
    main()

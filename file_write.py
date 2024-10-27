import logging

def write_to_file(content):
    try:
        with open("LogFile.txt", 'a') as f:
            f.write(content + '\n')
    except Exception as e:
        logging.error(f"Error writing to file: {e}")
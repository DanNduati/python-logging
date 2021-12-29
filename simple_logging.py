import logging

def main():
    logging.basicConfig(filename="sample.log",level=logging.INFO, format='%(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')
    logging.info("Program started")
    print("Hello Logging")
    logging.info("Done!")

if __name__ == "__main__":
    main()
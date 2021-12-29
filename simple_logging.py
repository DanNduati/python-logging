import logging

def main():

    logging.basicConfig(filename="sample.log",level=logging.INFO)
    logging.info("Program started")
    print("Hello Logging")
    logging.info("Done!")

if __name__ == "__main__":
    main()

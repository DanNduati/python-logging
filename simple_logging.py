import logging

logging.basicConfig(filename="sample.log",level=logging.INFO, format='%(name)s - %(levelname)s - %(asctime)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S')

def logvar():
    name = 'Dan'
    logging.error(f'{name} raised an error')

def main():
    
    logging.info("Running main")
    logvar()
    logging.info("Done!")

if __name__ == "__main__":
    main()
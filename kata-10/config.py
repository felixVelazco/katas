def main():
    try:
        archivo = "config.txt"
        configuration = open(archivo)
    #except FileNotFoundError as err:
    #    print("Couldn't find the "+archivo+" file!", err)
    #except IsADirectoryError as err:
    #     print("Found "+ archivo+" but it is a directory, couldn't read it", err)
    except PermissionError as err:
        print("Found "+archivo+" but you don't have the permissions to open it", err)
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()
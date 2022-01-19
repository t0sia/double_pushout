from src.gui.gui import GraphApp


if __name__ == "__main__":
    try:
        filename = input("\nGive path to input file: ")
        GraphApp(filename).run()
    except OSError:
        print("Invalid filepath")
    except ValueError:
        print("Invalid file format")

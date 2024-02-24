import argparse
from organizer import FileOrganizer

def main():
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("path", type=str, help="Directory path to organize")
    args = parser.parse_args()

    if not args.path:
        argparse.ArgumentParser().print_help()
        return
    
    organizer = FileOrganizer(args.path)
    organizer.organize()

if __name__ == "__main__":
    main()

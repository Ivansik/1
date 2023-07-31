import os
import json

NOTES_DATA_DIR = "notes_data"

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    return {"title": title, "content": content}

def save_note(note):
    filename = os.path.join(NOTES_DATA_DIR, note["title"] + ".json")
    with open(filename, "w") as file:
        json.dump(note, file)

def read_notes():
    notes = []
    for filename in os.listdir(NOTES_DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(NOTES_DATA_DIR, filename), "r") as file:
                note = json.load(file)
                notes.append(note)
    return notes

def edit_note():
    # Display the list of notes
    notes = read_notes()
    for idx, note in enumerate(notes):
        print(f"{idx + 1}. {note['title']}")

    # Ask the user to select the note to edit
    choice = int(input("Select the note to edit: ")) - 1

    # Edit the selected note
    if 0 <= choice < len(notes):
        edited_note = create_note()
        save_note(edited_note)
        print("Note edited successfully!")
    else:
        print("Invalid choice.")

def delete_note():
    # Display the list of notes
    notes = read_notes()
    for idx, note in enumerate(notes):
        print(f"{idx + 1}. {note['title']}")

    # Ask the user to select the note to delete
    choice = int(input("Select the note to delete: ")) - 1

    # Delete the selected note
    if 0 <= choice < len(notes):
        note = notes[choice]
        filename = os.path.join(NOTES_DATA_DIR, note["title"] + ".json")
        os.remove(filename)
        print("Note deleted successfully!")
    else:
        print("Invalid choice.")

def main():
    if not os.path.exists(NOTES_DATA_DIR):
        os.mkdir(NOTES_DATA_DIR)

    while True:
        print("\nMenu:")
        print("1. Create a new note")
        print("2. Read the list of notes")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            note = create_note()
            save_note(note)
            print("Note saved successfully!")
        elif choice == "2":
            notes = read_notes()
            for idx, note in enumerate(notes):
                print(f"{idx + 1}. {note['title']}: {note['content']}")
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

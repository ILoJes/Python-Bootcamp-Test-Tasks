from task3.NoteWorker import NoteWorker

myfilename = "notes.csv"

noteworker = NoteWorker(myfilename)
noteworker.print_notes_to_console()
noteworker.add_note('Zack Storm', 'Fantasy', 4)
noteworker.print_notes_to_console()
noteworker.remove_note('The Wire')
noteworker.print_notes_to_console()
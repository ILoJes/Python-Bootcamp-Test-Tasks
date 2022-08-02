import pandas


class NoteWorker:

    def __init__(self, filename, df=None):

        self.filename = filename
        self.df = None

    def read_notes(self):

        self.df = pandas.read_csv(self.filename, delimiter=';')
        # return self.df

    def add_note(self, film_name, note, rating):

        if self.df is None:
            self.read_notes()

        new_note = pandas.Series(data=[film_name, note, rating], index=self.df.columns, name=len(self.df.index))
        self.df = self.df.append(new_note)

    def remove_note(self, film_name):

        if self.df is None:
            self.read_notes()

        # del_row = self.df.query("film_name == " + film_name)
        # del_row = self.df[self.df["film_name"] == film_name]
        # print(del_row)
        # self.df.drop(del_row.index, inplace=True)
        self.df.drop(self.df[self.df["film_name"] == film_name].index, inplace=True)

    def print_notes_to_console(self):

        if self.df is None:
            self.read_notes()
        print('=============================== NOTES  ===============================')
        print(self.df)

    def get_film_with_highest_rate(self):

        if self.df is None:
            self.read_notes()

        self.df.sort_values(by='rating')

    def get_film_with_lowest_rate(self):

        pass

    def get_average_rating(self):


        pass

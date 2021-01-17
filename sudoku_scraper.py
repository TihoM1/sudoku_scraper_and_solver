"""
Program that scrapes sudoku web site and create gui for it in tkinter
"""
import os
import time

import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Text, Button, Entry, Label, messagebox, END, INSERT # pylint: disable = unused-import
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary # pylint: disable = unused-import

global NUMBER
NUMBER = 0

class WebScraper:
    """
    Class for scraping  sudoku web site
    """
    def scrape_web_site(self, web_site_url):
        """
        scrapes code
        """
        options = Options()
        driver = webdriver.Chrome(options = options)
        driver.get(web_site_url)
        driver.implicitly_wait(10)
        page = driver.page_source
        driver.quit()
        return BeautifulSoup(page, 'html.parser')
    def find_element_by_id(self, source, element, value):
        """
        finds specified element by its id
        """
        return source.find(element, id = value)
    def find_all_elements_with_a_value(self, source, element, value):
        """
        finds all elements that have a value
        """
        return source.find_all(element, value = value)
    def find_parents_id(self, element, value):
        """
        find the id of the parent of the specified element
        """
        return element.find_parent(value).get('id')

class GameBoard:
    """
    Matrix that stores values
    """
    def __init__(self):
        """
        Konstruktor
        """
        self.gameboard_matrix = [["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""],
                                ["", "", "", "", "", "", "", "", ""]]
        self.soup = WebScraper().scrape_web_site("https://nine.websudoku.com/")
        self.sudoku_table = WebScraper().find_element_by_id(self.soup, "table", "puzzle_grid" )
        self.fields_with_numbers = WebScraper().find_all_elements_with_a_value(self.sudoku_table,
        "input", True)
    def fill_matrix_with_starting_values(self):
        """
        Fills matrix with starting numbers
        """
        for i in self.fields_with_numbers:
            coordinates = WebScraper().find_parents_id(i, 'td' ).replace('c','')
            row = int(coordinates[0])
            column = int(coordinates[1])
            self.gameboard_matrix[row][column] = int(i['value'])
    def fill_text_fields_with_values(self):
        """
        Fills text fields with numbers from the matrix
        """
        text_index=0
        for row_in_matrix in range(9):
            for column_in_matrix in range(9):
                _num_to_add = self.gameboard_matrix[column_in_matrix][row_in_matrix]
                original_answer = self.gameboard_matrix[column_in_matrix][row_in_matrix]
                if _num_to_add == original_answer and _num_to_add != '' :
                    new_game_gui.texts[text_index].insert(1.0,'      \n' + '     '
                    + str(_num_to_add))
                    new_game_gui.texts[text_index].config(state = 'disabled', bg = "DodgerBlue2")
                else:
                    new_game_gui.texts[text_index].config(state = 'normal', bg = "#FFFFFF")
                text_index+=1
    def start_game(self):
        """
        Input starting numbers in matrix and text fields
        """
        self.fill_matrix_with_starting_values()
        self.fill_text_fields_with_values()

class GameBoardGui:
    """
    Class that creates, numbers for input,
    """
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku")
        self.root.resizable(False, False)
        self.root.configure(bg = "azure")
        self.texts = list(range(81))
        self.starting_time = time.time()
        _n=0
        #creating text fields
        for _rows in range(9):
            for _columns in range(9):
                self.texts[_n] = tk.Text(self.root,  width = 6, height = 3,
                    bg = "#FFFFFF", bd = 3, font='helvetica 12 bold')
                self.texts[_n].grid(row = _rows, column = _columns)
                _n+=1

        self.texts[0].bind('<Button-3>', lambda i : self.text_clicked(i=0))
        self.texts[1].bind('<Button-3>', lambda i : self.text_clicked(i=1))
        self.texts[2].bind('<Button-3>', lambda i : self.text_clicked(i=2))
        self.texts[3].bind('<Button-3>', lambda i : self.text_clicked(i=3))
        self.texts[4].bind('<Button-3>', lambda i : self.text_clicked(i=4))
        self.texts[5].bind('<Button-3>', lambda i : self.text_clicked(i=5))
        self.texts[6].bind('<Button-3>', lambda i : self.text_clicked(i=6))
        self.texts[7].bind('<Button-3>', lambda i : self.text_clicked(i=7))
        self.texts[8].bind('<Button-3>', lambda i : self.text_clicked(i=8))
        self.texts[9].bind('<Button-3>', lambda i : self.text_clicked(i=9))
        self.texts[10].bind('<Button-3>', lambda i : self.text_clicked(i=10))
        self.texts[11].bind('<Button-3>', lambda i : self.text_clicked(i=11))
        self.texts[12].bind('<Button-3>', lambda i : self.text_clicked(i=12))
        self.texts[13].bind('<Button-3>', lambda i : self.text_clicked(i=13))
        self.texts[14].bind('<Button-3>', lambda i : self.text_clicked(i=14))
        self.texts[15].bind('<Button-3>', lambda i : self.text_clicked(i=15))
        self.texts[16].bind('<Button-3>', lambda i : self.text_clicked(i=16))
        self.texts[17].bind('<Button-3>', lambda i : self.text_clicked(i=17))
        self.texts[18].bind('<Button-3>', lambda i : self.text_clicked(i=18))
        self.texts[19].bind('<Button-3>', lambda i : self.text_clicked(i=19))
        self.texts[20].bind('<Button-3>', lambda i : self.text_clicked(i=20))
        self.texts[21].bind('<Button-3>', lambda i : self.text_clicked(i=21))
        self.texts[22].bind('<Button-3>', lambda i : self.text_clicked(i=22))
        self.texts[23].bind('<Button-3>', lambda i : self.text_clicked(i=23))
        self.texts[24].bind('<Button-3>', lambda i : self.text_clicked(i=24))
        self.texts[25].bind('<Button-3>', lambda i : self.text_clicked(i=25))
        self.texts[26].bind('<Button-3>', lambda i : self.text_clicked(i=26))
        self.texts[27].bind('<Button-3>', lambda i : self.text_clicked(i=27))
        self.texts[28].bind('<Button-3>', lambda i : self.text_clicked(i=28))
        self.texts[29].bind('<Button-3>', lambda i : self.text_clicked(i=29))
        self.texts[30].bind('<Button-3>', lambda i : self.text_clicked(i=30))
        self.texts[31].bind('<Button-3>', lambda i : self.text_clicked(i=31))
        self.texts[32].bind('<Button-3>', lambda i : self.text_clicked(i=32))
        self.texts[33].bind('<Button-3>', lambda i : self.text_clicked(i=33))
        self.texts[34].bind('<Button-3>', lambda i : self.text_clicked(i=34))
        self.texts[35].bind('<Button-3>', lambda i : self.text_clicked(i=35))
        self.texts[36].bind('<Button-3>', lambda i : self.text_clicked(i=36))
        self.texts[37].bind('<Button-3>', lambda i : self.text_clicked(i=37))
        self.texts[38].bind('<Button-3>', lambda i : self.text_clicked(i=38))
        self.texts[39].bind('<Button-3>', lambda i : self.text_clicked(i=39))
        self.texts[40].bind('<Button-3>', lambda i : self.text_clicked(i=40))
        self.texts[41].bind('<Button-3>', lambda i : self.text_clicked(i=41))
        self.texts[42].bind('<Button-3>', lambda i : self.text_clicked(i=42))
        self.texts[43].bind('<Button-3>', lambda i : self.text_clicked(i=43))
        self.texts[44].bind('<Button-3>', lambda i : self.text_clicked(i=44))
        self.texts[45].bind('<Button-3>', lambda i : self.text_clicked(i=45))
        self.texts[46].bind('<Button-3>', lambda i : self.text_clicked(i=46))
        self.texts[47].bind('<Button-3>', lambda i : self.text_clicked(i=47))
        self.texts[48].bind('<Button-3>', lambda i : self.text_clicked(i=48))
        self.texts[49].bind('<Button-3>', lambda i : self.text_clicked(i=49))
        self.texts[50].bind('<Button-3>', lambda i : self.text_clicked(i=50))
        self.texts[51].bind('<Button-3>', lambda i : self.text_clicked(i=51))
        self.texts[52].bind('<Button-3>', lambda i : self.text_clicked(i=52))
        self.texts[53].bind('<Button-3>', lambda i : self.text_clicked(i=53))
        self.texts[54].bind('<Button-3>', lambda i : self.text_clicked(i=54))
        self.texts[55].bind('<Button-3>', lambda i : self.text_clicked(i=55))
        self.texts[56].bind('<Button-3>', lambda i : self.text_clicked(i=56))
        self.texts[57].bind('<Button-3>', lambda i : self.text_clicked(i=57))
        self.texts[58].bind('<Button-3>', lambda i : self.text_clicked(i=58))
        self.texts[59].bind('<Button-3>', lambda i : self.text_clicked(i=59))
        self.texts[60].bind('<Button-3>', lambda i : self.text_clicked(i=60))
        self.texts[61].bind('<Button-3>', lambda i : self.text_clicked(i=61))
        self.texts[62].bind('<Button-3>', lambda i : self.text_clicked(i=62))
        self.texts[63].bind('<Button-3>', lambda i : self.text_clicked(i=63))
        self.texts[64].bind('<Button-3>', lambda i : self.text_clicked(i=64))
        self.texts[65].bind('<Button-3>', lambda i : self.text_clicked(i=65))
        self.texts[66].bind('<Button-3>', lambda i : self.text_clicked(i=66))
        self.texts[67].bind('<Button-3>', lambda i : self.text_clicked(i=67))
        self.texts[68].bind('<Button-3>', lambda i : self.text_clicked(i=68))
        self.texts[69].bind('<Button-3>', lambda i : self.text_clicked(i=69))
        self.texts[70].bind('<Button-3>', lambda i : self.text_clicked(i=70))
        self.texts[71].bind('<Button-3>', lambda i : self.text_clicked(i=71))
        self.texts[72].bind('<Button-3>', lambda i : self.text_clicked(i=72))
        self.texts[73].bind('<Button-3>', lambda i : self.text_clicked(i=73))
        self.texts[74].bind('<Button-3>', lambda i : self.text_clicked(i=74))
        self.texts[75].bind('<Button-3>', lambda i : self.text_clicked(i=75))
        self.texts[76].bind('<Button-3>', lambda i : self.text_clicked(i=76))
        self.texts[77].bind('<Button-3>', lambda i : self.text_clicked(i=77))
        self.texts[78].bind('<Button-3>', lambda i : self.text_clicked(i=78))
        self.texts[79].bind('<Button-3>', lambda i : self.text_clicked(i=79))
        self.texts[80].bind('<Button-3>', lambda i : self.text_clicked(i=80))

        #separators
        self.separator1 = ttk.Separator(self.root, orient='horizontal').grid(
        row = 10, column = 0, columnspan = 9, pady = 8, ipadx = 275)
        self.separator2 = ttk.Separator(self.root, orient='vertical').grid(
        row = 0, column = 10, rowspan = 12, padx = 4, ipady = 320)

        #creating buttons
        self.buttons = list(range(9))
        for i in range(9):
            self.buttons[i] = tk.Button(self.root, width = 4, height = 2,
            text = str(i+1), font = 'helvetica 12 bold', bg = "cyan2",
            bd = 4)
            self.buttons[i].grid(row = i, column = 11, padx = 3 )

        self.buttons[0].config(command = lambda : self.num_clicked(1))
        self.buttons[1].config(command = lambda : self.num_clicked(2))
        self.buttons[2].config(command = lambda : self.num_clicked(3))
        self.buttons[3].config(command = lambda : self.num_clicked(4))
        self.buttons[4].config(command = lambda : self.num_clicked(5))
        self.buttons[5].config(command = lambda : self.num_clicked(6))
        self.buttons[6].config(command = lambda : self.num_clicked(7))
        self.buttons[7].config(command = lambda : self.num_clicked(8))
        self.buttons[8].config(command = lambda : self.num_clicked(9))

        self.label_name = ttk.Label(self.root, text = "Name:",
        font='helvetica 10 bold').grid(row = 11, column = 0)
        self.label_surname = ttk.Label(self.root, text = "Surname:",
        font='helvetica 10 bold').grid(row = 11, column = 2)

        self.entry1 = tk.Entry(self.root, width = 6,
        state = 'disabled')
        self.entry2 = tk.Entry(self.root, width = 6,
        state = 'disabled')
        self.entry1.grid(row=11, column = 1)
        self.entry2.grid(row=11, column = 3)

        self.button_stop_game = tk.Button(self.root, text ="Save\n Game",
        width = 5, height = 2, font = 'helvetica 11 bold',
        bg = "goldenrod1", relief = 'raised', bd = 4, command = lambda:
        self.save_game_clicked())
        self.button_stop_game.grid(row = 11, column = 4)

        self.del_button = tk.Button(self.root, width = 4, height = 2,
        text = "Del", font = 'helvetica 12 bold', bg = "gray",
        bd = 4, command = lambda: self.del_clicked())
        self.del_button.grid(row = 11, column = 11, padx = 3 )

    def num_clicked(self, button_number):
        """
        Giving value of button to text input number
        """
        global NUMBER
        NUMBER = button_number
        return NUMBER

    def text_clicked(self, i):
        """
        Input number in text field if its correct
        and not if its not
        """
        text_row = self.texts[i].grid_info()['row']
        text_column = self.texts[i].grid_info()['column']
        text_color = self.texts[i].cget("bg")
        if text_color == "DodgerBlue2":
            pass
        elif new_game_rules.check_single_row(text_row, NUMBER) and \
        new_game_rules.check_single_column(text_column, NUMBER) and \
        new_game_rules.check_3x3_block_field(text_column, text_row, NUMBER ) and \
        NUMBER != 123:
            self.texts[i].insert(1.0,'      \n' + '     '+str(NUMBER))
            self.texts[i].tag_add("center", 1.0, "end")
            self.texts[i].config(bg = 'spring green', state = 'disable')
            new_game.gameboard_matrix[text_column][text_row] = NUMBER
            new_game_rules.check_win()
        elif NUMBER == 123:
            self.texts[i].config(bg = 'white', state = 'normal')
            self.texts[i].delete(1.0, END)
            new_game.gameboard_matrix[text_column][text_row] = ''
        else:
            self.texts[i].config(bg = 'firebrick1')
            self.texts[i].delete(1.0, END)

    def save_game_clicked(self):
        """
        Saves game
        """
        new_game_rules.save_game_file()

    def del_clicked(self):
        """
        When del is clicked it changes
        input value to invalid number
        """
        global NUMBER
        NUMBER = 123
        return NUMBER


class GameLogic:
    """
    Class that starts game and checks if it is over
    """
    def check_win(self):
        """
        Check if game is over
        """
        for i in range(81):
            text_color = new_game_gui.texts[i].cget("bg")
            if text_color not in ('DodgerBlue2', 'spring green'):
                return False
        self.time_passed = self.measure_time(new_game_gui.starting_time)
        self.game_over()

    def check_single_row(self, row, value):
        """
        Checks row of text field
        """
        for column in range(9):
            comparing_value = new_game.gameboard_matrix[column][row]
            if comparing_value != '':
                if comparing_value == value:
                    return False
        return True

    def check_single_column(self,column,value):
        """
        Checks column of text field
        """
        for row in range(9):
            comparing_value=new_game.gameboard_matrix[column][row]
            if comparing_value != '':
                if comparing_value == value:
                    return False
        return True

    def check_3x3_block_field(self,column, row, value):
        """
        Checks 3x3 region of text field
        """
        for i in range(3):
            for j in range(3):
                comparing_value=new_game.gameboard_matrix[column-column%3+j][row-row%3+i]
                if comparing_value != '':
                    if comparing_value == value:
                        return False
        return True

    def game_over(self):
        """
        When game is over text fields are all green
        colored and buttons for input are disabled. Also
        two windows appear on screen.
        """
        for i in range(81):
            new_game_gui.texts[i].config(bg = 'green')
        for i in range(9):
            new_game_gui.buttons[i].config(state = 'disabled')
        new_game_gui.del_button.config(state = 'disabled')
        messagebox.showinfo("Game over", "Congratulations, you solved sudoku!")
        messagebox.showinfo("Game over", """You can input your name and surname to
        save your puzzle soulution. :)""")
        new_game_gui.entry1.config(state = 'normal')
        new_game_gui.entry2.config(state = 'normal')

    def measure_time(self, start_time):
        """
        Measures time of solving sudoku
        """
        endtime = time.time()
        game_time = endtime - start_time
        return game_time

    def save_game_file(self):
        """
        Saves players name, surname, puzzle solution,
        time and creates file with this informations.
        """
        self.player_name = new_game_gui.entry1.get()
        self.player_surname = new_game_gui.entry2.get()
        self.result_folder = "Results/"
        minutes  = self.time_passed // 60
        seconds = round(self.time_passed - self.time_passed//60*60, 2)
        str_min = str(minutes)
        str_sec = str(seconds)
        file_path = os.path.join(self.result_folder,
        f"{self.player_name}_{self.player_surname}_{minutes}_{seconds}.txt")
        result_file = open(file_path, "w")
        result_file.write("Time passed:\n   minutes: "+ str_min + "\n   seconds: " + str_sec)
        result_file.write("\nGame Solution:\n")
        for row in new_game.gameboard_matrix:
            for item in row:
                result_file.write("|" + str(item))
            result_file.write("|\n")
        result_file.close()
        new_game_gui.root.destroy()


new_game_gui = GameBoardGui()
new_game = GameBoard()
new_game_rules = GameLogic()
new_game.start_game()
new_game_gui.root.mainloop()


from typing import List, Dict, Mapping
import time
import csv
import argparse
import re

class textLoading:

    Dialog_Row = List[str]
    Choice_Row = List[str]
    Dialog_Format = List[Dialog_Row]
    storyCSVPATH = "story_fmt.csv"

    def argparser(storyCSVPATH):
        # Commandline arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('dialogcsv', type=str,
                            help='path to the dialog')

        return parser.parse_args()

    def load_csv_dialog(path_to_csv: str) -> Dialog_Format:
        # Load dialog from CSV file provided
        dialog_l = list()
        with open(path_to_csv, newline='') as csvfile:
            csv_dialog_reader = csv.reader(csvfile, skipinitialspace=True)
            for row in csv_dialog_reader:
                dialog_l.append(row)

        return dialog_l

    def select_choice_number(valid_selections: List[Choice_Row]) -> int:
        # Function to allow user to choose choices
        selection_number = None

        while True:

            print("Available choices:")
            for idx, choice in enumerate(valid_selections):
                print("{:>3}) {}".format(idx, choice))

            user_choice = input("> ")
            try:
                selection_number = int(user_choice)
                break
            except ValueError:
                print("Unknown choice number")

        return selection_number

    def look_for_result_row_str(dialog_lst: Dialog_Format, result_str: Choice_Row) -> int:
        if len(result_str) == 3:
            return 0

        return look_for_result_row(dialog_lst, int(re.search(r"RESULT(\d+)", result_str[3]).group(1)))

    def look_for_result_row(dialog_lst: Dialog_Format, result_num: int) -> int:
        line_num = 0
        for line_list in dialog_lst:
            if len(line_list) == 4:
                res = re.search(r"RESULT(\d+)", line_list[0])
                if res != None and int(res.group(1)) == result_num:
                    return line_num
            line_num += 1

        raise Exception("No corresponding result found!")

    def is_dialogue(dialog_r: Dialog_Row) -> bool:
        return len(dialog_r) == 2

    def is_choice(dialog_r: Dialog_Row) -> bool:
        row_len = len(dialog_r)
        if row_len == 3 or row_len == 4:
            return re.search(r"CHOICE(\d+)", dialog_r[0]) != None
        return False

    def is_result(dialog_r: Dialog_Row) -> bool:
        if len(dialog_r) == 4:
            return re.search(r"RESULT(\d+)", dialog_r[0]) != None
        return False

    def get_choices(dialog_lst: Dialog_Format, at_line: int) -> List[Choice_Row]:
        choices_list = list()
        while is_choice(dialog_lst[at_line]) == True:
            choices_list.append(dialog_lst[at_line])
            at_line += 1
        return choices_list

    def dialog_run():
        args = argparser()
        dialog = load_csv_dialog(args.dialogcsv)

        line_num = 0
        line_total = len(dialog)
        while line_num < line_total:

            if is_dialogue(dialog[line_num]):
                # Print dialog
                p_str = "{}: {}".format(dialog[line_num][0], dialog[line_num][1])
                print(p_str, end="")
                input() # Next line when user enters
            elif is_choice(dialog[line_num]):
                choices = get_choices(dialog, line_num)
                line_num = line_num + len(choices) - 1
                ch_num = select_choice_number(choices)
                ch_row = choices[ch_num]
                print("{}: {}".format(ch_row[1], ch_row[2]))
                at_row = look_for_result_row_str(dialog, choices[ch_num])
                if at_row > 0:
                    line_num = at_row
                    continue
            elif is_result(dialog[line_num]):
                p_str = "{}: {}".format(dialog[line_num][2], dialog[line_num][3])
                print(p_str, end="")
                input() # Next line when user enters
            else:
                return

            line_num += 1

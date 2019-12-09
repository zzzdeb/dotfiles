from output_functions import output_label, output_label_time
from click_functions import do_nothing, start_working, add_one_minute, stop


class Stage:
    def __init__(self, index, minutes, label, output, notification,
                 next_stage=None, left_click=do_nothing,
                 right_click=do_nothing):
        self.index = index
        self.minutes = minutes  # -1 = for ever
        self.label = label
        self.output = output
        self.notification = notification
        self.left_click = left_click
        self.right_click = right_click
        self.next_stage = next_stage

    def print_(self, label, remaining_time):
        print(self.output(label, remaining_time))


# this is where the real configuration happens
# define stages with all their parameters
rest_stage = Stage(2, 5, '', output_label_time, 
                   'Time to get back to work!',
                   None, add_one_minute, stop)
work_stage = Stage(1, 25, '', output_label_time, 
                   'Time to take a break!',
                   rest_stage, add_one_minute, stop)
off_stage = Stage(0, -1, '', output_label, '', work_stage, start_working)
rest_stage.next_stage = off_stage

# add these stages to this list
# the index of the stage object should match it's index in the list
# i know this isn't very elegant
STAGES = [
    off_stage,
    work_stage,
    rest_stage
]
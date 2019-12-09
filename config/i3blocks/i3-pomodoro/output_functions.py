"""output functions
take 2 arguments and return a formatted string for printing"""

def output_label_time(label, remaining_time):
    if remaining_time.seconds > 59:
        minutes = int(remaining_time.seconds / 60)
        return f'{label} {minutes}min'
    else:
        return f'{label} {remaining_time.seconds}s'

def output_label(label, remaining_time):
    return label
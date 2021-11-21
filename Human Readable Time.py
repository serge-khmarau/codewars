def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = (seconds - hours * 3600) % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

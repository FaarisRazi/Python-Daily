# Get N no. of days from (after) main_day. (or N number of days before main_day)

def days_from(main_day, N, before=False):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start_index = days_of_week.index(main_day)
    
    if before:
        print(f'\n{N} days before {main_day}:')
        days = [days_of_week[(start_index - i) % 7] for i in range(N+1)][::-1][:-1]
    else:
        print(f'\n{N} days after {main_day}:')
        days = [days_of_week[(start_index + i) % 7] for i in range(1, N + 1)]
        
    return days

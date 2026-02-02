attendance_book = {
    "Alice": True,
    "Bob": False
}

def check_attendance(name):
    # FIXME: KeyError: what if name doesn't exist?
    return attendance_book[name]

def add_student(name, list=[]): # FIXME: MutableDefaultArgument: list persists across calls
    list.append(name)
    return list

def get_student_by_index(index):
    students = ["Alice", "Bob", "Charlie"]
    try:
        return students[index]
    except IndexError:
        # idx를 벗어나면 False 반환
        return None

def mark_present(name):
    if name in attendance_book:
        attendance_book[name] = True
    # FIXME: ReturnMissing: returns None implicitly if name not found, might cause issues
    
def get_daily_tuple():
    t = ("Monday", "Tuesday")
    # FIXME: AttributeError: 'tuple' object has no attribute 'append'
    t.append("Wednesday")
    return t

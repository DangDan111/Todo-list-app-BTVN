#Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    """Thêm một công việc vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc mới: '{task_name}'")
#---Điểm bắt đầu của chương trình ---
if __name__=="__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài với Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
def list_tasks():
    if not tasks:
        print("Danh sách công việc trống!")
        return
    for i, task in enumerate(tasks, start=1):
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{i}. {status} {task['name']}")
def complete_task(task_index):
    """Đánh dấu công việc là đã hoàn thành."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"Đã hoàn thành: {tasks[task_index]['name']}")
    else:
        print("Chỉ số không hợp lệ!")
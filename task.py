from datetime import datetime


class Task:
    def __init__(self, id, text, datetime):
        self._id = id
        self.text = text
        self.datetime = datetime
        self._priority = 0
        self._cycle_remind = False
        self._cycle_value = 24  # Hours
        self._remind_before = False
        self._remind_before_value = 1
        self._active = True

    def done(self):
        self._active = False

    def is_active(self):
        return self._active


class TaskManager:
    def __init__(self):
        self._task_list = list()
        self._active_tasks = 0
        self._forgot_tasks = 0
        self._inactive_tasks = 0

    def get_new_index(self):  # [0 1 2 3 4 5 6] [0 4 6]
        curr_index_set = set([t.id for t in self._task_list])
        all_range_set = set([i for i in range(0, len(self._task_list))])
        free_index_set = all_range_set - curr_index_set
        if len(free_index_set) > 0:
            return free_index_set.pop()
        else:
            return len(self._task_list)

    def get_active_tasks(self):
        return [t for t in self._task_list if t.is_active()]

    def create_task(self, text, datetime):
        new_index = self.get_new_index()
        new_task = Task(new_index, text, datetime)
        self._task_list.append(new_task)
        self._active_tasks += 1

    def check_active_tasks(self):
        return self._active_tasks > 0

    def delete_task(self, id):
        del_task = [t for t in self._task_list if t.id == id]
        self._task_list.remove(del_task)

notebooks_dict = {}
class notebook_controller:
    def __init__(self):
        self.notebooks_dict = notebooks_dict
    def create_notebook(self):
        notebook_name = input("Enter the name of your notebook.")
        if notebook_name in self.notebooks_dict:
            print("This notebook already exists.")
        else:
            self.notebooks_dict[notebook_name] = notebook_class(notebook_name)
    def interact_with_notebook(self):

        if len(self.notebooks_dict) == 0:
            print("There is no notebook to interact with.")
        else:
            choose_notebook = input("Enter the name of the notebook you want to interact with.")
            if choose_notebook in self.notebooks_dict:
                current_notebook = self.notebooks_dict[choose_notebook]
                while True:
                    decision_tree = {
                        "add_note" : current_notebook.add_note,
                        "view_notes" : current_notebook.view_notes,
                        "delete_note" : current_notebook.delete_note
                    }
                    decision = input("What do you want to do ? " + choose_notebook)
                    if decision in decision_tree:
                        decision_tree[decision]()
                    elif decision == "exit":
                        break
                    else:
                        print("You entered a wrong command >>>" , decision)
            else:
                print("This notebook does not exist.")
    def delete_notebook(self):
        delete_notebook_name = input("Enter the name of the notebook you want to delete.")
        if delete_notebook_name in self.notebooks_dict:
            self.notebooks_dict.pop(delete_notebook_name)
        else:
            print("This notebook does not exist.")
    def view_notebooks(self):
            if len(self.notebooks_dict) == 0:
                print("There is no notebook to view.")
            else:
                print(self.notebooks_dict.keys())
controller = notebook_controller()
class notebook_class:
    def __init__(self, name):
        self.name = name
        self.local_notebook = {}
    def add_note(self):
        added_note = input("Enter your note.")
        added_note_num = len(self.local_notebook)
        self.local_notebook[added_note_num] = added_note
    def view_notes(self):
        if len(self.local_notebook) == 0:
            print("There is no note to view.")
        else:
            print(self.local_notebook)
    def delete_note(self):
        if len(self.local_notebook) == 0:
            print("There is no note to delete.")
        else:
            deleted_note = int(input("enter the number of the note you wanna delete"))
            self.local_notebook.pop(deleted_note)
            self.local_notebook_copy = self.local_notebook.copy()
            range_list = list(range(len(self.local_notebook)))
            for x , y , z in zip(range_list , self.local_notebook.values() , self.local_notebook.keys()):
                self.local_notebook_copy[x] = y
                self.local_notebook_copy.pop(z)
            self.local_notebook = self.local_notebook_copy.copy()
Notebook_decision_tree = {
    "create_notebook" : controller.create_notebook,
    "interact_with_notebook" : controller.interact_with_notebook,
    "delete_notebook" : controller.delete_notebook,
    "view_notebooks" : controller.view_notebooks
}
while True :
    choose_notebook_decision = input("What do you want to do (notebook manager) ?")
    if choose_notebook_decision in Notebook_decision_tree:
        Notebook_decision_tree[choose_notebook_decision]()
    else:
        print("This command does not exist in notebook manager >>> " , choose_notebook_decision)

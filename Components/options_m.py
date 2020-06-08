class Options():
    
    options = {
        1 : Opt.new_event(),
        2 : Opt.new_task(),
        3 : Opt.change_layoyt_calendar(),
        4 : Opt.change_layoyt_tasks()
        }
    name_options = {
        1 : 'Новое событие',
        2 : 'Новое дело',
        3 : 'Окно с календарем',
        4 : 'Окно с делами'
    }

    def new_event(self):
        pass

    def new_task(self):
        pass

    def change_layoyt_calendar(self):
        pass

    def change_layoyt_tasks(self):
        pass

    def delete_task(self):
        pass

    def update_task(self):
        pass



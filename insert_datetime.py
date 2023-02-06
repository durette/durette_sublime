import sublime, sublime_plugin, time, datetime
class insert_iso_dateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();
        for s in sel:
            self.view.replace(edit, s, datetime.date.today().strftime('%Y-%m-%d'))
class insert_six_dateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();
        for s in sel:
            self.view.replace(edit, s, datetime.date.today().strftime('%y%m%d'))

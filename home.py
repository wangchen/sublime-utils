import sublime, sublime_plugin, re

class HomeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        p = re.compile(r'[^\s]')
        regions = []
        for r in self.view.sel():
            line_region = self.view.line(r)
            line = self.view.substr(line_region)
            if len(line) == 0: continue
            m = p.search(line)
            if not m: continue
            offset = m.start()
            line_begin = line_region.begin()
            pos = line_begin + offset
            if pos == r.begin():
                pos = line_begin
            regions.append(sublime.Region(pos, pos))
        # clear & set cursors
        if len(regions) == 0: return
        self.view.sel().clear()
        for r in regions:
            self.view.sel().add(r)

# vim:fileencoding=utf-8:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import os


@requires_segment_info
class HgStatusSegment(Segment):

    def get_hg_status():
        has_modified_files = False
        has_untracked_files = False
        has_missing_files = False

        p = subprocess.Popen(['hg', 'status'], stdout=subprocess.PIPE)
        output = p.communicate()[0].decode("utf-8")

        for line in output.split('\n'):
            if line == '':
                continue
            elif line[0] == '?':
                has_untracked_files = True
            elif line[0] == '!':
                has_missing_files = True
            else:
                has_modified_files = True
        return has_modified_files, has_untracked_files, has_missing_files

    def get_hg_branch():
        branch = os.popen('hg branch 2> /dev/null').read().rstrip()
        if len(branch) == 0:
            return False
        has_modified_files, has_untracked_files, has_missing_files = self.get_hg_status()
        if has_modified_files or has_untracked_files or has_missing_files:
            extra = ''
            if has_untracked_files:
                extra += '+'
            if has_missing_files:
                extra += '!'
            branch += (' ' + extra if extra != '' else '')
        return branch

    def build_segments(self, branch):
        has_modified_files, has_untracked_files, has_missing_files = self.get_hg_status()

        if has_missing_files or has_modified_files or has_untracked_files:
            branch_group = 'hgstatus_branch_dirty'
        else:
            branch_group = 'hgstatus_branch_clean'

        segments = [
            {'contents': u'\ue0a0 %s' % branch, 'highlight_groups': [branch_group, 'hgstatus_branch', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'}
        ]

        if has_missing_files:
            segments.append({'contents': ' ✖ %d', 'highlight_groups': ['hgstatus_missing', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})
        if has_modified_files:
            segments.append({'contents': ' ✚ %d', 'highlight_groups': ['hgstatus_modified', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})
        if has_untracked_files:
            segments.append({'contents': ' … %d', 'highlight_groups': ['hgstatus_untracked', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})

        return segments

    def __call__(self, pl, segment_info):
        pl.debug('Running hgstatus %s')

        cwd = segment_info['getcwd']()

        if not cwd:
            return

        branch = self.get_hg_branch()

        if not branch:
            return

        return self.build_segments(branch)


hgstatus = with_docstring(HgStatusSegment(),
'''Return the status of a Mercurial working copy.''')

# vim:fileencoding=utf-8:noet

from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info
from subprocess import PIPE, Popen
import string


@requires_segment_info
class HgStatusSegment(Segment):

    def execute(self, pl, command):
        pl.debug('Executing command: %s' % ' '.join(command))

        proc = Popen(command, stdout=PIPE, stderr=PIPE)
        out, err = [item.decode('utf-8') for item in proc.communicate()]

        if out:
            pl.debug('Command output: %s' % out.strip(string.whitespace))
        if err:
            pl.debug('Command errors: %s' % err.strip(string.whitespace))

        return (out.splitlines(), err.splitlines())

    def get_hg_status(self, pl, cwd):
        has_modified_files = False
        has_untracked_files = False
        has_missing_files = False

        output, err = self.execute(pl, ['hg', 'status', '-R', cwd])

        if len(output) == 0:
            return has_modified_files, has_untracked_files, has_missing_files

        for line in output:
            if line == '':
                continue
            elif line[0] == '?':
                has_untracked_files = True
            elif line[0] == '!':
                has_missing_files = True
            elif line[0] == 'M':
                has_modified_files = True

        return has_modified_files, has_untracked_files, has_missing_files

    def get_hg_branch(self, pl, cwd):
        output, err = self.execute(pl, ['hg', 'branch', '-R', cwd])

        if len(output) == 0:
            return False

        branch = output[0]

        return branch

    def build_segments(self, branch, pl, cwd):
        has_modified_files, has_untracked_files, has_missing_files = self.get_hg_status(pl, cwd)

        if has_missing_files or has_modified_files or has_untracked_files:
            branch_group = 'hgstatus_branch_dirty'
        else:
            branch_group = 'hgstatus_branch_clean'

        segments = [
            {'contents': u'\ue0a0 %s' % branch, 'highlight_groups': [branch_group, 'hgstatus_branch', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'}
        ]

        if has_missing_files:
            segments.append({'contents': ' ✖', 'highlight_groups': ['hgstatus_missing', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})
        if has_modified_files:
            segments.append({'contents': ' ✚', 'highlight_groups': ['hgstatus_modified', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})
        if has_untracked_files:
            segments.append({'contents': ' …', 'highlight_groups': ['hgstatus_untracked', 'hgstatus'], 'divider_highlight_group': 'hgstatus:divider'})

        return segments

    def __call__(self, pl, segment_info):
        pl.debug('Running hgstatus...')

        cwd = segment_info['getcwd']()

        if not cwd:
            return

        branch = self.get_hg_branch(pl, cwd)

        if not branch:
            return

        return self.build_segments(branch, pl, cwd)


hgstatus = with_docstring(HgStatusSegment(), '''Return the status of a Mercurial working copy.''')

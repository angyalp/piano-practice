from PyQt5.Qt import QImage
import os
import subprocess


class SheetMusic:
    PNG_LY_OPTIONS = '''
        \\version "2.18.2"
        \paper{
            indent=0\mm
            line-width=120\mm
            oddFooterMarkup=##f
            oddHeaderMarkup=##f
            bookTitleMarkup = ##f
            scoreTitleMarkup = ##f
        }'''

    def __init__(self):
        # TODO Remove temp dir at exit.
        self.tmpDir = self._create_temp_dir()

    def _create_temp_dir(self):
        # TODO Generate a uniqe dir.
        return '/tmp'

    def _call_lilypond(self, ly_path):
        proc_ret = subprocess.run(['lilypond', '-dbackend=eps', '-dno-gs-load-fonts', '-dinclude-eps-fonts',
                                   '--png', ly_path], cwd=self.tmpDir)
        return proc_ret.returncode

    def generate_QImage(self, notes):
        ly_path = os.path.join(self.tmpDir, 'piano.ly')
        with open(ly_path, 'w') as ly_file:
            ly_file.write(SheetMusic.PNG_LY_OPTIONS)
            ly_file.write('\n{\n%s\n}' % notes)

        ret = self._call_lilypond(ly_path)
        if ret != 0:
            return None

        png_path = os.path.join(self.tmpDir, 'piano.png')
        image = QImage()
        image.load(png_path)
        return image

import verovio
from PyQt5.QtCore import QByteArray

#
# Ideas:
# Display statistics: total questions, wrong answers/correct answers
# Display note name
# Timeout for each exercise
# Configure notes, cleffs to practice
# Save statistics
#

#
# Display a note
# Wait for keypress:
# Correct: Display an inline message, wait for 2 seconds. Display next note.
# Incorrect: Display an inline message. Repeat until the correct note is pressed.
#
# Display the pressed note continuously (even if practice session is not active).
#


class SheetMusic:
    def __init__(self):
        self.svg_toolkit = verovio.toolkit()

    def generate_svg(self):
        self.svg_toolkit.loadData('''<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="http://music-encoding.org/schema/4.0.0/mei-all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="http://music-encoding.org/schema/4.0.0/mei-all.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?>
<mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="4.0.0">
    <music>
        <body>
            <mdiv>
                  <score>
                    <scoreDef xml:id="scoredef-0000000882993815">
                        <staffGrp xml:id="staffgrp-0000001378899944">
                            <staffGrp xml:id="staffgrp-0000000676578449" symbol="brace" barthru="true">
                                <staffDef xml:id="staffdef-0000001333031526" clef.shape="G" clef.line="2" key.mode="major" key.sig="2f" meter.count="4" meter.unit="4" n="1" lines="5" />
                                <staffDef xml:id="staffdef-0000001056861889" clef.shape="F" clef.line="4" key.mode="major" key.sig="2f" meter.count="4" meter.unit="4" n="2" lines="5" />
                            </staffGrp>
                        </staffGrp>
                    </scoreDef>
                    <section xml:id="section-0000000002098428">
                        <measure xml:id="measure-0000002001514163" n="1">
                            <staff xml:id="staff-0000001590902649" n="1">
                                <layer xml:id="layer-0000001301226049" n="1">
                                    <mRest xml:id="mrest-0000000876290743" />
                                </layer>
                                <layer xml:id="layer-0000000329236441" n="2">
                                    <rest xml:id="rest-0000001864398057" dur="2" ploc="e" oloc="4" />
                                    <rest xml:id="rest-0000000670972170" dur="4" ploc="c" oloc="4" />
                                    <note xml:id="note-0000001544465723" dur="4" oct="4" pname="d" stem.dir="down" />
                                </layer>
                            </staff>
                            <tempo xml:id="tempo-0000001647095430" place="above" staff="1" startid="#mrest-0000000876290743" midi.bpm="30">Adagio</tempo>
                        </measure>
                    </section>
                    </score>
            </mdiv>
        </body>
    </music>
</mei>
        ''')
        return self.svg_toolkit.renderToSvg()

    def clear(self):
        pass

    def set_question_note(self, note):
        pass

    def set_user_note(self, note):
        pass


class PracticeSession:
    def __init__(self, main_window):
        self.main_window = main_window
        self.sheet_music = SheetMusic()

    def start_session(self):
        next_note = self.generate_random_note()
        self.sheet_music.clear()
        self.sheet_music.set_question_note(next_note)
        svg_data = self.sheet_music.generate_svg()
        self.main_window.set_exercise_svg(svg_data)

    def generate_random_note(self):
        return 0

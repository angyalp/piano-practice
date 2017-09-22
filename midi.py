import time
import rtmidi
import sys


def list_ports():
    midi_in = rtmidi.RtMidiIn()
    for port in range(midi_in.getPortCount()):
        print('{} - {}'.format(port, midi_in.getPortName(port)))

        
def main(argv):
    if len(argv) != 2:
        list_ports()
        return
    port = int(argv[1])
    midi_in = rtmidi.RtMidiIn()
    midi_in.openPort(port)
    try:
        timer = time.time()
        while True:
            msg = midi_in.getMessage()

            if msg:
                print('{} {}'.format(msg, type(msg)))

                time.sleep(0.01)
    except KeyboardInterrupt:
        print('')
    finally:
        midi_in.closePort()
        del midi_in               

if __name__ == '__main__':
    main(sys.argv)

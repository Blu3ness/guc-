from os.path import exists
import subprocess

def networkDriveLetterTumbler():
    usedLetters = []
    unusedLetters = []
    for drive in range(ord('A'), ord('Z')+1):
        if exists(chr(drive) + ':') is True:
            usedLetters.append(chr(drive))
        if exists(chr(drive) + ':') is False:
            unusedLetters.append(chr(drive))
    print(unusedLetters[0])
    mapResultsDir(unusedLetters[0])

def mapResultsDir(openDriveLetter):
    print('Mapping network drive to: ' + openDriveLetter)
    subprocess.call(r'net use' + openDriveLetter + ': //jf4sapp/eredjou/results/GuC/', shell=True)
    NETWORK_SHARE = openDriveLetter + ':'

NETWORK_SHARE = ''


networkDriveLetterTumbler()
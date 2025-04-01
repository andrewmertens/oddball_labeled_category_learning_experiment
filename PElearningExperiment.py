﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on November 28, 2023, at 17:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import serial

# Create serial object for device at port 'COM4'
serialCom4 = serial.Serial(
    port='COM4',
    baudrate=9600,
    bytesize=8,
    parity='O',
    stopbits=1,
    timeout=None,
)
# Run 'Before Experiment' code from stimSize
alienH = .4
alienW = .2686

eyeSize = .11

explH = .1233
explW = .1

textH = .03
fixationH = .1



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'PElearningExperiment11-16'  # from the Builder filename that created this script
expInfo = {
    'participant (experimenter use only)': '',
    'LC (experimenter use only)': ['GH', 'HH', 'NL'],
    'LS (experimenter use only)': ['AB', 'BA'],
    'Age': '',
    'Gender': ['Female','Male','Trans male/Trans man','Trans female/Trans woman','Non-binary','Non-conforming','Prefer not to answer','Other; specify below'],
    'Specify here if you selected "Other" for gender above:': '',
    'Race/Ethnicity': ['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latino','Native Hawaiian or Pacific Islander','White','Prefer not to answer','Multiple/Other; specify below'],
    'Specify here if you selected "Other" for race/ethnicity above:': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant (experimenter use only)'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Andrew\\OneDrive - UCB-O365\\Grad School\\Research\\Dissertation\\CPlearning_experiment5\\psychopy_files_exp5\\PElearningExperiment.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# --- Initialize components for Routine "resting_instructions_1" ---
rest_instructions_close_pre = visual.TextStim(win=win, name='rest_instructions_close_pre',
    text='Before we begin, we will be measuring your brain activity when at rest. When you are ready, please sit still, close your eyes, and press the spacebar. You will hear a chime after 30 seconds letting you know when to open your eyes again.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resting_keyboard_1 = keyboard.Keyboard()

# --- Initialize components for Routine "resting_closed" ---
resting_closed_photobox_pre = visual.Rect(
    win=win, name='resting_closed_photobox_pre',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# point resting_closed_trigs_pre to device at port 'COM4' and make sure it's open
resting_closed_trigs_pre = serialCom4
resting_closed_trigs_pre.status = NOT_STARTED
if not resting_closed_trigs_pre.is_open:
    resting_closed_trigs_pre.open()

# --- Initialize components for Routine "resting_instructions_2" ---
resting_chime_1 = sound.Sound('stimuli/ding.wav', secs=2, stereo=True, hamming=True,
    name='resting_chime_1')
resting_chime_1.setVolume(1.0)
rest_instructions_open_pre = visual.TextStim(win=win, name='rest_instructions_open_pre',
    text='Now we will measure your resting activity again with your eyes open. When you are ready, please sit still and press the spacebar. Keep your eyes open and try to blink as little as possible during this 30 second recording period.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resting_keyboard_2 = keyboard.Keyboard()

# --- Initialize components for Routine "resting_open" ---
resting_open_photobox_pre = visual.Rect(
    win=win, name='resting_open_photobox_pre',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# point resting_open_trigs to device at port 'COM4' and make sure it's open
resting_open_trigs = serialCom4
resting_open_trigs.status = NOT_STARTED
if not resting_open_trigs.is_open:
    resting_open_trigs.open()

# --- Initialize components for Routine "sd_instructions1" ---
instructionSD1 = visual.TextStim(win=win, name='instructionSD1',
    text='Welcome trainee! You are about to take part in a training program to work with an extraterrestrial species. Before we begin your training, we have a simple task for you to complete. You will be presented very briefly with pairs of aliens like the ones shown here. Your task is to determine whether each pair is identical or not. If a pair is not identical, press the ‘d’ key to indicate they are different. If a pair is identical, press the ‘s’ key to indicate they are the same. Try it out with the pair shown here: press the ‘d’ key if they are different or the ‘s’ key if they are the same.',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
L_alien_body_sd_instruction1 = visual.ImageStim(
    win=win,
    name='L_alien_body_sd_instruction1', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
R_alien_body_sd_instruction1 = visual.ImageStim(
    win=win,
    name='R_alien_body_sd_instruction1', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
L_alien_eye_sd_instruction1 = visual.GratingStim(
    win=win, name='L_alien_eye_sd_instruction1',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(-.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
R_alien_eye_sd_instruction1 = visual.GratingStim(
    win=win, name='R_alien_eye_sd_instruction1',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
instructionSD_keyboard1 = keyboard.Keyboard()

# point sd_instruction_trigs_1 to device at port 'COM4' and make sure it's open
sd_instruction_trigs_1 = serialCom4
sd_instruction_trigs_1.status = NOT_STARTED
if not sd_instruction_trigs_1.is_open:
    sd_instruction_trigs_1.open()

# --- Initialize components for Routine "sd_instructions2" ---
instructionSD2 = visual.TextStim(win=win, name='instructionSD2',
    text='Good! In the task itself, pairs of aliens will be quickly flashed on the screen to the left and right of the + symbol as shown here. Keep your gaze on the location of the + symbol between the aliens when they appear. Try to be as quick and accurate as possible and do your best not to blink while the aliens are on screen. Every 4 trials there will be a break for you to blink. When you are ready, press the spacebar to begin.',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instruction_sd_fixation = visual.TextStim(win=win, name='instruction_sd_fixation',
    text='+',
    font='Open Sans',
    pos=(0, -.12), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
L_alien_body_sd_instruction2 = visual.ImageStim(
    win=win,
    name='L_alien_body_sd_instruction2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_body_sd_instruction2 = visual.ImageStim(
    win=win,
    name='R_alien_body_sd_instruction2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
L_alien_eye_sd_instruction2 = visual.GratingStim(
    win=win, name='L_alien_eye_sd_instruction2',units='height', 
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(-.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
R_alien_eye_sd_instruction2 = visual.GratingStim(
    win=win, name='R_alien_eye_sd_instruction2',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
instructionSD_keyboard2 = keyboard.Keyboard()

# point sd_instruction_trigs_2 to device at port 'COM4' and make sure it's open
sd_instruction_trigs_2 = serialCom4
sd_instruction_trigs_2.status = NOT_STARTED
if not sd_instruction_trigs_2.is_open:
    sd_instruction_trigs_2.open()

# --- Initialize components for Routine "sd_fixation" ---
sd_trial_no = visual.TextStim(win=win, name='sd_trial_no',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd_fixation_cross = visual.TextStim(win=win, name='sd_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, .08), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point sd_fix_trigs to device at port 'COM4' and make sure it's open
sd_fix_trigs = serialCom4
sd_fix_trigs.status = NOT_STARTED
if not sd_fix_trigs.is_open:
    sd_fix_trigs.open()

# --- Initialize components for Routine "same_diff" ---
sd_trial_no_2 = visual.TextStim(win=win, name='sd_trial_no_2',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
L_alien_body_sd = visual.ImageStim(
    win=win,
    name='L_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
R_alien_body_sd = visual.ImageStim(
    win=win,
    name='R_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
L_alien_eye_sd = visual.GratingStim(
    win=win, name='L_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_eye_sd = visual.GratingStim(
    win=win, name='R_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
sd_photo_box = visual.Rect(
    win=win, name='sd_photo_box',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# point sd_stim_trigs to device at port 'COM4' and make sure it's open
sd_stim_trigs = serialCom4
sd_stim_trigs.status = NOT_STARTED
if not sd_stim_trigs.is_open:
    sd_stim_trigs.open()
key_resp_sd = keyboard.Keyboard()
sd_hint = visual.TextStim(win=win, name='sd_hint',
    text="Reminder: same = 's' key; different = 'd' key",
    font='Open Sans',
    pos=(0, -.4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "sd_resp_triggers" ---

# point sd_resp_trigs to device at port 'COM4' and make sure it's open
sd_resp_trigs = serialCom4
sd_resp_trigs.status = NOT_STARTED
if not sd_resp_trigs.is_open:
    sd_resp_trigs.open()

# --- Initialize components for Routine "sd_blink" ---
sd_trial_no_3 = visual.TextStim(win=win, name='sd_trial_no_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd1_blink_text = visual.TextStim(win=win, name='sd1_blink_text',
    text='You can blink now! Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sd_blink_key = keyboard.Keyboard()

# point sd_blink_trigs to device at port 'COM4' and make sure it's open
sd_blink_trigs = serialCom4
sd_blink_trigs.status = NOT_STARTED
if not sd_blink_trigs.is_open:
    sd_blink_trigs.open()

# --- Initialize components for Routine "learning_instructions0" ---
instructionLearn0 = visual.TextStim(win=win, name='instructionLearn0',
    text='Well done! Now you are ready to begin your training to differentiate between extraterrestrial species on a newly found planet.\n\nTwo species exist on this planet: a friendly species that can be approached and a hostile species that must be avoided. Here you can see 4 different examples of aliens you might encounter. Note that differences in their eye patterns are what distinguish them from one another. \n\nIt will be your job to determine what eye patterns are representative of friendliness and and which are a sign of hostility.\nPress the spacebar to continue',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
alienBodyDemoLL = visual.ImageStim(
    win=win,
    name='alienBodyDemoLL', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.45, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeDemoLL = visual.GratingStim(
    win=win, name='alienEyeDemoLL',
    tex='sin', mask='gauss', anchor='center',
    ori=78.75, pos=(-.45, -.1), size=[eyeSize, eyeSize], sf=7.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
alienBodyDemoL = visual.ImageStim(
    win=win,
    name='alienBodyDemoL', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
alienEyeDemoL = visual.GratingStim(
    win=win, name='alienEyeDemoL',
    tex='sin', mask='gauss', anchor='center',
    ori=78.75, pos=(-.15, -.1), size=[eyeSize, eyeSize], sf=11.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
alienBodyDemoR = visual.ImageStim(
    win=win,
    name='alienBodyDemoR', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
alienEyeDemoR = visual.GratingStim(
    win=win, name='alienEyeDemoR',
    tex='sin', mask='gauss', anchor='center',
    ori=-11.25, pos=(.15, -.1), size=[eyeSize, eyeSize], sf=7.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-6.0)
alienBodyDemoRR = visual.ImageStim(
    win=win,
    name='alienBodyDemoRR', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
alienEyeDemoRR = visual.GratingStim(
    win=win, name='alienEyeDemoRR',
    tex='sin', mask='gauss', anchor='center',
    ori=-11.25, pos=(.45, -.1), size=[eyeSize, eyeSize], sf=11.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-8.0)
key_resp_learn_0 = keyboard.Keyboard()

# point learn_instruction_trigs_0 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_0 = serialCom4
learn_instruction_trigs_0.status = NOT_STARTED
if not learn_instruction_trigs_0.is_open:
    learn_instruction_trigs_0.open()

# --- Initialize components for Routine "learning_instructions1" ---
# Run 'Begin Experiment' code from conditionSetupCODE
if expInfo['LC (experimenter use only)'] == 'GH':
    friendly_label = 'havnori'
    hostile_label = 'gowachi'
    label_vol = 1
elif expInfo['LC (experimenter use only)'] == 'HH':
    friendly_label = 'gowachi'
    hostile_label = 'havnori'
    label_vol = 1
elif expInfo['LC (experimenter use only)'] == 'NL':
    friendly_label = 'no_label'
    hostile_label = 'no_label'
    label_vol = 0

if expInfo['LS (experimenter use only)'] == 'AB':
    learning_sequence1 = 'conditions/seqA.xlsx'
    learning_sequence2 = 'conditions/seqB.xlsx'
elif expInfo['LS (experimenter use only)'] == 'BA':
    learning_sequence1 = 'conditions/seqB.xlsx'
    learning_sequence2 = 'conditions/seqA.xlsx'

alienBodyDemo1 = visual.ImageStim(
    win=win,
    name='alienBodyDemo1', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeDemo1 = visual.GratingStim(
    win=win, name='alienEyeDemo1',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.45, .1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerDemo1_L = visual.ImageStim(
    win=win,
    name='explorerDemo1_L', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(.25, 0), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instructionLearn1 = visual.TextStim(win=win, name='instructionLearn1',
    text='This simulation will teach you how to determine which aliens are safe to approach and which you should avoid. Your goal will be to direct the space explorer towards friendly aliens and away from hostile ones. To practice this, press either the left arrow key to indicate that the explorer should move away or the right arrow key to indicate they should approach.',
    font='Open Sans',
    pos=(-.25, 0), height=textH, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_learn_1 = keyboard.Keyboard()

# point learn_instruction_trigs_1 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_1 = serialCom4
learn_instruction_trigs_1.status = NOT_STARTED
if not learn_instruction_trigs_1.is_open:
    learn_instruction_trigs_1.open()

# --- Initialize components for Routine "learning_instructions2" ---
alienBodyDemo1_2 = visual.ImageStim(
    win=win,
    name='alienBodyDemo1_2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
alienEyeDemo1_2 = visual.GratingStim(
    win=win, name='alienEyeDemo1_2',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.45, .1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
explorerDemo1_2_U = visual.ImageStim(
    win=win,
    name='explorerDemo1_2_U', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, .25), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
instructionLearn_2 = visual.TextStim(win=win, name='instructionLearn_2',
    text='Good! Note that the explorer can appear on one of four sides around the alien: above, below, to the left, or to the right. In the case shown here, where the explorer appears above the alien, you would press the down key to indicate that the explorer should approach it (i.e., if you think the alien is friendly) or the up key to indicate that they should give it more space (i.e., if you think the alien is hostile). To practice this, press either the up or down arrow key to continue.',
    font='Open Sans',
    pos=(-.25, 0), height=textH, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_learn_2 = keyboard.Keyboard()

# point learn_instruction_trigs_2 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_2 = serialCom4
learn_instruction_trigs_2.status = NOT_STARTED
if not learn_instruction_trigs_2.is_open:
    learn_instruction_trigs_2.open()

# --- Initialize components for Routine "learning_instructions3" ---
instructionLearn_3 = visual.TextStim(win=win, name='instructionLearn_3',
    text='We will provide you with feedback during this training so you can learn which aliens are friendly and which are hostile. When you answer correctly, you will hear a ‘boop’ sound. Press the ‘c’ key to hear it now.',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_3 = keyboard.Keyboard()

# point learn_instruction_trigs_3 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_3 = serialCom4
learn_instruction_trigs_3.status = NOT_STARTED
if not learn_instruction_trigs_3.is_open:
    learn_instruction_trigs_3.open()

# --- Initialize components for Routine "learning_instructions4" ---
correct_tone_instructions = sound.Sound('stimuli/bleep.wav', secs=.25, stereo=True, hamming=True,
    name='correct_tone_instructions')
correct_tone_instructions.setVolume(1.0)
instructionLearn4a = visual.TextStim(win=win, name='instructionLearn4a',
    text='We will provide you with feedback during this training so you can learn which aliens are friendly and which are hostile. When you answer correctly, you will hear a ‘boop’ sound. Press the ‘c’ key to hear it now.',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructionLearn4b = visual.TextStim(win=win, name='instructionLearn4b',
    text='When you answer incorrectly, you will hear a ‘buzz’ sound. Press the ‘i’ key to hear it now.',
    font='Open Sans',
    pos=(0, -.1), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_learn_4 = keyboard.Keyboard()

# point learn_instruction_trigs_4 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_4 = serialCom4
learn_instruction_trigs_4.status = NOT_STARTED
if not learn_instruction_trigs_4.is_open:
    learn_instruction_trigs_4.open()

# --- Initialize components for Routine "learning_instructions5" ---
incorrect_tone_instructions = sound.Sound('stimuli/buzz.wav', secs=.25, stereo=True, hamming=True,
    name='incorrect_tone_instructions')
incorrect_tone_instructions.setVolume(1.0)
instructionLearn5a = visual.TextStim(win=win, name='instructionLearn5a',
    text='We will provide you with feedback during this training so you can learn which aliens are friendly and which are hostile. When you answer correctly, you will hear a ‘boop’ sound. Press the ‘c’ key to hear it now.',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
instructionLearn5b = visual.TextStim(win=win, name='instructionLearn5b',
    text='When you answer incorrectly, you will hear a ‘buzz’ sound. Press the ‘i’ key to hear it now.',
    font='Open Sans',
    pos=(0, -.1), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point learn_instruction_trigs_5 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_5 = serialCom4
learn_instruction_trigs_5.status = NOT_STARTED
if not learn_instruction_trigs_5.is_open:
    learn_instruction_trigs_5.open()

# --- Initialize components for Routine "learning_label_instructions" ---
learning_label_instruction_text = visual.TextStim(win=win, name='learning_label_instruction_text',
    text='Previous explorers have given names to the two species: Gowachi and Havnori. You will hear the name of the species of each alien you view in addition to the feedback sounds. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
label_instructions_key_resp = keyboard.Keyboard()

# point learn_label_instruction_trigs to device at port 'COM4' and make sure it's open
learn_label_instruction_trigs = serialCom4
learn_label_instruction_trigs.status = NOT_STARTED
if not learn_label_instruction_trigs.is_open:
    learn_label_instruction_trigs.open()

# --- Initialize components for Routine "learning_instructions6" ---
instructionLearn6 = visual.TextStim(win=win, name='instructionLearn6',
    text='You are now ready to begin training! There will be two sessions to the training, each of which will be followed by an additional session of the task you completed previously (i.e., determining whether pairs of aliens are identical or not). The counter at the top will indicate your progress in the current session. Press the spacebar when you are prepared to start.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_6 = keyboard.Keyboard()

# point learn_instruction_trigs_6 to device at port 'COM4' and make sure it's open
learn_instruction_trigs_6 = serialCom4
learn_instruction_trigs_6.status = NOT_STARTED
if not learn_instruction_trigs_6.is_open:
    learn_instruction_trigs_6.open()

# --- Initialize components for Routine "learning_fixation" ---
learn_trialNum_1 = visual.TextStim(win=win, name='learn_trialNum_1',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fixationLearn = visual.TextStim(win=win, name='fixationLearn',
    text='+',
    font='Open Sans',
    pos=(0, .1), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point learn_fix_trigs to device at port 'COM4' and make sure it's open
learn_fix_trigs = serialCom4
learn_fix_trigs.status = NOT_STARTED
if not learn_fix_trigs.is_open:
    learn_fix_trigs.open()

# --- Initialize components for Routine "learning_presentation" ---
learn_trialNum_2 = visual.TextStim(win=win, name='learn_trialNum_2',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
alienBodyLearn = visual.ImageStim(
    win=win,
    name='alienBodyLearn', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn = visual.GratingStim(
    win=win, name='alienEyeLearn',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerLearn = visual.ImageStim(
    win=win,
    name='explorerLearn', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
learn_photo_box = visual.Rect(
    win=win, name='learn_photo_box',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
key_resp_learn = keyboard.Keyboard()

# point learn_stim_trigs to device at port 'COM4' and make sure it's open
learn_stim_trigs = serialCom4
learn_stim_trigs.status = NOT_STARTED
if not learn_stim_trigs.is_open:
    learn_stim_trigs.open()
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    units='height', pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "learning_feedback" ---
feedbackSoundLearn = sound.Sound('A', secs=.25, stereo=True, hamming=True,
    name='feedbackSoundLearn')
feedbackSoundLearn.setVolume(1.0)

# point learn_feedback_trigs to device at port 'COM4' and make sure it's open
learn_feedback_trigs = serialCom4
learn_feedback_trigs.status = NOT_STARTED
if not learn_feedback_trigs.is_open:
    learn_feedback_trigs.open()
learn_trialNum_3 = visual.TextStim(win=win, name='learn_trialNum_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
alienBodyLearn2 = visual.ImageStim(
    win=win,
    name='alienBodyLearn2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
alienEyeLearn2 = visual.GratingStim(
    win=win, name='alienEyeLearn2',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
explorerLearn2 = visual.ImageStim(
    win=win,
    name='explorerLearn2', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "learning_feedback_label" ---
trainingLabelLearn = sound.Sound('A', secs=.8, stereo=True, hamming=True,
    name='trainingLabelLearn')
trainingLabelLearn.setVolume(1.0)

# point learn_label_trigs to device at port 'COM4' and make sure it's open
learn_label_trigs = serialCom4
learn_label_trigs.status = NOT_STARTED
if not learn_label_trigs.is_open:
    learn_label_trigs.open()
learn_trialNum_4 = visual.TextStim(win=win, name='learn_trialNum_4',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
alienBodyLearn3 = visual.ImageStim(
    win=win,
    name='alienBodyLearn3', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
alienEyeLearn3 = visual.GratingStim(
    win=win, name='alienEyeLearn3',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
explorerLearn3 = visual.ImageStim(
    win=win,
    name='explorerLearn3', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "learning_blink" ---
learn_trialNum_5 = visual.TextStim(win=win, name='learn_trialNum_5',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
alienBodyLearn4 = visual.ImageStim(
    win=win,
    name='alienBodyLearn4', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn4 = visual.GratingStim(
    win=win, name='alienEyeLearn4',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerLearn4 = visual.ImageStim(
    win=win,
    name='explorerLearn4', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
learning_blink_text = visual.TextStim(win=win, name='learning_blink_text',
    text='You can blink now! Press the spacebar to continue.',
    font='Open Sans',
    units='height', pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
learning_blink_key = keyboard.Keyboard()

# point learn_blink_trigs to device at port 'COM4' and make sure it's open
learn_blink_trigs = serialCom4
learn_blink_trigs.status = NOT_STARTED
if not learn_blink_trigs.is_open:
    learn_blink_trigs.open()

# --- Initialize components for Routine "break1" ---
break1_text = visual.TextStim(win=win, name='break1_text',
    text='Time to take a break! An experimenter will be in momentarily.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break1_keys = keyboard.Keyboard()

# point break1_trigs to device at port 'COM4' and make sure it's open
break1_trigs = serialCom4
break1_trigs.status = NOT_STARTED
if not break1_trigs.is_open:
    break1_trigs.open()

# --- Initialize components for Routine "sd2_instructions" ---
sd2_instruction_text = visual.TextStim(win=win, name='sd2_instruction_text',
    text='Great work so far. Before continuing to the second half of your training, you will be determining whether pairs of aliens are identical or not as you did before. Once again, you will indicate when aliens are the same using the ‘s’ key and indicate when they are different using the ‘d’ key. Press the spacebar when you are ready to continue.',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
L_alien_body_sd2_instruction = visual.ImageStim(
    win=win,
    name='L_alien_body_sd2_instruction', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
R_alien_body_sd2_instruction = visual.ImageStim(
    win=win,
    name='R_alien_body_sd2_instruction', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
L_alien_eye_sd2_instruction = visual.GratingStim(
    win=win, name='L_alien_eye_sd2_instruction',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(-.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_eye_sd2_instruction = visual.GratingStim(
    win=win, name='R_alien_eye_sd2_instruction',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
sd2_instruction_keyboard = keyboard.Keyboard()

# point sd2_instruction_trigs to device at port 'COM4' and make sure it's open
sd2_instruction_trigs = serialCom4
sd2_instruction_trigs.status = NOT_STARTED
if not sd2_instruction_trigs.is_open:
    sd2_instruction_trigs.open()

# --- Initialize components for Routine "sd_fixation" ---
sd_trial_no = visual.TextStim(win=win, name='sd_trial_no',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd_fixation_cross = visual.TextStim(win=win, name='sd_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, .08), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point sd_fix_trigs to device at port 'COM4' and make sure it's open
sd_fix_trigs = serialCom4
sd_fix_trigs.status = NOT_STARTED
if not sd_fix_trigs.is_open:
    sd_fix_trigs.open()

# --- Initialize components for Routine "same_diff" ---
sd_trial_no_2 = visual.TextStim(win=win, name='sd_trial_no_2',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
L_alien_body_sd = visual.ImageStim(
    win=win,
    name='L_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
R_alien_body_sd = visual.ImageStim(
    win=win,
    name='R_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
L_alien_eye_sd = visual.GratingStim(
    win=win, name='L_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_eye_sd = visual.GratingStim(
    win=win, name='R_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
sd_photo_box = visual.Rect(
    win=win, name='sd_photo_box',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# point sd_stim_trigs to device at port 'COM4' and make sure it's open
sd_stim_trigs = serialCom4
sd_stim_trigs.status = NOT_STARTED
if not sd_stim_trigs.is_open:
    sd_stim_trigs.open()
key_resp_sd = keyboard.Keyboard()
sd_hint = visual.TextStim(win=win, name='sd_hint',
    text="Reminder: same = 's' key; different = 'd' key",
    font='Open Sans',
    pos=(0, -.4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "sd_resp_triggers" ---

# point sd_resp_trigs to device at port 'COM4' and make sure it's open
sd_resp_trigs = serialCom4
sd_resp_trigs.status = NOT_STARTED
if not sd_resp_trigs.is_open:
    sd_resp_trigs.open()

# --- Initialize components for Routine "sd_blink" ---
sd_trial_no_3 = visual.TextStim(win=win, name='sd_trial_no_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd1_blink_text = visual.TextStim(win=win, name='sd1_blink_text',
    text='You can blink now! Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sd_blink_key = keyboard.Keyboard()

# point sd_blink_trigs to device at port 'COM4' and make sure it's open
sd_blink_trigs = serialCom4
sd_blink_trigs.status = NOT_STARTED
if not sd_blink_trigs.is_open:
    sd_blink_trigs.open()

# --- Initialize components for Routine "break2" ---
break2_text = visual.TextStim(win=win, name='break2_text',
    text='Time to take a break! An experimenter will be in momentarily.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break2_keys = keyboard.Keyboard()

# point break2_trigs to device at port 'COM4' and make sure it's open
break2_trigs = serialCom4
break2_trigs.status = NOT_STARTED
if not break2_trigs.is_open:
    break2_trigs.open()

# --- Initialize components for Routine "learning2_instructions" ---
alienBodyDemo2 = visual.ImageStim(
    win=win,
    name='alienBodyDemo2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
alienEyeDemo2 = visual.GratingStim(
    win=win, name='alienEyeDemo2',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.45, .1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-1.0)
explorerDemo2_U = visual.ImageStim(
    win=win,
    name='explorerDemo2_U', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, .25), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
instructionLearn2 = visual.TextStim(win=win, name='instructionLearn2',
    text='You’re doing great! Now you will complete your training to distinguish between friendly and hostile aliens. As before you will use the arrow keys to direct the space explorer towards friendly aliens and away from hostile ones. Press the spacebar when you are ready to continue.',
    font='Open Sans',
    pos=(-.25, 0), height=textH, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
learning2_keyboard = keyboard.Keyboard()

# point learn2_instruction_trigs to device at port 'COM4' and make sure it's open
learn2_instruction_trigs = serialCom4
learn2_instruction_trigs.status = NOT_STARTED
if not learn2_instruction_trigs.is_open:
    learn2_instruction_trigs.open()

# --- Initialize components for Routine "learning_fixation" ---
learn_trialNum_1 = visual.TextStim(win=win, name='learn_trialNum_1',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
fixationLearn = visual.TextStim(win=win, name='fixationLearn',
    text='+',
    font='Open Sans',
    pos=(0, .1), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point learn_fix_trigs to device at port 'COM4' and make sure it's open
learn_fix_trigs = serialCom4
learn_fix_trigs.status = NOT_STARTED
if not learn_fix_trigs.is_open:
    learn_fix_trigs.open()

# --- Initialize components for Routine "learning_presentation" ---
learn_trialNum_2 = visual.TextStim(win=win, name='learn_trialNum_2',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
alienBodyLearn = visual.ImageStim(
    win=win,
    name='alienBodyLearn', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn = visual.GratingStim(
    win=win, name='alienEyeLearn',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerLearn = visual.ImageStim(
    win=win,
    name='explorerLearn', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
learn_photo_box = visual.Rect(
    win=win, name='learn_photo_box',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
key_resp_learn = keyboard.Keyboard()

# point learn_stim_trigs to device at port 'COM4' and make sure it's open
learn_stim_trigs = serialCom4
learn_stim_trigs.status = NOT_STARTED
if not learn_stim_trigs.is_open:
    learn_stim_trigs.open()
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    units='height', pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "learning_feedback" ---
feedbackSoundLearn = sound.Sound('A', secs=.25, stereo=True, hamming=True,
    name='feedbackSoundLearn')
feedbackSoundLearn.setVolume(1.0)

# point learn_feedback_trigs to device at port 'COM4' and make sure it's open
learn_feedback_trigs = serialCom4
learn_feedback_trigs.status = NOT_STARTED
if not learn_feedback_trigs.is_open:
    learn_feedback_trigs.open()
learn_trialNum_3 = visual.TextStim(win=win, name='learn_trialNum_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
alienBodyLearn2 = visual.ImageStim(
    win=win,
    name='alienBodyLearn2', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
alienEyeLearn2 = visual.GratingStim(
    win=win, name='alienEyeLearn2',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
explorerLearn2 = visual.ImageStim(
    win=win,
    name='explorerLearn2', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "learning_feedback_label" ---
trainingLabelLearn = sound.Sound('A', secs=.8, stereo=True, hamming=True,
    name='trainingLabelLearn')
trainingLabelLearn.setVolume(1.0)

# point learn_label_trigs to device at port 'COM4' and make sure it's open
learn_label_trigs = serialCom4
learn_label_trigs.status = NOT_STARTED
if not learn_label_trigs.is_open:
    learn_label_trigs.open()
learn_trialNum_4 = visual.TextStim(win=win, name='learn_trialNum_4',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
alienBodyLearn3 = visual.ImageStim(
    win=win,
    name='alienBodyLearn3', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
alienEyeLearn3 = visual.GratingStim(
    win=win, name='alienEyeLearn3',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
explorerLearn3 = visual.ImageStim(
    win=win,
    name='explorerLearn3', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)

# --- Initialize components for Routine "learning_blink" ---
learn_trialNum_5 = visual.TextStim(win=win, name='learn_trialNum_5',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
alienBodyLearn4 = visual.ImageStim(
    win=win,
    name='alienBodyLearn4', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn4 = visual.GratingStim(
    win=win, name='alienEyeLearn4',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerLearn4 = visual.ImageStim(
    win=win,
    name='explorerLearn4', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
learning_blink_text = visual.TextStim(win=win, name='learning_blink_text',
    text='You can blink now! Press the spacebar to continue.',
    font='Open Sans',
    units='height', pos=(0, -.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
learning_blink_key = keyboard.Keyboard()

# point learn_blink_trigs to device at port 'COM4' and make sure it's open
learn_blink_trigs = serialCom4
learn_blink_trigs.status = NOT_STARTED
if not learn_blink_trigs.is_open:
    learn_blink_trigs.open()

# --- Initialize components for Routine "break3" ---
break3_text = visual.TextStim(win=win, name='break3_text',
    text='Time to take a break! An experimenter will be in momentarily.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
break3_keys = keyboard.Keyboard()

# point break3_trigs to device at port 'COM4' and make sure it's open
break3_trigs = serialCom4
break3_trigs.status = NOT_STARTED
if not break3_trigs.is_open:
    break3_trigs.open()

# --- Initialize components for Routine "sd3_instructions" ---
sd3_instruction_text = visual.TextStim(win=win, name='sd3_instruction_text',
    text='Well done! Now that you have mastered your training, we will ask you to complete one final session of the alien pair task, indicating when aliens are the same using the ‘s’ key and indicating when they are different using the ‘d’ key. After that, there will just be a few final questions for you to answer and you will be done! Press the spacebar when you are ready to continue.',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
L_alien_body_sd3_instruction = visual.ImageStim(
    win=win,
    name='L_alien_body_sd3_instruction', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
R_alien_body_sd3_instruction = visual.ImageStim(
    win=win,
    name='R_alien_body_sd3_instruction', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, -.2), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
L_alien_eye_sd3_instruction = visual.GratingStim(
    win=win, name='L_alien_eye_sd3_instruction',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(-.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_eye_sd3_instruction = visual.GratingStim(
    win=win, name='R_alien_eye_sd3_instruction',
    tex='sin', mask='gauss', anchor='center',
    ori=41.0, pos=(.15, -.1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
sd3_instruction_keyboard = keyboard.Keyboard()

# point sd3_instruction_trigs to device at port 'COM4' and make sure it's open
sd3_instruction_trigs = serialCom4
sd3_instruction_trigs.status = NOT_STARTED
if not sd3_instruction_trigs.is_open:
    sd3_instruction_trigs.open()

# --- Initialize components for Routine "sd_fixation" ---
sd_trial_no = visual.TextStim(win=win, name='sd_trial_no',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd_fixation_cross = visual.TextStim(win=win, name='sd_fixation_cross',
    text='+',
    font='Open Sans',
    pos=(0, .08), height=fixationH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# point sd_fix_trigs to device at port 'COM4' and make sure it's open
sd_fix_trigs = serialCom4
sd_fix_trigs.status = NOT_STARTED
if not sd_fix_trigs.is_open:
    sd_fix_trigs.open()

# --- Initialize components for Routine "same_diff" ---
sd_trial_no_2 = visual.TextStim(win=win, name='sd_trial_no_2',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
L_alien_body_sd = visual.ImageStim(
    win=win,
    name='L_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(-.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
R_alien_body_sd = visual.ImageStim(
    win=win,
    name='R_alien_body_sd', 
    image='stimuli/alienBody5.png', mask=None, anchor='center',
    ori=0.0, pos=(.15, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
L_alien_eye_sd = visual.GratingStim(
    win=win, name='L_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(-.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
R_alien_eye_sd = visual.GratingStim(
    win=win, name='R_alien_eye_sd',
    tex='sin', mask='gauss', anchor='center',
    ori=1.0, pos=(.15, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
sd_photo_box = visual.Rect(
    win=win, name='sd_photo_box',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)

# point sd_stim_trigs to device at port 'COM4' and make sure it's open
sd_stim_trigs = serialCom4
sd_stim_trigs.status = NOT_STARTED
if not sd_stim_trigs.is_open:
    sd_stim_trigs.open()
key_resp_sd = keyboard.Keyboard()
sd_hint = visual.TextStim(win=win, name='sd_hint',
    text="Reminder: same = 's' key; different = 'd' key",
    font='Open Sans',
    pos=(0, -.4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "sd_resp_triggers" ---

# point sd_resp_trigs to device at port 'COM4' and make sure it's open
sd_resp_trigs = serialCom4
sd_resp_trigs.status = NOT_STARTED
if not sd_resp_trigs.is_open:
    sd_resp_trigs.open()

# --- Initialize components for Routine "sd_blink" ---
sd_trial_no_3 = visual.TextStim(win=win, name='sd_trial_no_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
sd1_blink_text = visual.TextStim(win=win, name='sd1_blink_text',
    text='You can blink now! Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sd_blink_key = keyboard.Keyboard()

# point sd_blink_trigs to device at port 'COM4' and make sure it's open
sd_blink_trigs = serialCom4
sd_blink_trigs.status = NOT_STARTED
if not sd_blink_trigs.is_open:
    sd_blink_trigs.open()

# --- Initialize components for Routine "resting_instructions_3" ---
rest_instructions_close_post = visual.TextStim(win=win, name='rest_instructions_close_post',
    text='That concludes the experiment! We will now measure your resting brain activity once more. When you are ready, please sit still, close your eyes, and press the spacebar. You will hear a chime after 30 seconds letting you know when to open your eyes again.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resting_keyboard_3 = keyboard.Keyboard()

# --- Initialize components for Routine "resting_closed_post" ---
resting_closed_photobox_post = visual.Rect(
    win=win, name='resting_closed_photobox_post',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# point resting_closed_trigs_post to device at port 'COM4' and make sure it's open
resting_closed_trigs_post = serialCom4
resting_closed_trigs_post.status = NOT_STARTED
if not resting_closed_trigs_post.is_open:
    resting_closed_trigs_post.open()

# --- Initialize components for Routine "resting_instructions_4" ---
resting_chime_2 = sound.Sound('stimuli/ding.wav', secs=2, stereo=True, hamming=True,
    name='resting_chime_2')
resting_chime_2.setVolume(1.0)
rest_instructions_open_post = visual.TextStim(win=win, name='rest_instructions_open_post',
    text='As before, we will now measure your resting activity with your eyes open. When you are ready, please sit still and press the spacebar. Keep your eyes open and try to blink as little as possible during this 30 second recording period.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
resting_keyboard_4 = keyboard.Keyboard()

# --- Initialize components for Routine "resting_open_post" ---
resting_open_photobox_post = visual.Rect(
    win=win, name='resting_open_photobox_post',units='norm', 
    width=(0.1, 0.4)[0], height=(0.1, 0.4)[1],
    ori=0.0, pos=(.95, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# point resting_open_trigs_post to device at port 'COM4' and make sure it's open
resting_open_trigs_post = serialCom4
resting_open_trigs_post.status = NOT_STARTED
if not resting_open_trigs_post.is_open:
    resting_open_trigs_post.open()

# --- Initialize components for Routine "exit_instructions" ---
instructionExit = visual.TextStim(win=win, name='instructionExit',
    text='Thank you so much for your hard work today. In the next and final section, questions about your experience today will appear at the top of the screen on each page. Please type your answer to each question and press the Enter (or Return) key to go to the next page. There are a total of 4 questions to answer. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_exit_1 = keyboard.Keyboard()

# point exit_instruction_trigs to device at port 'COM4' and make sure it's open
exit_instruction_trigs = serialCom4
exit_instruction_trigs.status = NOT_STARTED
if not exit_instruction_trigs.is_open:
    exit_instruction_trigs.open()

# --- Initialize components for Routine "exit_questionnaire" ---
exitQ_number = visual.TextStim(win=win, name='exitQ_number',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
exitQuestion = visual.TextStim(win=win, name='exitQuestion',
    text='',
    font='Open Sans',
    pos=(0, .3), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
exitResponse = visual.TextBox2(
     win, text=None, placeholder='Type here...', font='Open Sans',
     pos=(0, 0),     letterHeight=textH,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0, speechPoint=None,
     padding=0.0, alignment='center',
     anchor='center', overflow='visible',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='exitResponse',
     depth=-3, autoLog=True,
)
exitContinueText = visual.TextStim(win=win, name='exitContinueText',
    text='Press the Enter key to continue',
    font='Open Sans',
    pos=(0, -.4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_exit_2 = keyboard.Keyboard()

# point exit_question_trigs to device at port 'COM4' and make sure it's open
exit_question_trigs = serialCom4
exit_question_trigs.status = NOT_STARTED
if not exit_question_trigs.is_open:
    exit_question_trigs.open()

# --- Initialize components for Routine "experiment_end" ---
end_chime = sound.Sound('stimuli/ding.wav', secs=2, stereo=True, hamming=True,
    name='end_chime')
end_chime.setVolume(1.0)
thank_you = visual.TextStim(win=win, name='thank_you',
    text='You are done! An experimenter will be in momentarily to remove the cap. Thank you for your time!',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "resting_instructions_1" ---
continueRoutine = True
# update component parameters for each repeat
resting_keyboard_1.keys = []
resting_keyboard_1.rt = []
_resting_keyboard_1_allKeys = []
# keep track of which components have finished
resting_instructions_1Components = [rest_instructions_close_pre, resting_keyboard_1]
for thisComponent in resting_instructions_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_instructions_1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_instructions_close_pre* updates
    
    # if rest_instructions_close_pre is starting this frame...
    if rest_instructions_close_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_close_pre.frameNStart = frameN  # exact frame index
        rest_instructions_close_pre.tStart = t  # local t and not account for scr refresh
        rest_instructions_close_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_close_pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_instructions_close_pre.started')
        # update status
        rest_instructions_close_pre.status = STARTED
        rest_instructions_close_pre.setAutoDraw(True)
    
    # if rest_instructions_close_pre is active this frame...
    if rest_instructions_close_pre.status == STARTED:
        # update params
        pass
    
    # *resting_keyboard_1* updates
    waitOnFlip = False
    
    # if resting_keyboard_1 is starting this frame...
    if resting_keyboard_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_keyboard_1.frameNStart = frameN  # exact frame index
        resting_keyboard_1.tStart = t  # local t and not account for scr refresh
        resting_keyboard_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_keyboard_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_keyboard_1.started')
        # update status
        resting_keyboard_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resting_keyboard_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resting_keyboard_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resting_keyboard_1.status == STARTED and not waitOnFlip:
        theseKeys = resting_keyboard_1.getKeys(keyList=['space'], waitRelease=False)
        _resting_keyboard_1_allKeys.extend(theseKeys)
        if len(_resting_keyboard_1_allKeys):
            resting_keyboard_1.keys = _resting_keyboard_1_allKeys[-1].name  # just the last key pressed
            resting_keyboard_1.rt = _resting_keyboard_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_instructions_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_instructions_1" ---
for thisComponent in resting_instructions_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resting_keyboard_1.keys in ['', [], None]:  # No response was made
    resting_keyboard_1.keys = None
thisExp.addData('resting_keyboard_1.keys',resting_keyboard_1.keys)
if resting_keyboard_1.keys != None:  # we had a response
    thisExp.addData('resting_keyboard_1.rt', resting_keyboard_1.rt)
thisExp.nextEntry()
# the Routine "resting_instructions_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_closed" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
resting_closedComponents = [resting_closed_photobox_pre, resting_closed_trigs_pre]
for thisComponent in resting_closedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_closed" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_closed_photobox_pre* updates
    
    # if resting_closed_photobox_pre is starting this frame...
    if resting_closed_photobox_pre.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        resting_closed_photobox_pre.frameNStart = frameN  # exact frame index
        resting_closed_photobox_pre.tStart = t  # local t and not account for scr refresh
        resting_closed_photobox_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_closed_photobox_pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_closed_photobox_pre.started')
        # update status
        resting_closed_photobox_pre.status = STARTED
        resting_closed_photobox_pre.setAutoDraw(True)
    
    # if resting_closed_photobox_pre is active this frame...
    if resting_closed_photobox_pre.status == STARTED:
        # update params
        pass
    
    # if resting_closed_photobox_pre is stopping this frame...
    if resting_closed_photobox_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_closed_photobox_pre.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            resting_closed_photobox_pre.tStop = t  # not accounting for scr refresh
            resting_closed_photobox_pre.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_closed_photobox_pre.stopped')
            # update status
            resting_closed_photobox_pre.status = FINISHED
            resting_closed_photobox_pre.setAutoDraw(False)
    
    # if resting_closed_trigs_pre is starting this frame...
    if resting_closed_trigs_pre.status == NOT_STARTED and resting_closed_photobox_pre.status == STARTED:
        # keep track of start time/frame for later
        resting_closed_trigs_pre.frameNStart = frameN  # exact frame index
        resting_closed_trigs_pre.tStart = t  # local t and not account for scr refresh
        resting_closed_trigs_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_closed_trigs_pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_closed_trigs_pre.started')
        # update status
        resting_closed_trigs_pre.status = STARTED
        win.callOnFlip(resting_closed_trigs_pre.write, bytes(chr(1), 'utf8'))
        resting_closed_trigs_pre.status = STARTED
    
    # if resting_closed_trigs_pre is stopping this frame...
    if resting_closed_trigs_pre.status == STARTED:
        if bool(resting_closed_photobox_pre.status == FINISHED):
            # keep track of stop time/frame for later
            resting_closed_trigs_pre.tStop = t  # not accounting for scr refresh
            resting_closed_trigs_pre.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_closed_trigs_pre.stopped')
            # update status
            resting_closed_trigs_pre.status = FINISHED
            win.callOnFlip(resting_closed_trigs_pre.write, bytes(chr(2), 'utf8'))
            resting_closed_trigs_pre.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_closedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_closed" ---
for thisComponent in resting_closedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "resting_closed" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_instructions_2" ---
continueRoutine = True
# update component parameters for each repeat
resting_chime_1.setSound('stimuli/ding.wav', secs=2, hamming=True)
resting_chime_1.setVolume(1.0, log=False)
resting_keyboard_2.keys = []
resting_keyboard_2.rt = []
_resting_keyboard_2_allKeys = []
# keep track of which components have finished
resting_instructions_2Components = [resting_chime_1, rest_instructions_open_pre, resting_keyboard_2]
for thisComponent in resting_instructions_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_instructions_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop resting_chime_1
    
    # if resting_chime_1 is starting this frame...
    if resting_chime_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_chime_1.frameNStart = frameN  # exact frame index
        resting_chime_1.tStart = t  # local t and not account for scr refresh
        resting_chime_1.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('resting_chime_1.started', tThisFlipGlobal)
        # update status
        resting_chime_1.status = STARTED
        resting_chime_1.play(when=win)  # sync with win flip
    
    # if resting_chime_1 is stopping this frame...
    if resting_chime_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_chime_1.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            resting_chime_1.tStop = t  # not accounting for scr refresh
            resting_chime_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_chime_1.stopped')
            # update status
            resting_chime_1.status = FINISHED
            resting_chime_1.stop()
    
    # *rest_instructions_open_pre* updates
    
    # if rest_instructions_open_pre is starting this frame...
    if rest_instructions_open_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_open_pre.frameNStart = frameN  # exact frame index
        rest_instructions_open_pre.tStart = t  # local t and not account for scr refresh
        rest_instructions_open_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_open_pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_instructions_open_pre.started')
        # update status
        rest_instructions_open_pre.status = STARTED
        rest_instructions_open_pre.setAutoDraw(True)
    
    # if rest_instructions_open_pre is active this frame...
    if rest_instructions_open_pre.status == STARTED:
        # update params
        pass
    
    # *resting_keyboard_2* updates
    waitOnFlip = False
    
    # if resting_keyboard_2 is starting this frame...
    if resting_keyboard_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_keyboard_2.frameNStart = frameN  # exact frame index
        resting_keyboard_2.tStart = t  # local t and not account for scr refresh
        resting_keyboard_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_keyboard_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_keyboard_2.started')
        # update status
        resting_keyboard_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resting_keyboard_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resting_keyboard_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resting_keyboard_2.status == STARTED and not waitOnFlip:
        theseKeys = resting_keyboard_2.getKeys(keyList=['space'], waitRelease=False)
        _resting_keyboard_2_allKeys.extend(theseKeys)
        if len(_resting_keyboard_2_allKeys):
            resting_keyboard_2.keys = _resting_keyboard_2_allKeys[-1].name  # just the last key pressed
            resting_keyboard_2.rt = _resting_keyboard_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_instructions_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_instructions_2" ---
for thisComponent in resting_instructions_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
resting_chime_1.stop()  # ensure sound has stopped at end of routine
# check responses
if resting_keyboard_2.keys in ['', [], None]:  # No response was made
    resting_keyboard_2.keys = None
thisExp.addData('resting_keyboard_2.keys',resting_keyboard_2.keys)
if resting_keyboard_2.keys != None:  # we had a response
    thisExp.addData('resting_keyboard_2.rt', resting_keyboard_2.rt)
thisExp.nextEntry()
# the Routine "resting_instructions_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_open" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
resting_openComponents = [resting_open_photobox_pre, resting_open_trigs]
for thisComponent in resting_openComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_open" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_open_photobox_pre* updates
    
    # if resting_open_photobox_pre is starting this frame...
    if resting_open_photobox_pre.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        resting_open_photobox_pre.frameNStart = frameN  # exact frame index
        resting_open_photobox_pre.tStart = t  # local t and not account for scr refresh
        resting_open_photobox_pre.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_open_photobox_pre, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_open_photobox_pre.started')
        # update status
        resting_open_photobox_pre.status = STARTED
        resting_open_photobox_pre.setAutoDraw(True)
    
    # if resting_open_photobox_pre is active this frame...
    if resting_open_photobox_pre.status == STARTED:
        # update params
        pass
    
    # if resting_open_photobox_pre is stopping this frame...
    if resting_open_photobox_pre.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_open_photobox_pre.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            resting_open_photobox_pre.tStop = t  # not accounting for scr refresh
            resting_open_photobox_pre.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_open_photobox_pre.stopped')
            # update status
            resting_open_photobox_pre.status = FINISHED
            resting_open_photobox_pre.setAutoDraw(False)
    
    # if resting_open_trigs is starting this frame...
    if resting_open_trigs.status == NOT_STARTED and resting_open_photobox_pre.status == STARTED:
        # keep track of start time/frame for later
        resting_open_trigs.frameNStart = frameN  # exact frame index
        resting_open_trigs.tStart = t  # local t and not account for scr refresh
        resting_open_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_open_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_open_trigs.started')
        # update status
        resting_open_trigs.status = STARTED
        win.callOnFlip(resting_open_trigs.write, bytes(chr(3), 'utf8'))
        resting_open_trigs.status = STARTED
    
    # if resting_open_trigs is stopping this frame...
    if resting_open_trigs.status == STARTED:
        if bool(resting_open_photobox_pre.status == FINISHED):
            # keep track of stop time/frame for later
            resting_open_trigs.tStop = t  # not accounting for scr refresh
            resting_open_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_open_trigs.stopped')
            # update status
            resting_open_trigs.status = FINISHED
            win.callOnFlip(resting_open_trigs.write, bytes(chr(4), 'utf8'))
            resting_open_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_openComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_open" ---
for thisComponent in resting_openComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "resting_open" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "sd_instructions1" ---
continueRoutine = True
# update component parameters for each repeat
instructionSD_keyboard1.keys = []
instructionSD_keyboard1.rt = []
_instructionSD_keyboard1_allKeys = []
# keep track of which components have finished
sd_instructions1Components = [instructionSD1, L_alien_body_sd_instruction1, R_alien_body_sd_instruction1, L_alien_eye_sd_instruction1, R_alien_eye_sd_instruction1, instructionSD_keyboard1, sd_instruction_trigs_1]
for thisComponent in sd_instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "sd_instructions1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionSD1* updates
    
    # if instructionSD1 is starting this frame...
    if instructionSD1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionSD1.frameNStart = frameN  # exact frame index
        instructionSD1.tStart = t  # local t and not account for scr refresh
        instructionSD1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionSD1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionSD1.started')
        # update status
        instructionSD1.status = STARTED
        instructionSD1.setAutoDraw(True)
    
    # if instructionSD1 is active this frame...
    if instructionSD1.status == STARTED:
        # update params
        pass
    
    # *L_alien_body_sd_instruction1* updates
    
    # if L_alien_body_sd_instruction1 is starting this frame...
    if L_alien_body_sd_instruction1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_body_sd_instruction1.frameNStart = frameN  # exact frame index
        L_alien_body_sd_instruction1.tStart = t  # local t and not account for scr refresh
        L_alien_body_sd_instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_body_sd_instruction1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_body_sd_instruction1.started')
        # update status
        L_alien_body_sd_instruction1.status = STARTED
        L_alien_body_sd_instruction1.setAutoDraw(True)
    
    # if L_alien_body_sd_instruction1 is active this frame...
    if L_alien_body_sd_instruction1.status == STARTED:
        # update params
        pass
    
    # *R_alien_body_sd_instruction1* updates
    
    # if R_alien_body_sd_instruction1 is starting this frame...
    if R_alien_body_sd_instruction1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_body_sd_instruction1.frameNStart = frameN  # exact frame index
        R_alien_body_sd_instruction1.tStart = t  # local t and not account for scr refresh
        R_alien_body_sd_instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_body_sd_instruction1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_body_sd_instruction1.started')
        # update status
        R_alien_body_sd_instruction1.status = STARTED
        R_alien_body_sd_instruction1.setAutoDraw(True)
    
    # if R_alien_body_sd_instruction1 is active this frame...
    if R_alien_body_sd_instruction1.status == STARTED:
        # update params
        pass
    
    # *L_alien_eye_sd_instruction1* updates
    
    # if L_alien_eye_sd_instruction1 is starting this frame...
    if L_alien_eye_sd_instruction1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_eye_sd_instruction1.frameNStart = frameN  # exact frame index
        L_alien_eye_sd_instruction1.tStart = t  # local t and not account for scr refresh
        L_alien_eye_sd_instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_eye_sd_instruction1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_eye_sd_instruction1.started')
        # update status
        L_alien_eye_sd_instruction1.status = STARTED
        L_alien_eye_sd_instruction1.setAutoDraw(True)
    
    # if L_alien_eye_sd_instruction1 is active this frame...
    if L_alien_eye_sd_instruction1.status == STARTED:
        # update params
        pass
    
    # *R_alien_eye_sd_instruction1* updates
    
    # if R_alien_eye_sd_instruction1 is starting this frame...
    if R_alien_eye_sd_instruction1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_eye_sd_instruction1.frameNStart = frameN  # exact frame index
        R_alien_eye_sd_instruction1.tStart = t  # local t and not account for scr refresh
        R_alien_eye_sd_instruction1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_eye_sd_instruction1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_eye_sd_instruction1.started')
        # update status
        R_alien_eye_sd_instruction1.status = STARTED
        R_alien_eye_sd_instruction1.setAutoDraw(True)
    
    # if R_alien_eye_sd_instruction1 is active this frame...
    if R_alien_eye_sd_instruction1.status == STARTED:
        # update params
        pass
    
    # *instructionSD_keyboard1* updates
    waitOnFlip = False
    
    # if instructionSD_keyboard1 is starting this frame...
    if instructionSD_keyboard1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionSD_keyboard1.frameNStart = frameN  # exact frame index
        instructionSD_keyboard1.tStart = t  # local t and not account for scr refresh
        instructionSD_keyboard1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionSD_keyboard1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionSD_keyboard1.started')
        # update status
        instructionSD_keyboard1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructionSD_keyboard1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructionSD_keyboard1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructionSD_keyboard1.status == STARTED and not waitOnFlip:
        theseKeys = instructionSD_keyboard1.getKeys(keyList=['s'], waitRelease=False)
        _instructionSD_keyboard1_allKeys.extend(theseKeys)
        if len(_instructionSD_keyboard1_allKeys):
            instructionSD_keyboard1.keys = _instructionSD_keyboard1_allKeys[-1].name  # just the last key pressed
            instructionSD_keyboard1.rt = _instructionSD_keyboard1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if sd_instruction_trigs_1 is starting this frame...
    if sd_instruction_trigs_1.status == NOT_STARTED and instructionSD1.status == STARTED:
        # keep track of start time/frame for later
        sd_instruction_trigs_1.frameNStart = frameN  # exact frame index
        sd_instruction_trigs_1.tStart = t  # local t and not account for scr refresh
        sd_instruction_trigs_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd_instruction_trigs_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd_instruction_trigs_1.started')
        # update status
        sd_instruction_trigs_1.status = STARTED
        win.callOnFlip(sd_instruction_trigs_1.write, bytes(chr(5), 'utf8'))
        sd_instruction_trigs_1.status = STARTED
    
    # if sd_instruction_trigs_1 is stopping this frame...
    if sd_instruction_trigs_1.status == STARTED:
        if bool(len(_instructionSD_keyboard1_allKeys)):
            # keep track of stop time/frame for later
            sd_instruction_trigs_1.tStop = t  # not accounting for scr refresh
            sd_instruction_trigs_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_instruction_trigs_1.stopped')
            # update status
            sd_instruction_trigs_1.status = FINISHED
            win.callOnFlip(sd_instruction_trigs_1.write, bytes(chr(6), 'utf8'))
            sd_instruction_trigs_1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sd_instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "sd_instructions1" ---
for thisComponent in sd_instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instructionSD_keyboard1.keys in ['', [], None]:  # No response was made
    instructionSD_keyboard1.keys = None
thisExp.addData('instructionSD_keyboard1.keys',instructionSD_keyboard1.keys)
if instructionSD_keyboard1.keys != None:  # we had a response
    thisExp.addData('instructionSD_keyboard1.rt', instructionSD_keyboard1.rt)
thisExp.nextEntry()
# the Routine "sd_instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "sd_instructions2" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from sd_instruction_code
#use version 22.1.2
opacClock = core.Clock()
instructionSD_keyboard2.keys = []
instructionSD_keyboard2.rt = []
_instructionSD_keyboard2_allKeys = []
# keep track of which components have finished
sd_instructions2Components = [instructionSD2, instruction_sd_fixation, L_alien_body_sd_instruction2, R_alien_body_sd_instruction2, L_alien_eye_sd_instruction2, R_alien_eye_sd_instruction2, instructionSD_keyboard2, sd_instruction_trigs_2]
for thisComponent in sd_instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "sd_instructions2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from sd_instruction_code
    if opacClock.getTime() <= 0.2:
       SDop = 1
    elif opacClock.getTime() <= 1: #after 0.5 seconds
       SDop = 0
    if opacClock.getTime() >= 1:
        opacClock.reset()
    
    # *instructionSD2* updates
    
    # if instructionSD2 is starting this frame...
    if instructionSD2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionSD2.frameNStart = frameN  # exact frame index
        instructionSD2.tStart = t  # local t and not account for scr refresh
        instructionSD2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionSD2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionSD2.started')
        # update status
        instructionSD2.status = STARTED
        instructionSD2.setAutoDraw(True)
    
    # if instructionSD2 is active this frame...
    if instructionSD2.status == STARTED:
        # update params
        pass
    
    # *instruction_sd_fixation* updates
    
    # if instruction_sd_fixation is starting this frame...
    if instruction_sd_fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_sd_fixation.frameNStart = frameN  # exact frame index
        instruction_sd_fixation.tStart = t  # local t and not account for scr refresh
        instruction_sd_fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_sd_fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_sd_fixation.started')
        # update status
        instruction_sd_fixation.status = STARTED
        instruction_sd_fixation.setAutoDraw(True)
    
    # if instruction_sd_fixation is active this frame...
    if instruction_sd_fixation.status == STARTED:
        # update params
        pass
    
    # *L_alien_body_sd_instruction2* updates
    
    # if L_alien_body_sd_instruction2 is starting this frame...
    if L_alien_body_sd_instruction2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_body_sd_instruction2.frameNStart = frameN  # exact frame index
        L_alien_body_sd_instruction2.tStart = t  # local t and not account for scr refresh
        L_alien_body_sd_instruction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_body_sd_instruction2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_body_sd_instruction2.started')
        # update status
        L_alien_body_sd_instruction2.status = STARTED
        L_alien_body_sd_instruction2.setAutoDraw(True)
    
    # if L_alien_body_sd_instruction2 is active this frame...
    if L_alien_body_sd_instruction2.status == STARTED:
        # update params
        L_alien_body_sd_instruction2.setOpacity(SDop, log=False)
    
    # *R_alien_body_sd_instruction2* updates
    
    # if R_alien_body_sd_instruction2 is starting this frame...
    if R_alien_body_sd_instruction2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_body_sd_instruction2.frameNStart = frameN  # exact frame index
        R_alien_body_sd_instruction2.tStart = t  # local t and not account for scr refresh
        R_alien_body_sd_instruction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_body_sd_instruction2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_body_sd_instruction2.started')
        # update status
        R_alien_body_sd_instruction2.status = STARTED
        R_alien_body_sd_instruction2.setAutoDraw(True)
    
    # if R_alien_body_sd_instruction2 is active this frame...
    if R_alien_body_sd_instruction2.status == STARTED:
        # update params
        R_alien_body_sd_instruction2.setOpacity(SDop, log=False)
    
    # *L_alien_eye_sd_instruction2* updates
    
    # if L_alien_eye_sd_instruction2 is starting this frame...
    if L_alien_eye_sd_instruction2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_eye_sd_instruction2.frameNStart = frameN  # exact frame index
        L_alien_eye_sd_instruction2.tStart = t  # local t and not account for scr refresh
        L_alien_eye_sd_instruction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_eye_sd_instruction2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_eye_sd_instruction2.started')
        # update status
        L_alien_eye_sd_instruction2.status = STARTED
        L_alien_eye_sd_instruction2.setAutoDraw(True)
    
    # if L_alien_eye_sd_instruction2 is active this frame...
    if L_alien_eye_sd_instruction2.status == STARTED:
        # update params
        L_alien_eye_sd_instruction2.setOpacity(SDop, log=False)
    
    # *R_alien_eye_sd_instruction2* updates
    
    # if R_alien_eye_sd_instruction2 is starting this frame...
    if R_alien_eye_sd_instruction2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_eye_sd_instruction2.frameNStart = frameN  # exact frame index
        R_alien_eye_sd_instruction2.tStart = t  # local t and not account for scr refresh
        R_alien_eye_sd_instruction2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_eye_sd_instruction2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_eye_sd_instruction2.started')
        # update status
        R_alien_eye_sd_instruction2.status = STARTED
        R_alien_eye_sd_instruction2.setAutoDraw(True)
    
    # if R_alien_eye_sd_instruction2 is active this frame...
    if R_alien_eye_sd_instruction2.status == STARTED:
        # update params
        R_alien_eye_sd_instruction2.setOpacity(SDop, log=False)
    
    # *instructionSD_keyboard2* updates
    waitOnFlip = False
    
    # if instructionSD_keyboard2 is starting this frame...
    if instructionSD_keyboard2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        instructionSD_keyboard2.frameNStart = frameN  # exact frame index
        instructionSD_keyboard2.tStart = t  # local t and not account for scr refresh
        instructionSD_keyboard2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionSD_keyboard2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionSD_keyboard2.started')
        # update status
        instructionSD_keyboard2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instructionSD_keyboard2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instructionSD_keyboard2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instructionSD_keyboard2.status == STARTED and not waitOnFlip:
        theseKeys = instructionSD_keyboard2.getKeys(keyList=['space'], waitRelease=False)
        _instructionSD_keyboard2_allKeys.extend(theseKeys)
        if len(_instructionSD_keyboard2_allKeys):
            instructionSD_keyboard2.keys = _instructionSD_keyboard2_allKeys[-1].name  # just the last key pressed
            instructionSD_keyboard2.rt = _instructionSD_keyboard2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if sd_instruction_trigs_2 is starting this frame...
    if sd_instruction_trigs_2.status == NOT_STARTED and instructionSD2.status == STARTED:
        # keep track of start time/frame for later
        sd_instruction_trigs_2.frameNStart = frameN  # exact frame index
        sd_instruction_trigs_2.tStart = t  # local t and not account for scr refresh
        sd_instruction_trigs_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd_instruction_trigs_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd_instruction_trigs_2.started')
        # update status
        sd_instruction_trigs_2.status = STARTED
        win.callOnFlip(sd_instruction_trigs_2.write, bytes(chr(5), 'utf8'))
        sd_instruction_trigs_2.status = STARTED
    
    # if sd_instruction_trigs_2 is stopping this frame...
    if sd_instruction_trigs_2.status == STARTED:
        if bool(len(_instructionSD_keyboard2_allKeys)):
            # keep track of stop time/frame for later
            sd_instruction_trigs_2.tStop = t  # not accounting for scr refresh
            sd_instruction_trigs_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_instruction_trigs_2.stopped')
            # update status
            sd_instruction_trigs_2.status = FINISHED
            win.callOnFlip(sd_instruction_trigs_2.write, bytes(chr(6), 'utf8'))
            sd_instruction_trigs_2.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sd_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "sd_instructions2" ---
for thisComponent in sd_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# Run 'End Routine' code from sd_instruction_code
sd_blink_counter = 0
# check responses
if instructionSD_keyboard2.keys in ['', [], None]:  # No response was made
    instructionSD_keyboard2.keys = None
thisExp.addData('instructionSD_keyboard2.keys',instructionSD_keyboard2.keys)
if instructionSD_keyboard2.keys != None:  # we had a response
    thisExp.addData('instructionSD_keyboard2.rt', instructionSD_keyboard2.rt)
thisExp.nextEntry()
# the Routine "sd_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sd1_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/sd.xlsx'),
    seed=None, name='sd1_loop')
thisExp.addLoop(sd1_loop)  # add the loop to the experiment
thisSd1_loop = sd1_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSd1_loop.rgb)
if thisSd1_loop != None:
    for paramName in thisSd1_loop:
        exec('{} = thisSd1_loop[paramName]'.format(paramName))

for thisSd1_loop in sd1_loop:
    currentLoop = sd1_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSd1_loop.rgb)
    if thisSd1_loop != None:
        for paramName in thisSd1_loop:
            exec('{} = thisSd1_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "sd_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_trial_no_code
    sd_trial_nums = 'Progress: ' + str(currentLoop.thisN + 1) + ' of ' + str(currentLoop.nTotal)
    
    sd_trial_no.setText(sd_trial_nums)
    # keep track of which components have finished
    sd_fixationComponents = [sd_trial_no, sd_fixation_cross, sd_fix_trigs]
    for thisComponent in sd_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no* updates
        
        # if sd_trial_no is starting this frame...
        if sd_trial_no.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_trial_no.frameNStart = frameN  # exact frame index
            sd_trial_no.tStart = t  # local t and not account for scr refresh
            sd_trial_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no.started')
            # update status
            sd_trial_no.status = STARTED
            sd_trial_no.setAutoDraw(True)
        
        # if sd_trial_no is active this frame...
        if sd_trial_no.status == STARTED:
            # update params
            pass
        
        # if sd_trial_no is stopping this frame...
        if sd_trial_no.status == STARTED:
            if frameN >= (sd_trial_no.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_trial_no.tStop = t  # not accounting for scr refresh
                sd_trial_no.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_trial_no.stopped')
                # update status
                sd_trial_no.status = FINISHED
                sd_trial_no.setAutoDraw(False)
        
        # *sd_fixation_cross* updates
        
        # if sd_fixation_cross is starting this frame...
        if sd_fixation_cross.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_fixation_cross.frameNStart = frameN  # exact frame index
            sd_fixation_cross.tStart = t  # local t and not account for scr refresh
            sd_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fixation_cross.started')
            # update status
            sd_fixation_cross.status = STARTED
            sd_fixation_cross.setAutoDraw(True)
        
        # if sd_fixation_cross is active this frame...
        if sd_fixation_cross.status == STARTED:
            # update params
            pass
        
        # if sd_fixation_cross is stopping this frame...
        if sd_fixation_cross.status == STARTED:
            if frameN >= (sd_fixation_cross.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_fixation_cross.tStop = t  # not accounting for scr refresh
                sd_fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fixation_cross.stopped')
                # update status
                sd_fixation_cross.status = FINISHED
                sd_fixation_cross.setAutoDraw(False)
        
        # if sd_fix_trigs is starting this frame...
        if sd_fix_trigs.status == NOT_STARTED and sd_fixation_cross.status == STARTED:
            # keep track of start time/frame for later
            sd_fix_trigs.frameNStart = frameN  # exact frame index
            sd_fix_trigs.tStart = t  # local t and not account for scr refresh
            sd_fix_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fix_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fix_trigs.started')
            # update status
            sd_fix_trigs.status = STARTED
            win.callOnFlip(sd_fix_trigs.write, bytes(chr(177), 'utf8'))
            sd_fix_trigs.status = STARTED
        
        # if sd_fix_trigs is stopping this frame...
        if sd_fix_trigs.status == STARTED:
            if bool(sd_fixation_cross.status == FINISHED):
                # keep track of stop time/frame for later
                sd_fix_trigs.tStop = t  # not accounting for scr refresh
                sd_fix_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fix_trigs.stopped')
                # update status
                sd_fix_trigs.status = FINISHED
                win.callOnFlip(sd_fix_trigs.write, bytes(chr(178), 'utf8'))
                sd_fix_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_fixation" ---
    for thisComponent in sd_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "sd_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "same_diff" ---
    continueRoutine = True
    # update component parameters for each repeat
    sd_trial_no_2.setText(sd_trial_nums)
    L_alien_eye_sd.setOri(sd_L_eye_ori)
    L_alien_eye_sd.setSF(sd_L_eye_sf)
    R_alien_eye_sd.setOri(sd_R_eye_ori)
    R_alien_eye_sd.setSF(sd_R_eye_sf)
    key_resp_sd.keys = []
    key_resp_sd.rt = []
    _key_resp_sd_allKeys = []
    # keep track of which components have finished
    same_diffComponents = [sd_trial_no_2, L_alien_body_sd, R_alien_body_sd, L_alien_eye_sd, R_alien_eye_sd, sd_photo_box, sd_stim_trigs, key_resp_sd, sd_hint]
    for thisComponent in same_diffComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "same_diff" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_2* updates
        
        # if sd_trial_no_2 is starting this frame...
        if sd_trial_no_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_2.frameNStart = frameN  # exact frame index
            sd_trial_no_2.tStart = t  # local t and not account for scr refresh
            sd_trial_no_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_2.started')
            # update status
            sd_trial_no_2.status = STARTED
            sd_trial_no_2.setAutoDraw(True)
        
        # if sd_trial_no_2 is active this frame...
        if sd_trial_no_2.status == STARTED:
            # update params
            pass
        
        # *L_alien_body_sd* updates
        
        # if L_alien_body_sd is starting this frame...
        if L_alien_body_sd.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            L_alien_body_sd.frameNStart = frameN  # exact frame index
            L_alien_body_sd.tStart = t  # local t and not account for scr refresh
            L_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_body_sd.started')
            # update status
            L_alien_body_sd.status = STARTED
            L_alien_body_sd.setAutoDraw(True)
        
        # if L_alien_body_sd is active this frame...
        if L_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_body_sd is stopping this frame...
        if L_alien_body_sd.status == STARTED:
            if frameN >= (L_alien_body_sd.frameNStart + 12):
                # keep track of stop time/frame for later
                L_alien_body_sd.tStop = t  # not accounting for scr refresh
                L_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_body_sd.stopped')
                # update status
                L_alien_body_sd.status = FINISHED
                L_alien_body_sd.setAutoDraw(False)
        
        # *R_alien_body_sd* updates
        
        # if R_alien_body_sd is starting this frame...
        if R_alien_body_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_body_sd.frameNStart = frameN  # exact frame index
            R_alien_body_sd.tStart = t  # local t and not account for scr refresh
            R_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_body_sd.started')
            # update status
            R_alien_body_sd.status = STARTED
            R_alien_body_sd.setAutoDraw(True)
        
        # if R_alien_body_sd is active this frame...
        if R_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_body_sd is stopping this frame...
        if R_alien_body_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_body_sd.tStop = t  # not accounting for scr refresh
                R_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_body_sd.stopped')
                # update status
                R_alien_body_sd.status = FINISHED
                R_alien_body_sd.setAutoDraw(False)
        
        # *L_alien_eye_sd* updates
        
        # if L_alien_eye_sd is starting this frame...
        if L_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            L_alien_eye_sd.frameNStart = frameN  # exact frame index
            L_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            L_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_eye_sd.started')
            # update status
            L_alien_eye_sd.status = STARTED
            L_alien_eye_sd.setAutoDraw(True)
        
        # if L_alien_eye_sd is active this frame...
        if L_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_eye_sd is stopping this frame...
        if L_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                L_alien_eye_sd.tStop = t  # not accounting for scr refresh
                L_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_eye_sd.stopped')
                # update status
                L_alien_eye_sd.status = FINISHED
                L_alien_eye_sd.setAutoDraw(False)
        
        # *R_alien_eye_sd* updates
        
        # if R_alien_eye_sd is starting this frame...
        if R_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_eye_sd.frameNStart = frameN  # exact frame index
            R_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            R_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_eye_sd.started')
            # update status
            R_alien_eye_sd.status = STARTED
            R_alien_eye_sd.setAutoDraw(True)
        
        # if R_alien_eye_sd is active this frame...
        if R_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_eye_sd is stopping this frame...
        if R_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_eye_sd.tStop = t  # not accounting for scr refresh
                R_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_eye_sd.stopped')
                # update status
                R_alien_eye_sd.status = FINISHED
                R_alien_eye_sd.setAutoDraw(False)
        
        # *sd_photo_box* updates
        
        # if sd_photo_box is starting this frame...
        if sd_photo_box.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_photo_box.frameNStart = frameN  # exact frame index
            sd_photo_box.tStart = t  # local t and not account for scr refresh
            sd_photo_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_photo_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_photo_box.started')
            # update status
            sd_photo_box.status = STARTED
            sd_photo_box.setAutoDraw(True)
        
        # if sd_photo_box is active this frame...
        if sd_photo_box.status == STARTED:
            # update params
            pass
        
        # if sd_photo_box is stopping this frame...
        if sd_photo_box.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_photo_box.tStop = t  # not accounting for scr refresh
                sd_photo_box.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_photo_box.stopped')
                # update status
                sd_photo_box.status = FINISHED
                sd_photo_box.setAutoDraw(False)
        
        # if sd_stim_trigs is starting this frame...
        if sd_stim_trigs.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_stim_trigs.frameNStart = frameN  # exact frame index
            sd_stim_trigs.tStart = t  # local t and not account for scr refresh
            sd_stim_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_stim_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_stim_trigs.started')
            # update status
            sd_stim_trigs.status = STARTED
            win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_ontrig), 'utf8'))
            sd_stim_trigs.status = STARTED
        
        # if sd_stim_trigs is stopping this frame...
        if sd_stim_trigs.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_stim_trigs.tStop = t  # not accounting for scr refresh
                sd_stim_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_stim_trigs.stopped')
                # update status
                sd_stim_trigs.status = FINISHED
                win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_offtrig), 'utf8'))
                sd_stim_trigs.status = FINISHED
        
        # *key_resp_sd* updates
        waitOnFlip = False
        
        # if key_resp_sd is starting this frame...
        if key_resp_sd.status == NOT_STARTED and L_alien_body_sd.status == FINISHED:
            # keep track of start time/frame for later
            key_resp_sd.frameNStart = frameN  # exact frame index
            key_resp_sd.tStart = t  # local t and not account for scr refresh
            key_resp_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_sd.started')
            # update status
            key_resp_sd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_sd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_sd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_sd.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_sd.getKeys(keyList=['s','d'], waitRelease=False)
            _key_resp_sd_allKeys.extend(theseKeys)
            if len(_key_resp_sd_allKeys):
                key_resp_sd.keys = _key_resp_sd_allKeys[-1].name  # just the last key pressed
                key_resp_sd.rt = _key_resp_sd_allKeys[-1].rt
                # was this correct?
                if (key_resp_sd.keys == str(sd_correct_key)) or (key_resp_sd.keys == sd_correct_key):
                    key_resp_sd.corr = 1
                else:
                    key_resp_sd.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *sd_hint* updates
        
        # if sd_hint is starting this frame...
        if sd_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sd_hint.frameNStart = frameN  # exact frame index
            sd_hint.tStart = t  # local t and not account for scr refresh
            sd_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_hint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_hint.started')
            # update status
            sd_hint.status = STARTED
            sd_hint.setAutoDraw(True)
        
        # if sd_hint is active this frame...
        if sd_hint.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in same_diffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "same_diff" ---
    for thisComponent in same_diffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_sd.keys in ['', [], None]:  # No response was made
        key_resp_sd.keys = None
        # was no response the correct answer?!
        if str(sd_correct_key).lower() == 'none':
           key_resp_sd.corr = 1;  # correct non-response
        else:
           key_resp_sd.corr = 0;  # failed to respond (incorrectly)
    # store data for sd1_loop (TrialHandler)
    sd1_loop.addData('key_resp_sd.keys',key_resp_sd.keys)
    sd1_loop.addData('key_resp_sd.corr', key_resp_sd.corr)
    if key_resp_sd.keys != None:  # we had a response
        sd1_loop.addData('key_resp_sd.rt', key_resp_sd.rt)
    # the Routine "same_diff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sd_resp_triggers" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_resp_trigger_code
    if key_resp_sd.corr:
        sd_acc_trig = 169
    else:
        sd_acc_trig = 168
    # keep track of which components have finished
    sd_resp_triggersComponents = [sd_resp_trigs]
    for thisComponent in sd_resp_triggersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_resp_triggers" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sd_resp_trigs is starting this frame...
        if sd_resp_trigs.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_resp_trigs.frameNStart = frameN  # exact frame index
            sd_resp_trigs.tStart = t  # local t and not account for scr refresh
            sd_resp_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_resp_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_resp_trigs.started')
            # update status
            sd_resp_trigs.status = STARTED
            win.callOnFlip(sd_resp_trigs.write, bytes(chr(167), 'utf8'))
            sd_resp_trigs.status = STARTED
        
        # if sd_resp_trigs is stopping this frame...
        if sd_resp_trigs.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > .1-frameTolerance:
                # keep track of stop time/frame for later
                sd_resp_trigs.tStop = t  # not accounting for scr refresh
                sd_resp_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_resp_trigs.stopped')
                # update status
                sd_resp_trigs.status = FINISHED
                win.callOnFlip(sd_resp_trigs.write, bytes(chr(sd_acc_trig), 'utf8'))
                sd_resp_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_resp_triggersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_resp_triggers" ---
    for thisComponent in sd_resp_triggersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.100000)
    
    # --- Prepare to start Routine "sd_blink" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_blink_code
    sd_blink_counter = sd_blink_counter + 1
    if sd_blink_counter == 4:
        sd_blink_counter = 0
    else:
        continueRoutine = False
    sd_trial_no_3.setText(sd_trial_nums)
    sd_blink_key.keys = []
    sd_blink_key.rt = []
    _sd_blink_key_allKeys = []
    # keep track of which components have finished
    sd_blinkComponents = [sd_trial_no_3, sd1_blink_text, sd_blink_key, sd_blink_trigs]
    for thisComponent in sd_blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_blink" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_3* updates
        
        # if sd_trial_no_3 is starting this frame...
        if sd_trial_no_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_3.frameNStart = frameN  # exact frame index
            sd_trial_no_3.tStart = t  # local t and not account for scr refresh
            sd_trial_no_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_3.started')
            # update status
            sd_trial_no_3.status = STARTED
            sd_trial_no_3.setAutoDraw(True)
        
        # if sd_trial_no_3 is active this frame...
        if sd_trial_no_3.status == STARTED:
            # update params
            pass
        
        # *sd1_blink_text* updates
        
        # if sd1_blink_text is starting this frame...
        if sd1_blink_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd1_blink_text.frameNStart = frameN  # exact frame index
            sd1_blink_text.tStart = t  # local t and not account for scr refresh
            sd1_blink_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd1_blink_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd1_blink_text.started')
            # update status
            sd1_blink_text.status = STARTED
            sd1_blink_text.setAutoDraw(True)
        
        # if sd1_blink_text is active this frame...
        if sd1_blink_text.status == STARTED:
            # update params
            pass
        
        # *sd_blink_key* updates
        waitOnFlip = False
        
        # if sd_blink_key is starting this frame...
        if sd_blink_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_blink_key.frameNStart = frameN  # exact frame index
            sd_blink_key.tStart = t  # local t and not account for scr refresh
            sd_blink_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_key.started')
            # update status
            sd_blink_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sd_blink_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sd_blink_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sd_blink_key.status == STARTED and not waitOnFlip:
            theseKeys = sd_blink_key.getKeys(keyList=['space'], waitRelease=False)
            _sd_blink_key_allKeys.extend(theseKeys)
            if len(_sd_blink_key_allKeys):
                sd_blink_key.keys = _sd_blink_key_allKeys[-1].name  # just the last key pressed
                sd_blink_key.rt = _sd_blink_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if sd_blink_trigs is starting this frame...
        if sd_blink_trigs.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_blink_trigs.frameNStart = frameN  # exact frame index
            sd_blink_trigs.tStart = t  # local t and not account for scr refresh
            sd_blink_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_trigs.started')
            # update status
            sd_blink_trigs.status = STARTED
            win.callOnFlip(sd_blink_trigs.write, bytes(chr(179), 'utf8'))
            sd_blink_trigs.status = STARTED
        
        # if sd_blink_trigs is stopping this frame...
        if sd_blink_trigs.status == STARTED:
            if bool(sd_blink_key.keys == 'space'):
                # keep track of stop time/frame for later
                sd_blink_trigs.tStop = t  # not accounting for scr refresh
                sd_blink_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_blink_trigs.stopped')
                # update status
                sd_blink_trigs.status = FINISHED
                win.callOnFlip(sd_blink_trigs.write, bytes(chr(180), 'utf8'))
                sd_blink_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_blink" ---
    for thisComponent in sd_blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sd_blink_key.keys in ['', [], None]:  # No response was made
        sd_blink_key.keys = None
    sd1_loop.addData('sd_blink_key.keys',sd_blink_key.keys)
    if sd_blink_key.keys != None:  # we had a response
        sd1_loop.addData('sd_blink_key.rt', sd_blink_key.rt)
    # the Routine "sd_blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'sd1_loop'


# --- Prepare to start Routine "learning_instructions0" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_0.keys = []
key_resp_learn_0.rt = []
_key_resp_learn_0_allKeys = []
# keep track of which components have finished
learning_instructions0Components = [instructionLearn0, alienBodyDemoLL, alienEyeDemoLL, alienBodyDemoL, alienEyeDemoL, alienBodyDemoR, alienEyeDemoR, alienBodyDemoRR, alienEyeDemoRR, key_resp_learn_0, learn_instruction_trigs_0]
for thisComponent in learning_instructions0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions0" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn0* updates
    
    # if instructionLearn0 is starting this frame...
    if instructionLearn0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn0.frameNStart = frameN  # exact frame index
        instructionLearn0.tStart = t  # local t and not account for scr refresh
        instructionLearn0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn0, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn0.started')
        # update status
        instructionLearn0.status = STARTED
        instructionLearn0.setAutoDraw(True)
    
    # if instructionLearn0 is active this frame...
    if instructionLearn0.status == STARTED:
        # update params
        pass
    
    # *alienBodyDemoLL* updates
    
    # if alienBodyDemoLL is starting this frame...
    if alienBodyDemoLL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoLL.frameNStart = frameN  # exact frame index
        alienBodyDemoLL.tStart = t  # local t and not account for scr refresh
        alienBodyDemoLL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoLL, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemoLL.started')
        # update status
        alienBodyDemoLL.status = STARTED
        alienBodyDemoLL.setAutoDraw(True)
    
    # if alienBodyDemoLL is active this frame...
    if alienBodyDemoLL.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemoLL* updates
    
    # if alienEyeDemoLL is starting this frame...
    if alienEyeDemoLL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoLL.frameNStart = frameN  # exact frame index
        alienEyeDemoLL.tStart = t  # local t and not account for scr refresh
        alienEyeDemoLL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoLL, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemoLL.started')
        # update status
        alienEyeDemoLL.status = STARTED
        alienEyeDemoLL.setAutoDraw(True)
    
    # if alienEyeDemoLL is active this frame...
    if alienEyeDemoLL.status == STARTED:
        # update params
        pass
    
    # *alienBodyDemoL* updates
    
    # if alienBodyDemoL is starting this frame...
    if alienBodyDemoL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoL.frameNStart = frameN  # exact frame index
        alienBodyDemoL.tStart = t  # local t and not account for scr refresh
        alienBodyDemoL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoL, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemoL.started')
        # update status
        alienBodyDemoL.status = STARTED
        alienBodyDemoL.setAutoDraw(True)
    
    # if alienBodyDemoL is active this frame...
    if alienBodyDemoL.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemoL* updates
    
    # if alienEyeDemoL is starting this frame...
    if alienEyeDemoL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoL.frameNStart = frameN  # exact frame index
        alienEyeDemoL.tStart = t  # local t and not account for scr refresh
        alienEyeDemoL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoL, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemoL.started')
        # update status
        alienEyeDemoL.status = STARTED
        alienEyeDemoL.setAutoDraw(True)
    
    # if alienEyeDemoL is active this frame...
    if alienEyeDemoL.status == STARTED:
        # update params
        pass
    
    # *alienBodyDemoR* updates
    
    # if alienBodyDemoR is starting this frame...
    if alienBodyDemoR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoR.frameNStart = frameN  # exact frame index
        alienBodyDemoR.tStart = t  # local t and not account for scr refresh
        alienBodyDemoR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoR, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemoR.started')
        # update status
        alienBodyDemoR.status = STARTED
        alienBodyDemoR.setAutoDraw(True)
    
    # if alienBodyDemoR is active this frame...
    if alienBodyDemoR.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemoR* updates
    
    # if alienEyeDemoR is starting this frame...
    if alienEyeDemoR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoR.frameNStart = frameN  # exact frame index
        alienEyeDemoR.tStart = t  # local t and not account for scr refresh
        alienEyeDemoR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoR, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemoR.started')
        # update status
        alienEyeDemoR.status = STARTED
        alienEyeDemoR.setAutoDraw(True)
    
    # if alienEyeDemoR is active this frame...
    if alienEyeDemoR.status == STARTED:
        # update params
        pass
    
    # *alienBodyDemoRR* updates
    
    # if alienBodyDemoRR is starting this frame...
    if alienBodyDemoRR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoRR.frameNStart = frameN  # exact frame index
        alienBodyDemoRR.tStart = t  # local t and not account for scr refresh
        alienBodyDemoRR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoRR, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemoRR.started')
        # update status
        alienBodyDemoRR.status = STARTED
        alienBodyDemoRR.setAutoDraw(True)
    
    # if alienBodyDemoRR is active this frame...
    if alienBodyDemoRR.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemoRR* updates
    
    # if alienEyeDemoRR is starting this frame...
    if alienEyeDemoRR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoRR.frameNStart = frameN  # exact frame index
        alienEyeDemoRR.tStart = t  # local t and not account for scr refresh
        alienEyeDemoRR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoRR, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemoRR.started')
        # update status
        alienEyeDemoRR.status = STARTED
        alienEyeDemoRR.setAutoDraw(True)
    
    # if alienEyeDemoRR is active this frame...
    if alienEyeDemoRR.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_0* updates
    waitOnFlip = False
    
    # if key_resp_learn_0 is starting this frame...
    if key_resp_learn_0.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_0.frameNStart = frameN  # exact frame index
        key_resp_learn_0.tStart = t  # local t and not account for scr refresh
        key_resp_learn_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_0, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_learn_0.started')
        # update status
        key_resp_learn_0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_learn_0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_learn_0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_learn_0.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_learn_0.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_learn_0_allKeys.extend(theseKeys)
        if len(_key_resp_learn_0_allKeys):
            key_resp_learn_0.keys = _key_resp_learn_0_allKeys[-1].name  # just the last key pressed
            key_resp_learn_0.rt = _key_resp_learn_0_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_0 is starting this frame...
    if learn_instruction_trigs_0.status == NOT_STARTED and instructionLearn0.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_0.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_0.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_0, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_0.started')
        # update status
        learn_instruction_trigs_0.status = STARTED
        win.callOnFlip(learn_instruction_trigs_0.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_0.status = STARTED
    
    # if learn_instruction_trigs_0 is stopping this frame...
    if learn_instruction_trigs_0.status == STARTED:
        if bool(len(_key_resp_learn_0_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_0.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_0.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_0.stopped')
            # update status
            learn_instruction_trigs_0.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_0.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_0.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions0" ---
for thisComponent in learning_instructions0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_learn_0.keys in ['', [], None]:  # No response was made
    key_resp_learn_0.keys = None
thisExp.addData('key_resp_learn_0.keys',key_resp_learn_0.keys)
if key_resp_learn_0.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_0.rt', key_resp_learn_0.rt)
thisExp.nextEntry()
# the Routine "learning_instructions0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions1" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_1.keys = []
key_resp_learn_1.rt = []
_key_resp_learn_1_allKeys = []
# keep track of which components have finished
learning_instructions1Components = [alienBodyDemo1, alienEyeDemo1, explorerDemo1_L, instructionLearn1, key_resp_learn_1, learn_instruction_trigs_1]
for thisComponent in learning_instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo1* updates
    
    # if alienBodyDemo1 is starting this frame...
    if alienBodyDemo1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo1.frameNStart = frameN  # exact frame index
        alienBodyDemo1.tStart = t  # local t and not account for scr refresh
        alienBodyDemo1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemo1.started')
        # update status
        alienBodyDemo1.status = STARTED
        alienBodyDemo1.setAutoDraw(True)
    
    # if alienBodyDemo1 is active this frame...
    if alienBodyDemo1.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemo1* updates
    
    # if alienEyeDemo1 is starting this frame...
    if alienEyeDemo1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo1.frameNStart = frameN  # exact frame index
        alienEyeDemo1.tStart = t  # local t and not account for scr refresh
        alienEyeDemo1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemo1.started')
        # update status
        alienEyeDemo1.status = STARTED
        alienEyeDemo1.setAutoDraw(True)
    
    # if alienEyeDemo1 is active this frame...
    if alienEyeDemo1.status == STARTED:
        # update params
        pass
    
    # *explorerDemo1_L* updates
    
    # if explorerDemo1_L is starting this frame...
    if explorerDemo1_L.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo1_L.frameNStart = frameN  # exact frame index
        explorerDemo1_L.tStart = t  # local t and not account for scr refresh
        explorerDemo1_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo1_L, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'explorerDemo1_L.started')
        # update status
        explorerDemo1_L.status = STARTED
        explorerDemo1_L.setAutoDraw(True)
    
    # if explorerDemo1_L is active this frame...
    if explorerDemo1_L.status == STARTED:
        # update params
        pass
    
    # *instructionLearn1* updates
    
    # if instructionLearn1 is starting this frame...
    if instructionLearn1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn1.frameNStart = frameN  # exact frame index
        instructionLearn1.tStart = t  # local t and not account for scr refresh
        instructionLearn1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn1.started')
        # update status
        instructionLearn1.status = STARTED
        instructionLearn1.setAutoDraw(True)
    
    # if instructionLearn1 is active this frame...
    if instructionLearn1.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_1* updates
    waitOnFlip = False
    
    # if key_resp_learn_1 is starting this frame...
    if key_resp_learn_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_1.frameNStart = frameN  # exact frame index
        key_resp_learn_1.tStart = t  # local t and not account for scr refresh
        key_resp_learn_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_1, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp_learn_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_learn_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_learn_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_learn_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_learn_1.getKeys(keyList=['left', 'right'], waitRelease=False)
        _key_resp_learn_1_allKeys.extend(theseKeys)
        if len(_key_resp_learn_1_allKeys):
            key_resp_learn_1.keys = _key_resp_learn_1_allKeys[-1].name  # just the last key pressed
            key_resp_learn_1.rt = _key_resp_learn_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_1 is starting this frame...
    if learn_instruction_trigs_1.status == NOT_STARTED and instructionLearn1.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_1.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_1.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_1.started')
        # update status
        learn_instruction_trigs_1.status = STARTED
        win.callOnFlip(learn_instruction_trigs_1.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_1.status = STARTED
    
    # if learn_instruction_trigs_1 is stopping this frame...
    if learn_instruction_trigs_1.status == STARTED:
        if bool(len(_key_resp_learn_1_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_1.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_1.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_1.stopped')
            # update status
            learn_instruction_trigs_1.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_1.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_1.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions1" ---
for thisComponent in learning_instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "learning_instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_2.keys = []
key_resp_learn_2.rt = []
_key_resp_learn_2_allKeys = []
# keep track of which components have finished
learning_instructions2Components = [alienBodyDemo1_2, alienEyeDemo1_2, explorerDemo1_2_U, instructionLearn_2, key_resp_learn_2, learn_instruction_trigs_2]
for thisComponent in learning_instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo1_2* updates
    
    # if alienBodyDemo1_2 is starting this frame...
    if alienBodyDemo1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo1_2.frameNStart = frameN  # exact frame index
        alienBodyDemo1_2.tStart = t  # local t and not account for scr refresh
        alienBodyDemo1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemo1_2.started')
        # update status
        alienBodyDemo1_2.status = STARTED
        alienBodyDemo1_2.setAutoDraw(True)
    
    # if alienBodyDemo1_2 is active this frame...
    if alienBodyDemo1_2.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemo1_2* updates
    
    # if alienEyeDemo1_2 is starting this frame...
    if alienEyeDemo1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo1_2.frameNStart = frameN  # exact frame index
        alienEyeDemo1_2.tStart = t  # local t and not account for scr refresh
        alienEyeDemo1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo1_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemo1_2.started')
        # update status
        alienEyeDemo1_2.status = STARTED
        alienEyeDemo1_2.setAutoDraw(True)
    
    # if alienEyeDemo1_2 is active this frame...
    if alienEyeDemo1_2.status == STARTED:
        # update params
        pass
    
    # *explorerDemo1_2_U* updates
    
    # if explorerDemo1_2_U is starting this frame...
    if explorerDemo1_2_U.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo1_2_U.frameNStart = frameN  # exact frame index
        explorerDemo1_2_U.tStart = t  # local t and not account for scr refresh
        explorerDemo1_2_U.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo1_2_U, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'explorerDemo1_2_U.started')
        # update status
        explorerDemo1_2_U.status = STARTED
        explorerDemo1_2_U.setAutoDraw(True)
    
    # if explorerDemo1_2_U is active this frame...
    if explorerDemo1_2_U.status == STARTED:
        # update params
        pass
    
    # *instructionLearn_2* updates
    
    # if instructionLearn_2 is starting this frame...
    if instructionLearn_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn_2.frameNStart = frameN  # exact frame index
        instructionLearn_2.tStart = t  # local t and not account for scr refresh
        instructionLearn_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn_2.started')
        # update status
        instructionLearn_2.status = STARTED
        instructionLearn_2.setAutoDraw(True)
    
    # if instructionLearn_2 is active this frame...
    if instructionLearn_2.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_2* updates
    waitOnFlip = False
    
    # if key_resp_learn_2 is starting this frame...
    if key_resp_learn_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_2.frameNStart = frameN  # exact frame index
        key_resp_learn_2.tStart = t  # local t and not account for scr refresh
        key_resp_learn_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp_learn_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_learn_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_learn_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_learn_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_learn_2.getKeys(keyList=['up','down'], waitRelease=False)
        _key_resp_learn_2_allKeys.extend(theseKeys)
        if len(_key_resp_learn_2_allKeys):
            key_resp_learn_2.keys = _key_resp_learn_2_allKeys[-1].name  # just the last key pressed
            key_resp_learn_2.rt = _key_resp_learn_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_2 is starting this frame...
    if learn_instruction_trigs_2.status == NOT_STARTED and instructionLearn_2.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_2.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_2.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_2.started')
        # update status
        learn_instruction_trigs_2.status = STARTED
        win.callOnFlip(learn_instruction_trigs_2.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_2.status = STARTED
    
    # if learn_instruction_trigs_2 is stopping this frame...
    if learn_instruction_trigs_2.status == STARTED:
        if bool(len(_key_resp_learn_2_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_2.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_2.stopped')
            # update status
            learn_instruction_trigs_2.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_2.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_2.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions2" ---
for thisComponent in learning_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "learning_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions3" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_3.keys = []
key_resp_learn_3.rt = []
_key_resp_learn_3_allKeys = []
# keep track of which components have finished
learning_instructions3Components = [instructionLearn_3, key_resp_learn_3, learn_instruction_trigs_3]
for thisComponent in learning_instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn_3* updates
    
    # if instructionLearn_3 is starting this frame...
    if instructionLearn_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn_3.frameNStart = frameN  # exact frame index
        instructionLearn_3.tStart = t  # local t and not account for scr refresh
        instructionLearn_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn_3.started')
        # update status
        instructionLearn_3.status = STARTED
        instructionLearn_3.setAutoDraw(True)
    
    # if instructionLearn_3 is active this frame...
    if instructionLearn_3.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_3* updates
    
    # if key_resp_learn_3 is starting this frame...
    if key_resp_learn_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_3.frameNStart = frameN  # exact frame index
        key_resp_learn_3.tStart = t  # local t and not account for scr refresh
        key_resp_learn_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_3, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp_learn_3.status = STARTED
        # keyboard checking is just starting
        key_resp_learn_3.clock.reset()  # now t=0
        key_resp_learn_3.clearEvents(eventType='keyboard')
    if key_resp_learn_3.status == STARTED:
        theseKeys = key_resp_learn_3.getKeys(keyList=['c'], waitRelease=False)
        _key_resp_learn_3_allKeys.extend(theseKeys)
        if len(_key_resp_learn_3_allKeys):
            key_resp_learn_3.keys = _key_resp_learn_3_allKeys[-1].name  # just the last key pressed
            key_resp_learn_3.rt = _key_resp_learn_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_3 is starting this frame...
    if learn_instruction_trigs_3.status == NOT_STARTED and instructionLearn_3.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_3.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_3.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_3.started')
        # update status
        learn_instruction_trigs_3.status = STARTED
        win.callOnFlip(learn_instruction_trigs_3.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_3.status = STARTED
    
    # if learn_instruction_trigs_3 is stopping this frame...
    if learn_instruction_trigs_3.status == STARTED:
        if bool(len(_key_resp_learn_3_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_3.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_3.stopped')
            # update status
            learn_instruction_trigs_3.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_3.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_3.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions3" ---
for thisComponent in learning_instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_learn_3.keys in ['', [], None]:  # No response was made
    key_resp_learn_3.keys = None
thisExp.addData('key_resp_learn_3.keys',key_resp_learn_3.keys)
if key_resp_learn_3.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_3.rt', key_resp_learn_3.rt)
thisExp.nextEntry()
# the Routine "learning_instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions4" ---
continueRoutine = True
# update component parameters for each repeat
correct_tone_instructions.setSound('stimuli/bleep.wav', secs=.25, hamming=True)
correct_tone_instructions.setVolume(1.0, log=False)
key_resp_learn_4.keys = []
key_resp_learn_4.rt = []
_key_resp_learn_4_allKeys = []
# keep track of which components have finished
learning_instructions4Components = [correct_tone_instructions, instructionLearn4a, instructionLearn4b, key_resp_learn_4, learn_instruction_trigs_4]
for thisComponent in learning_instructions4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions4" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop correct_tone_instructions
    
    # if correct_tone_instructions is starting this frame...
    if correct_tone_instructions.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
        # keep track of start time/frame for later
        correct_tone_instructions.frameNStart = frameN  # exact frame index
        correct_tone_instructions.tStart = t  # local t and not account for scr refresh
        correct_tone_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('correct_tone_instructions.started', tThisFlipGlobal)
        # update status
        correct_tone_instructions.status = STARTED
        correct_tone_instructions.play(when=win)  # sync with win flip
    
    # if correct_tone_instructions is stopping this frame...
    if correct_tone_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > correct_tone_instructions.tStartRefresh + .25-frameTolerance:
            # keep track of stop time/frame for later
            correct_tone_instructions.tStop = t  # not accounting for scr refresh
            correct_tone_instructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'correct_tone_instructions.stopped')
            # update status
            correct_tone_instructions.status = FINISHED
            correct_tone_instructions.stop()
    
    # *instructionLearn4a* updates
    
    # if instructionLearn4a is starting this frame...
    if instructionLearn4a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn4a.frameNStart = frameN  # exact frame index
        instructionLearn4a.tStart = t  # local t and not account for scr refresh
        instructionLearn4a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn4a, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn4a.started')
        # update status
        instructionLearn4a.status = STARTED
        instructionLearn4a.setAutoDraw(True)
    
    # if instructionLearn4a is active this frame...
    if instructionLearn4a.status == STARTED:
        # update params
        pass
    
    # *instructionLearn4b* updates
    
    # if instructionLearn4b is starting this frame...
    if instructionLearn4b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn4b.frameNStart = frameN  # exact frame index
        instructionLearn4b.tStart = t  # local t and not account for scr refresh
        instructionLearn4b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn4b, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn4b.started')
        # update status
        instructionLearn4b.status = STARTED
        instructionLearn4b.setAutoDraw(True)
    
    # if instructionLearn4b is active this frame...
    if instructionLearn4b.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_4* updates
    waitOnFlip = False
    
    # if key_resp_learn_4 is starting this frame...
    if key_resp_learn_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_4.frameNStart = frameN  # exact frame index
        key_resp_learn_4.tStart = t  # local t and not account for scr refresh
        key_resp_learn_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_learn_4.started')
        # update status
        key_resp_learn_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_learn_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_learn_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_learn_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_learn_4.getKeys(keyList=['i'], waitRelease=False)
        _key_resp_learn_4_allKeys.extend(theseKeys)
        if len(_key_resp_learn_4_allKeys):
            key_resp_learn_4.keys = _key_resp_learn_4_allKeys[-1].name  # just the last key pressed
            key_resp_learn_4.rt = _key_resp_learn_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_4 is starting this frame...
    if learn_instruction_trigs_4.status == NOT_STARTED and instructionLearn4a.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_4.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_4.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_4.started')
        # update status
        learn_instruction_trigs_4.status = STARTED
        win.callOnFlip(learn_instruction_trigs_4.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_4.status = STARTED
    
    # if learn_instruction_trigs_4 is stopping this frame...
    if learn_instruction_trigs_4.status == STARTED:
        if bool(len(_key_resp_learn_4_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_4.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_4.stopped')
            # update status
            learn_instruction_trigs_4.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_4.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_4.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions4" ---
for thisComponent in learning_instructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
correct_tone_instructions.stop()  # ensure sound has stopped at end of routine
# check responses
if key_resp_learn_4.keys in ['', [], None]:  # No response was made
    key_resp_learn_4.keys = None
thisExp.addData('key_resp_learn_4.keys',key_resp_learn_4.keys)
if key_resp_learn_4.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_4.rt', key_resp_learn_4.rt)
thisExp.nextEntry()
# the Routine "learning_instructions4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions5" ---
continueRoutine = True
# update component parameters for each repeat
incorrect_tone_instructions.setSound('stimuli/buzz.wav', secs=.25, hamming=True)
incorrect_tone_instructions.setVolume(1.0, log=False)
# keep track of which components have finished
learning_instructions5Components = [incorrect_tone_instructions, instructionLearn5a, instructionLearn5b, learn_instruction_trigs_5]
for thisComponent in learning_instructions5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions5" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop incorrect_tone_instructions
    
    # if incorrect_tone_instructions is starting this frame...
    if incorrect_tone_instructions.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
        # keep track of start time/frame for later
        incorrect_tone_instructions.frameNStart = frameN  # exact frame index
        incorrect_tone_instructions.tStart = t  # local t and not account for scr refresh
        incorrect_tone_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('incorrect_tone_instructions.started', tThisFlipGlobal)
        # update status
        incorrect_tone_instructions.status = STARTED
        incorrect_tone_instructions.play(when=win)  # sync with win flip
    
    # if incorrect_tone_instructions is stopping this frame...
    if incorrect_tone_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > incorrect_tone_instructions.tStartRefresh + .25-frameTolerance:
            # keep track of stop time/frame for later
            incorrect_tone_instructions.tStop = t  # not accounting for scr refresh
            incorrect_tone_instructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'incorrect_tone_instructions.stopped')
            # update status
            incorrect_tone_instructions.status = FINISHED
            incorrect_tone_instructions.stop()
    
    # *instructionLearn5a* updates
    
    # if instructionLearn5a is starting this frame...
    if instructionLearn5a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn5a.frameNStart = frameN  # exact frame index
        instructionLearn5a.tStart = t  # local t and not account for scr refresh
        instructionLearn5a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn5a, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn5a.started')
        # update status
        instructionLearn5a.status = STARTED
        instructionLearn5a.setAutoDraw(True)
    
    # if instructionLearn5a is active this frame...
    if instructionLearn5a.status == STARTED:
        # update params
        pass
    
    # if instructionLearn5a is stopping this frame...
    if instructionLearn5a.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructionLearn5a.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            instructionLearn5a.tStop = t  # not accounting for scr refresh
            instructionLearn5a.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructionLearn5a.stopped')
            # update status
            instructionLearn5a.status = FINISHED
            instructionLearn5a.setAutoDraw(False)
    
    # *instructionLearn5b* updates
    
    # if instructionLearn5b is starting this frame...
    if instructionLearn5b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn5b.frameNStart = frameN  # exact frame index
        instructionLearn5b.tStart = t  # local t and not account for scr refresh
        instructionLearn5b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn5b, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn5b.started')
        # update status
        instructionLearn5b.status = STARTED
        instructionLearn5b.setAutoDraw(True)
    
    # if instructionLearn5b is active this frame...
    if instructionLearn5b.status == STARTED:
        # update params
        pass
    
    # if instructionLearn5b is stopping this frame...
    if instructionLearn5b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructionLearn5b.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            instructionLearn5b.tStop = t  # not accounting for scr refresh
            instructionLearn5b.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructionLearn5b.stopped')
            # update status
            instructionLearn5b.status = FINISHED
            instructionLearn5b.setAutoDraw(False)
    
    # if learn_instruction_trigs_5 is starting this frame...
    if learn_instruction_trigs_5.status == NOT_STARTED and instructionLearn5a.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_5.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_5.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_5.started')
        # update status
        learn_instruction_trigs_5.status = STARTED
        win.callOnFlip(learn_instruction_trigs_5.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_5.status = STARTED
    
    # if learn_instruction_trigs_5 is stopping this frame...
    if learn_instruction_trigs_5.status == STARTED:
        if bool(instructionLearn5a.status == FINISHED):
            # keep track of stop time/frame for later
            learn_instruction_trigs_5.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_5.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_5.stopped')
            # update status
            learn_instruction_trigs_5.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_5.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_5.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions5" ---
for thisComponent in learning_instructions5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
incorrect_tone_instructions.stop()  # ensure sound has stopped at end of routine
# the Routine "learning_instructions5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_label_instructions" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from labelONLYinstructionsCODE
if expInfo['LC (experimenter use only)'] == 'NL':
    continueRoutine=False
label_instructions_key_resp.keys = []
label_instructions_key_resp.rt = []
_label_instructions_key_resp_allKeys = []
# keep track of which components have finished
learning_label_instructionsComponents = [learning_label_instruction_text, label_instructions_key_resp, learn_label_instruction_trigs]
for thisComponent in learning_label_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_label_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *learning_label_instruction_text* updates
    
    # if learning_label_instruction_text is starting this frame...
    if learning_label_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learning_label_instruction_text.frameNStart = frameN  # exact frame index
        learning_label_instruction_text.tStart = t  # local t and not account for scr refresh
        learning_label_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning_label_instruction_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learning_label_instruction_text.started')
        # update status
        learning_label_instruction_text.status = STARTED
        learning_label_instruction_text.setAutoDraw(True)
    
    # if learning_label_instruction_text is active this frame...
    if learning_label_instruction_text.status == STARTED:
        # update params
        pass
    
    # *label_instructions_key_resp* updates
    waitOnFlip = False
    
    # if label_instructions_key_resp is starting this frame...
    if label_instructions_key_resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        label_instructions_key_resp.frameNStart = frameN  # exact frame index
        label_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        label_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(label_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        label_instructions_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(label_instructions_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(label_instructions_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if label_instructions_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = label_instructions_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _label_instructions_key_resp_allKeys.extend(theseKeys)
        if len(_label_instructions_key_resp_allKeys):
            label_instructions_key_resp.keys = _label_instructions_key_resp_allKeys[-1].name  # just the last key pressed
            label_instructions_key_resp.rt = _label_instructions_key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_label_instruction_trigs is starting this frame...
    if learn_label_instruction_trigs.status == NOT_STARTED and learning_label_instruction_text.status == STARTED:
        # keep track of start time/frame for later
        learn_label_instruction_trigs.frameNStart = frameN  # exact frame index
        learn_label_instruction_trigs.tStart = t  # local t and not account for scr refresh
        learn_label_instruction_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_label_instruction_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_label_instruction_trigs.started')
        # update status
        learn_label_instruction_trigs.status = STARTED
        win.callOnFlip(learn_label_instruction_trigs.write, bytes(chr(7), 'utf8'))
        learn_label_instruction_trigs.status = STARTED
    
    # if learn_label_instruction_trigs is stopping this frame...
    if learn_label_instruction_trigs.status == STARTED:
        if bool(len(_label_instructions_key_resp_allKeys)):
            # keep track of stop time/frame for later
            learn_label_instruction_trigs.tStop = t  # not accounting for scr refresh
            learn_label_instruction_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_label_instruction_trigs.stopped')
            # update status
            learn_label_instruction_trigs.status = FINISHED
            win.callOnFlip(learn_label_instruction_trigs.write, bytes(chr(8), 'utf8'))
            learn_label_instruction_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_label_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_label_instructions" ---
for thisComponent in learning_label_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "learning_label_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_instructions6" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_6.keys = []
key_resp_learn_6.rt = []
_key_resp_learn_6_allKeys = []
# keep track of which components have finished
learning_instructions6Components = [instructionLearn6, key_resp_learn_6, learn_instruction_trigs_6]
for thisComponent in learning_instructions6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning_instructions6" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn6* updates
    
    # if instructionLearn6 is starting this frame...
    if instructionLearn6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn6.frameNStart = frameN  # exact frame index
        instructionLearn6.tStart = t  # local t and not account for scr refresh
        instructionLearn6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn6.started')
        # update status
        instructionLearn6.status = STARTED
        instructionLearn6.setAutoDraw(True)
    
    # if instructionLearn6 is active this frame...
    if instructionLearn6.status == STARTED:
        # update params
        pass
    
    # *key_resp_learn_6* updates
    waitOnFlip = False
    
    # if key_resp_learn_6 is starting this frame...
    if key_resp_learn_6.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_6.frameNStart = frameN  # exact frame index
        key_resp_learn_6.tStart = t  # local t and not account for scr refresh
        key_resp_learn_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_learn_6.started')
        # update status
        key_resp_learn_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_learn_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_learn_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_learn_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_learn_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_learn_6_allKeys.extend(theseKeys)
        if len(_key_resp_learn_6_allKeys):
            key_resp_learn_6.keys = _key_resp_learn_6_allKeys[-1].name  # just the last key pressed
            key_resp_learn_6.rt = _key_resp_learn_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn_instruction_trigs_6 is starting this frame...
    if learn_instruction_trigs_6.status == NOT_STARTED and instructionLearn6.status == STARTED:
        # keep track of start time/frame for later
        learn_instruction_trigs_6.frameNStart = frameN  # exact frame index
        learn_instruction_trigs_6.tStart = t  # local t and not account for scr refresh
        learn_instruction_trigs_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn_instruction_trigs_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn_instruction_trigs_6.started')
        # update status
        learn_instruction_trigs_6.status = STARTED
        win.callOnFlip(learn_instruction_trigs_6.write, bytes(chr(7), 'utf8'))
        learn_instruction_trigs_6.status = STARTED
    
    # if learn_instruction_trigs_6 is stopping this frame...
    if learn_instruction_trigs_6.status == STARTED:
        if bool(len(_key_resp_learn_6_allKeys)):
            # keep track of stop time/frame for later
            learn_instruction_trigs_6.tStop = t  # not accounting for scr refresh
            learn_instruction_trigs_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_instruction_trigs_6.stopped')
            # update status
            learn_instruction_trigs_6.status = FINISHED
            win.callOnFlip(learn_instruction_trigs_6.write, bytes(chr(8), 'utf8'))
            learn_instruction_trigs_6.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_instructions6" ---
for thisComponent in learning_instructions6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_learn_6.keys in ['', [], None]:  # No response was made
    key_resp_learn_6.keys = None
thisExp.addData('key_resp_learn_6.keys',key_resp_learn_6.keys)
if key_resp_learn_6.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_6.rt', key_resp_learn_6.rt)
thisExp.nextEntry()
# the Routine "learning_instructions6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learning1_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(learning_sequence1),
    seed=None, name='learning1_loop')
thisExp.addLoop(learning1_loop)  # add the loop to the experiment
thisLearning1_loop = learning1_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning1_loop.rgb)
if thisLearning1_loop != None:
    for paramName in thisLearning1_loop:
        exec('{} = thisLearning1_loop[paramName]'.format(paramName))

for thisLearning1_loop in learning1_loop:
    currentLoop = learning1_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLearning1_loop.rgb)
    if thisLearning1_loop != None:
        for paramName in thisLearning1_loop:
            exec('{} = thisLearning1_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "learning_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learn_trial_no_code
    learn_trial_nums = "Training Progress: " + str(currentLoop.thisN + 1) + " of " + str(currentLoop.nTotal);
    
    learn_trialNum_1.setText(learn_trial_nums)
    # keep track of which components have finished
    learning_fixationComponents = [learn_trialNum_1, fixationLearn, learn_fix_trigs]
    for thisComponent in learning_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_1* updates
        
        # if learn_trialNum_1 is starting this frame...
        if learn_trialNum_1.status == NOT_STARTED and fixationLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_1.frameNStart = frameN  # exact frame index
            learn_trialNum_1.tStart = t  # local t and not account for scr refresh
            learn_trialNum_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_1.started')
            # update status
            learn_trialNum_1.status = STARTED
            learn_trialNum_1.setAutoDraw(True)
        
        # if learn_trialNum_1 is active this frame...
        if learn_trialNum_1.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_1 is stopping this frame...
        if learn_trialNum_1.status == STARTED:
            if bool(fixationLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_1.tStop = t  # not accounting for scr refresh
                learn_trialNum_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_1.stopped')
                # update status
                learn_trialNum_1.status = FINISHED
                learn_trialNum_1.setAutoDraw(False)
        
        # *fixationLearn* updates
        
        # if fixationLearn is starting this frame...
        if fixationLearn.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            fixationLearn.frameNStart = frameN  # exact frame index
            fixationLearn.tStart = t  # local t and not account for scr refresh
            fixationLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixationLearn.started')
            # update status
            fixationLearn.status = STARTED
            fixationLearn.setAutoDraw(True)
        
        # if fixationLearn is active this frame...
        if fixationLearn.status == STARTED:
            # update params
            pass
        
        # if fixationLearn is stopping this frame...
        if fixationLearn.status == STARTED:
            if frameN >= (fixationLearn.frameNStart + 30):
                # keep track of stop time/frame for later
                fixationLearn.tStop = t  # not accounting for scr refresh
                fixationLearn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationLearn.stopped')
                # update status
                fixationLearn.status = FINISHED
                fixationLearn.setAutoDraw(False)
        
        # if learn_fix_trigs is starting this frame...
        if learn_fix_trigs.status == NOT_STARTED and fixationLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_fix_trigs.frameNStart = frameN  # exact frame index
            learn_fix_trigs.tStart = t  # local t and not account for scr refresh
            learn_fix_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_fix_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_fix_trigs.started')
            # update status
            learn_fix_trigs.status = STARTED
            win.callOnFlip(learn_fix_trigs.write, bytes(chr(177), 'utf8'))
            learn_fix_trigs.status = STARTED
        
        # if learn_fix_trigs is stopping this frame...
        if learn_fix_trigs.status == STARTED:
            if bool(fixationLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_fix_trigs.tStop = t  # not accounting for scr refresh
                learn_fix_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_fix_trigs.stopped')
                # update status
                learn_fix_trigs.status = FINISHED
                win.callOnFlip(learn_fix_trigs.write, bytes(chr(178), 'utf8'))
                learn_fix_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_fixation" ---
    for thisComponent in learning_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "learning_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_presentation" ---
    continueRoutine = True
    # update component parameters for each repeat
    learn_trialNum_2.setText(learn_trial_nums)
    alienEyeLearn.setOri(learn_ori_val)
    alienEyeLearn.setSF(learn_freq_val)
    explorerLearn.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    key_resp_learn.keys = []
    key_resp_learn.rt = []
    _key_resp_learn_allKeys = []
    # keep track of which components have finished
    learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, learn_photo_box, key_resp_learn, learn_stim_trigs, learning_hint]
    for thisComponent in learning_presentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_presentation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_2* updates
        
        # if learn_trialNum_2 is starting this frame...
        if learn_trialNum_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_2.frameNStart = frameN  # exact frame index
            learn_trialNum_2.tStart = t  # local t and not account for scr refresh
            learn_trialNum_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_2.started')
            # update status
            learn_trialNum_2.status = STARTED
            learn_trialNum_2.setAutoDraw(True)
        
        # if learn_trialNum_2 is active this frame...
        if learn_trialNum_2.status == STARTED:
            # update params
            pass
        
        # *alienBodyLearn* updates
        
        # if alienBodyLearn is starting this frame...
        if alienBodyLearn.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            alienBodyLearn.frameNStart = frameN  # exact frame index
            alienBodyLearn.tStart = t  # local t and not account for scr refresh
            alienBodyLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn.started')
            # update status
            alienBodyLearn.status = STARTED
            alienBodyLearn.setAutoDraw(True)
        
        # if alienBodyLearn is active this frame...
        if alienBodyLearn.status == STARTED:
            # update params
            pass
        
        # *alienEyeLearn* updates
        
        # if alienEyeLearn is starting this frame...
        if alienEyeLearn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn.frameNStart = frameN  # exact frame index
            alienEyeLearn.tStart = t  # local t and not account for scr refresh
            alienEyeLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn.started')
            # update status
            alienEyeLearn.status = STARTED
            alienEyeLearn.setAutoDraw(True)
        
        # if alienEyeLearn is active this frame...
        if alienEyeLearn.status == STARTED:
            # update params
            pass
        
        # *explorerLearn* updates
        
        # if explorerLearn is starting this frame...
        if explorerLearn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn.frameNStart = frameN  # exact frame index
            explorerLearn.tStart = t  # local t and not account for scr refresh
            explorerLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn.started')
            # update status
            explorerLearn.status = STARTED
            explorerLearn.setAutoDraw(True)
        
        # if explorerLearn is active this frame...
        if explorerLearn.status == STARTED:
            # update params
            pass
        
        # *learn_photo_box* updates
        
        # if learn_photo_box is starting this frame...
        if learn_photo_box.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_photo_box.frameNStart = frameN  # exact frame index
            learn_photo_box.tStart = t  # local t and not account for scr refresh
            learn_photo_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_photo_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_photo_box.started')
            # update status
            learn_photo_box.status = STARTED
            learn_photo_box.setAutoDraw(True)
        
        # if learn_photo_box is active this frame...
        if learn_photo_box.status == STARTED:
            # update params
            pass
        
        # *key_resp_learn* updates
        waitOnFlip = False
        
        # if key_resp_learn is starting this frame...
        if key_resp_learn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            key_resp_learn.frameNStart = frameN  # exact frame index
            key_resp_learn.tStart = t  # local t and not account for scr refresh
            key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_learn.started')
            # update status
            key_resp_learn.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_learn.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_learn.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_learn.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_learn.getKeys(keyList=[learn_legal_keys1,learn_legal_keys2], waitRelease=False)
            _key_resp_learn_allKeys.extend(theseKeys)
            if len(_key_resp_learn_allKeys):
                key_resp_learn.keys = _key_resp_learn_allKeys[-1].name  # just the last key pressed
                key_resp_learn.rt = _key_resp_learn_allKeys[-1].rt
                # was this correct?
                if (key_resp_learn.keys == str(learn_correct_key)) or (key_resp_learn.keys == learn_correct_key):
                    key_resp_learn.corr = 1
                else:
                    key_resp_learn.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # if learn_stim_trigs is starting this frame...
        if learn_stim_trigs.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_stim_trigs.frameNStart = frameN  # exact frame index
            learn_stim_trigs.tStart = t  # local t and not account for scr refresh
            learn_stim_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_stim_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_stim_trigs.started', t)
            # update status
            learn_stim_trigs.status = STARTED
            learn_stim_trigs.write(bytes(chr(learn_ontrig), 'utf8'))
            learn_stim_trigs.status = STARTED
        
        # if learn_stim_trigs is stopping this frame...
        if learn_stim_trigs.status == STARTED:
            if bool(len(_key_resp_learn_allKeys)):
                # keep track of stop time/frame for later
                learn_stim_trigs.tStop = t  # not accounting for scr refresh
                learn_stim_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_stim_trigs.stopped', t)
                # update status
                learn_stim_trigs.status = FINISHED
                learn_stim_trigs.write(bytes(chr(learn_offtrig), 'utf8'))
                learn_stim_trigs.status = FINISHED
        
        # *learning_hint* updates
        
        # if learning_hint is starting this frame...
        if learning_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            learning_hint.frameNStart = frameN  # exact frame index
            learning_hint.tStart = t  # local t and not account for scr refresh
            learning_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_hint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_hint.started')
            # update status
            learning_hint.status = STARTED
            learning_hint.setAutoDraw(True)
        
        # if learning_hint is active this frame...
        if learning_hint.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_presentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_presentation" ---
    for thisComponent in learning_presentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_learn.keys in ['', [], None]:  # No response was made
        key_resp_learn.keys = None
        # was no response the correct answer?!
        if str(learn_correct_key).lower() == 'none':
           key_resp_learn.corr = 1;  # correct non-response
        else:
           key_resp_learn.corr = 0;  # failed to respond (incorrectly)
    # store data for learning1_loop (TrialHandler)
    learning1_loop.addData('key_resp_learn.keys',key_resp_learn.keys)
    learning1_loop.addData('key_resp_learn.corr', key_resp_learn.corr)
    if key_resp_learn.keys != None:  # we had a response
        learning1_loop.addData('key_resp_learn.rt', key_resp_learn.rt)
    # the Routine "learning_presentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learningFeedbackCODE
    if key_resp_learn.corr:
      feedback_tone = 'stimuli/bleep.wav'
      learn_acc_trig = 172
    else:
      feedback_tone = 'stimuli/buzz.wav'
      learn_acc_trig = 171
    feedbackSoundLearn.setSound(feedback_tone, secs=.25, hamming=True)
    feedbackSoundLearn.setVolume(1.0, log=False)
    learn_trialNum_3.setText(learn_trial_nums)
    alienEyeLearn2.setOri(learn_ori_val)
    alienEyeLearn2.setSF(learn_freq_val)
    explorerLearn2.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    # keep track of which components have finished
    learning_feedbackComponents = [feedbackSoundLearn, learn_feedback_trigs, learn_trialNum_3, alienBodyLearn2, alienEyeLearn2, explorerLearn2]
    for thisComponent in learning_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop feedbackSoundLearn
        
        # if feedbackSoundLearn is starting this frame...
        if feedbackSoundLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackSoundLearn.frameNStart = frameN  # exact frame index
            feedbackSoundLearn.tStart = t  # local t and not account for scr refresh
            feedbackSoundLearn.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('feedbackSoundLearn.started', tThisFlipGlobal)
            # update status
            feedbackSoundLearn.status = STARTED
            feedbackSoundLearn.play(when=win)  # sync with win flip
        
        # if feedbackSoundLearn is stopping this frame...
        if feedbackSoundLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackSoundLearn.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                feedbackSoundLearn.tStop = t  # not accounting for scr refresh
                feedbackSoundLearn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackSoundLearn.stopped')
                # update status
                feedbackSoundLearn.status = FINISHED
                feedbackSoundLearn.stop()
        
        # if learn_feedback_trigs is starting this frame...
        if learn_feedback_trigs.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_feedback_trigs.frameNStart = frameN  # exact frame index
            learn_feedback_trigs.tStart = t  # local t and not account for scr refresh
            learn_feedback_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_feedback_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_feedback_trigs.started', t)
            # update status
            learn_feedback_trigs.status = STARTED
            learn_feedback_trigs.write(bytes(chr(170), 'utf8'))
            learn_feedback_trigs.status = STARTED
        
        # if learn_feedback_trigs is stopping this frame...
        if learn_feedback_trigs.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_feedback_trigs.tStop = t  # not accounting for scr refresh
                learn_feedback_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_feedback_trigs.stopped', t)
                # update status
                learn_feedback_trigs.status = FINISHED
                learn_feedback_trigs.write(bytes(chr(learn_acc_trig), 'utf8'))
                learn_feedback_trigs.status = FINISHED
        
        # *learn_trialNum_3* updates
        
        # if learn_trialNum_3 is starting this frame...
        if learn_trialNum_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_3.frameNStart = frameN  # exact frame index
            learn_trialNum_3.tStart = t  # local t and not account for scr refresh
            learn_trialNum_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_3.started')
            # update status
            learn_trialNum_3.status = STARTED
            learn_trialNum_3.setAutoDraw(True)
        
        # if learn_trialNum_3 is active this frame...
        if learn_trialNum_3.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_3 is stopping this frame...
        if learn_trialNum_3.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_3.tStop = t  # not accounting for scr refresh
                learn_trialNum_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_3.stopped')
                # update status
                learn_trialNum_3.status = FINISHED
                learn_trialNum_3.setAutoDraw(False)
        
        # *alienBodyLearn2* updates
        
        # if alienBodyLearn2 is starting this frame...
        if alienBodyLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            alienBodyLearn2.frameNStart = frameN  # exact frame index
            alienBodyLearn2.tStart = t  # local t and not account for scr refresh
            alienBodyLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn2.started')
            # update status
            alienBodyLearn2.status = STARTED
            alienBodyLearn2.setAutoDraw(True)
        
        # if alienBodyLearn2 is active this frame...
        if alienBodyLearn2.status == STARTED:
            # update params
            pass
        
        # if alienBodyLearn2 is stopping this frame...
        if alienBodyLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienBodyLearn2.tStop = t  # not accounting for scr refresh
                alienBodyLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienBodyLearn2.stopped')
                # update status
                alienBodyLearn2.status = FINISHED
                alienBodyLearn2.setAutoDraw(False)
        
        # *alienEyeLearn2* updates
        
        # if alienEyeLearn2 is starting this frame...
        if alienEyeLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn2.frameNStart = frameN  # exact frame index
            alienEyeLearn2.tStart = t  # local t and not account for scr refresh
            alienEyeLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn2.started')
            # update status
            alienEyeLearn2.status = STARTED
            alienEyeLearn2.setAutoDraw(True)
        
        # if alienEyeLearn2 is active this frame...
        if alienEyeLearn2.status == STARTED:
            # update params
            pass
        
        # if alienEyeLearn2 is stopping this frame...
        if alienEyeLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienEyeLearn2.tStop = t  # not accounting for scr refresh
                alienEyeLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienEyeLearn2.stopped')
                # update status
                alienEyeLearn2.status = FINISHED
                alienEyeLearn2.setAutoDraw(False)
        
        # *explorerLearn2* updates
        
        # if explorerLearn2 is starting this frame...
        if explorerLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn2.frameNStart = frameN  # exact frame index
            explorerLearn2.tStart = t  # local t and not account for scr refresh
            explorerLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn2.started')
            # update status
            explorerLearn2.status = STARTED
            explorerLearn2.setAutoDraw(True)
        
        # if explorerLearn2 is active this frame...
        if explorerLearn2.status == STARTED:
            # update params
            pass
        
        # if explorerLearn2 is stopping this frame...
        if explorerLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                explorerLearn2.tStop = t  # not accounting for scr refresh
                explorerLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explorerLearn2.stopped')
                # update status
                explorerLearn2.status = FINISHED
                explorerLearn2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_feedback" ---
    for thisComponent in learning_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedbackSoundLearn.stop()  # ensure sound has stopped at end of routine
    # the Routine "learning_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_feedback_label" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learningLabelFeedbackCODE
    if learn_trial_type == 'friendly':
        labelLearn = 'stimuli/'+friendly_label+'.wav'
    elif learn_trial_type == 'hostile':
        labelLearn = 'stimuli/'+hostile_label+'.wav'
    
    if friendly_label == 'havnori':
        if learn_trial_type == 'friendly':
            label_trig = 174
        elif learn_trial_type == 'hostile':
            label_trig = 175
    elif friendly_label == 'gowachi':
        if learn_trial_type == 'friendly':
            label_trig = 175
        elif learn_trial_type == 'hostile':
            label_trig = 174
    else:
        label_trig = 176
    
    thisExp.addData('hostileLabel_learn', hostile_label)
    trainingLabelLearn.setSound(labelLearn, secs=.8, hamming=True)
    trainingLabelLearn.setVolume(label_vol, log=False)
    learn_trialNum_4.setText(learn_trial_nums)
    alienEyeLearn3.setOri(learn_ori_val)
    alienEyeLearn3.setSF(learn_freq_val)
    explorerLearn3.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    # keep track of which components have finished
    learning_feedback_labelComponents = [trainingLabelLearn, learn_label_trigs, learn_trialNum_4, alienBodyLearn3, alienEyeLearn3, explorerLearn3]
    for thisComponent in learning_feedback_labelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_feedback_label" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop trainingLabelLearn
        
        # if trainingLabelLearn is starting this frame...
        if trainingLabelLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            trainingLabelLearn.frameNStart = frameN  # exact frame index
            trainingLabelLearn.tStart = t  # local t and not account for scr refresh
            trainingLabelLearn.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            trainingLabelLearn.status = STARTED
            trainingLabelLearn.play(when=win)  # sync with win flip
        
        # if trainingLabelLearn is stopping this frame...
        if trainingLabelLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trainingLabelLearn.tStartRefresh + .8-frameTolerance:
                # keep track of stop time/frame for later
                trainingLabelLearn.tStop = t  # not accounting for scr refresh
                trainingLabelLearn.frameNStop = frameN  # exact frame index
                # update status
                trainingLabelLearn.status = FINISHED
                trainingLabelLearn.stop()
        
        # if learn_label_trigs is starting this frame...
        if learn_label_trigs.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_label_trigs.frameNStart = frameN  # exact frame index
            learn_label_trigs.tStart = t  # local t and not account for scr refresh
            learn_label_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_label_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_label_trigs.started', t)
            # update status
            learn_label_trigs.status = STARTED
            learn_label_trigs.write(bytes(chr(173), 'utf8'))
            learn_label_trigs.status = STARTED
        
        # if learn_label_trigs is stopping this frame...
        if learn_label_trigs.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_label_trigs.tStop = t  # not accounting for scr refresh
                learn_label_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_label_trigs.stopped', t)
                # update status
                learn_label_trigs.status = FINISHED
                learn_label_trigs.write(bytes(chr(label_trig), 'utf8'))
                learn_label_trigs.status = FINISHED
        
        # *learn_trialNum_4* updates
        
        # if learn_trialNum_4 is starting this frame...
        if learn_trialNum_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_4.frameNStart = frameN  # exact frame index
            learn_trialNum_4.tStart = t  # local t and not account for scr refresh
            learn_trialNum_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_4.started')
            # update status
            learn_trialNum_4.status = STARTED
            learn_trialNum_4.setAutoDraw(True)
        
        # if learn_trialNum_4 is active this frame...
        if learn_trialNum_4.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_4 is stopping this frame...
        if learn_trialNum_4.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_4.tStop = t  # not accounting for scr refresh
                learn_trialNum_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_4.stopped')
                # update status
                learn_trialNum_4.status = FINISHED
                learn_trialNum_4.setAutoDraw(False)
        
        # *alienBodyLearn3* updates
        
        # if alienBodyLearn3 is starting this frame...
        if alienBodyLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            alienBodyLearn3.frameNStart = frameN  # exact frame index
            alienBodyLearn3.tStart = t  # local t and not account for scr refresh
            alienBodyLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn3.started')
            # update status
            alienBodyLearn3.status = STARTED
            alienBodyLearn3.setAutoDraw(True)
        
        # if alienBodyLearn3 is active this frame...
        if alienBodyLearn3.status == STARTED:
            # update params
            pass
        
        # if alienBodyLearn3 is stopping this frame...
        if alienBodyLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienBodyLearn3.tStop = t  # not accounting for scr refresh
                alienBodyLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienBodyLearn3.stopped')
                # update status
                alienBodyLearn3.status = FINISHED
                alienBodyLearn3.setAutoDraw(False)
        
        # *alienEyeLearn3* updates
        
        # if alienEyeLearn3 is starting this frame...
        if alienEyeLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn3.frameNStart = frameN  # exact frame index
            alienEyeLearn3.tStart = t  # local t and not account for scr refresh
            alienEyeLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn3.started')
            # update status
            alienEyeLearn3.status = STARTED
            alienEyeLearn3.setAutoDraw(True)
        
        # if alienEyeLearn3 is active this frame...
        if alienEyeLearn3.status == STARTED:
            # update params
            pass
        
        # if alienEyeLearn3 is stopping this frame...
        if alienEyeLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienEyeLearn3.tStop = t  # not accounting for scr refresh
                alienEyeLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienEyeLearn3.stopped')
                # update status
                alienEyeLearn3.status = FINISHED
                alienEyeLearn3.setAutoDraw(False)
        
        # *explorerLearn3* updates
        
        # if explorerLearn3 is starting this frame...
        if explorerLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn3.frameNStart = frameN  # exact frame index
            explorerLearn3.tStart = t  # local t and not account for scr refresh
            explorerLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn3.started')
            # update status
            explorerLearn3.status = STARTED
            explorerLearn3.setAutoDraw(True)
        
        # if explorerLearn3 is active this frame...
        if explorerLearn3.status == STARTED:
            # update params
            pass
        
        # if explorerLearn3 is stopping this frame...
        if explorerLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                explorerLearn3.tStop = t  # not accounting for scr refresh
                explorerLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explorerLearn3.stopped')
                # update status
                explorerLearn3.status = FINISHED
                explorerLearn3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_feedback_labelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_feedback_label" ---
    for thisComponent in learning_feedback_labelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trainingLabelLearn.stop()  # ensure sound has stopped at end of routine
    # the Routine "learning_feedback_label" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_blink" ---
    continueRoutine = True
    # update component parameters for each repeat
    learn_trialNum_5.setText(learn_trial_nums)
    alienEyeLearn4.setOri(learn_ori_val)
    alienEyeLearn4.setSF(learn_freq_val)
    explorerLearn4.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    learning_blink_key.keys = []
    learning_blink_key.rt = []
    _learning_blink_key_allKeys = []
    # keep track of which components have finished
    learning_blinkComponents = [learn_trialNum_5, alienBodyLearn4, alienEyeLearn4, explorerLearn4, learning_blink_text, learning_blink_key, learn_blink_trigs]
    for thisComponent in learning_blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_blink" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_5* updates
        
        # if learn_trialNum_5 is starting this frame...
        if learn_trialNum_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn_trialNum_5.frameNStart = frameN  # exact frame index
            learn_trialNum_5.tStart = t  # local t and not account for scr refresh
            learn_trialNum_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_5.started')
            # update status
            learn_trialNum_5.status = STARTED
            learn_trialNum_5.setAutoDraw(True)
        
        # if learn_trialNum_5 is active this frame...
        if learn_trialNum_5.status == STARTED:
            # update params
            pass
        
        # *alienBodyLearn4* updates
        
        # if alienBodyLearn4 is starting this frame...
        if alienBodyLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alienBodyLearn4.frameNStart = frameN  # exact frame index
            alienBodyLearn4.tStart = t  # local t and not account for scr refresh
            alienBodyLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn4.started')
            # update status
            alienBodyLearn4.status = STARTED
            alienBodyLearn4.setAutoDraw(True)
        
        # if alienBodyLearn4 is active this frame...
        if alienBodyLearn4.status == STARTED:
            # update params
            pass
        
        # *alienEyeLearn4* updates
        
        # if alienEyeLearn4 is starting this frame...
        if alienEyeLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alienEyeLearn4.frameNStart = frameN  # exact frame index
            alienEyeLearn4.tStart = t  # local t and not account for scr refresh
            alienEyeLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn4.started')
            # update status
            alienEyeLearn4.status = STARTED
            alienEyeLearn4.setAutoDraw(True)
        
        # if alienEyeLearn4 is active this frame...
        if alienEyeLearn4.status == STARTED:
            # update params
            pass
        
        # *explorerLearn4* updates
        
        # if explorerLearn4 is starting this frame...
        if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            explorerLearn4.frameNStart = frameN  # exact frame index
            explorerLearn4.tStart = t  # local t and not account for scr refresh
            explorerLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn4.started')
            # update status
            explorerLearn4.status = STARTED
            explorerLearn4.setAutoDraw(True)
        
        # if explorerLearn4 is active this frame...
        if explorerLearn4.status == STARTED:
            # update params
            pass
        
        # *learning_blink_text* updates
        
        # if learning_blink_text is starting this frame...
        if learning_blink_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            learning_blink_text.frameNStart = frameN  # exact frame index
            learning_blink_text.tStart = t  # local t and not account for scr refresh
            learning_blink_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_blink_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_blink_text.started')
            # update status
            learning_blink_text.status = STARTED
            learning_blink_text.setAutoDraw(True)
        
        # if learning_blink_text is active this frame...
        if learning_blink_text.status == STARTED:
            # update params
            pass
        
        # *learning_blink_key* updates
        waitOnFlip = False
        
        # if learning_blink_key is starting this frame...
        if learning_blink_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            learning_blink_key.frameNStart = frameN  # exact frame index
            learning_blink_key.tStart = t  # local t and not account for scr refresh
            learning_blink_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_blink_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_blink_key.started')
            # update status
            learning_blink_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learning_blink_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learning_blink_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learning_blink_key.status == STARTED and not waitOnFlip:
            theseKeys = learning_blink_key.getKeys(keyList=['space'], waitRelease=False)
            _learning_blink_key_allKeys.extend(theseKeys)
            if len(_learning_blink_key_allKeys):
                learning_blink_key.keys = _learning_blink_key_allKeys[-1].name  # just the last key pressed
                learning_blink_key.rt = _learning_blink_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if learn_blink_trigs is starting this frame...
        if learn_blink_trigs.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            learn_blink_trigs.frameNStart = frameN  # exact frame index
            learn_blink_trigs.tStart = t  # local t and not account for scr refresh
            learn_blink_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_blink_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_blink_trigs.started', t)
            # update status
            learn_blink_trigs.status = STARTED
            learn_blink_trigs.write(bytes(chr(179), 'utf8'))
            learn_blink_trigs.status = STARTED
        
        # if learn_blink_trigs is stopping this frame...
        if learn_blink_trigs.status == STARTED:
            if bool(len(_learning_blink_key_allKeys)):
                # keep track of stop time/frame for later
                learn_blink_trigs.tStop = t  # not accounting for scr refresh
                learn_blink_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_blink_trigs.stopped', t)
                # update status
                learn_blink_trigs.status = FINISHED
                learn_blink_trigs.write(bytes(chr(180), 'utf8'))
                learn_blink_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_blink" ---
    for thisComponent in learning_blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if learning_blink_key.keys in ['', [], None]:  # No response was made
        learning_blink_key.keys = None
    learning1_loop.addData('learning_blink_key.keys',learning_blink_key.keys)
    if learning_blink_key.keys != None:  # we had a response
        learning1_loop.addData('learning_blink_key.rt', learning_blink_key.rt)
    # the Routine "learning_blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'learning1_loop'


# --- Prepare to start Routine "break1" ---
continueRoutine = True
# update component parameters for each repeat
break1_keys.keys = []
break1_keys.rt = []
_break1_keys_allKeys = []
# keep track of which components have finished
break1Components = [break1_text, break1_keys, break1_trigs]
for thisComponent in break1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "break1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break1_text* updates
    
    # if break1_text is starting this frame...
    if break1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break1_text.frameNStart = frameN  # exact frame index
        break1_text.tStart = t  # local t and not account for scr refresh
        break1_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break1_text.started')
        # update status
        break1_text.status = STARTED
        break1_text.setAutoDraw(True)
    
    # if break1_text is active this frame...
    if break1_text.status == STARTED:
        # update params
        pass
    
    # *break1_keys* updates
    waitOnFlip = False
    
    # if break1_keys is starting this frame...
    if break1_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break1_keys.frameNStart = frameN  # exact frame index
        break1_keys.tStart = t  # local t and not account for scr refresh
        break1_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1_keys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break1_keys.started')
        # update status
        break1_keys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break1_keys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break1_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break1_keys.status == STARTED and not waitOnFlip:
        theseKeys = break1_keys.getKeys(keyList=['return'], waitRelease=False)
        _break1_keys_allKeys.extend(theseKeys)
        if len(_break1_keys_allKeys):
            break1_keys.keys = _break1_keys_allKeys[-1].name  # just the last key pressed
            break1_keys.rt = _break1_keys_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if break1_trigs is starting this frame...
    if break1_trigs.status == NOT_STARTED and break1_text.status == STARTED:
        # keep track of start time/frame for later
        break1_trigs.frameNStart = frameN  # exact frame index
        break1_trigs.tStart = t  # local t and not account for scr refresh
        break1_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break1_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break1_trigs.started')
        # update status
        break1_trigs.status = STARTED
        win.callOnFlip(break1_trigs.write, bytes(chr(15), 'utf8'))
        break1_trigs.status = STARTED
    
    # if break1_trigs is stopping this frame...
    if break1_trigs.status == STARTED:
        if bool(len(_break1_keys_allKeys)):
            # keep track of stop time/frame for later
            break1_trigs.tStop = t  # not accounting for scr refresh
            break1_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break1_trigs.stopped')
            # update status
            break1_trigs.status = FINISHED
            win.callOnFlip(break1_trigs.write, bytes(chr(16), 'utf8'))
            break1_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "break1" ---
for thisComponent in break1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if break1_keys.keys in ['', [], None]:  # No response was made
    break1_keys.keys = None
thisExp.addData('break1_keys.keys',break1_keys.keys)
if break1_keys.keys != None:  # we had a response
    thisExp.addData('break1_keys.rt', break1_keys.rt)
thisExp.nextEntry()
# the Routine "break1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "sd2_instructions" ---
continueRoutine = True
# update component parameters for each repeat
sd2_instruction_keyboard.keys = []
sd2_instruction_keyboard.rt = []
_sd2_instruction_keyboard_allKeys = []
# keep track of which components have finished
sd2_instructionsComponents = [sd2_instruction_text, L_alien_body_sd2_instruction, R_alien_body_sd2_instruction, L_alien_eye_sd2_instruction, R_alien_eye_sd2_instruction, sd2_instruction_keyboard, sd2_instruction_trigs]
for thisComponent in sd2_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "sd2_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sd2_instruction_text* updates
    
    # if sd2_instruction_text is starting this frame...
    if sd2_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sd2_instruction_text.frameNStart = frameN  # exact frame index
        sd2_instruction_text.tStart = t  # local t and not account for scr refresh
        sd2_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd2_instruction_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd2_instruction_text.started')
        # update status
        sd2_instruction_text.status = STARTED
        sd2_instruction_text.setAutoDraw(True)
    
    # if sd2_instruction_text is active this frame...
    if sd2_instruction_text.status == STARTED:
        # update params
        pass
    
    # *L_alien_body_sd2_instruction* updates
    
    # if L_alien_body_sd2_instruction is starting this frame...
    if L_alien_body_sd2_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_body_sd2_instruction.frameNStart = frameN  # exact frame index
        L_alien_body_sd2_instruction.tStart = t  # local t and not account for scr refresh
        L_alien_body_sd2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_body_sd2_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_body_sd2_instruction.started')
        # update status
        L_alien_body_sd2_instruction.status = STARTED
        L_alien_body_sd2_instruction.setAutoDraw(True)
    
    # if L_alien_body_sd2_instruction is active this frame...
    if L_alien_body_sd2_instruction.status == STARTED:
        # update params
        pass
    
    # *R_alien_body_sd2_instruction* updates
    
    # if R_alien_body_sd2_instruction is starting this frame...
    if R_alien_body_sd2_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_body_sd2_instruction.frameNStart = frameN  # exact frame index
        R_alien_body_sd2_instruction.tStart = t  # local t and not account for scr refresh
        R_alien_body_sd2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_body_sd2_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_body_sd2_instruction.started')
        # update status
        R_alien_body_sd2_instruction.status = STARTED
        R_alien_body_sd2_instruction.setAutoDraw(True)
    
    # if R_alien_body_sd2_instruction is active this frame...
    if R_alien_body_sd2_instruction.status == STARTED:
        # update params
        pass
    
    # *L_alien_eye_sd2_instruction* updates
    
    # if L_alien_eye_sd2_instruction is starting this frame...
    if L_alien_eye_sd2_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_eye_sd2_instruction.frameNStart = frameN  # exact frame index
        L_alien_eye_sd2_instruction.tStart = t  # local t and not account for scr refresh
        L_alien_eye_sd2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_eye_sd2_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_eye_sd2_instruction.started')
        # update status
        L_alien_eye_sd2_instruction.status = STARTED
        L_alien_eye_sd2_instruction.setAutoDraw(True)
    
    # if L_alien_eye_sd2_instruction is active this frame...
    if L_alien_eye_sd2_instruction.status == STARTED:
        # update params
        pass
    
    # *R_alien_eye_sd2_instruction* updates
    
    # if R_alien_eye_sd2_instruction is starting this frame...
    if R_alien_eye_sd2_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_eye_sd2_instruction.frameNStart = frameN  # exact frame index
        R_alien_eye_sd2_instruction.tStart = t  # local t and not account for scr refresh
        R_alien_eye_sd2_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_eye_sd2_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_eye_sd2_instruction.started')
        # update status
        R_alien_eye_sd2_instruction.status = STARTED
        R_alien_eye_sd2_instruction.setAutoDraw(True)
    
    # if R_alien_eye_sd2_instruction is active this frame...
    if R_alien_eye_sd2_instruction.status == STARTED:
        # update params
        pass
    
    # *sd2_instruction_keyboard* updates
    waitOnFlip = False
    
    # if sd2_instruction_keyboard is starting this frame...
    if sd2_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        sd2_instruction_keyboard.frameNStart = frameN  # exact frame index
        sd2_instruction_keyboard.tStart = t  # local t and not account for scr refresh
        sd2_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd2_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd2_instruction_keyboard.started')
        # update status
        sd2_instruction_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sd2_instruction_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sd2_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sd2_instruction_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = sd2_instruction_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _sd2_instruction_keyboard_allKeys.extend(theseKeys)
        if len(_sd2_instruction_keyboard_allKeys):
            sd2_instruction_keyboard.keys = _sd2_instruction_keyboard_allKeys[-1].name  # just the last key pressed
            sd2_instruction_keyboard.rt = _sd2_instruction_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if sd2_instruction_trigs is starting this frame...
    if sd2_instruction_trigs.status == NOT_STARTED and sd2_instruction_text.status == STARTED:
        # keep track of start time/frame for later
        sd2_instruction_trigs.frameNStart = frameN  # exact frame index
        sd2_instruction_trigs.tStart = t  # local t and not account for scr refresh
        sd2_instruction_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd2_instruction_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd2_instruction_trigs.started')
        # update status
        sd2_instruction_trigs.status = STARTED
        win.callOnFlip(sd2_instruction_trigs.write, bytes(chr(5), 'utf8'))
        sd2_instruction_trigs.status = STARTED
    
    # if sd2_instruction_trigs is stopping this frame...
    if sd2_instruction_trigs.status == STARTED:
        if bool(len(_sd2_instruction_keyboard_allKeys)):
            # keep track of stop time/frame for later
            sd2_instruction_trigs.tStop = t  # not accounting for scr refresh
            sd2_instruction_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd2_instruction_trigs.stopped')
            # update status
            sd2_instruction_trigs.status = FINISHED
            win.callOnFlip(sd2_instruction_trigs.write, bytes(chr(6), 'utf8'))
            sd2_instruction_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sd2_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "sd2_instructions" ---
for thisComponent in sd2_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if sd2_instruction_keyboard.keys in ['', [], None]:  # No response was made
    sd2_instruction_keyboard.keys = None
thisExp.addData('sd2_instruction_keyboard.keys',sd2_instruction_keyboard.keys)
if sd2_instruction_keyboard.keys != None:  # we had a response
    thisExp.addData('sd2_instruction_keyboard.rt', sd2_instruction_keyboard.rt)
thisExp.nextEntry()
# the Routine "sd2_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sd2_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/sd.xlsx'),
    seed=None, name='sd2_loop')
thisExp.addLoop(sd2_loop)  # add the loop to the experiment
thisSd2_loop = sd2_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSd2_loop.rgb)
if thisSd2_loop != None:
    for paramName in thisSd2_loop:
        exec('{} = thisSd2_loop[paramName]'.format(paramName))

for thisSd2_loop in sd2_loop:
    currentLoop = sd2_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSd2_loop.rgb)
    if thisSd2_loop != None:
        for paramName in thisSd2_loop:
            exec('{} = thisSd2_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "sd_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_trial_no_code
    sd_trial_nums = 'Progress: ' + str(currentLoop.thisN + 1) + ' of ' + str(currentLoop.nTotal)
    
    sd_trial_no.setText(sd_trial_nums)
    # keep track of which components have finished
    sd_fixationComponents = [sd_trial_no, sd_fixation_cross, sd_fix_trigs]
    for thisComponent in sd_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no* updates
        
        # if sd_trial_no is starting this frame...
        if sd_trial_no.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_trial_no.frameNStart = frameN  # exact frame index
            sd_trial_no.tStart = t  # local t and not account for scr refresh
            sd_trial_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no.started')
            # update status
            sd_trial_no.status = STARTED
            sd_trial_no.setAutoDraw(True)
        
        # if sd_trial_no is active this frame...
        if sd_trial_no.status == STARTED:
            # update params
            pass
        
        # if sd_trial_no is stopping this frame...
        if sd_trial_no.status == STARTED:
            if frameN >= (sd_trial_no.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_trial_no.tStop = t  # not accounting for scr refresh
                sd_trial_no.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_trial_no.stopped')
                # update status
                sd_trial_no.status = FINISHED
                sd_trial_no.setAutoDraw(False)
        
        # *sd_fixation_cross* updates
        
        # if sd_fixation_cross is starting this frame...
        if sd_fixation_cross.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_fixation_cross.frameNStart = frameN  # exact frame index
            sd_fixation_cross.tStart = t  # local t and not account for scr refresh
            sd_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fixation_cross.started')
            # update status
            sd_fixation_cross.status = STARTED
            sd_fixation_cross.setAutoDraw(True)
        
        # if sd_fixation_cross is active this frame...
        if sd_fixation_cross.status == STARTED:
            # update params
            pass
        
        # if sd_fixation_cross is stopping this frame...
        if sd_fixation_cross.status == STARTED:
            if frameN >= (sd_fixation_cross.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_fixation_cross.tStop = t  # not accounting for scr refresh
                sd_fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fixation_cross.stopped')
                # update status
                sd_fixation_cross.status = FINISHED
                sd_fixation_cross.setAutoDraw(False)
        
        # if sd_fix_trigs is starting this frame...
        if sd_fix_trigs.status == NOT_STARTED and sd_fixation_cross.status == STARTED:
            # keep track of start time/frame for later
            sd_fix_trigs.frameNStart = frameN  # exact frame index
            sd_fix_trigs.tStart = t  # local t and not account for scr refresh
            sd_fix_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fix_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fix_trigs.started')
            # update status
            sd_fix_trigs.status = STARTED
            win.callOnFlip(sd_fix_trigs.write, bytes(chr(177), 'utf8'))
            sd_fix_trigs.status = STARTED
        
        # if sd_fix_trigs is stopping this frame...
        if sd_fix_trigs.status == STARTED:
            if bool(sd_fixation_cross.status == FINISHED):
                # keep track of stop time/frame for later
                sd_fix_trigs.tStop = t  # not accounting for scr refresh
                sd_fix_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fix_trigs.stopped')
                # update status
                sd_fix_trigs.status = FINISHED
                win.callOnFlip(sd_fix_trigs.write, bytes(chr(178), 'utf8'))
                sd_fix_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_fixation" ---
    for thisComponent in sd_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "sd_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "same_diff" ---
    continueRoutine = True
    # update component parameters for each repeat
    sd_trial_no_2.setText(sd_trial_nums)
    L_alien_eye_sd.setOri(sd_L_eye_ori)
    L_alien_eye_sd.setSF(sd_L_eye_sf)
    R_alien_eye_sd.setOri(sd_R_eye_ori)
    R_alien_eye_sd.setSF(sd_R_eye_sf)
    key_resp_sd.keys = []
    key_resp_sd.rt = []
    _key_resp_sd_allKeys = []
    # keep track of which components have finished
    same_diffComponents = [sd_trial_no_2, L_alien_body_sd, R_alien_body_sd, L_alien_eye_sd, R_alien_eye_sd, sd_photo_box, sd_stim_trigs, key_resp_sd, sd_hint]
    for thisComponent in same_diffComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "same_diff" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_2* updates
        
        # if sd_trial_no_2 is starting this frame...
        if sd_trial_no_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_2.frameNStart = frameN  # exact frame index
            sd_trial_no_2.tStart = t  # local t and not account for scr refresh
            sd_trial_no_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_2.started')
            # update status
            sd_trial_no_2.status = STARTED
            sd_trial_no_2.setAutoDraw(True)
        
        # if sd_trial_no_2 is active this frame...
        if sd_trial_no_2.status == STARTED:
            # update params
            pass
        
        # *L_alien_body_sd* updates
        
        # if L_alien_body_sd is starting this frame...
        if L_alien_body_sd.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            L_alien_body_sd.frameNStart = frameN  # exact frame index
            L_alien_body_sd.tStart = t  # local t and not account for scr refresh
            L_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_body_sd.started')
            # update status
            L_alien_body_sd.status = STARTED
            L_alien_body_sd.setAutoDraw(True)
        
        # if L_alien_body_sd is active this frame...
        if L_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_body_sd is stopping this frame...
        if L_alien_body_sd.status == STARTED:
            if frameN >= (L_alien_body_sd.frameNStart + 12):
                # keep track of stop time/frame for later
                L_alien_body_sd.tStop = t  # not accounting for scr refresh
                L_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_body_sd.stopped')
                # update status
                L_alien_body_sd.status = FINISHED
                L_alien_body_sd.setAutoDraw(False)
        
        # *R_alien_body_sd* updates
        
        # if R_alien_body_sd is starting this frame...
        if R_alien_body_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_body_sd.frameNStart = frameN  # exact frame index
            R_alien_body_sd.tStart = t  # local t and not account for scr refresh
            R_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_body_sd.started')
            # update status
            R_alien_body_sd.status = STARTED
            R_alien_body_sd.setAutoDraw(True)
        
        # if R_alien_body_sd is active this frame...
        if R_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_body_sd is stopping this frame...
        if R_alien_body_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_body_sd.tStop = t  # not accounting for scr refresh
                R_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_body_sd.stopped')
                # update status
                R_alien_body_sd.status = FINISHED
                R_alien_body_sd.setAutoDraw(False)
        
        # *L_alien_eye_sd* updates
        
        # if L_alien_eye_sd is starting this frame...
        if L_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            L_alien_eye_sd.frameNStart = frameN  # exact frame index
            L_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            L_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_eye_sd.started')
            # update status
            L_alien_eye_sd.status = STARTED
            L_alien_eye_sd.setAutoDraw(True)
        
        # if L_alien_eye_sd is active this frame...
        if L_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_eye_sd is stopping this frame...
        if L_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                L_alien_eye_sd.tStop = t  # not accounting for scr refresh
                L_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_eye_sd.stopped')
                # update status
                L_alien_eye_sd.status = FINISHED
                L_alien_eye_sd.setAutoDraw(False)
        
        # *R_alien_eye_sd* updates
        
        # if R_alien_eye_sd is starting this frame...
        if R_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_eye_sd.frameNStart = frameN  # exact frame index
            R_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            R_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_eye_sd.started')
            # update status
            R_alien_eye_sd.status = STARTED
            R_alien_eye_sd.setAutoDraw(True)
        
        # if R_alien_eye_sd is active this frame...
        if R_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_eye_sd is stopping this frame...
        if R_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_eye_sd.tStop = t  # not accounting for scr refresh
                R_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_eye_sd.stopped')
                # update status
                R_alien_eye_sd.status = FINISHED
                R_alien_eye_sd.setAutoDraw(False)
        
        # *sd_photo_box* updates
        
        # if sd_photo_box is starting this frame...
        if sd_photo_box.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_photo_box.frameNStart = frameN  # exact frame index
            sd_photo_box.tStart = t  # local t and not account for scr refresh
            sd_photo_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_photo_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_photo_box.started')
            # update status
            sd_photo_box.status = STARTED
            sd_photo_box.setAutoDraw(True)
        
        # if sd_photo_box is active this frame...
        if sd_photo_box.status == STARTED:
            # update params
            pass
        
        # if sd_photo_box is stopping this frame...
        if sd_photo_box.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_photo_box.tStop = t  # not accounting for scr refresh
                sd_photo_box.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_photo_box.stopped')
                # update status
                sd_photo_box.status = FINISHED
                sd_photo_box.setAutoDraw(False)
        
        # if sd_stim_trigs is starting this frame...
        if sd_stim_trigs.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_stim_trigs.frameNStart = frameN  # exact frame index
            sd_stim_trigs.tStart = t  # local t and not account for scr refresh
            sd_stim_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_stim_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_stim_trigs.started')
            # update status
            sd_stim_trigs.status = STARTED
            win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_ontrig), 'utf8'))
            sd_stim_trigs.status = STARTED
        
        # if sd_stim_trigs is stopping this frame...
        if sd_stim_trigs.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_stim_trigs.tStop = t  # not accounting for scr refresh
                sd_stim_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_stim_trigs.stopped')
                # update status
                sd_stim_trigs.status = FINISHED
                win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_offtrig), 'utf8'))
                sd_stim_trigs.status = FINISHED
        
        # *key_resp_sd* updates
        waitOnFlip = False
        
        # if key_resp_sd is starting this frame...
        if key_resp_sd.status == NOT_STARTED and L_alien_body_sd.status == FINISHED:
            # keep track of start time/frame for later
            key_resp_sd.frameNStart = frameN  # exact frame index
            key_resp_sd.tStart = t  # local t and not account for scr refresh
            key_resp_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_sd.started')
            # update status
            key_resp_sd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_sd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_sd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_sd.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_sd.getKeys(keyList=['s','d'], waitRelease=False)
            _key_resp_sd_allKeys.extend(theseKeys)
            if len(_key_resp_sd_allKeys):
                key_resp_sd.keys = _key_resp_sd_allKeys[-1].name  # just the last key pressed
                key_resp_sd.rt = _key_resp_sd_allKeys[-1].rt
                # was this correct?
                if (key_resp_sd.keys == str(sd_correct_key)) or (key_resp_sd.keys == sd_correct_key):
                    key_resp_sd.corr = 1
                else:
                    key_resp_sd.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *sd_hint* updates
        
        # if sd_hint is starting this frame...
        if sd_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sd_hint.frameNStart = frameN  # exact frame index
            sd_hint.tStart = t  # local t and not account for scr refresh
            sd_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_hint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_hint.started')
            # update status
            sd_hint.status = STARTED
            sd_hint.setAutoDraw(True)
        
        # if sd_hint is active this frame...
        if sd_hint.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in same_diffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "same_diff" ---
    for thisComponent in same_diffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_sd.keys in ['', [], None]:  # No response was made
        key_resp_sd.keys = None
        # was no response the correct answer?!
        if str(sd_correct_key).lower() == 'none':
           key_resp_sd.corr = 1;  # correct non-response
        else:
           key_resp_sd.corr = 0;  # failed to respond (incorrectly)
    # store data for sd2_loop (TrialHandler)
    sd2_loop.addData('key_resp_sd.keys',key_resp_sd.keys)
    sd2_loop.addData('key_resp_sd.corr', key_resp_sd.corr)
    if key_resp_sd.keys != None:  # we had a response
        sd2_loop.addData('key_resp_sd.rt', key_resp_sd.rt)
    # the Routine "same_diff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sd_resp_triggers" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_resp_trigger_code
    if key_resp_sd.corr:
        sd_acc_trig = 169
    else:
        sd_acc_trig = 168
    # keep track of which components have finished
    sd_resp_triggersComponents = [sd_resp_trigs]
    for thisComponent in sd_resp_triggersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_resp_triggers" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sd_resp_trigs is starting this frame...
        if sd_resp_trigs.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_resp_trigs.frameNStart = frameN  # exact frame index
            sd_resp_trigs.tStart = t  # local t and not account for scr refresh
            sd_resp_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_resp_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_resp_trigs.started')
            # update status
            sd_resp_trigs.status = STARTED
            win.callOnFlip(sd_resp_trigs.write, bytes(chr(167), 'utf8'))
            sd_resp_trigs.status = STARTED
        
        # if sd_resp_trigs is stopping this frame...
        if sd_resp_trigs.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > .1-frameTolerance:
                # keep track of stop time/frame for later
                sd_resp_trigs.tStop = t  # not accounting for scr refresh
                sd_resp_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_resp_trigs.stopped')
                # update status
                sd_resp_trigs.status = FINISHED
                win.callOnFlip(sd_resp_trigs.write, bytes(chr(sd_acc_trig), 'utf8'))
                sd_resp_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_resp_triggersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_resp_triggers" ---
    for thisComponent in sd_resp_triggersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.100000)
    
    # --- Prepare to start Routine "sd_blink" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_blink_code
    sd_blink_counter = sd_blink_counter + 1
    if sd_blink_counter == 4:
        sd_blink_counter = 0
    else:
        continueRoutine = False
    sd_trial_no_3.setText(sd_trial_nums)
    sd_blink_key.keys = []
    sd_blink_key.rt = []
    _sd_blink_key_allKeys = []
    # keep track of which components have finished
    sd_blinkComponents = [sd_trial_no_3, sd1_blink_text, sd_blink_key, sd_blink_trigs]
    for thisComponent in sd_blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_blink" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_3* updates
        
        # if sd_trial_no_3 is starting this frame...
        if sd_trial_no_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_3.frameNStart = frameN  # exact frame index
            sd_trial_no_3.tStart = t  # local t and not account for scr refresh
            sd_trial_no_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_3.started')
            # update status
            sd_trial_no_3.status = STARTED
            sd_trial_no_3.setAutoDraw(True)
        
        # if sd_trial_no_3 is active this frame...
        if sd_trial_no_3.status == STARTED:
            # update params
            pass
        
        # *sd1_blink_text* updates
        
        # if sd1_blink_text is starting this frame...
        if sd1_blink_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd1_blink_text.frameNStart = frameN  # exact frame index
            sd1_blink_text.tStart = t  # local t and not account for scr refresh
            sd1_blink_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd1_blink_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd1_blink_text.started')
            # update status
            sd1_blink_text.status = STARTED
            sd1_blink_text.setAutoDraw(True)
        
        # if sd1_blink_text is active this frame...
        if sd1_blink_text.status == STARTED:
            # update params
            pass
        
        # *sd_blink_key* updates
        waitOnFlip = False
        
        # if sd_blink_key is starting this frame...
        if sd_blink_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_blink_key.frameNStart = frameN  # exact frame index
            sd_blink_key.tStart = t  # local t and not account for scr refresh
            sd_blink_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_key.started')
            # update status
            sd_blink_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sd_blink_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sd_blink_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sd_blink_key.status == STARTED and not waitOnFlip:
            theseKeys = sd_blink_key.getKeys(keyList=['space'], waitRelease=False)
            _sd_blink_key_allKeys.extend(theseKeys)
            if len(_sd_blink_key_allKeys):
                sd_blink_key.keys = _sd_blink_key_allKeys[-1].name  # just the last key pressed
                sd_blink_key.rt = _sd_blink_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if sd_blink_trigs is starting this frame...
        if sd_blink_trigs.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_blink_trigs.frameNStart = frameN  # exact frame index
            sd_blink_trigs.tStart = t  # local t and not account for scr refresh
            sd_blink_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_trigs.started')
            # update status
            sd_blink_trigs.status = STARTED
            win.callOnFlip(sd_blink_trigs.write, bytes(chr(179), 'utf8'))
            sd_blink_trigs.status = STARTED
        
        # if sd_blink_trigs is stopping this frame...
        if sd_blink_trigs.status == STARTED:
            if bool(sd_blink_key.keys == 'space'):
                # keep track of stop time/frame for later
                sd_blink_trigs.tStop = t  # not accounting for scr refresh
                sd_blink_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_blink_trigs.stopped')
                # update status
                sd_blink_trigs.status = FINISHED
                win.callOnFlip(sd_blink_trigs.write, bytes(chr(180), 'utf8'))
                sd_blink_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_blink" ---
    for thisComponent in sd_blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sd_blink_key.keys in ['', [], None]:  # No response was made
        sd_blink_key.keys = None
    sd2_loop.addData('sd_blink_key.keys',sd_blink_key.keys)
    if sd_blink_key.keys != None:  # we had a response
        sd2_loop.addData('sd_blink_key.rt', sd_blink_key.rt)
    # the Routine "sd_blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'sd2_loop'


# --- Prepare to start Routine "break2" ---
continueRoutine = True
# update component parameters for each repeat
break2_keys.keys = []
break2_keys.rt = []
_break2_keys_allKeys = []
# keep track of which components have finished
break2Components = [break2_text, break2_keys, break2_trigs]
for thisComponent in break2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "break2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break2_text* updates
    
    # if break2_text is starting this frame...
    if break2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break2_text.frameNStart = frameN  # exact frame index
        break2_text.tStart = t  # local t and not account for scr refresh
        break2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break2_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break2_text.started')
        # update status
        break2_text.status = STARTED
        break2_text.setAutoDraw(True)
    
    # if break2_text is active this frame...
    if break2_text.status == STARTED:
        # update params
        pass
    
    # *break2_keys* updates
    waitOnFlip = False
    
    # if break2_keys is starting this frame...
    if break2_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break2_keys.frameNStart = frameN  # exact frame index
        break2_keys.tStart = t  # local t and not account for scr refresh
        break2_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break2_keys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break2_keys.started')
        # update status
        break2_keys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break2_keys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break2_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break2_keys.status == STARTED and not waitOnFlip:
        theseKeys = break2_keys.getKeys(keyList=['return'], waitRelease=False)
        _break2_keys_allKeys.extend(theseKeys)
        if len(_break2_keys_allKeys):
            break2_keys.keys = _break2_keys_allKeys[-1].name  # just the last key pressed
            break2_keys.rt = _break2_keys_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if break2_trigs is starting this frame...
    if break2_trigs.status == NOT_STARTED and break2_text.status == STARTED:
        # keep track of start time/frame for later
        break2_trigs.frameNStart = frameN  # exact frame index
        break2_trigs.tStart = t  # local t and not account for scr refresh
        break2_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break2_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break2_trigs.started')
        # update status
        break2_trigs.status = STARTED
        win.callOnFlip(break2_trigs.write, bytes(chr(17), 'utf8'))
        break2_trigs.status = STARTED
    
    # if break2_trigs is stopping this frame...
    if break2_trigs.status == STARTED:
        if bool(len(_break2_keys_allKeys)):
            # keep track of stop time/frame for later
            break2_trigs.tStop = t  # not accounting for scr refresh
            break2_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break2_trigs.stopped')
            # update status
            break2_trigs.status = FINISHED
            win.callOnFlip(break2_trigs.write, bytes(chr(18), 'utf8'))
            break2_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "break2" ---
for thisComponent in break2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if break2_keys.keys in ['', [], None]:  # No response was made
    break2_keys.keys = None
thisExp.addData('break2_keys.keys',break2_keys.keys)
if break2_keys.keys != None:  # we had a response
    thisExp.addData('break2_keys.rt', break2_keys.rt)
thisExp.nextEntry()
# the Routine "break2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning2_instructions" ---
continueRoutine = True
# update component parameters for each repeat
learning2_keyboard.keys = []
learning2_keyboard.rt = []
_learning2_keyboard_allKeys = []
# keep track of which components have finished
learning2_instructionsComponents = [alienBodyDemo2, alienEyeDemo2, explorerDemo2_U, instructionLearn2, learning2_keyboard, learn2_instruction_trigs]
for thisComponent in learning2_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "learning2_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo2* updates
    
    # if alienBodyDemo2 is starting this frame...
    if alienBodyDemo2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo2.frameNStart = frameN  # exact frame index
        alienBodyDemo2.tStart = t  # local t and not account for scr refresh
        alienBodyDemo2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienBodyDemo2.started')
        # update status
        alienBodyDemo2.status = STARTED
        alienBodyDemo2.setAutoDraw(True)
    
    # if alienBodyDemo2 is active this frame...
    if alienBodyDemo2.status == STARTED:
        # update params
        pass
    
    # *alienEyeDemo2* updates
    
    # if alienEyeDemo2 is starting this frame...
    if alienEyeDemo2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo2.frameNStart = frameN  # exact frame index
        alienEyeDemo2.tStart = t  # local t and not account for scr refresh
        alienEyeDemo2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'alienEyeDemo2.started')
        # update status
        alienEyeDemo2.status = STARTED
        alienEyeDemo2.setAutoDraw(True)
    
    # if alienEyeDemo2 is active this frame...
    if alienEyeDemo2.status == STARTED:
        # update params
        pass
    
    # *explorerDemo2_U* updates
    
    # if explorerDemo2_U is starting this frame...
    if explorerDemo2_U.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo2_U.frameNStart = frameN  # exact frame index
        explorerDemo2_U.tStart = t  # local t and not account for scr refresh
        explorerDemo2_U.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo2_U, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'explorerDemo2_U.started')
        # update status
        explorerDemo2_U.status = STARTED
        explorerDemo2_U.setAutoDraw(True)
    
    # if explorerDemo2_U is active this frame...
    if explorerDemo2_U.status == STARTED:
        # update params
        pass
    
    # *instructionLearn2* updates
    
    # if instructionLearn2 is starting this frame...
    if instructionLearn2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn2.frameNStart = frameN  # exact frame index
        instructionLearn2.tStart = t  # local t and not account for scr refresh
        instructionLearn2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionLearn2.started')
        # update status
        instructionLearn2.status = STARTED
        instructionLearn2.setAutoDraw(True)
    
    # if instructionLearn2 is active this frame...
    if instructionLearn2.status == STARTED:
        # update params
        pass
    
    # *learning2_keyboard* updates
    waitOnFlip = False
    
    # if learning2_keyboard is starting this frame...
    if learning2_keyboard.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        learning2_keyboard.frameNStart = frameN  # exact frame index
        learning2_keyboard.tStart = t  # local t and not account for scr refresh
        learning2_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning2_keyboard, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learning2_keyboard.started')
        # update status
        learning2_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(learning2_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(learning2_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if learning2_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = learning2_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _learning2_keyboard_allKeys.extend(theseKeys)
        if len(_learning2_keyboard_allKeys):
            learning2_keyboard.keys = _learning2_keyboard_allKeys[-1].name  # just the last key pressed
            learning2_keyboard.rt = _learning2_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if learn2_instruction_trigs is starting this frame...
    if learn2_instruction_trigs.status == NOT_STARTED and instructionLearn2.status == STARTED:
        # keep track of start time/frame for later
        learn2_instruction_trigs.frameNStart = frameN  # exact frame index
        learn2_instruction_trigs.tStart = t  # local t and not account for scr refresh
        learn2_instruction_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learn2_instruction_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'learn2_instruction_trigs.started')
        # update status
        learn2_instruction_trigs.status = STARTED
        win.callOnFlip(learn2_instruction_trigs.write, bytes(chr(7), 'utf8'))
        learn2_instruction_trigs.status = STARTED
    
    # if learn2_instruction_trigs is stopping this frame...
    if learn2_instruction_trigs.status == STARTED:
        if bool(len(_learning2_keyboard_allKeys)):
            # keep track of stop time/frame for later
            learn2_instruction_trigs.tStop = t  # not accounting for scr refresh
            learn2_instruction_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn2_instruction_trigs.stopped')
            # update status
            learn2_instruction_trigs.status = FINISHED
            win.callOnFlip(learn2_instruction_trigs.write, bytes(chr(8), 'utf8'))
            learn2_instruction_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning2_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning2_instructions" ---
for thisComponent in learning2_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if learning2_keyboard.keys in ['', [], None]:  # No response was made
    learning2_keyboard.keys = None
thisExp.addData('learning2_keyboard.keys',learning2_keyboard.keys)
if learning2_keyboard.keys != None:  # we had a response
    thisExp.addData('learning2_keyboard.rt', learning2_keyboard.rt)
thisExp.nextEntry()
# the Routine "learning2_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learning2_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(learning_sequence2),
    seed=None, name='learning2_loop')
thisExp.addLoop(learning2_loop)  # add the loop to the experiment
thisLearning2_loop = learning2_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning2_loop.rgb)
if thisLearning2_loop != None:
    for paramName in thisLearning2_loop:
        exec('{} = thisLearning2_loop[paramName]'.format(paramName))

for thisLearning2_loop in learning2_loop:
    currentLoop = learning2_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLearning2_loop.rgb)
    if thisLearning2_loop != None:
        for paramName in thisLearning2_loop:
            exec('{} = thisLearning2_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "learning_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learn_trial_no_code
    learn_trial_nums = "Training Progress: " + str(currentLoop.thisN + 1) + " of " + str(currentLoop.nTotal);
    
    learn_trialNum_1.setText(learn_trial_nums)
    # keep track of which components have finished
    learning_fixationComponents = [learn_trialNum_1, fixationLearn, learn_fix_trigs]
    for thisComponent in learning_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_1* updates
        
        # if learn_trialNum_1 is starting this frame...
        if learn_trialNum_1.status == NOT_STARTED and fixationLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_1.frameNStart = frameN  # exact frame index
            learn_trialNum_1.tStart = t  # local t and not account for scr refresh
            learn_trialNum_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_1.started')
            # update status
            learn_trialNum_1.status = STARTED
            learn_trialNum_1.setAutoDraw(True)
        
        # if learn_trialNum_1 is active this frame...
        if learn_trialNum_1.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_1 is stopping this frame...
        if learn_trialNum_1.status == STARTED:
            if bool(fixationLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_1.tStop = t  # not accounting for scr refresh
                learn_trialNum_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_1.stopped')
                # update status
                learn_trialNum_1.status = FINISHED
                learn_trialNum_1.setAutoDraw(False)
        
        # *fixationLearn* updates
        
        # if fixationLearn is starting this frame...
        if fixationLearn.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            fixationLearn.frameNStart = frameN  # exact frame index
            fixationLearn.tStart = t  # local t and not account for scr refresh
            fixationLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixationLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixationLearn.started')
            # update status
            fixationLearn.status = STARTED
            fixationLearn.setAutoDraw(True)
        
        # if fixationLearn is active this frame...
        if fixationLearn.status == STARTED:
            # update params
            pass
        
        # if fixationLearn is stopping this frame...
        if fixationLearn.status == STARTED:
            if frameN >= (fixationLearn.frameNStart + 30):
                # keep track of stop time/frame for later
                fixationLearn.tStop = t  # not accounting for scr refresh
                fixationLearn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixationLearn.stopped')
                # update status
                fixationLearn.status = FINISHED
                fixationLearn.setAutoDraw(False)
        
        # if learn_fix_trigs is starting this frame...
        if learn_fix_trigs.status == NOT_STARTED and fixationLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_fix_trigs.frameNStart = frameN  # exact frame index
            learn_fix_trigs.tStart = t  # local t and not account for scr refresh
            learn_fix_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_fix_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_fix_trigs.started')
            # update status
            learn_fix_trigs.status = STARTED
            win.callOnFlip(learn_fix_trigs.write, bytes(chr(177), 'utf8'))
            learn_fix_trigs.status = STARTED
        
        # if learn_fix_trigs is stopping this frame...
        if learn_fix_trigs.status == STARTED:
            if bool(fixationLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_fix_trigs.tStop = t  # not accounting for scr refresh
                learn_fix_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_fix_trigs.stopped')
                # update status
                learn_fix_trigs.status = FINISHED
                win.callOnFlip(learn_fix_trigs.write, bytes(chr(178), 'utf8'))
                learn_fix_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_fixation" ---
    for thisComponent in learning_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "learning_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_presentation" ---
    continueRoutine = True
    # update component parameters for each repeat
    learn_trialNum_2.setText(learn_trial_nums)
    alienEyeLearn.setOri(learn_ori_val)
    alienEyeLearn.setSF(learn_freq_val)
    explorerLearn.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    key_resp_learn.keys = []
    key_resp_learn.rt = []
    _key_resp_learn_allKeys = []
    # keep track of which components have finished
    learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, learn_photo_box, key_resp_learn, learn_stim_trigs, learning_hint]
    for thisComponent in learning_presentationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_presentation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_2* updates
        
        # if learn_trialNum_2 is starting this frame...
        if learn_trialNum_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_2.frameNStart = frameN  # exact frame index
            learn_trialNum_2.tStart = t  # local t and not account for scr refresh
            learn_trialNum_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_2.started')
            # update status
            learn_trialNum_2.status = STARTED
            learn_trialNum_2.setAutoDraw(True)
        
        # if learn_trialNum_2 is active this frame...
        if learn_trialNum_2.status == STARTED:
            # update params
            pass
        
        # *alienBodyLearn* updates
        
        # if alienBodyLearn is starting this frame...
        if alienBodyLearn.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            alienBodyLearn.frameNStart = frameN  # exact frame index
            alienBodyLearn.tStart = t  # local t and not account for scr refresh
            alienBodyLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn.started')
            # update status
            alienBodyLearn.status = STARTED
            alienBodyLearn.setAutoDraw(True)
        
        # if alienBodyLearn is active this frame...
        if alienBodyLearn.status == STARTED:
            # update params
            pass
        
        # *alienEyeLearn* updates
        
        # if alienEyeLearn is starting this frame...
        if alienEyeLearn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn.frameNStart = frameN  # exact frame index
            alienEyeLearn.tStart = t  # local t and not account for scr refresh
            alienEyeLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn.started')
            # update status
            alienEyeLearn.status = STARTED
            alienEyeLearn.setAutoDraw(True)
        
        # if alienEyeLearn is active this frame...
        if alienEyeLearn.status == STARTED:
            # update params
            pass
        
        # *explorerLearn* updates
        
        # if explorerLearn is starting this frame...
        if explorerLearn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn.frameNStart = frameN  # exact frame index
            explorerLearn.tStart = t  # local t and not account for scr refresh
            explorerLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn.started')
            # update status
            explorerLearn.status = STARTED
            explorerLearn.setAutoDraw(True)
        
        # if explorerLearn is active this frame...
        if explorerLearn.status == STARTED:
            # update params
            pass
        
        # *learn_photo_box* updates
        
        # if learn_photo_box is starting this frame...
        if learn_photo_box.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_photo_box.frameNStart = frameN  # exact frame index
            learn_photo_box.tStart = t  # local t and not account for scr refresh
            learn_photo_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_photo_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_photo_box.started')
            # update status
            learn_photo_box.status = STARTED
            learn_photo_box.setAutoDraw(True)
        
        # if learn_photo_box is active this frame...
        if learn_photo_box.status == STARTED:
            # update params
            pass
        
        # *key_resp_learn* updates
        waitOnFlip = False
        
        # if key_resp_learn is starting this frame...
        if key_resp_learn.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            key_resp_learn.frameNStart = frameN  # exact frame index
            key_resp_learn.tStart = t  # local t and not account for scr refresh
            key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_learn.started')
            # update status
            key_resp_learn.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_learn.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_learn.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_learn.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_learn.getKeys(keyList=[learn_legal_keys1,learn_legal_keys2], waitRelease=False)
            _key_resp_learn_allKeys.extend(theseKeys)
            if len(_key_resp_learn_allKeys):
                key_resp_learn.keys = _key_resp_learn_allKeys[-1].name  # just the last key pressed
                key_resp_learn.rt = _key_resp_learn_allKeys[-1].rt
                # was this correct?
                if (key_resp_learn.keys == str(learn_correct_key)) or (key_resp_learn.keys == learn_correct_key):
                    key_resp_learn.corr = 1
                else:
                    key_resp_learn.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # if learn_stim_trigs is starting this frame...
        if learn_stim_trigs.status == NOT_STARTED and alienBodyLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_stim_trigs.frameNStart = frameN  # exact frame index
            learn_stim_trigs.tStart = t  # local t and not account for scr refresh
            learn_stim_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_stim_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_stim_trigs.started', t)
            # update status
            learn_stim_trigs.status = STARTED
            learn_stim_trigs.write(bytes(chr(learn_ontrig), 'utf8'))
            learn_stim_trigs.status = STARTED
        
        # if learn_stim_trigs is stopping this frame...
        if learn_stim_trigs.status == STARTED:
            if bool(len(_key_resp_learn_allKeys)):
                # keep track of stop time/frame for later
                learn_stim_trigs.tStop = t  # not accounting for scr refresh
                learn_stim_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_stim_trigs.stopped', t)
                # update status
                learn_stim_trigs.status = FINISHED
                learn_stim_trigs.write(bytes(chr(learn_offtrig), 'utf8'))
                learn_stim_trigs.status = FINISHED
        
        # *learning_hint* updates
        
        # if learning_hint is starting this frame...
        if learning_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            learning_hint.frameNStart = frameN  # exact frame index
            learning_hint.tStart = t  # local t and not account for scr refresh
            learning_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_hint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_hint.started')
            # update status
            learning_hint.status = STARTED
            learning_hint.setAutoDraw(True)
        
        # if learning_hint is active this frame...
        if learning_hint.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_presentationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_presentation" ---
    for thisComponent in learning_presentationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_learn.keys in ['', [], None]:  # No response was made
        key_resp_learn.keys = None
        # was no response the correct answer?!
        if str(learn_correct_key).lower() == 'none':
           key_resp_learn.corr = 1;  # correct non-response
        else:
           key_resp_learn.corr = 0;  # failed to respond (incorrectly)
    # store data for learning2_loop (TrialHandler)
    learning2_loop.addData('key_resp_learn.keys',key_resp_learn.keys)
    learning2_loop.addData('key_resp_learn.corr', key_resp_learn.corr)
    if key_resp_learn.keys != None:  # we had a response
        learning2_loop.addData('key_resp_learn.rt', key_resp_learn.rt)
    # the Routine "learning_presentation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learningFeedbackCODE
    if key_resp_learn.corr:
      feedback_tone = 'stimuli/bleep.wav'
      learn_acc_trig = 172
    else:
      feedback_tone = 'stimuli/buzz.wav'
      learn_acc_trig = 171
    feedbackSoundLearn.setSound(feedback_tone, secs=.25, hamming=True)
    feedbackSoundLearn.setVolume(1.0, log=False)
    learn_trialNum_3.setText(learn_trial_nums)
    alienEyeLearn2.setOri(learn_ori_val)
    alienEyeLearn2.setSF(learn_freq_val)
    explorerLearn2.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    # keep track of which components have finished
    learning_feedbackComponents = [feedbackSoundLearn, learn_feedback_trigs, learn_trialNum_3, alienBodyLearn2, alienEyeLearn2, explorerLearn2]
    for thisComponent in learning_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop feedbackSoundLearn
        
        # if feedbackSoundLearn is starting this frame...
        if feedbackSoundLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackSoundLearn.frameNStart = frameN  # exact frame index
            feedbackSoundLearn.tStart = t  # local t and not account for scr refresh
            feedbackSoundLearn.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('feedbackSoundLearn.started', tThisFlipGlobal)
            # update status
            feedbackSoundLearn.status = STARTED
            feedbackSoundLearn.play(when=win)  # sync with win flip
        
        # if feedbackSoundLearn is stopping this frame...
        if feedbackSoundLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackSoundLearn.tStartRefresh + .25-frameTolerance:
                # keep track of stop time/frame for later
                feedbackSoundLearn.tStop = t  # not accounting for scr refresh
                feedbackSoundLearn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedbackSoundLearn.stopped')
                # update status
                feedbackSoundLearn.status = FINISHED
                feedbackSoundLearn.stop()
        
        # if learn_feedback_trigs is starting this frame...
        if learn_feedback_trigs.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_feedback_trigs.frameNStart = frameN  # exact frame index
            learn_feedback_trigs.tStart = t  # local t and not account for scr refresh
            learn_feedback_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_feedback_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_feedback_trigs.started', t)
            # update status
            learn_feedback_trigs.status = STARTED
            learn_feedback_trigs.write(bytes(chr(170), 'utf8'))
            learn_feedback_trigs.status = STARTED
        
        # if learn_feedback_trigs is stopping this frame...
        if learn_feedback_trigs.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_feedback_trigs.tStop = t  # not accounting for scr refresh
                learn_feedback_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_feedback_trigs.stopped', t)
                # update status
                learn_feedback_trigs.status = FINISHED
                learn_feedback_trigs.write(bytes(chr(learn_acc_trig), 'utf8'))
                learn_feedback_trigs.status = FINISHED
        
        # *learn_trialNum_3* updates
        
        # if learn_trialNum_3 is starting this frame...
        if learn_trialNum_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_3.frameNStart = frameN  # exact frame index
            learn_trialNum_3.tStart = t  # local t and not account for scr refresh
            learn_trialNum_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_3.started')
            # update status
            learn_trialNum_3.status = STARTED
            learn_trialNum_3.setAutoDraw(True)
        
        # if learn_trialNum_3 is active this frame...
        if learn_trialNum_3.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_3 is stopping this frame...
        if learn_trialNum_3.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_3.tStop = t  # not accounting for scr refresh
                learn_trialNum_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_3.stopped')
                # update status
                learn_trialNum_3.status = FINISHED
                learn_trialNum_3.setAutoDraw(False)
        
        # *alienBodyLearn2* updates
        
        # if alienBodyLearn2 is starting this frame...
        if alienBodyLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            alienBodyLearn2.frameNStart = frameN  # exact frame index
            alienBodyLearn2.tStart = t  # local t and not account for scr refresh
            alienBodyLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn2.started')
            # update status
            alienBodyLearn2.status = STARTED
            alienBodyLearn2.setAutoDraw(True)
        
        # if alienBodyLearn2 is active this frame...
        if alienBodyLearn2.status == STARTED:
            # update params
            pass
        
        # if alienBodyLearn2 is stopping this frame...
        if alienBodyLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienBodyLearn2.tStop = t  # not accounting for scr refresh
                alienBodyLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienBodyLearn2.stopped')
                # update status
                alienBodyLearn2.status = FINISHED
                alienBodyLearn2.setAutoDraw(False)
        
        # *alienEyeLearn2* updates
        
        # if alienEyeLearn2 is starting this frame...
        if alienEyeLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn2.frameNStart = frameN  # exact frame index
            alienEyeLearn2.tStart = t  # local t and not account for scr refresh
            alienEyeLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn2.started')
            # update status
            alienEyeLearn2.status = STARTED
            alienEyeLearn2.setAutoDraw(True)
        
        # if alienEyeLearn2 is active this frame...
        if alienEyeLearn2.status == STARTED:
            # update params
            pass
        
        # if alienEyeLearn2 is stopping this frame...
        if alienEyeLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienEyeLearn2.tStop = t  # not accounting for scr refresh
                alienEyeLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienEyeLearn2.stopped')
                # update status
                alienEyeLearn2.status = FINISHED
                alienEyeLearn2.setAutoDraw(False)
        
        # *explorerLearn2* updates
        
        # if explorerLearn2 is starting this frame...
        if explorerLearn2.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn2.frameNStart = frameN  # exact frame index
            explorerLearn2.tStart = t  # local t and not account for scr refresh
            explorerLearn2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn2.started')
            # update status
            explorerLearn2.status = STARTED
            explorerLearn2.setAutoDraw(True)
        
        # if explorerLearn2 is active this frame...
        if explorerLearn2.status == STARTED:
            # update params
            pass
        
        # if explorerLearn2 is stopping this frame...
        if explorerLearn2.status == STARTED:
            if bool(feedbackSoundLearn.status == FINISHED):
                # keep track of stop time/frame for later
                explorerLearn2.tStop = t  # not accounting for scr refresh
                explorerLearn2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explorerLearn2.stopped')
                # update status
                explorerLearn2.status = FINISHED
                explorerLearn2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_feedback" ---
    for thisComponent in learning_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    feedbackSoundLearn.stop()  # ensure sound has stopped at end of routine
    # the Routine "learning_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_feedback_label" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learningLabelFeedbackCODE
    if learn_trial_type == 'friendly':
        labelLearn = 'stimuli/'+friendly_label+'.wav'
    elif learn_trial_type == 'hostile':
        labelLearn = 'stimuli/'+hostile_label+'.wav'
    
    if friendly_label == 'havnori':
        if learn_trial_type == 'friendly':
            label_trig = 174
        elif learn_trial_type == 'hostile':
            label_trig = 175
    elif friendly_label == 'gowachi':
        if learn_trial_type == 'friendly':
            label_trig = 175
        elif learn_trial_type == 'hostile':
            label_trig = 174
    else:
        label_trig = 176
    
    thisExp.addData('hostileLabel_learn', hostile_label)
    trainingLabelLearn.setSound(labelLearn, secs=.8, hamming=True)
    trainingLabelLearn.setVolume(label_vol, log=False)
    learn_trialNum_4.setText(learn_trial_nums)
    alienEyeLearn3.setOri(learn_ori_val)
    alienEyeLearn3.setSF(learn_freq_val)
    explorerLearn3.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    # keep track of which components have finished
    learning_feedback_labelComponents = [trainingLabelLearn, learn_label_trigs, learn_trialNum_4, alienBodyLearn3, alienEyeLearn3, explorerLearn3]
    for thisComponent in learning_feedback_labelComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_feedback_label" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop trainingLabelLearn
        
        # if trainingLabelLearn is starting this frame...
        if trainingLabelLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            trainingLabelLearn.frameNStart = frameN  # exact frame index
            trainingLabelLearn.tStart = t  # local t and not account for scr refresh
            trainingLabelLearn.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            trainingLabelLearn.status = STARTED
            trainingLabelLearn.play(when=win)  # sync with win flip
        
        # if trainingLabelLearn is stopping this frame...
        if trainingLabelLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trainingLabelLearn.tStartRefresh + .8-frameTolerance:
                # keep track of stop time/frame for later
                trainingLabelLearn.tStop = t  # not accounting for scr refresh
                trainingLabelLearn.frameNStop = frameN  # exact frame index
                # update status
                trainingLabelLearn.status = FINISHED
                trainingLabelLearn.stop()
        
        # if learn_label_trigs is starting this frame...
        if learn_label_trigs.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_label_trigs.frameNStart = frameN  # exact frame index
            learn_label_trigs.tStart = t  # local t and not account for scr refresh
            learn_label_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_label_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_label_trigs.started', t)
            # update status
            learn_label_trigs.status = STARTED
            learn_label_trigs.write(bytes(chr(173), 'utf8'))
            learn_label_trigs.status = STARTED
        
        # if learn_label_trigs is stopping this frame...
        if learn_label_trigs.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_label_trigs.tStop = t  # not accounting for scr refresh
                learn_label_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_label_trigs.stopped', t)
                # update status
                learn_label_trigs.status = FINISHED
                learn_label_trigs.write(bytes(chr(label_trig), 'utf8'))
                learn_label_trigs.status = FINISHED
        
        # *learn_trialNum_4* updates
        
        # if learn_trialNum_4 is starting this frame...
        if learn_trialNum_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            learn_trialNum_4.frameNStart = frameN  # exact frame index
            learn_trialNum_4.tStart = t  # local t and not account for scr refresh
            learn_trialNum_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_4.started')
            # update status
            learn_trialNum_4.status = STARTED
            learn_trialNum_4.setAutoDraw(True)
        
        # if learn_trialNum_4 is active this frame...
        if learn_trialNum_4.status == STARTED:
            # update params
            pass
        
        # if learn_trialNum_4 is stopping this frame...
        if learn_trialNum_4.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                learn_trialNum_4.tStop = t  # not accounting for scr refresh
                learn_trialNum_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learn_trialNum_4.stopped')
                # update status
                learn_trialNum_4.status = FINISHED
                learn_trialNum_4.setAutoDraw(False)
        
        # *alienBodyLearn3* updates
        
        # if alienBodyLearn3 is starting this frame...
        if alienBodyLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            alienBodyLearn3.frameNStart = frameN  # exact frame index
            alienBodyLearn3.tStart = t  # local t and not account for scr refresh
            alienBodyLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn3.started')
            # update status
            alienBodyLearn3.status = STARTED
            alienBodyLearn3.setAutoDraw(True)
        
        # if alienBodyLearn3 is active this frame...
        if alienBodyLearn3.status == STARTED:
            # update params
            pass
        
        # if alienBodyLearn3 is stopping this frame...
        if alienBodyLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienBodyLearn3.tStop = t  # not accounting for scr refresh
                alienBodyLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienBodyLearn3.stopped')
                # update status
                alienBodyLearn3.status = FINISHED
                alienBodyLearn3.setAutoDraw(False)
        
        # *alienEyeLearn3* updates
        
        # if alienEyeLearn3 is starting this frame...
        if alienEyeLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            alienEyeLearn3.frameNStart = frameN  # exact frame index
            alienEyeLearn3.tStart = t  # local t and not account for scr refresh
            alienEyeLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn3.started')
            # update status
            alienEyeLearn3.status = STARTED
            alienEyeLearn3.setAutoDraw(True)
        
        # if alienEyeLearn3 is active this frame...
        if alienEyeLearn3.status == STARTED:
            # update params
            pass
        
        # if alienEyeLearn3 is stopping this frame...
        if alienEyeLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                alienEyeLearn3.tStop = t  # not accounting for scr refresh
                alienEyeLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'alienEyeLearn3.stopped')
                # update status
                alienEyeLearn3.status = FINISHED
                alienEyeLearn3.setAutoDraw(False)
        
        # *explorerLearn3* updates
        
        # if explorerLearn3 is starting this frame...
        if explorerLearn3.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
            # keep track of start time/frame for later
            explorerLearn3.frameNStart = frameN  # exact frame index
            explorerLearn3.tStart = t  # local t and not account for scr refresh
            explorerLearn3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn3.started')
            # update status
            explorerLearn3.status = STARTED
            explorerLearn3.setAutoDraw(True)
        
        # if explorerLearn3 is active this frame...
        if explorerLearn3.status == STARTED:
            # update params
            pass
        
        # if explorerLearn3 is stopping this frame...
        if explorerLearn3.status == STARTED:
            if bool(trainingLabelLearn.status == FINISHED):
                # keep track of stop time/frame for later
                explorerLearn3.tStop = t  # not accounting for scr refresh
                explorerLearn3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explorerLearn3.stopped')
                # update status
                explorerLearn3.status = FINISHED
                explorerLearn3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_feedback_labelComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_feedback_label" ---
    for thisComponent in learning_feedback_labelComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trainingLabelLearn.stop()  # ensure sound has stopped at end of routine
    # the Routine "learning_feedback_label" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "learning_blink" ---
    continueRoutine = True
    # update component parameters for each repeat
    learn_trialNum_5.setText(learn_trial_nums)
    alienEyeLearn4.setOri(learn_ori_val)
    alienEyeLearn4.setSF(learn_freq_val)
    explorerLearn4.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
    learning_blink_key.keys = []
    learning_blink_key.rt = []
    _learning_blink_key_allKeys = []
    # keep track of which components have finished
    learning_blinkComponents = [learn_trialNum_5, alienBodyLearn4, alienEyeLearn4, explorerLearn4, learning_blink_text, learning_blink_key, learn_blink_trigs]
    for thisComponent in learning_blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_blink" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn_trialNum_5* updates
        
        # if learn_trialNum_5 is starting this frame...
        if learn_trialNum_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn_trialNum_5.frameNStart = frameN  # exact frame index
            learn_trialNum_5.tStart = t  # local t and not account for scr refresh
            learn_trialNum_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_trialNum_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn_trialNum_5.started')
            # update status
            learn_trialNum_5.status = STARTED
            learn_trialNum_5.setAutoDraw(True)
        
        # if learn_trialNum_5 is active this frame...
        if learn_trialNum_5.status == STARTED:
            # update params
            pass
        
        # *alienBodyLearn4* updates
        
        # if alienBodyLearn4 is starting this frame...
        if alienBodyLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alienBodyLearn4.frameNStart = frameN  # exact frame index
            alienBodyLearn4.tStart = t  # local t and not account for scr refresh
            alienBodyLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienBodyLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienBodyLearn4.started')
            # update status
            alienBodyLearn4.status = STARTED
            alienBodyLearn4.setAutoDraw(True)
        
        # if alienBodyLearn4 is active this frame...
        if alienBodyLearn4.status == STARTED:
            # update params
            pass
        
        # *alienEyeLearn4* updates
        
        # if alienEyeLearn4 is starting this frame...
        if alienEyeLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            alienEyeLearn4.frameNStart = frameN  # exact frame index
            alienEyeLearn4.tStart = t  # local t and not account for scr refresh
            alienEyeLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(alienEyeLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'alienEyeLearn4.started')
            # update status
            alienEyeLearn4.status = STARTED
            alienEyeLearn4.setAutoDraw(True)
        
        # if alienEyeLearn4 is active this frame...
        if alienEyeLearn4.status == STARTED:
            # update params
            pass
        
        # *explorerLearn4* updates
        
        # if explorerLearn4 is starting this frame...
        if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            explorerLearn4.frameNStart = frameN  # exact frame index
            explorerLearn4.tStart = t  # local t and not account for scr refresh
            explorerLearn4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explorerLearn4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explorerLearn4.started')
            # update status
            explorerLearn4.status = STARTED
            explorerLearn4.setAutoDraw(True)
        
        # if explorerLearn4 is active this frame...
        if explorerLearn4.status == STARTED:
            # update params
            pass
        
        # *learning_blink_text* updates
        
        # if learning_blink_text is starting this frame...
        if learning_blink_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            learning_blink_text.frameNStart = frameN  # exact frame index
            learning_blink_text.tStart = t  # local t and not account for scr refresh
            learning_blink_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_blink_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_blink_text.started')
            # update status
            learning_blink_text.status = STARTED
            learning_blink_text.setAutoDraw(True)
        
        # if learning_blink_text is active this frame...
        if learning_blink_text.status == STARTED:
            # update params
            pass
        
        # *learning_blink_key* updates
        waitOnFlip = False
        
        # if learning_blink_key is starting this frame...
        if learning_blink_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            learning_blink_key.frameNStart = frameN  # exact frame index
            learning_blink_key.tStart = t  # local t and not account for scr refresh
            learning_blink_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_blink_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learning_blink_key.started')
            # update status
            learning_blink_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learning_blink_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learning_blink_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learning_blink_key.status == STARTED and not waitOnFlip:
            theseKeys = learning_blink_key.getKeys(keyList=['space'], waitRelease=False)
            _learning_blink_key_allKeys.extend(theseKeys)
            if len(_learning_blink_key_allKeys):
                learning_blink_key.keys = _learning_blink_key_allKeys[-1].name  # just the last key pressed
                learning_blink_key.rt = _learning_blink_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if learn_blink_trigs is starting this frame...
        if learn_blink_trigs.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            learn_blink_trigs.frameNStart = frameN  # exact frame index
            learn_blink_trigs.tStart = t  # local t and not account for scr refresh
            learn_blink_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn_blink_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('learn_blink_trigs.started', t)
            # update status
            learn_blink_trigs.status = STARTED
            learn_blink_trigs.write(bytes(chr(179), 'utf8'))
            learn_blink_trigs.status = STARTED
        
        # if learn_blink_trigs is stopping this frame...
        if learn_blink_trigs.status == STARTED:
            if bool(len(_learning_blink_key_allKeys)):
                # keep track of stop time/frame for later
                learn_blink_trigs.tStop = t  # not accounting for scr refresh
                learn_blink_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('learn_blink_trigs.stopped', t)
                # update status
                learn_blink_trigs.status = FINISHED
                learn_blink_trigs.write(bytes(chr(180), 'utf8'))
                learn_blink_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_blink" ---
    for thisComponent in learning_blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if learning_blink_key.keys in ['', [], None]:  # No response was made
        learning_blink_key.keys = None
    learning2_loop.addData('learning_blink_key.keys',learning_blink_key.keys)
    if learning_blink_key.keys != None:  # we had a response
        learning2_loop.addData('learning_blink_key.rt', learning_blink_key.rt)
    # the Routine "learning_blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'learning2_loop'


# --- Prepare to start Routine "break3" ---
continueRoutine = True
# update component parameters for each repeat
break3_keys.keys = []
break3_keys.rt = []
_break3_keys_allKeys = []
# keep track of which components have finished
break3Components = [break3_text, break3_keys, break3_trigs]
for thisComponent in break3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "break3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *break3_text* updates
    
    # if break3_text is starting this frame...
    if break3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break3_text.frameNStart = frameN  # exact frame index
        break3_text.tStart = t  # local t and not account for scr refresh
        break3_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break3_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break3_text.started')
        # update status
        break3_text.status = STARTED
        break3_text.setAutoDraw(True)
    
    # if break3_text is active this frame...
    if break3_text.status == STARTED:
        # update params
        pass
    
    # *break3_keys* updates
    waitOnFlip = False
    
    # if break3_keys is starting this frame...
    if break3_keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        break3_keys.frameNStart = frameN  # exact frame index
        break3_keys.tStart = t  # local t and not account for scr refresh
        break3_keys.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break3_keys, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break3_keys.started')
        # update status
        break3_keys.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(break3_keys.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(break3_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if break3_keys.status == STARTED and not waitOnFlip:
        theseKeys = break3_keys.getKeys(keyList=['return'], waitRelease=False)
        _break3_keys_allKeys.extend(theseKeys)
        if len(_break3_keys_allKeys):
            break3_keys.keys = _break3_keys_allKeys[-1].name  # just the last key pressed
            break3_keys.rt = _break3_keys_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if break3_trigs is starting this frame...
    if break3_trigs.status == NOT_STARTED and break3_text.status == STARTED:
        # keep track of start time/frame for later
        break3_trigs.frameNStart = frameN  # exact frame index
        break3_trigs.tStart = t  # local t and not account for scr refresh
        break3_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(break3_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'break3_trigs.started')
        # update status
        break3_trigs.status = STARTED
        win.callOnFlip(break3_trigs.write, bytes(chr(19), 'utf8'))
        break3_trigs.status = STARTED
    
    # if break3_trigs is stopping this frame...
    if break3_trigs.status == STARTED:
        if bool(len(_break3_keys_allKeys)):
            # keep track of stop time/frame for later
            break3_trigs.tStop = t  # not accounting for scr refresh
            break3_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'break3_trigs.stopped')
            # update status
            break3_trigs.status = FINISHED
            win.callOnFlip(break3_trigs.write, bytes(chr(20), 'utf8'))
            break3_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in break3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "break3" ---
for thisComponent in break3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if break3_keys.keys in ['', [], None]:  # No response was made
    break3_keys.keys = None
thisExp.addData('break3_keys.keys',break3_keys.keys)
if break3_keys.keys != None:  # we had a response
    thisExp.addData('break3_keys.rt', break3_keys.rt)
thisExp.nextEntry()
# the Routine "break3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "sd3_instructions" ---
continueRoutine = True
# update component parameters for each repeat
sd3_instruction_keyboard.keys = []
sd3_instruction_keyboard.rt = []
_sd3_instruction_keyboard_allKeys = []
# keep track of which components have finished
sd3_instructionsComponents = [sd3_instruction_text, L_alien_body_sd3_instruction, R_alien_body_sd3_instruction, L_alien_eye_sd3_instruction, R_alien_eye_sd3_instruction, sd3_instruction_keyboard, sd3_instruction_trigs]
for thisComponent in sd3_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "sd3_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *sd3_instruction_text* updates
    
    # if sd3_instruction_text is starting this frame...
    if sd3_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        sd3_instruction_text.frameNStart = frameN  # exact frame index
        sd3_instruction_text.tStart = t  # local t and not account for scr refresh
        sd3_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd3_instruction_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd3_instruction_text.started')
        # update status
        sd3_instruction_text.status = STARTED
        sd3_instruction_text.setAutoDraw(True)
    
    # if sd3_instruction_text is active this frame...
    if sd3_instruction_text.status == STARTED:
        # update params
        pass
    
    # *L_alien_body_sd3_instruction* updates
    
    # if L_alien_body_sd3_instruction is starting this frame...
    if L_alien_body_sd3_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_body_sd3_instruction.frameNStart = frameN  # exact frame index
        L_alien_body_sd3_instruction.tStart = t  # local t and not account for scr refresh
        L_alien_body_sd3_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_body_sd3_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_body_sd3_instruction.started')
        # update status
        L_alien_body_sd3_instruction.status = STARTED
        L_alien_body_sd3_instruction.setAutoDraw(True)
    
    # if L_alien_body_sd3_instruction is active this frame...
    if L_alien_body_sd3_instruction.status == STARTED:
        # update params
        pass
    
    # *R_alien_body_sd3_instruction* updates
    
    # if R_alien_body_sd3_instruction is starting this frame...
    if R_alien_body_sd3_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_body_sd3_instruction.frameNStart = frameN  # exact frame index
        R_alien_body_sd3_instruction.tStart = t  # local t and not account for scr refresh
        R_alien_body_sd3_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_body_sd3_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_body_sd3_instruction.started')
        # update status
        R_alien_body_sd3_instruction.status = STARTED
        R_alien_body_sd3_instruction.setAutoDraw(True)
    
    # if R_alien_body_sd3_instruction is active this frame...
    if R_alien_body_sd3_instruction.status == STARTED:
        # update params
        pass
    
    # *L_alien_eye_sd3_instruction* updates
    
    # if L_alien_eye_sd3_instruction is starting this frame...
    if L_alien_eye_sd3_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        L_alien_eye_sd3_instruction.frameNStart = frameN  # exact frame index
        L_alien_eye_sd3_instruction.tStart = t  # local t and not account for scr refresh
        L_alien_eye_sd3_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(L_alien_eye_sd3_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'L_alien_eye_sd3_instruction.started')
        # update status
        L_alien_eye_sd3_instruction.status = STARTED
        L_alien_eye_sd3_instruction.setAutoDraw(True)
    
    # if L_alien_eye_sd3_instruction is active this frame...
    if L_alien_eye_sd3_instruction.status == STARTED:
        # update params
        pass
    
    # *R_alien_eye_sd3_instruction* updates
    
    # if R_alien_eye_sd3_instruction is starting this frame...
    if R_alien_eye_sd3_instruction.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        R_alien_eye_sd3_instruction.frameNStart = frameN  # exact frame index
        R_alien_eye_sd3_instruction.tStart = t  # local t and not account for scr refresh
        R_alien_eye_sd3_instruction.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(R_alien_eye_sd3_instruction, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'R_alien_eye_sd3_instruction.started')
        # update status
        R_alien_eye_sd3_instruction.status = STARTED
        R_alien_eye_sd3_instruction.setAutoDraw(True)
    
    # if R_alien_eye_sd3_instruction is active this frame...
    if R_alien_eye_sd3_instruction.status == STARTED:
        # update params
        pass
    
    # *sd3_instruction_keyboard* updates
    waitOnFlip = False
    
    # if sd3_instruction_keyboard is starting this frame...
    if sd3_instruction_keyboard.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        sd3_instruction_keyboard.frameNStart = frameN  # exact frame index
        sd3_instruction_keyboard.tStart = t  # local t and not account for scr refresh
        sd3_instruction_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd3_instruction_keyboard, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd3_instruction_keyboard.started')
        # update status
        sd3_instruction_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sd3_instruction_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sd3_instruction_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sd3_instruction_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = sd3_instruction_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _sd3_instruction_keyboard_allKeys.extend(theseKeys)
        if len(_sd3_instruction_keyboard_allKeys):
            sd3_instruction_keyboard.keys = _sd3_instruction_keyboard_allKeys[-1].name  # just the last key pressed
            sd3_instruction_keyboard.rt = _sd3_instruction_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if sd3_instruction_trigs is starting this frame...
    if sd3_instruction_trigs.status == NOT_STARTED and sd3_instruction_text.status == STARTED:
        # keep track of start time/frame for later
        sd3_instruction_trigs.frameNStart = frameN  # exact frame index
        sd3_instruction_trigs.tStart = t  # local t and not account for scr refresh
        sd3_instruction_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sd3_instruction_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'sd3_instruction_trigs.started')
        # update status
        sd3_instruction_trigs.status = STARTED
        win.callOnFlip(sd3_instruction_trigs.write, bytes(chr(5), 'utf8'))
        sd3_instruction_trigs.status = STARTED
    
    # if sd3_instruction_trigs is stopping this frame...
    if sd3_instruction_trigs.status == STARTED:
        if bool(len(_sd3_instruction_keyboard_allKeys)):
            # keep track of stop time/frame for later
            sd3_instruction_trigs.tStop = t  # not accounting for scr refresh
            sd3_instruction_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd3_instruction_trigs.stopped')
            # update status
            sd3_instruction_trigs.status = FINISHED
            win.callOnFlip(sd3_instruction_trigs.write, bytes(chr(6), 'utf8'))
            sd3_instruction_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in sd3_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "sd3_instructions" ---
for thisComponent in sd3_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if sd3_instruction_keyboard.keys in ['', [], None]:  # No response was made
    sd3_instruction_keyboard.keys = None
thisExp.addData('sd3_instruction_keyboard.keys',sd3_instruction_keyboard.keys)
if sd3_instruction_keyboard.keys != None:  # we had a response
    thisExp.addData('sd3_instruction_keyboard.rt', sd3_instruction_keyboard.rt)
thisExp.nextEntry()
# the Routine "sd3_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
sd3_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/sd.xlsx'),
    seed=None, name='sd3_loop')
thisExp.addLoop(sd3_loop)  # add the loop to the experiment
thisSd3_loop = sd3_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSd3_loop.rgb)
if thisSd3_loop != None:
    for paramName in thisSd3_loop:
        exec('{} = thisSd3_loop[paramName]'.format(paramName))

for thisSd3_loop in sd3_loop:
    currentLoop = sd3_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSd3_loop.rgb)
    if thisSd3_loop != None:
        for paramName in thisSd3_loop:
            exec('{} = thisSd3_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "sd_fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_trial_no_code
    sd_trial_nums = 'Progress: ' + str(currentLoop.thisN + 1) + ' of ' + str(currentLoop.nTotal)
    
    sd_trial_no.setText(sd_trial_nums)
    # keep track of which components have finished
    sd_fixationComponents = [sd_trial_no, sd_fixation_cross, sd_fix_trigs]
    for thisComponent in sd_fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no* updates
        
        # if sd_trial_no is starting this frame...
        if sd_trial_no.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_trial_no.frameNStart = frameN  # exact frame index
            sd_trial_no.tStart = t  # local t and not account for scr refresh
            sd_trial_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no.started')
            # update status
            sd_trial_no.status = STARTED
            sd_trial_no.setAutoDraw(True)
        
        # if sd_trial_no is active this frame...
        if sd_trial_no.status == STARTED:
            # update params
            pass
        
        # if sd_trial_no is stopping this frame...
        if sd_trial_no.status == STARTED:
            if frameN >= (sd_trial_no.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_trial_no.tStop = t  # not accounting for scr refresh
                sd_trial_no.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_trial_no.stopped')
                # update status
                sd_trial_no.status = FINISHED
                sd_trial_no.setAutoDraw(False)
        
        # *sd_fixation_cross* updates
        
        # if sd_fixation_cross is starting this frame...
        if sd_fixation_cross.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_fixation_cross.frameNStart = frameN  # exact frame index
            sd_fixation_cross.tStart = t  # local t and not account for scr refresh
            sd_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fixation_cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fixation_cross.started')
            # update status
            sd_fixation_cross.status = STARTED
            sd_fixation_cross.setAutoDraw(True)
        
        # if sd_fixation_cross is active this frame...
        if sd_fixation_cross.status == STARTED:
            # update params
            pass
        
        # if sd_fixation_cross is stopping this frame...
        if sd_fixation_cross.status == STARTED:
            if frameN >= (sd_fixation_cross.frameNStart + 30):
                # keep track of stop time/frame for later
                sd_fixation_cross.tStop = t  # not accounting for scr refresh
                sd_fixation_cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fixation_cross.stopped')
                # update status
                sd_fixation_cross.status = FINISHED
                sd_fixation_cross.setAutoDraw(False)
        
        # if sd_fix_trigs is starting this frame...
        if sd_fix_trigs.status == NOT_STARTED and sd_fixation_cross.status == STARTED:
            # keep track of start time/frame for later
            sd_fix_trigs.frameNStart = frameN  # exact frame index
            sd_fix_trigs.tStart = t  # local t and not account for scr refresh
            sd_fix_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_fix_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_fix_trigs.started')
            # update status
            sd_fix_trigs.status = STARTED
            win.callOnFlip(sd_fix_trigs.write, bytes(chr(177), 'utf8'))
            sd_fix_trigs.status = STARTED
        
        # if sd_fix_trigs is stopping this frame...
        if sd_fix_trigs.status == STARTED:
            if bool(sd_fixation_cross.status == FINISHED):
                # keep track of stop time/frame for later
                sd_fix_trigs.tStop = t  # not accounting for scr refresh
                sd_fix_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_fix_trigs.stopped')
                # update status
                sd_fix_trigs.status = FINISHED
                win.callOnFlip(sd_fix_trigs.write, bytes(chr(178), 'utf8'))
                sd_fix_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_fixation" ---
    for thisComponent in sd_fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "sd_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "same_diff" ---
    continueRoutine = True
    # update component parameters for each repeat
    sd_trial_no_2.setText(sd_trial_nums)
    L_alien_eye_sd.setOri(sd_L_eye_ori)
    L_alien_eye_sd.setSF(sd_L_eye_sf)
    R_alien_eye_sd.setOri(sd_R_eye_ori)
    R_alien_eye_sd.setSF(sd_R_eye_sf)
    key_resp_sd.keys = []
    key_resp_sd.rt = []
    _key_resp_sd_allKeys = []
    # keep track of which components have finished
    same_diffComponents = [sd_trial_no_2, L_alien_body_sd, R_alien_body_sd, L_alien_eye_sd, R_alien_eye_sd, sd_photo_box, sd_stim_trigs, key_resp_sd, sd_hint]
    for thisComponent in same_diffComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "same_diff" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_2* updates
        
        # if sd_trial_no_2 is starting this frame...
        if sd_trial_no_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_2.frameNStart = frameN  # exact frame index
            sd_trial_no_2.tStart = t  # local t and not account for scr refresh
            sd_trial_no_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_2.started')
            # update status
            sd_trial_no_2.status = STARTED
            sd_trial_no_2.setAutoDraw(True)
        
        # if sd_trial_no_2 is active this frame...
        if sd_trial_no_2.status == STARTED:
            # update params
            pass
        
        # *L_alien_body_sd* updates
        
        # if L_alien_body_sd is starting this frame...
        if L_alien_body_sd.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            L_alien_body_sd.frameNStart = frameN  # exact frame index
            L_alien_body_sd.tStart = t  # local t and not account for scr refresh
            L_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_body_sd.started')
            # update status
            L_alien_body_sd.status = STARTED
            L_alien_body_sd.setAutoDraw(True)
        
        # if L_alien_body_sd is active this frame...
        if L_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_body_sd is stopping this frame...
        if L_alien_body_sd.status == STARTED:
            if frameN >= (L_alien_body_sd.frameNStart + 12):
                # keep track of stop time/frame for later
                L_alien_body_sd.tStop = t  # not accounting for scr refresh
                L_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_body_sd.stopped')
                # update status
                L_alien_body_sd.status = FINISHED
                L_alien_body_sd.setAutoDraw(False)
        
        # *R_alien_body_sd* updates
        
        # if R_alien_body_sd is starting this frame...
        if R_alien_body_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_body_sd.frameNStart = frameN  # exact frame index
            R_alien_body_sd.tStart = t  # local t and not account for scr refresh
            R_alien_body_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_body_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_body_sd.started')
            # update status
            R_alien_body_sd.status = STARTED
            R_alien_body_sd.setAutoDraw(True)
        
        # if R_alien_body_sd is active this frame...
        if R_alien_body_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_body_sd is stopping this frame...
        if R_alien_body_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_body_sd.tStop = t  # not accounting for scr refresh
                R_alien_body_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_body_sd.stopped')
                # update status
                R_alien_body_sd.status = FINISHED
                R_alien_body_sd.setAutoDraw(False)
        
        # *L_alien_eye_sd* updates
        
        # if L_alien_eye_sd is starting this frame...
        if L_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            L_alien_eye_sd.frameNStart = frameN  # exact frame index
            L_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            L_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(L_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'L_alien_eye_sd.started')
            # update status
            L_alien_eye_sd.status = STARTED
            L_alien_eye_sd.setAutoDraw(True)
        
        # if L_alien_eye_sd is active this frame...
        if L_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if L_alien_eye_sd is stopping this frame...
        if L_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                L_alien_eye_sd.tStop = t  # not accounting for scr refresh
                L_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'L_alien_eye_sd.stopped')
                # update status
                L_alien_eye_sd.status = FINISHED
                L_alien_eye_sd.setAutoDraw(False)
        
        # *R_alien_eye_sd* updates
        
        # if R_alien_eye_sd is starting this frame...
        if R_alien_eye_sd.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            R_alien_eye_sd.frameNStart = frameN  # exact frame index
            R_alien_eye_sd.tStart = t  # local t and not account for scr refresh
            R_alien_eye_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(R_alien_eye_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'R_alien_eye_sd.started')
            # update status
            R_alien_eye_sd.status = STARTED
            R_alien_eye_sd.setAutoDraw(True)
        
        # if R_alien_eye_sd is active this frame...
        if R_alien_eye_sd.status == STARTED:
            # update params
            pass
        
        # if R_alien_eye_sd is stopping this frame...
        if R_alien_eye_sd.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                R_alien_eye_sd.tStop = t  # not accounting for scr refresh
                R_alien_eye_sd.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'R_alien_eye_sd.stopped')
                # update status
                R_alien_eye_sd.status = FINISHED
                R_alien_eye_sd.setAutoDraw(False)
        
        # *sd_photo_box* updates
        
        # if sd_photo_box is starting this frame...
        if sd_photo_box.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_photo_box.frameNStart = frameN  # exact frame index
            sd_photo_box.tStart = t  # local t and not account for scr refresh
            sd_photo_box.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_photo_box, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_photo_box.started')
            # update status
            sd_photo_box.status = STARTED
            sd_photo_box.setAutoDraw(True)
        
        # if sd_photo_box is active this frame...
        if sd_photo_box.status == STARTED:
            # update params
            pass
        
        # if sd_photo_box is stopping this frame...
        if sd_photo_box.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_photo_box.tStop = t  # not accounting for scr refresh
                sd_photo_box.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_photo_box.stopped')
                # update status
                sd_photo_box.status = FINISHED
                sd_photo_box.setAutoDraw(False)
        
        # if sd_stim_trigs is starting this frame...
        if sd_stim_trigs.status == NOT_STARTED and L_alien_body_sd.status == STARTED:
            # keep track of start time/frame for later
            sd_stim_trigs.frameNStart = frameN  # exact frame index
            sd_stim_trigs.tStart = t  # local t and not account for scr refresh
            sd_stim_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_stim_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_stim_trigs.started')
            # update status
            sd_stim_trigs.status = STARTED
            win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_ontrig), 'utf8'))
            sd_stim_trigs.status = STARTED
        
        # if sd_stim_trigs is stopping this frame...
        if sd_stim_trigs.status == STARTED:
            if bool(L_alien_body_sd.status == FINISHED):
                # keep track of stop time/frame for later
                sd_stim_trigs.tStop = t  # not accounting for scr refresh
                sd_stim_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_stim_trigs.stopped')
                # update status
                sd_stim_trigs.status = FINISHED
                win.callOnFlip(sd_stim_trigs.write, bytes(chr(sd_offtrig), 'utf8'))
                sd_stim_trigs.status = FINISHED
        
        # *key_resp_sd* updates
        waitOnFlip = False
        
        # if key_resp_sd is starting this frame...
        if key_resp_sd.status == NOT_STARTED and L_alien_body_sd.status == FINISHED:
            # keep track of start time/frame for later
            key_resp_sd.frameNStart = frameN  # exact frame index
            key_resp_sd.tStart = t  # local t and not account for scr refresh
            key_resp_sd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_sd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_sd.started')
            # update status
            key_resp_sd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_sd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_sd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_sd.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_sd.getKeys(keyList=['s','d'], waitRelease=False)
            _key_resp_sd_allKeys.extend(theseKeys)
            if len(_key_resp_sd_allKeys):
                key_resp_sd.keys = _key_resp_sd_allKeys[-1].name  # just the last key pressed
                key_resp_sd.rt = _key_resp_sd_allKeys[-1].rt
                # was this correct?
                if (key_resp_sd.keys == str(sd_correct_key)) or (key_resp_sd.keys == sd_correct_key):
                    key_resp_sd.corr = 1
                else:
                    key_resp_sd.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *sd_hint* updates
        
        # if sd_hint is starting this frame...
        if sd_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            sd_hint.frameNStart = frameN  # exact frame index
            sd_hint.tStart = t  # local t and not account for scr refresh
            sd_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_hint, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_hint.started')
            # update status
            sd_hint.status = STARTED
            sd_hint.setAutoDraw(True)
        
        # if sd_hint is active this frame...
        if sd_hint.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in same_diffComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "same_diff" ---
    for thisComponent in same_diffComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_sd.keys in ['', [], None]:  # No response was made
        key_resp_sd.keys = None
        # was no response the correct answer?!
        if str(sd_correct_key).lower() == 'none':
           key_resp_sd.corr = 1;  # correct non-response
        else:
           key_resp_sd.corr = 0;  # failed to respond (incorrectly)
    # store data for sd3_loop (TrialHandler)
    sd3_loop.addData('key_resp_sd.keys',key_resp_sd.keys)
    sd3_loop.addData('key_resp_sd.corr', key_resp_sd.corr)
    if key_resp_sd.keys != None:  # we had a response
        sd3_loop.addData('key_resp_sd.rt', key_resp_sd.rt)
    # the Routine "same_diff" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "sd_resp_triggers" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_resp_trigger_code
    if key_resp_sd.corr:
        sd_acc_trig = 169
    else:
        sd_acc_trig = 168
    # keep track of which components have finished
    sd_resp_triggersComponents = [sd_resp_trigs]
    for thisComponent in sd_resp_triggersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_resp_triggers" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.1:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # if sd_resp_trigs is starting this frame...
        if sd_resp_trigs.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_resp_trigs.frameNStart = frameN  # exact frame index
            sd_resp_trigs.tStart = t  # local t and not account for scr refresh
            sd_resp_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_resp_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_resp_trigs.started')
            # update status
            sd_resp_trigs.status = STARTED
            win.callOnFlip(sd_resp_trigs.write, bytes(chr(167), 'utf8'))
            sd_resp_trigs.status = STARTED
        
        # if sd_resp_trigs is stopping this frame...
        if sd_resp_trigs.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > .1-frameTolerance:
                # keep track of stop time/frame for later
                sd_resp_trigs.tStop = t  # not accounting for scr refresh
                sd_resp_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_resp_trigs.stopped')
                # update status
                sd_resp_trigs.status = FINISHED
                win.callOnFlip(sd_resp_trigs.write, bytes(chr(sd_acc_trig), 'utf8'))
                sd_resp_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_resp_triggersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_resp_triggers" ---
    for thisComponent in sd_resp_triggersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.100000)
    
    # --- Prepare to start Routine "sd_blink" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from sd_blink_code
    sd_blink_counter = sd_blink_counter + 1
    if sd_blink_counter == 4:
        sd_blink_counter = 0
    else:
        continueRoutine = False
    sd_trial_no_3.setText(sd_trial_nums)
    sd_blink_key.keys = []
    sd_blink_key.rt = []
    _sd_blink_key_allKeys = []
    # keep track of which components have finished
    sd_blinkComponents = [sd_trial_no_3, sd1_blink_text, sd_blink_key, sd_blink_trigs]
    for thisComponent in sd_blinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "sd_blink" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sd_trial_no_3* updates
        
        # if sd_trial_no_3 is starting this frame...
        if sd_trial_no_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sd_trial_no_3.frameNStart = frameN  # exact frame index
            sd_trial_no_3.tStart = t  # local t and not account for scr refresh
            sd_trial_no_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_trial_no_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_trial_no_3.started')
            # update status
            sd_trial_no_3.status = STARTED
            sd_trial_no_3.setAutoDraw(True)
        
        # if sd_trial_no_3 is active this frame...
        if sd_trial_no_3.status == STARTED:
            # update params
            pass
        
        # *sd1_blink_text* updates
        
        # if sd1_blink_text is starting this frame...
        if sd1_blink_text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd1_blink_text.frameNStart = frameN  # exact frame index
            sd1_blink_text.tStart = t  # local t and not account for scr refresh
            sd1_blink_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd1_blink_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd1_blink_text.started')
            # update status
            sd1_blink_text.status = STARTED
            sd1_blink_text.setAutoDraw(True)
        
        # if sd1_blink_text is active this frame...
        if sd1_blink_text.status == STARTED:
            # update params
            pass
        
        # *sd_blink_key* updates
        waitOnFlip = False
        
        # if sd_blink_key is starting this frame...
        if sd_blink_key.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sd_blink_key.frameNStart = frameN  # exact frame index
            sd_blink_key.tStart = t  # local t and not account for scr refresh
            sd_blink_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_key, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_key.started')
            # update status
            sd_blink_key.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sd_blink_key.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sd_blink_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sd_blink_key.status == STARTED and not waitOnFlip:
            theseKeys = sd_blink_key.getKeys(keyList=['space'], waitRelease=False)
            _sd_blink_key_allKeys.extend(theseKeys)
            if len(_sd_blink_key_allKeys):
                sd_blink_key.keys = _sd_blink_key_allKeys[-1].name  # just the last key pressed
                sd_blink_key.rt = _sd_blink_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if sd_blink_trigs is starting this frame...
        if sd_blink_trigs.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            sd_blink_trigs.frameNStart = frameN  # exact frame index
            sd_blink_trigs.tStart = t  # local t and not account for scr refresh
            sd_blink_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sd_blink_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'sd_blink_trigs.started')
            # update status
            sd_blink_trigs.status = STARTED
            win.callOnFlip(sd_blink_trigs.write, bytes(chr(179), 'utf8'))
            sd_blink_trigs.status = STARTED
        
        # if sd_blink_trigs is stopping this frame...
        if sd_blink_trigs.status == STARTED:
            if bool(sd_blink_key.keys == 'space'):
                # keep track of stop time/frame for later
                sd_blink_trigs.tStop = t  # not accounting for scr refresh
                sd_blink_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sd_blink_trigs.stopped')
                # update status
                sd_blink_trigs.status = FINISHED
                win.callOnFlip(sd_blink_trigs.write, bytes(chr(180), 'utf8'))
                sd_blink_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sd_blinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "sd_blink" ---
    for thisComponent in sd_blinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if sd_blink_key.keys in ['', [], None]:  # No response was made
        sd_blink_key.keys = None
    sd3_loop.addData('sd_blink_key.keys',sd_blink_key.keys)
    if sd_blink_key.keys != None:  # we had a response
        sd3_loop.addData('sd_blink_key.rt', sd_blink_key.rt)
    # the Routine "sd_blink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'sd3_loop'


# --- Prepare to start Routine "resting_instructions_3" ---
continueRoutine = True
# update component parameters for each repeat
resting_keyboard_3.keys = []
resting_keyboard_3.rt = []
_resting_keyboard_3_allKeys = []
# keep track of which components have finished
resting_instructions_3Components = [rest_instructions_close_post, resting_keyboard_3]
for thisComponent in resting_instructions_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_instructions_3" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rest_instructions_close_post* updates
    
    # if rest_instructions_close_post is starting this frame...
    if rest_instructions_close_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_close_post.frameNStart = frameN  # exact frame index
        rest_instructions_close_post.tStart = t  # local t and not account for scr refresh
        rest_instructions_close_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_close_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_instructions_close_post.started')
        # update status
        rest_instructions_close_post.status = STARTED
        rest_instructions_close_post.setAutoDraw(True)
    
    # if rest_instructions_close_post is active this frame...
    if rest_instructions_close_post.status == STARTED:
        # update params
        pass
    
    # *resting_keyboard_3* updates
    waitOnFlip = False
    
    # if resting_keyboard_3 is starting this frame...
    if resting_keyboard_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_keyboard_3.frameNStart = frameN  # exact frame index
        resting_keyboard_3.tStart = t  # local t and not account for scr refresh
        resting_keyboard_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_keyboard_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_keyboard_3.started')
        # update status
        resting_keyboard_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resting_keyboard_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resting_keyboard_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resting_keyboard_3.status == STARTED and not waitOnFlip:
        theseKeys = resting_keyboard_3.getKeys(keyList=['space'], waitRelease=False)
        _resting_keyboard_3_allKeys.extend(theseKeys)
        if len(_resting_keyboard_3_allKeys):
            resting_keyboard_3.keys = _resting_keyboard_3_allKeys[-1].name  # just the last key pressed
            resting_keyboard_3.rt = _resting_keyboard_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_instructions_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_instructions_3" ---
for thisComponent in resting_instructions_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resting_keyboard_3.keys in ['', [], None]:  # No response was made
    resting_keyboard_3.keys = None
thisExp.addData('resting_keyboard_3.keys',resting_keyboard_3.keys)
if resting_keyboard_3.keys != None:  # we had a response
    thisExp.addData('resting_keyboard_3.rt', resting_keyboard_3.rt)
thisExp.nextEntry()
# the Routine "resting_instructions_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_closed_post" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
resting_closed_postComponents = [resting_closed_photobox_post, resting_closed_trigs_post]
for thisComponent in resting_closed_postComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_closed_post" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_closed_photobox_post* updates
    
    # if resting_closed_photobox_post is starting this frame...
    if resting_closed_photobox_post.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        resting_closed_photobox_post.frameNStart = frameN  # exact frame index
        resting_closed_photobox_post.tStart = t  # local t and not account for scr refresh
        resting_closed_photobox_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_closed_photobox_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_closed_photobox_post.started')
        # update status
        resting_closed_photobox_post.status = STARTED
        resting_closed_photobox_post.setAutoDraw(True)
    
    # if resting_closed_photobox_post is active this frame...
    if resting_closed_photobox_post.status == STARTED:
        # update params
        pass
    
    # if resting_closed_photobox_post is stopping this frame...
    if resting_closed_photobox_post.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_closed_photobox_post.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            resting_closed_photobox_post.tStop = t  # not accounting for scr refresh
            resting_closed_photobox_post.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_closed_photobox_post.stopped')
            # update status
            resting_closed_photobox_post.status = FINISHED
            resting_closed_photobox_post.setAutoDraw(False)
    
    # if resting_closed_trigs_post is starting this frame...
    if resting_closed_trigs_post.status == NOT_STARTED and resting_closed_photobox_post.status == STARTED:
        # keep track of start time/frame for later
        resting_closed_trigs_post.frameNStart = frameN  # exact frame index
        resting_closed_trigs_post.tStart = t  # local t and not account for scr refresh
        resting_closed_trigs_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_closed_trigs_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_closed_trigs_post.started')
        # update status
        resting_closed_trigs_post.status = STARTED
        win.callOnFlip(resting_closed_trigs_post.write, bytes(chr(11), 'utf8'))
        resting_closed_trigs_post.status = STARTED
    
    # if resting_closed_trigs_post is stopping this frame...
    if resting_closed_trigs_post.status == STARTED:
        if bool(resting_closed_photobox_post.status == FINISHED):
            # keep track of stop time/frame for later
            resting_closed_trigs_post.tStop = t  # not accounting for scr refresh
            resting_closed_trigs_post.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_closed_trigs_post.stopped')
            # update status
            resting_closed_trigs_post.status = FINISHED
            win.callOnFlip(resting_closed_trigs_post.write, bytes(chr(12), 'utf8'))
            resting_closed_trigs_post.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_closed_postComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_closed_post" ---
for thisComponent in resting_closed_postComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "resting_closed_post" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_instructions_4" ---
continueRoutine = True
# update component parameters for each repeat
resting_chime_2.setSound('stimuli/ding.wav', secs=2, hamming=True)
resting_chime_2.setVolume(1.0, log=False)
resting_keyboard_4.keys = []
resting_keyboard_4.rt = []
_resting_keyboard_4_allKeys = []
# keep track of which components have finished
resting_instructions_4Components = [resting_chime_2, rest_instructions_open_post, resting_keyboard_4]
for thisComponent in resting_instructions_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_instructions_4" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop resting_chime_2
    
    # if resting_chime_2 is starting this frame...
    if resting_chime_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_chime_2.frameNStart = frameN  # exact frame index
        resting_chime_2.tStart = t  # local t and not account for scr refresh
        resting_chime_2.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('resting_chime_2.started', tThisFlipGlobal)
        # update status
        resting_chime_2.status = STARTED
        resting_chime_2.play(when=win)  # sync with win flip
    
    # if resting_chime_2 is stopping this frame...
    if resting_chime_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_chime_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            resting_chime_2.tStop = t  # not accounting for scr refresh
            resting_chime_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_chime_2.stopped')
            # update status
            resting_chime_2.status = FINISHED
            resting_chime_2.stop()
    
    # *rest_instructions_open_post* updates
    
    # if rest_instructions_open_post is starting this frame...
    if rest_instructions_open_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rest_instructions_open_post.frameNStart = frameN  # exact frame index
        rest_instructions_open_post.tStart = t  # local t and not account for scr refresh
        rest_instructions_open_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rest_instructions_open_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'rest_instructions_open_post.started')
        # update status
        rest_instructions_open_post.status = STARTED
        rest_instructions_open_post.setAutoDraw(True)
    
    # if rest_instructions_open_post is active this frame...
    if rest_instructions_open_post.status == STARTED:
        # update params
        pass
    
    # *resting_keyboard_4* updates
    waitOnFlip = False
    
    # if resting_keyboard_4 is starting this frame...
    if resting_keyboard_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resting_keyboard_4.frameNStart = frameN  # exact frame index
        resting_keyboard_4.tStart = t  # local t and not account for scr refresh
        resting_keyboard_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_keyboard_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_keyboard_4.started')
        # update status
        resting_keyboard_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resting_keyboard_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resting_keyboard_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resting_keyboard_4.status == STARTED and not waitOnFlip:
        theseKeys = resting_keyboard_4.getKeys(keyList=['space'], waitRelease=False)
        _resting_keyboard_4_allKeys.extend(theseKeys)
        if len(_resting_keyboard_4_allKeys):
            resting_keyboard_4.keys = _resting_keyboard_4_allKeys[-1].name  # just the last key pressed
            resting_keyboard_4.rt = _resting_keyboard_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_instructions_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_instructions_4" ---
for thisComponent in resting_instructions_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
resting_chime_2.stop()  # ensure sound has stopped at end of routine
# check responses
if resting_keyboard_4.keys in ['', [], None]:  # No response was made
    resting_keyboard_4.keys = None
thisExp.addData('resting_keyboard_4.keys',resting_keyboard_4.keys)
if resting_keyboard_4.keys != None:  # we had a response
    thisExp.addData('resting_keyboard_4.rt', resting_keyboard_4.rt)
thisExp.nextEntry()
# the Routine "resting_instructions_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "resting_open_post" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
resting_open_postComponents = [resting_open_photobox_post, resting_open_trigs_post]
for thisComponent in resting_open_postComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "resting_open_post" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resting_open_photobox_post* updates
    
    # if resting_open_photobox_post is starting this frame...
    if resting_open_photobox_post.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        resting_open_photobox_post.frameNStart = frameN  # exact frame index
        resting_open_photobox_post.tStart = t  # local t and not account for scr refresh
        resting_open_photobox_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_open_photobox_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_open_photobox_post.started')
        # update status
        resting_open_photobox_post.status = STARTED
        resting_open_photobox_post.setAutoDraw(True)
    
    # if resting_open_photobox_post is active this frame...
    if resting_open_photobox_post.status == STARTED:
        # update params
        pass
    
    # if resting_open_photobox_post is stopping this frame...
    if resting_open_photobox_post.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resting_open_photobox_post.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            resting_open_photobox_post.tStop = t  # not accounting for scr refresh
            resting_open_photobox_post.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_open_photobox_post.stopped')
            # update status
            resting_open_photobox_post.status = FINISHED
            resting_open_photobox_post.setAutoDraw(False)
    
    # if resting_open_trigs_post is starting this frame...
    if resting_open_trigs_post.status == NOT_STARTED and resting_open_photobox_post.status == STARTED:
        # keep track of start time/frame for later
        resting_open_trigs_post.frameNStart = frameN  # exact frame index
        resting_open_trigs_post.tStart = t  # local t and not account for scr refresh
        resting_open_trigs_post.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resting_open_trigs_post, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resting_open_trigs_post.started')
        # update status
        resting_open_trigs_post.status = STARTED
        win.callOnFlip(resting_open_trigs_post.write, bytes(chr(13), 'utf8'))
        resting_open_trigs_post.status = STARTED
    
    # if resting_open_trigs_post is stopping this frame...
    if resting_open_trigs_post.status == STARTED:
        if bool(resting_open_photobox_post.status == FINISHED):
            # keep track of stop time/frame for later
            resting_open_trigs_post.tStop = t  # not accounting for scr refresh
            resting_open_trigs_post.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resting_open_trigs_post.stopped')
            # update status
            resting_open_trigs_post.status = FINISHED
            win.callOnFlip(resting_open_trigs_post.write, bytes(chr(14), 'utf8'))
            resting_open_trigs_post.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in resting_open_postComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "resting_open_post" ---
for thisComponent in resting_open_postComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "resting_open_post" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "exit_instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_exit_1.keys = []
key_resp_exit_1.rt = []
_key_resp_exit_1_allKeys = []
# keep track of which components have finished
exit_instructionsComponents = [instructionExit, key_resp_exit_1, exit_instruction_trigs]
for thisComponent in exit_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "exit_instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionExit* updates
    
    # if instructionExit is starting this frame...
    if instructionExit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionExit.frameNStart = frameN  # exact frame index
        instructionExit.tStart = t  # local t and not account for scr refresh
        instructionExit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionExit, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructionExit.started')
        # update status
        instructionExit.status = STARTED
        instructionExit.setAutoDraw(True)
    
    # if instructionExit is active this frame...
    if instructionExit.status == STARTED:
        # update params
        pass
    
    # *key_resp_exit_1* updates
    waitOnFlip = False
    
    # if key_resp_exit_1 is starting this frame...
    if key_resp_exit_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_exit_1.frameNStart = frameN  # exact frame index
        key_resp_exit_1.tStart = t  # local t and not account for scr refresh
        key_resp_exit_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_exit_1, 'tStartRefresh')  # time at next scr refresh
        # update status
        key_resp_exit_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_exit_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_exit_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_exit_1.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_exit_1.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_exit_1_allKeys.extend(theseKeys)
        if len(_key_resp_exit_1_allKeys):
            key_resp_exit_1.keys = _key_resp_exit_1_allKeys[-1].name  # just the last key pressed
            key_resp_exit_1.rt = _key_resp_exit_1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # if exit_instruction_trigs is starting this frame...
    if exit_instruction_trigs.status == NOT_STARTED and instructionExit.status == STARTED:
        # keep track of start time/frame for later
        exit_instruction_trigs.frameNStart = frameN  # exact frame index
        exit_instruction_trigs.tStart = t  # local t and not account for scr refresh
        exit_instruction_trigs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exit_instruction_trigs, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'exit_instruction_trigs.started')
        # update status
        exit_instruction_trigs.status = STARTED
        win.callOnFlip(exit_instruction_trigs.write, bytes(chr(9), 'utf8'))
        exit_instruction_trigs.status = STARTED
    
    # if exit_instruction_trigs is stopping this frame...
    if exit_instruction_trigs.status == STARTED:
        if bool(len(_key_resp_exit_1_allKeys)):
            # keep track of stop time/frame for later
            exit_instruction_trigs.tStop = t  # not accounting for scr refresh
            exit_instruction_trigs.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exit_instruction_trigs.stopped')
            # update status
            exit_instruction_trigs.status = FINISHED
            win.callOnFlip(exit_instruction_trigs.write, bytes(chr(10), 'utf8'))
            exit_instruction_trigs.status = FINISHED
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exit_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "exit_instructions" ---
for thisComponent in exit_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "exit_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
exitQ_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/exitQuestions.xlsx'),
    seed=None, name='exitQ_loop')
thisExp.addLoop(exitQ_loop)  # add the loop to the experiment
thisExitQ_loop = exitQ_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExitQ_loop.rgb)
if thisExitQ_loop != None:
    for paramName in thisExitQ_loop:
        exec('{} = thisExitQ_loop[paramName]'.format(paramName))

for thisExitQ_loop in exitQ_loop:
    currentLoop = exitQ_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExitQ_loop.rgb)
    if thisExitQ_loop != None:
        for paramName in thisExitQ_loop:
            exec('{} = thisExitQ_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "exit_questionnaire" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from exitResponseTextCODE
    exitResponse.text=""
    exitQ_number.setText("Question {} out of {}".format(exitQ_loop.thisN + 1, exitQ_loop.nTotal))
    exitQuestion.setText(exitQ)
    exitResponse.reset()
    key_resp_exit_2.keys = []
    key_resp_exit_2.rt = []
    _key_resp_exit_2_allKeys = []
    # keep track of which components have finished
    exit_questionnaireComponents = [exitQ_number, exitQuestion, exitResponse, exitContinueText, key_resp_exit_2, exit_question_trigs]
    for thisComponent in exit_questionnaireComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exit_questionnaire" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *exitQ_number* updates
        
        # if exitQ_number is starting this frame...
        if exitQ_number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitQ_number.frameNStart = frameN  # exact frame index
            exitQ_number.tStart = t  # local t and not account for scr refresh
            exitQ_number.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitQ_number, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitQ_number.started')
            # update status
            exitQ_number.status = STARTED
            exitQ_number.setAutoDraw(True)
        
        # if exitQ_number is active this frame...
        if exitQ_number.status == STARTED:
            # update params
            pass
        
        # *exitQuestion* updates
        
        # if exitQuestion is starting this frame...
        if exitQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitQuestion.frameNStart = frameN  # exact frame index
            exitQuestion.tStart = t  # local t and not account for scr refresh
            exitQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitQuestion, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitQuestion.started')
            # update status
            exitQuestion.status = STARTED
            exitQuestion.setAutoDraw(True)
        
        # if exitQuestion is active this frame...
        if exitQuestion.status == STARTED:
            # update params
            pass
        
        # *exitResponse* updates
        
        # if exitResponse is starting this frame...
        if exitResponse.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            exitResponse.frameNStart = frameN  # exact frame index
            exitResponse.tStart = t  # local t and not account for scr refresh
            exitResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitResponse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitResponse.started')
            # update status
            exitResponse.status = STARTED
            exitResponse.setAutoDraw(True)
        
        # if exitResponse is active this frame...
        if exitResponse.status == STARTED:
            # update params
            pass
        
        # *exitContinueText* updates
        
        # if exitContinueText is starting this frame...
        if exitContinueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitContinueText.frameNStart = frameN  # exact frame index
            exitContinueText.tStart = t  # local t and not account for scr refresh
            exitContinueText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitContinueText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitContinueText.started')
            # update status
            exitContinueText.status = STARTED
            exitContinueText.setAutoDraw(True)
        
        # if exitContinueText is active this frame...
        if exitContinueText.status == STARTED:
            # update params
            pass
        
        # *key_resp_exit_2* updates
        waitOnFlip = False
        
        # if key_resp_exit_2 is starting this frame...
        if key_resp_exit_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_exit_2.frameNStart = frameN  # exact frame index
            key_resp_exit_2.tStart = t  # local t and not account for scr refresh
            key_resp_exit_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_exit_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_exit_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_exit_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_exit_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_exit_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_exit_2.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_exit_2_allKeys.extend(theseKeys)
            if len(_key_resp_exit_2_allKeys):
                key_resp_exit_2.keys = _key_resp_exit_2_allKeys[-1].name  # just the last key pressed
                key_resp_exit_2.rt = _key_resp_exit_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # if exit_question_trigs is starting this frame...
        if exit_question_trigs.status == NOT_STARTED and exitQuestion.status == STARTED:
            # keep track of start time/frame for later
            exit_question_trigs.frameNStart = frameN  # exact frame index
            exit_question_trigs.tStart = t  # local t and not account for scr refresh
            exit_question_trigs.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exit_question_trigs, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exit_question_trigs.started')
            # update status
            exit_question_trigs.status = STARTED
            win.callOnFlip(exit_question_trigs.write, bytes(chr(181), 'utf8'))
            exit_question_trigs.status = STARTED
        
        # if exit_question_trigs is stopping this frame...
        if exit_question_trigs.status == STARTED:
            if bool(len(_key_resp_exit_2_allKeys)):
                # keep track of stop time/frame for later
                exit_question_trigs.tStop = t  # not accounting for scr refresh
                exit_question_trigs.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'exit_question_trigs.stopped')
                # update status
                exit_question_trigs.status = FINISHED
                win.callOnFlip(exit_question_trigs.write, bytes(chr(182), 'utf8'))
                exit_question_trigs.status = FINISHED
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exit_questionnaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exit_questionnaire" ---
    for thisComponent in exit_questionnaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exitQ_loop.addData('exitResponse.text',exitResponse.text)
    # the Routine "exit_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'exitQ_loop'


# --- Prepare to start Routine "experiment_end" ---
continueRoutine = True
# update component parameters for each repeat
end_chime.setSound('stimuli/ding.wav', secs=2, hamming=True)
end_chime.setVolume(1.0, log=False)
# keep track of which components have finished
experiment_endComponents = [end_chime, thank_you]
for thisComponent in experiment_endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "experiment_end" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop end_chime
    
    # if end_chime is starting this frame...
    if end_chime.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_chime.frameNStart = frameN  # exact frame index
        end_chime.tStart = t  # local t and not account for scr refresh
        end_chime.tStartRefresh = tThisFlipGlobal  # on global time
        # add timestamp to datafile
        thisExp.addData('end_chime.started', tThisFlipGlobal)
        # update status
        end_chime.status = STARTED
        end_chime.play(when=win)  # sync with win flip
    
    # if end_chime is stopping this frame...
    if end_chime.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_chime.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            end_chime.tStop = t  # not accounting for scr refresh
            end_chime.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_chime.stopped')
            # update status
            end_chime.status = FINISHED
            end_chime.stop()
    
    # *thank_you* updates
    
    # if thank_you is starting this frame...
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'thank_you.started')
        # update status
        thank_you.status = STARTED
        thank_you.setAutoDraw(True)
    
    # if thank_you is active this frame...
    if thank_you.status == STARTED:
        # update params
        pass
    
    # if thank_you is stopping this frame...
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'thank_you.stopped')
            # update status
            thank_you.status = FINISHED
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "experiment_end" ---
for thisComponent in experiment_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
end_chime.stop()  # ensure sound has stopped at end of routine
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)
# Close resting_closed_trigs_pre
if resting_closed_trigs_pre.is_open:
    resting_closed_trigs_pre.close()
# Close resting_open_trigs
if resting_open_trigs.is_open:
    resting_open_trigs.close()
# Close sd_instruction_trigs_1
if sd_instruction_trigs_1.is_open:
    sd_instruction_trigs_1.close()
# Close sd_instruction_trigs_2
if sd_instruction_trigs_2.is_open:
    sd_instruction_trigs_2.close()
# Close sd_fix_trigs
if sd_fix_trigs.is_open:
    sd_fix_trigs.close()
# Close sd_stim_trigs
if sd_stim_trigs.is_open:
    sd_stim_trigs.close()
# Close sd_resp_trigs
if sd_resp_trigs.is_open:
    sd_resp_trigs.close()
# Close sd_blink_trigs
if sd_blink_trigs.is_open:
    sd_blink_trigs.close()
# Close learn_instruction_trigs_0
if learn_instruction_trigs_0.is_open:
    learn_instruction_trigs_0.close()
# Close learn_instruction_trigs_1
if learn_instruction_trigs_1.is_open:
    learn_instruction_trigs_1.close()
# Close learn_instruction_trigs_2
if learn_instruction_trigs_2.is_open:
    learn_instruction_trigs_2.close()
# Close learn_instruction_trigs_3
if learn_instruction_trigs_3.is_open:
    learn_instruction_trigs_3.close()
# Close learn_instruction_trigs_4
if learn_instruction_trigs_4.is_open:
    learn_instruction_trigs_4.close()
# Close learn_instruction_trigs_5
if learn_instruction_trigs_5.is_open:
    learn_instruction_trigs_5.close()
# Close learn_label_instruction_trigs
if learn_label_instruction_trigs.is_open:
    learn_label_instruction_trigs.close()
# Close learn_instruction_trigs_6
if learn_instruction_trigs_6.is_open:
    learn_instruction_trigs_6.close()
# Close learn_fix_trigs
if learn_fix_trigs.is_open:
    learn_fix_trigs.close()
# Close learn_stim_trigs
if learn_stim_trigs.is_open:
    learn_stim_trigs.close()
# Close learn_feedback_trigs
if learn_feedback_trigs.is_open:
    learn_feedback_trigs.close()
# Close learn_label_trigs
if learn_label_trigs.is_open:
    learn_label_trigs.close()
# Close learn_blink_trigs
if learn_blink_trigs.is_open:
    learn_blink_trigs.close()
# Close break1_trigs
if break1_trigs.is_open:
    break1_trigs.close()
# Close sd2_instruction_trigs
if sd2_instruction_trigs.is_open:
    sd2_instruction_trigs.close()
# Close sd_fix_trigs
if sd_fix_trigs.is_open:
    sd_fix_trigs.close()
# Close sd_stim_trigs
if sd_stim_trigs.is_open:
    sd_stim_trigs.close()
# Close sd_resp_trigs
if sd_resp_trigs.is_open:
    sd_resp_trigs.close()
# Close sd_blink_trigs
if sd_blink_trigs.is_open:
    sd_blink_trigs.close()
# Close break2_trigs
if break2_trigs.is_open:
    break2_trigs.close()
# Close learn2_instruction_trigs
if learn2_instruction_trigs.is_open:
    learn2_instruction_trigs.close()
# Close learn_fix_trigs
if learn_fix_trigs.is_open:
    learn_fix_trigs.close()
# Close learn_stim_trigs
if learn_stim_trigs.is_open:
    learn_stim_trigs.close()
# Close learn_feedback_trigs
if learn_feedback_trigs.is_open:
    learn_feedback_trigs.close()
# Close learn_label_trigs
if learn_label_trigs.is_open:
    learn_label_trigs.close()
# Close learn_blink_trigs
if learn_blink_trigs.is_open:
    learn_blink_trigs.close()
# Close break3_trigs
if break3_trigs.is_open:
    break3_trigs.close()
# Close sd3_instruction_trigs
if sd3_instruction_trigs.is_open:
    sd3_instruction_trigs.close()
# Close sd_fix_trigs
if sd_fix_trigs.is_open:
    sd_fix_trigs.close()
# Close sd_stim_trigs
if sd_stim_trigs.is_open:
    sd_stim_trigs.close()
# Close sd_resp_trigs
if sd_resp_trigs.is_open:
    sd_resp_trigs.close()
# Close sd_blink_trigs
if sd_blink_trigs.is_open:
    sd_blink_trigs.close()
# Close resting_closed_trigs_post
if resting_closed_trigs_post.is_open:
    resting_closed_trigs_post.close()
# Close resting_open_trigs_post
if resting_open_trigs_post.is_open:
    resting_open_trigs_post.close()
# Close exit_instruction_trigs
if exit_instruction_trigs.is_open:
    exit_instruction_trigs.close()
# Close exit_question_trigs
if exit_question_trigs.is_open:
    exit_question_trigs.close()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

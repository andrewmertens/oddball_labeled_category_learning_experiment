#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on April 13, 2025, at 14:09
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

# Run 'Before Experiment' code from stim_setup
alienH = .4
alienW = .2686

eyeSize = .11

explH = .1233
explW = .1

textH = .04
fixationH = .1

healthbarH = .4
healthbarW = .06
healthbarPosH = -.4
healthbarPosV = -.2


alien_body_file = 'stimuli/alienBody6.png'

full_health_score = 20 #starting hp
health_score = full_health_score
health_modifier = 1 #starting modifier (full health)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'PElearningExperiment4-1-25'  # from the Builder filename that created this script
expInfo = {
    'participant (experimenter use only)': '',
    'LC (experimenter use only)': ['GH', 'HH', 'NL'],
    'LS (experimenter use only)': ['HL', 'LH'],
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
    originPath='C:\\Users\\Andrew\\OneDrive - UCB-O365\\Grad School\\Research\\Dissertation\\CPlearning_experiment6\\oddball_labeled_category_learning_experiment\\PElearningExperiment_lastrun.py',
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

# --- Initialize components for Routine "learning_instructions0" ---
instructionLearn0 = visual.TextStim(win=win, name='instructionLearn0',
    text='Welcome trainee! You are about to take part in a training program to differentiate between extraterrestrial species on a newly found planet.\n\nTwo species exist on this planet: a friendly species that can be approached and a hostile species that must be avoided. Here you can see 4 different examples of aliens you might encounter. Note that differences in their eye patterns are what distinguish them from one another. \n\nIt will be your job to determine what eye patterns are representative of friendliness and and which are a sign of hostility.\nPress the spacebar to continue',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=1.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
alienBodyDemoLL = visual.ImageStim(
    win=win,
    name='alienBodyDemoLL', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(-.45, -.3), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
alienEyeDemoLL = visual.GratingStim(
    win=win, name='alienEyeDemoLL',
    tex='sin', mask='circle', anchor='center',
    ori=78.75, pos=(-.45, -.2), size=[eyeSize, eyeSize], sf=7.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-3.0)
alienBodyDemoL = visual.ImageStim(
    win=win,
    name='alienBodyDemoL', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(-.15, -.3), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
alienEyeDemoL = visual.GratingStim(
    win=win, name='alienEyeDemoL',
    tex='sin', mask='circle', anchor='center',
    ori=78.75, pos=(-.15, -.2), size=[eyeSize, eyeSize], sf=11.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-5.0)
alienBodyDemoR = visual.ImageStim(
    win=win,
    name='alienBodyDemoR', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(.15, -.3), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
alienEyeDemoR = visual.GratingStim(
    win=win, name='alienEyeDemoR',
    tex='sin', mask='circle', anchor='center',
    ori=-11.25, pos=(.15, -.2), size=[eyeSize, eyeSize], sf=7.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-7.0)
alienBodyDemoRR = visual.ImageStim(
    win=win,
    name='alienBodyDemoRR', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(.45, -.3), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
alienEyeDemoRR = visual.GratingStim(
    win=win, name='alienEyeDemoRR',
    tex='sin', mask='circle', anchor='center',
    ori=-11.25, pos=(.45, -.2), size=[eyeSize, eyeSize], sf=11.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-9.0)
key_resp_learn_0 = keyboard.Keyboard()

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

if expInfo['LS (experimenter use only)'] == 'HL':
    learning_sequence1 = 'conditions/oddhigh_conditions.xlsx'
    learning_sequence2 = 'conditions/oddlow_conditions.xlsx'
elif expInfo['LS (experimenter use only)'] == 'LH':
    learning_sequence1 = 'conditions/oddlow_conditions.xlsx'
    learning_sequence2 = 'conditions/oddhigh_conditions.xlsx'

alienBodyDemo1 = visual.ImageStim(
    win=win,
    name='alienBodyDemo1', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeDemo1 = visual.GratingStim(
    win=win, name='alienEyeDemo1',
    tex='sin', mask='circle', anchor='center',
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

# --- Initialize components for Routine "learning_instructions2" ---
alienBodyDemo1_2 = visual.ImageStim(
    win=win,
    name='alienBodyDemo1_2', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
alienEyeDemo1_2 = visual.GratingStim(
    win=win, name='alienEyeDemo1_2',
    tex='sin', mask='circle', anchor='center',
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

# --- Initialize components for Routine "learning_instructions3" ---
instructionLearn_3 = visual.TextStim(win=win, name='instructionLearn_3',
    text='We will provide you with feedback during this training so you can learn which aliens are friendly and which are hostile. When you answer correctly, you will hear a ‘boop’ sound. Press the ‘c’ key to hear it now.',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_3 = keyboard.Keyboard()

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

# --- Initialize components for Routine "learning_healthbar_instructions1" ---
health_border_instructions_1 = visual.Rect(
    win=win, name='health_border_instructions_1',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
health_fill_instructions_1 = visual.Rect(
    win=win, name='health_fill_instructions_1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-2.0, interpolate=True)
health_instructions_explorer_1 = visual.ImageStim(
    win=win,
    name='health_instructions_explorer_1', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(-.2, 0), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
health_instructions_text_1 = visual.TextStim(win=win, name='health_instructions_text_1',
    text="Additionally, your explorer's health is represented by this red health bar. Every time you make an incorrect response, the explorer's health will decrease.\n\nPress the spacebar to continue.",
    font='Open Sans',
    pos=(.1, 0), height=textH, wrapWidth=0.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
health_instructions_keys_1 = keyboard.Keyboard()

# --- Initialize components for Routine "learning_healthbar_instructions2" ---
health_border_instructions_2 = visual.Rect(
    win=win, name='health_border_instructions_2',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-1.0, interpolate=True)
health_fill_instructions_2 = visual.Rect(
    win=win, name='health_fill_instructions_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-2.0, interpolate=True)
health_instructions_explorer_2 = visual.ImageStim(
    win=win,
    name='health_instructions_explorer_2', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(-.2, 0), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
health_instructions_text_2 = visual.TextStim(win=win, name='health_instructions_text_2',
    text="Don't worry if your explorer's health runs out! If this happens, your explorer will just need to rest for 10 seconds before continuing.\n\nPress the spacebar to continue.",
    font='Open Sans',
    pos=(.1, 0), height=textH, wrapWidth=0.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
health_instructions_keys_2 = keyboard.Keyboard()

# --- Initialize components for Routine "learning_label_instructions" ---
learning_label_instruction_text = visual.TextStim(win=win, name='learning_label_instruction_text',
    text='Previous explorers have given names to the two species: Gowachi and Havnori. You will hear the name of the species of each alien you view in addition to the feedback sounds. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
label_instructions_key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "learning_instructions6" ---
instructionLearn6 = visual.TextStim(win=win, name='instructionLearn6',
    text='You are now ready to begin training! This task is divided into 10 sessions, after each of which you will be given a choice to take a short break. The counter at the top will indicate your progress in the current session. Try to respond as quickly and accurately as possible. Press the spacebar when you are prepared to start.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_6 = keyboard.Keyboard()

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
health_border_1 = visual.Rect(
    win=win, name='health_border_1',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
health_fill_1 = visual.Rect(
    win=win, name='health_fill_1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-4.0, interpolate=True)

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
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn = visual.GratingStim(
    win=win, name='alienEyeLearn',
    tex='sin', mask='circle', anchor='center',
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
health_border_2 = visual.Rect(
    win=win, name='health_border_2',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_2 = visual.Rect(
    win=win, name='health_fill_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    pos=(0, -.35), height=textH, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "learning_feedback" ---
feedbackSoundLearn = sound.Sound('A', secs=.25, stereo=True, hamming=True,
    name='feedbackSoundLearn')
feedbackSoundLearn.setVolume(1.0)
learn_trialNum_3 = visual.TextStim(win=win, name='learn_trialNum_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
alienBodyLearn2 = visual.ImageStim(
    win=win,
    name='alienBodyLearn2', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
alienEyeLearn2 = visual.GratingStim(
    win=win, name='alienEyeLearn2',
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
explorerLearn2 = visual.ImageStim(
    win=win,
    name='explorerLearn2', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
health_border_3 = visual.Rect(
    win=win, name='health_border_3',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_3 = visual.Rect(
    win=win, name='health_fill_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "learning_feedback_label" ---
trainingLabelLearn = sound.Sound('A', secs=.8, stereo=True, hamming=True,
    name='trainingLabelLearn')
trainingLabelLearn.setVolume(1.0)
learn_trialNum_4 = visual.TextStim(win=win, name='learn_trialNum_4',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
alienBodyLearn3 = visual.ImageStim(
    win=win,
    name='alienBodyLearn3', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
alienEyeLearn3 = visual.GratingStim(
    win=win, name='alienEyeLearn3',
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
explorerLearn3 = visual.ImageStim(
    win=win,
    name='explorerLearn3', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
health_border_4 = visual.Rect(
    win=win, name='health_border_4',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_4 = visual.Rect(
    win=win, name='health_fill_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "learning_regen" ---
explorerLearn4 = visual.ImageStim(
    win=win,
    name='explorerLearn4', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(-.2, 0), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
health_border_regen = visual.Rect(
    win=win, name='health_border_regen',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-2.0, interpolate=True)
health_fill_regen = visual.Rect(
    win=win, name='health_fill_regen',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-3.0, interpolate=True)
learning_text_regen = visual.TextStim(win=win, name='learning_text_regen',
    text='The explorer has low health and needs to rest before continuing.\nPlease wait.',
    font='Open Sans',
    pos=(.1, 0), height=textH, wrapWidth=0.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "learning_backmask" ---
# Run 'Begin Experiment' code from backmask_noise_code
noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
learn_trialNum_5 = visual.TextStim(win=win, name='learn_trialNum_5',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
noise_backmask = visual.GratingStim(
    win=win, name='noise_backmask',
    tex=noiseTexture, mask='circle', anchor='center',
    ori=0.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
health_border_5 = visual.Rect(
    win=win, name='health_border_5',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
health_fill_5 = visual.Rect(
    win=win, name='health_fill_5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "learning1_break1" ---
learn1_break1_text = visual.TextStim(win=win, name='learn1_break1_text',
    text='Would you like to take a break before proceeding? If so, stay on this screen. \n\nWhen you would like to proceed, press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
learn1_break1_keys = keyboard.Keyboard()

# --- Initialize components for Routine "learning2_instructions" ---
alienBodyDemo2 = visual.ImageStim(
    win=win,
    name='alienBodyDemo2', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(.45, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeDemo2 = visual.GratingStim(
    win=win, name='alienEyeDemo2',
    tex='sin', mask='circle', anchor='center',
    ori=41.0, pos=(.45, .1), size=[eyeSize, eyeSize], sf=10.0, phase=0.0,
    color=[1, 1, 1], colorSpace='rgb',
    opacity=1.0, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
explorerDemo2_U = visual.ImageStim(
    win=win,
    name='explorerDemo2_U', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(.45, .25), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instructionLearn2 = visual.TextStim(win=win, name='instructionLearn2',
    text='You’re doing great! You are currently at the halfway point of your training. The second part of your training will take place on a different part of the planet. The same friendly and hostile species exist on this part of the planet. \n\nAs before you will use the arrow keys to direct the space explorer towards friendly aliens and away from hostile ones. Press the spacebar when you are ready to continue.',
    font='Open Sans',
    pos=(-.25, 0), height=textH, wrapWidth=0.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
learning2_keyboard = keyboard.Keyboard()

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
health_border_1 = visual.Rect(
    win=win, name='health_border_1',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
health_fill_1 = visual.Rect(
    win=win, name='health_fill_1',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-4.0, interpolate=True)

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
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
alienEyeLearn = visual.GratingStim(
    win=win, name='alienEyeLearn',
    tex='sin', mask='circle', anchor='center',
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
health_border_2 = visual.Rect(
    win=win, name='health_border_2',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_2 = visual.Rect(
    win=win, name='health_fill_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    pos=(0, -.35), height=textH, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# --- Initialize components for Routine "learning_feedback" ---
feedbackSoundLearn = sound.Sound('A', secs=.25, stereo=True, hamming=True,
    name='feedbackSoundLearn')
feedbackSoundLearn.setVolume(1.0)
learn_trialNum_3 = visual.TextStim(win=win, name='learn_trialNum_3',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
alienBodyLearn2 = visual.ImageStim(
    win=win,
    name='alienBodyLearn2', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
alienEyeLearn2 = visual.GratingStim(
    win=win, name='alienEyeLearn2',
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
explorerLearn2 = visual.ImageStim(
    win=win,
    name='explorerLearn2', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
health_border_3 = visual.Rect(
    win=win, name='health_border_3',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_3 = visual.Rect(
    win=win, name='health_fill_3',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "learning_feedback_label" ---
trainingLabelLearn = sound.Sound('A', secs=.8, stereo=True, hamming=True,
    name='trainingLabelLearn')
trainingLabelLearn.setVolume(1.0)
learn_trialNum_4 = visual.TextStim(win=win, name='learn_trialNum_4',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
alienBodyLearn3 = visual.ImageStim(
    win=win,
    name='alienBodyLearn3', 
    image=alien_body_file, mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=[alienW, alienH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
alienEyeLearn3 = visual.GratingStim(
    win=win, name='alienEyeLearn3',
    tex='sin', mask='circle', anchor='center',
    ori=1.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-4.0)
explorerLearn3 = visual.ImageStim(
    win=win,
    name='explorerLearn3', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
health_border_4 = visual.Rect(
    win=win, name='health_border_4',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-6.0, interpolate=True)
health_fill_4 = visual.Rect(
    win=win, name='health_fill_4',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-7.0, interpolate=True)

# --- Initialize components for Routine "learning_regen" ---
explorerLearn4 = visual.ImageStim(
    win=win,
    name='explorerLearn4', 
    image='stimuli/spaceExplorer2.png', mask=None, anchor='center',
    ori=0.0, pos=(-.2, 0), size=[explW, explH],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
health_border_regen = visual.Rect(
    win=win, name='health_border_regen',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-2.0, interpolate=True)
health_fill_regen = visual.Rect(
    win=win, name='health_fill_regen',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-3.0, interpolate=True)
learning_text_regen = visual.TextStim(win=win, name='learning_text_regen',
    text='The explorer has low health and needs to rest before continuing.\nPlease wait.',
    font='Open Sans',
    pos=(.1, 0), height=textH, wrapWidth=0.4, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "learning_backmask" ---
# Run 'Begin Experiment' code from backmask_noise_code
noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
learn_trialNum_5 = visual.TextStim(win=win, name='learn_trialNum_5',
    text='',
    font='Open Sans',
    pos=(0, .4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
noise_backmask = visual.GratingStim(
    win=win, name='noise_backmask',
    tex=noiseTexture, mask='circle', anchor='center',
    ori=0.0, pos=(0, .1), size=[eyeSize, eyeSize], sf=1.0, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=None, contrast=0.5, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-2.0)
health_border_5 = visual.Rect(
    win=win, name='health_border_5',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-3.0, interpolate=True)
health_fill_5 = visual.Rect(
    win=win, name='health_fill_5',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-4.0, interpolate=True)

# --- Initialize components for Routine "learning2_break1" ---
learn2_break1_text = visual.TextStim(win=win, name='learn2_break1_text',
    text='Would you like to take a break before proceeding? If so, stay on this screen. \n\nWhen you would like to proceed, press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
learn2_break1_keys = keyboard.Keyboard()

# --- Initialize components for Routine "exit_instructions" ---
instructionExit = visual.TextStim(win=win, name='instructionExit',
    text='That concludes the experiment! Thank you so much for your hard work today. In the next and final section, questions about your experience today will appear at the top of the screen on each page. Please type your answer to each question and press the Enter (or Return) key to go to the next page. There are a total of 4 questions to answer. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_exit_1 = keyboard.Keyboard()

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

# --- Initialize components for Routine "experiment_end" ---
thank_you = visual.TextStim(win=win, name='thank_you',
    text='Thank you for participating in our project on language and categorization. In the project you just took part in, we are exploring how language affects the categorization of objects. As one of the conditions of the experiment, you may or may not have seen labels in conjunction with the aliens you saw in this experiment. We are examining the effect of these labels on categorization. \nPrevious research has shown that both written and verbal labels aid in category learning. This study aims to determine whether labels cause this effect by making differences between features of members of different categories more distinct while making differences between members of the same category less distinct.\nIf you have any questions or concerns about the project, please contact Andrew Mertens by email at Andrew.mertens@colorado.edu (you can also find this email on the SONA page for this experiment).\nPlease press the spacebar when you are done reading this page to conclude the experiment.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
experiment_end_key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "learning_instructions0" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_learn_0.keys = []
key_resp_learn_0.rt = []
_key_resp_learn_0_allKeys = []
# keep track of which components have finished
learning_instructions0Components = [instructionLearn0, alienBodyDemoLL, alienEyeDemoLL, alienBodyDemoL, alienEyeDemoL, alienBodyDemoR, alienEyeDemoR, alienBodyDemoRR, alienEyeDemoRR, key_resp_learn_0]
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
learning_instructions1Components = [alienBodyDemo1, alienEyeDemo1, explorerDemo1_L, instructionLearn1, key_resp_learn_1]
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
learning_instructions2Components = [alienBodyDemo1_2, alienEyeDemo1_2, explorerDemo1_2_U, instructionLearn_2, key_resp_learn_2]
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
learning_instructions3Components = [instructionLearn_3, key_resp_learn_3]
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
learning_instructions4Components = [correct_tone_instructions, instructionLearn4a, instructionLearn4b, key_resp_learn_4]
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
learning_instructions5Components = [incorrect_tone_instructions, instructionLearn5a, instructionLearn5b]
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
while continueRoutine and routineTimer.getTime() < 1.0:
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
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# --- Prepare to start Routine "learning_healthbar_instructions1" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from health_instructions_code_1
health_inst_timer = core.Clock()
health_instructions_keys_1.keys = []
health_instructions_keys_1.rt = []
_health_instructions_keys_1_allKeys = []
# keep track of which components have finished
learning_healthbar_instructions1Components = [health_border_instructions_1, health_fill_instructions_1, health_instructions_explorer_1, health_instructions_text_1, health_instructions_keys_1]
for thisComponent in learning_healthbar_instructions1Components:
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

# --- Run Routine "learning_healthbar_instructions1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from health_instructions_code_1
    curr_health_inst_time = round(health_inst_timer.getTime())
    health_score_inst = 19 + (curr_health_inst_time % 2) #alternates between 1 and 0 based on timer in 1 sec increments
    health_modifier_inst = health_score_inst/full_health_score
    
    # *health_border_instructions_1* updates
    
    # if health_border_instructions_1 is starting this frame...
    if health_border_instructions_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_border_instructions_1.frameNStart = frameN  # exact frame index
        health_border_instructions_1.tStart = t  # local t and not account for scr refresh
        health_border_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_border_instructions_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_border_instructions_1.started')
        # update status
        health_border_instructions_1.status = STARTED
        health_border_instructions_1.setAutoDraw(True)
    
    # if health_border_instructions_1 is active this frame...
    if health_border_instructions_1.status == STARTED:
        # update params
        pass
    
    # *health_fill_instructions_1* updates
    
    # if health_fill_instructions_1 is starting this frame...
    if health_fill_instructions_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_fill_instructions_1.frameNStart = frameN  # exact frame index
        health_fill_instructions_1.tStart = t  # local t and not account for scr refresh
        health_fill_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_fill_instructions_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_fill_instructions_1.started')
        # update status
        health_fill_instructions_1.status = STARTED
        health_fill_instructions_1.setAutoDraw(True)
    
    # if health_fill_instructions_1 is active this frame...
    if health_fill_instructions_1.status == STARTED:
        # update params
        health_fill_instructions_1.setSize((healthbarW, (healthbarH*health_modifier_inst)), log=False)
    
    # *health_instructions_explorer_1* updates
    
    # if health_instructions_explorer_1 is starting this frame...
    if health_instructions_explorer_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_explorer_1.frameNStart = frameN  # exact frame index
        health_instructions_explorer_1.tStart = t  # local t and not account for scr refresh
        health_instructions_explorer_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_explorer_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_explorer_1.started')
        # update status
        health_instructions_explorer_1.status = STARTED
        health_instructions_explorer_1.setAutoDraw(True)
    
    # if health_instructions_explorer_1 is active this frame...
    if health_instructions_explorer_1.status == STARTED:
        # update params
        pass
    
    # *health_instructions_text_1* updates
    
    # if health_instructions_text_1 is starting this frame...
    if health_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_text_1.frameNStart = frameN  # exact frame index
        health_instructions_text_1.tStart = t  # local t and not account for scr refresh
        health_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_text_1.started')
        # update status
        health_instructions_text_1.status = STARTED
        health_instructions_text_1.setAutoDraw(True)
    
    # if health_instructions_text_1 is active this frame...
    if health_instructions_text_1.status == STARTED:
        # update params
        pass
    
    # *health_instructions_keys_1* updates
    waitOnFlip = False
    
    # if health_instructions_keys_1 is starting this frame...
    if health_instructions_keys_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_keys_1.frameNStart = frameN  # exact frame index
        health_instructions_keys_1.tStart = t  # local t and not account for scr refresh
        health_instructions_keys_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_keys_1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_keys_1.started')
        # update status
        health_instructions_keys_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(health_instructions_keys_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(health_instructions_keys_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if health_instructions_keys_1.status == STARTED and not waitOnFlip:
        theseKeys = health_instructions_keys_1.getKeys(keyList=['space'], waitRelease=False)
        _health_instructions_keys_1_allKeys.extend(theseKeys)
        if len(_health_instructions_keys_1_allKeys):
            health_instructions_keys_1.keys = _health_instructions_keys_1_allKeys[-1].name  # just the last key pressed
            health_instructions_keys_1.rt = _health_instructions_keys_1_allKeys[-1].rt
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
    for thisComponent in learning_healthbar_instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_healthbar_instructions1" ---
for thisComponent in learning_healthbar_instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if health_instructions_keys_1.keys in ['', [], None]:  # No response was made
    health_instructions_keys_1.keys = None
thisExp.addData('health_instructions_keys_1.keys',health_instructions_keys_1.keys)
if health_instructions_keys_1.keys != None:  # we had a response
    thisExp.addData('health_instructions_keys_1.rt', health_instructions_keys_1.rt)
thisExp.nextEntry()
# the Routine "learning_healthbar_instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "learning_healthbar_instructions2" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from health_instructions_code_2
health_inst_timer.reset()
health_instructions_keys_2.keys = []
health_instructions_keys_2.rt = []
_health_instructions_keys_2_allKeys = []
# keep track of which components have finished
learning_healthbar_instructions2Components = [health_border_instructions_2, health_fill_instructions_2, health_instructions_explorer_2, health_instructions_text_2, health_instructions_keys_2]
for thisComponent in learning_healthbar_instructions2Components:
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

# --- Run Routine "learning_healthbar_instructions2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # Run 'Each Frame' code from health_instructions_code_2
    if round(health_inst_timer.getTime()) >= 11:
        health_inst_timer.reset()
    
    health_score_inst = round(health_inst_timer.getTime())
    health_modifier_inst = health_score_inst/full_health_score
    
    # *health_border_instructions_2* updates
    
    # if health_border_instructions_2 is starting this frame...
    if health_border_instructions_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_border_instructions_2.frameNStart = frameN  # exact frame index
        health_border_instructions_2.tStart = t  # local t and not account for scr refresh
        health_border_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_border_instructions_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_border_instructions_2.started')
        # update status
        health_border_instructions_2.status = STARTED
        health_border_instructions_2.setAutoDraw(True)
    
    # if health_border_instructions_2 is active this frame...
    if health_border_instructions_2.status == STARTED:
        # update params
        pass
    
    # *health_fill_instructions_2* updates
    
    # if health_fill_instructions_2 is starting this frame...
    if health_fill_instructions_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_fill_instructions_2.frameNStart = frameN  # exact frame index
        health_fill_instructions_2.tStart = t  # local t and not account for scr refresh
        health_fill_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_fill_instructions_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_fill_instructions_2.started')
        # update status
        health_fill_instructions_2.status = STARTED
        health_fill_instructions_2.setAutoDraw(True)
    
    # if health_fill_instructions_2 is active this frame...
    if health_fill_instructions_2.status == STARTED:
        # update params
        health_fill_instructions_2.setSize((healthbarW, (healthbarH*health_modifier_inst)), log=False)
    
    # *health_instructions_explorer_2* updates
    
    # if health_instructions_explorer_2 is starting this frame...
    if health_instructions_explorer_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_explorer_2.frameNStart = frameN  # exact frame index
        health_instructions_explorer_2.tStart = t  # local t and not account for scr refresh
        health_instructions_explorer_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_explorer_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_explorer_2.started')
        # update status
        health_instructions_explorer_2.status = STARTED
        health_instructions_explorer_2.setAutoDraw(True)
    
    # if health_instructions_explorer_2 is active this frame...
    if health_instructions_explorer_2.status == STARTED:
        # update params
        pass
    
    # *health_instructions_text_2* updates
    
    # if health_instructions_text_2 is starting this frame...
    if health_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_text_2.frameNStart = frameN  # exact frame index
        health_instructions_text_2.tStart = t  # local t and not account for scr refresh
        health_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_text_2.started')
        # update status
        health_instructions_text_2.status = STARTED
        health_instructions_text_2.setAutoDraw(True)
    
    # if health_instructions_text_2 is active this frame...
    if health_instructions_text_2.status == STARTED:
        # update params
        pass
    
    # *health_instructions_keys_2* updates
    waitOnFlip = False
    
    # if health_instructions_keys_2 is starting this frame...
    if health_instructions_keys_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_keys_2.frameNStart = frameN  # exact frame index
        health_instructions_keys_2.tStart = t  # local t and not account for scr refresh
        health_instructions_keys_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_keys_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'health_instructions_keys_2.started')
        # update status
        health_instructions_keys_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(health_instructions_keys_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(health_instructions_keys_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if health_instructions_keys_2.status == STARTED and not waitOnFlip:
        theseKeys = health_instructions_keys_2.getKeys(keyList=['space'], waitRelease=False)
        _health_instructions_keys_2_allKeys.extend(theseKeys)
        if len(_health_instructions_keys_2_allKeys):
            health_instructions_keys_2.keys = _health_instructions_keys_2_allKeys[-1].name  # just the last key pressed
            health_instructions_keys_2.rt = _health_instructions_keys_2_allKeys[-1].rt
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
    for thisComponent in learning_healthbar_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "learning_healthbar_instructions2" ---
for thisComponent in learning_healthbar_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if health_instructions_keys_2.keys in ['', [], None]:  # No response was made
    health_instructions_keys_2.keys = None
thisExp.addData('health_instructions_keys_2.keys',health_instructions_keys_2.keys)
if health_instructions_keys_2.keys != None:  # we had a response
    thisExp.addData('health_instructions_keys_2.rt', health_instructions_keys_2.rt)
thisExp.nextEntry()
# the Routine "learning_healthbar_instructions2" was not non-slip safe, so reset the non-slip timer
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
learning_label_instructionsComponents = [learning_label_instruction_text, label_instructions_key_resp]
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
learning_instructions6Components = [instructionLearn6, key_resp_learn_6]
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
learning1_oddcond_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(learning_sequence1),
    seed=None, name='learning1_oddcond_loop')
thisExp.addLoop(learning1_oddcond_loop)  # add the loop to the experiment
thisLearning1_oddcond_loop = learning1_oddcond_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning1_oddcond_loop.rgb)
if thisLearning1_oddcond_loop != None:
    for paramName in thisLearning1_oddcond_loop:
        exec('{} = thisLearning1_oddcond_loop[paramName]'.format(paramName))

for thisLearning1_oddcond_loop in learning1_oddcond_loop:
    currentLoop = learning1_oddcond_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLearning1_oddcond_loop.rgb)
    if thisLearning1_oddcond_loop != None:
        for paramName in thisLearning1_oddcond_loop:
            exec('{} = thisLearning1_oddcond_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    learning1_block_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blocks),
        seed=None, name='learning1_block_loop')
    thisExp.addLoop(learning1_block_loop)  # add the loop to the experiment
    thisLearning1_block_loop = learning1_block_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearning1_block_loop.rgb)
    if thisLearning1_block_loop != None:
        for paramName in thisLearning1_block_loop:
            exec('{} = thisLearning1_block_loop[paramName]'.format(paramName))
    
    for thisLearning1_block_loop in learning1_block_loop:
        currentLoop = learning1_block_loop
        # abbreviate parameter names if possible (e.g. rgb = thisLearning1_block_loop.rgb)
        if thisLearning1_block_loop != None:
            for paramName in thisLearning1_block_loop:
                exec('{} = thisLearning1_block_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "learning_fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from learn_trial_no_code
        learn_trial_nums = "Training Module Progress: " + str(currentLoop.thisN + 1) + " of " + str(currentLoop.nTotal);
        
        learn_trialNum_1.setText(learn_trial_nums)
        health_fill_1.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_fixationComponents = [learn_trialNum_1, fixationLearn, health_border_1, health_fill_1]
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
            
            # *health_border_1* updates
            
            # if health_border_1 is starting this frame...
            if health_border_1.status == NOT_STARTED and fixationLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_1.frameNStart = frameN  # exact frame index
                health_border_1.tStart = t  # local t and not account for scr refresh
                health_border_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_1.started')
                # update status
                health_border_1.status = STARTED
                health_border_1.setAutoDraw(True)
            
            # if health_border_1 is active this frame...
            if health_border_1.status == STARTED:
                # update params
                pass
            
            # if health_border_1 is stopping this frame...
            if health_border_1.status == STARTED:
                if bool(fixationLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_1.tStop = t  # not accounting for scr refresh
                    health_border_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_1.stopped')
                    # update status
                    health_border_1.status = FINISHED
                    health_border_1.setAutoDraw(False)
            
            # *health_fill_1* updates
            
            # if health_fill_1 is starting this frame...
            if health_fill_1.status == NOT_STARTED and fixationLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_1.frameNStart = frameN  # exact frame index
                health_fill_1.tStart = t  # local t and not account for scr refresh
                health_fill_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_1.started')
                # update status
                health_fill_1.status = STARTED
                health_fill_1.setAutoDraw(True)
            
            # if health_fill_1 is active this frame...
            if health_fill_1.status == STARTED:
                # update params
                pass
            
            # if health_fill_1 is stopping this frame...
            if health_fill_1.status == STARTED:
                if bool(fixationLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_1.tStop = t  # not accounting for scr refresh
                    health_fill_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_1.stopped')
                    # update status
                    health_fill_1.status = FINISHED
                    health_fill_1.setAutoDraw(False)
            
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
        health_fill_2.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, learn_photo_box, key_resp_learn, health_border_2, health_fill_2, learning_hint]
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
            if explorerLearn.status == NOT_STARTED and frameN >= 31:
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
            
            # if learn_photo_box is stopping this frame...
            if learn_photo_box.status == STARTED:
                if bool(len(_key_resp_learn_allKeys)):
                    # keep track of stop time/frame for later
                    learn_photo_box.tStop = t  # not accounting for scr refresh
                    learn_photo_box.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learn_photo_box.stopped')
                    # update status
                    learn_photo_box.status = FINISHED
                    learn_photo_box.setAutoDraw(False)
            
            # *key_resp_learn* updates
            waitOnFlip = False
            
            # if key_resp_learn is starting this frame...
            if key_resp_learn.status == NOT_STARTED and explorerLearn.status == STARTED:
                # keep track of start time/frame for later
                key_resp_learn.frameNStart = frameN  # exact frame index
                key_resp_learn.tStart = t  # local t and not account for scr refresh
                key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_learn.started')
                # update status
                key_resp_learn.status = STARTED
                # AllowedKeys looks like a variable named `learn_legal_keys`
                if not type(learn_legal_keys) in [list, tuple, np.ndarray]:
                    if not isinstance(learn_legal_keys, str):
                        logging.error('AllowedKeys variable `learn_legal_keys` is not string- or list-like.')
                        core.quit()
                    elif not ',' in learn_legal_keys:
                        learn_legal_keys = (learn_legal_keys,)
                    else:
                        learn_legal_keys = eval(learn_legal_keys)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_learn.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_learn.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_learn.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_learn.getKeys(keyList=list(learn_legal_keys), waitRelease=False)
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
            
            # *health_border_2* updates
            
            # if health_border_2 is starting this frame...
            if health_border_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_2.frameNStart = frameN  # exact frame index
                health_border_2.tStart = t  # local t and not account for scr refresh
                health_border_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_2.started')
                # update status
                health_border_2.status = STARTED
                health_border_2.setAutoDraw(True)
            
            # if health_border_2 is active this frame...
            if health_border_2.status == STARTED:
                # update params
                pass
            
            # *health_fill_2* updates
            
            # if health_fill_2 is starting this frame...
            if health_fill_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_2.frameNStart = frameN  # exact frame index
                health_fill_2.tStart = t  # local t and not account for scr refresh
                health_fill_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_2.started')
                # update status
                health_fill_2.status = STARTED
                health_fill_2.setAutoDraw(True)
            
            # if health_fill_2 is active this frame...
            if health_fill_2.status == STARTED:
                # update params
                pass
            
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
        # store data for learning1_block_loop (TrialHandler)
        learning1_block_loop.addData('key_resp_learn.keys',key_resp_learn.keys)
        learning1_block_loop.addData('key_resp_learn.corr', key_resp_learn.corr)
        if key_resp_learn.keys != None:  # we had a response
            learning1_block_loop.addData('key_resp_learn.rt', key_resp_learn.rt)
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
          health_score = health_score - 1 #hp reduction
        
        #multiplied by the height param of the health_fill poly to represent proportional health
        health_modifier = health_score/full_health_score #proportional health based on current hp
        feedbackSoundLearn.setSound(feedback_tone, secs=.25, hamming=True)
        feedbackSoundLearn.setVolume(1.0, log=False)
        learn_trialNum_3.setText(learn_trial_nums)
        alienEyeLearn2.setOri(learn_ori_val)
        alienEyeLearn2.setSF(learn_freq_val)
        explorerLearn2.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
        health_fill_3.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_feedbackComponents = [feedbackSoundLearn, learn_trialNum_3, alienBodyLearn2, alienEyeLearn2, explorerLearn2, health_border_3, health_fill_3]
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
            
            # *health_border_3* updates
            
            # if health_border_3 is starting this frame...
            if health_border_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_3.frameNStart = frameN  # exact frame index
                health_border_3.tStart = t  # local t and not account for scr refresh
                health_border_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_3.started')
                # update status
                health_border_3.status = STARTED
                health_border_3.setAutoDraw(True)
            
            # if health_border_3 is active this frame...
            if health_border_3.status == STARTED:
                # update params
                pass
            
            # if health_border_3 is stopping this frame...
            if health_border_3.status == STARTED:
                if bool(feedbackSoundLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_3.tStop = t  # not accounting for scr refresh
                    health_border_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_3.stopped')
                    # update status
                    health_border_3.status = FINISHED
                    health_border_3.setAutoDraw(False)
            
            # *health_fill_3* updates
            
            # if health_fill_3 is starting this frame...
            if health_fill_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_3.frameNStart = frameN  # exact frame index
                health_fill_3.tStart = t  # local t and not account for scr refresh
                health_fill_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_3.started')
                # update status
                health_fill_3.status = STARTED
                health_fill_3.setAutoDraw(True)
            
            # if health_fill_3 is active this frame...
            if health_fill_3.status == STARTED:
                # update params
                pass
            
            # if health_fill_3 is stopping this frame...
            if health_fill_3.status == STARTED:
                if bool(feedbackSoundLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_3.tStop = t  # not accounting for scr refresh
                    health_fill_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_3.stopped')
                    # update status
                    health_fill_3.status = FINISHED
                    health_fill_3.setAutoDraw(False)
            
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
        if learn_stim_type == 'friendly':
            labelLearn = 'stimuli/'+friendly_label+'.wav'
        elif learn_stim_type == 'hostile':
            labelLearn = 'stimuli/'+hostile_label+'.wav'
        
        if friendly_label == 'havnori':
            if learn_stim_type == 'friendly':
                label_trig = 174
            elif learn_stim_type == 'hostile':
                label_trig = 175
        elif friendly_label == 'gowachi':
            if learn_stim_type == 'friendly':
                label_trig = 175
            elif learn_stim_type == 'hostile':
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
        health_fill_4.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_feedback_labelComponents = [trainingLabelLearn, learn_trialNum_4, alienBodyLearn3, alienEyeLearn3, explorerLearn3, health_border_4, health_fill_4]
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
            
            # *health_border_4* updates
            
            # if health_border_4 is starting this frame...
            if health_border_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_4.frameNStart = frameN  # exact frame index
                health_border_4.tStart = t  # local t and not account for scr refresh
                health_border_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_4.started')
                # update status
                health_border_4.status = STARTED
                health_border_4.setAutoDraw(True)
            
            # if health_border_4 is active this frame...
            if health_border_4.status == STARTED:
                # update params
                pass
            
            # if health_border_4 is stopping this frame...
            if health_border_4.status == STARTED:
                if bool(trainingLabelLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_4.tStop = t  # not accounting for scr refresh
                    health_border_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_4.stopped')
                    # update status
                    health_border_4.status = FINISHED
                    health_border_4.setAutoDraw(False)
            
            # *health_fill_4* updates
            
            # if health_fill_4 is starting this frame...
            if health_fill_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_4.frameNStart = frameN  # exact frame index
                health_fill_4.tStart = t  # local t and not account for scr refresh
                health_fill_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_4.started')
                # update status
                health_fill_4.status = STARTED
                health_fill_4.setAutoDraw(True)
            
            # if health_fill_4 is active this frame...
            if health_fill_4.status == STARTED:
                # update params
                pass
            
            # if health_fill_4 is stopping this frame...
            if health_fill_4.status == STARTED:
                if bool(trainingLabelLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_4.tStop = t  # not accounting for scr refresh
                    health_fill_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_4.stopped')
                    # update status
                    health_fill_4.status = FINISHED
                    health_fill_4.setAutoDraw(False)
            
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
        
        # --- Prepare to start Routine "learning_regen" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from learning_regen_code
        if health_score != 0:
            has_health = True
            continueRoutine=False
        else:
            has_health = False
            regen_timer = core.Clock()
        # keep track of which components have finished
        learning_regenComponents = [explorerLearn4, health_border_regen, health_fill_regen, learning_text_regen]
        for thisComponent in learning_regenComponents:
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
        
        # --- Run Routine "learning_regen" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from learning_regen_code
            if has_health == False:
                regen_health = regen_timer.getTime()
                health_score = round(regen_timer.getTime())
                health_modifier = health_score/full_health_score
            
            # *explorerLearn4* updates
            
            # if explorerLearn4 is starting this frame...
            if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
            
            # if explorerLearn4 is stopping this frame...
            if explorerLearn4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn4.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn4.tStop = t  # not accounting for scr refresh
                    explorerLearn4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'explorerLearn4.stopped')
                    # update status
                    explorerLearn4.status = FINISHED
                    explorerLearn4.setAutoDraw(False)
            
            # *health_border_regen* updates
            
            # if health_border_regen is starting this frame...
            if health_border_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_regen.frameNStart = frameN  # exact frame index
                health_border_regen.tStart = t  # local t and not account for scr refresh
                health_border_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_regen.started')
                # update status
                health_border_regen.status = STARTED
                health_border_regen.setAutoDraw(True)
            
            # if health_border_regen is active this frame...
            if health_border_regen.status == STARTED:
                # update params
                pass
            
            # if health_border_regen is stopping this frame...
            if health_border_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_regen.tStop = t  # not accounting for scr refresh
                    health_border_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_regen.stopped')
                    # update status
                    health_border_regen.status = FINISHED
                    health_border_regen.setAutoDraw(False)
            
            # *health_fill_regen* updates
            
            # if health_fill_regen is starting this frame...
            if health_fill_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_regen.frameNStart = frameN  # exact frame index
                health_fill_regen.tStart = t  # local t and not account for scr refresh
                health_fill_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_regen.started')
                # update status
                health_fill_regen.status = STARTED
                health_fill_regen.setAutoDraw(True)
            
            # if health_fill_regen is active this frame...
            if health_fill_regen.status == STARTED:
                # update params
                health_fill_regen.setSize((healthbarW, (healthbarH*health_modifier)), log=False)
            
            # if health_fill_regen is stopping this frame...
            if health_fill_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_regen.tStop = t  # not accounting for scr refresh
                    health_fill_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_regen.stopped')
                    # update status
                    health_fill_regen.status = FINISHED
                    health_fill_regen.setAutoDraw(False)
            
            # *learning_text_regen* updates
            
            # if learning_text_regen is starting this frame...
            if learning_text_regen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_text_regen.frameNStart = frameN  # exact frame index
                learning_text_regen.tStart = t  # local t and not account for scr refresh
                learning_text_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_text_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_text_regen.started')
                # update status
                learning_text_regen.status = STARTED
                learning_text_regen.setAutoDraw(True)
            
            # if learning_text_regen is active this frame...
            if learning_text_regen.status == STARTED:
                # update params
                pass
            
            # if learning_text_regen is stopping this frame...
            if learning_text_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_text_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_text_regen.tStop = t  # not accounting for scr refresh
                    learning_text_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_text_regen.stopped')
                    # update status
                    learning_text_regen.status = FINISHED
                    learning_text_regen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_regenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "learning_regen" ---
        for thisComponent in learning_regenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from learning_regen_code
        if has_health == False:
            health_score = 10
            health_modifier = health_score/full_health_score
            has_health = True
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "learning_backmask" ---
        continueRoutine = True
        # update component parameters for each repeat
        learn_trialNum_5.setText(learn_trial_nums)
        noise_backmask.setSF(0.5)
        health_fill_5.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_backmaskComponents = [learn_trialNum_5, noise_backmask, health_border_5, health_fill_5]
        for thisComponent in learning_backmaskComponents:
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
        
        # --- Run Routine "learning_backmask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from backmask_noise_code
            noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
            
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
            
            # if learn_trialNum_5 is stopping this frame...
            if learn_trialNum_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_5.tStop = t  # not accounting for scr refresh
                    learn_trialNum_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learn_trialNum_5.stopped')
                    # update status
                    learn_trialNum_5.status = FINISHED
                    learn_trialNum_5.setAutoDraw(False)
            
            # *noise_backmask* updates
            
            # if noise_backmask is starting this frame...
            if noise_backmask.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                noise_backmask.frameNStart = frameN  # exact frame index
                noise_backmask.tStart = t  # local t and not account for scr refresh
                noise_backmask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_backmask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noise_backmask.started')
                # update status
                noise_backmask.status = STARTED
                noise_backmask.setAutoDraw(True)
            
            # if noise_backmask is active this frame...
            if noise_backmask.status == STARTED:
                # update params
                noise_backmask.setTex(noiseTexture, log=False)
            
            # if noise_backmask is stopping this frame...
            if noise_backmask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_backmask.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_backmask.tStop = t  # not accounting for scr refresh
                    noise_backmask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noise_backmask.stopped')
                    # update status
                    noise_backmask.status = FINISHED
                    noise_backmask.setAutoDraw(False)
            
            # *health_border_5* updates
            
            # if health_border_5 is starting this frame...
            if health_border_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_5.frameNStart = frameN  # exact frame index
                health_border_5.tStart = t  # local t and not account for scr refresh
                health_border_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_5.started')
                # update status
                health_border_5.status = STARTED
                health_border_5.setAutoDraw(True)
            
            # if health_border_5 is active this frame...
            if health_border_5.status == STARTED:
                # update params
                pass
            
            # if health_border_5 is stopping this frame...
            if health_border_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_5.tStop = t  # not accounting for scr refresh
                    health_border_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_5.stopped')
                    # update status
                    health_border_5.status = FINISHED
                    health_border_5.setAutoDraw(False)
            
            # *health_fill_5* updates
            
            # if health_fill_5 is starting this frame...
            if health_fill_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_5.frameNStart = frameN  # exact frame index
                health_fill_5.tStart = t  # local t and not account for scr refresh
                health_fill_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_5.started')
                # update status
                health_fill_5.status = STARTED
                health_fill_5.setAutoDraw(True)
            
            # if health_fill_5 is active this frame...
            if health_fill_5.status == STARTED:
                # update params
                pass
            
            # if health_fill_5 is stopping this frame...
            if health_fill_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_5.tStop = t  # not accounting for scr refresh
                    health_fill_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_5.stopped')
                    # update status
                    health_fill_5.status = FINISHED
                    health_fill_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_backmaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "learning_backmask" ---
        for thisComponent in learning_backmaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'learning1_block_loop'
    
    
    # --- Prepare to start Routine "learning1_break1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from learn1_break1_code
    if learning1_oddcond_loop.nRemaining == 0:
        continueRoutine=False
    
    #give up to 10 hp after finishing each block
    if (full_health_score - health_score) < 10:
        health_score = full_health_score
    else:
        health_score = health_score + 10
    
    health_modifier = health_score/full_health_score
    
    learn1_break1_trig = learning1_oddcond_loop.thisN + 15
    learn1_break1_keys.keys = []
    learn1_break1_keys.rt = []
    _learn1_break1_keys_allKeys = []
    # keep track of which components have finished
    learning1_break1Components = [learn1_break1_text, learn1_break1_keys]
    for thisComponent in learning1_break1Components:
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
    
    # --- Run Routine "learning1_break1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn1_break1_text* updates
        
        # if learn1_break1_text is starting this frame...
        if learn1_break1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn1_break1_text.frameNStart = frameN  # exact frame index
            learn1_break1_text.tStart = t  # local t and not account for scr refresh
            learn1_break1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn1_break1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn1_break1_text.started')
            # update status
            learn1_break1_text.status = STARTED
            learn1_break1_text.setAutoDraw(True)
        
        # if learn1_break1_text is active this frame...
        if learn1_break1_text.status == STARTED:
            # update params
            pass
        
        # *learn1_break1_keys* updates
        waitOnFlip = False
        
        # if learn1_break1_keys is starting this frame...
        if learn1_break1_keys.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            learn1_break1_keys.frameNStart = frameN  # exact frame index
            learn1_break1_keys.tStart = t  # local t and not account for scr refresh
            learn1_break1_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn1_break1_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn1_break1_keys.started')
            # update status
            learn1_break1_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learn1_break1_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learn1_break1_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learn1_break1_keys.status == STARTED and not waitOnFlip:
            theseKeys = learn1_break1_keys.getKeys(keyList=['space'], waitRelease=False)
            _learn1_break1_keys_allKeys.extend(theseKeys)
            if len(_learn1_break1_keys_allKeys):
                learn1_break1_keys.keys = _learn1_break1_keys_allKeys[-1].name  # just the last key pressed
                learn1_break1_keys.rt = _learn1_break1_keys_allKeys[-1].rt
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
        for thisComponent in learning1_break1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning1_break1" ---
    for thisComponent in learning1_break1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if learn1_break1_keys.keys in ['', [], None]:  # No response was made
        learn1_break1_keys.keys = None
    learning1_oddcond_loop.addData('learn1_break1_keys.keys',learn1_break1_keys.keys)
    if learn1_break1_keys.keys != None:  # we had a response
        learning1_oddcond_loop.addData('learn1_break1_keys.rt', learn1_break1_keys.rt)
    # the Routine "learning1_break1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'learning1_oddcond_loop'


# --- Prepare to start Routine "learning2_instructions" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from health_reset_code
#sets health back to full for second half of task
health_score = full_health_score
health_modifier = health_score/full_health_score
learning2_keyboard.keys = []
learning2_keyboard.rt = []
_learning2_keyboard_allKeys = []
# keep track of which components have finished
learning2_instructionsComponents = [alienBodyDemo2, alienEyeDemo2, explorerDemo2_U, instructionLearn2, learning2_keyboard]
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
learning2_oddcond_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(learning_sequence2),
    seed=None, name='learning2_oddcond_loop')
thisExp.addLoop(learning2_oddcond_loop)  # add the loop to the experiment
thisLearning2_oddcond_loop = learning2_oddcond_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearning2_oddcond_loop.rgb)
if thisLearning2_oddcond_loop != None:
    for paramName in thisLearning2_oddcond_loop:
        exec('{} = thisLearning2_oddcond_loop[paramName]'.format(paramName))

for thisLearning2_oddcond_loop in learning2_oddcond_loop:
    currentLoop = learning2_oddcond_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLearning2_oddcond_loop.rgb)
    if thisLearning2_oddcond_loop != None:
        for paramName in thisLearning2_oddcond_loop:
            exec('{} = thisLearning2_oddcond_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    learning2_block_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(blocks),
        seed=None, name='learning2_block_loop')
    thisExp.addLoop(learning2_block_loop)  # add the loop to the experiment
    thisLearning2_block_loop = learning2_block_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLearning2_block_loop.rgb)
    if thisLearning2_block_loop != None:
        for paramName in thisLearning2_block_loop:
            exec('{} = thisLearning2_block_loop[paramName]'.format(paramName))
    
    for thisLearning2_block_loop in learning2_block_loop:
        currentLoop = learning2_block_loop
        # abbreviate parameter names if possible (e.g. rgb = thisLearning2_block_loop.rgb)
        if thisLearning2_block_loop != None:
            for paramName in thisLearning2_block_loop:
                exec('{} = thisLearning2_block_loop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "learning_fixation" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from learn_trial_no_code
        learn_trial_nums = "Training Module Progress: " + str(currentLoop.thisN + 1) + " of " + str(currentLoop.nTotal);
        
        learn_trialNum_1.setText(learn_trial_nums)
        health_fill_1.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_fixationComponents = [learn_trialNum_1, fixationLearn, health_border_1, health_fill_1]
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
            
            # *health_border_1* updates
            
            # if health_border_1 is starting this frame...
            if health_border_1.status == NOT_STARTED and fixationLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_1.frameNStart = frameN  # exact frame index
                health_border_1.tStart = t  # local t and not account for scr refresh
                health_border_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_1.started')
                # update status
                health_border_1.status = STARTED
                health_border_1.setAutoDraw(True)
            
            # if health_border_1 is active this frame...
            if health_border_1.status == STARTED:
                # update params
                pass
            
            # if health_border_1 is stopping this frame...
            if health_border_1.status == STARTED:
                if bool(fixationLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_1.tStop = t  # not accounting for scr refresh
                    health_border_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_1.stopped')
                    # update status
                    health_border_1.status = FINISHED
                    health_border_1.setAutoDraw(False)
            
            # *health_fill_1* updates
            
            # if health_fill_1 is starting this frame...
            if health_fill_1.status == NOT_STARTED and fixationLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_1.frameNStart = frameN  # exact frame index
                health_fill_1.tStart = t  # local t and not account for scr refresh
                health_fill_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_1.started')
                # update status
                health_fill_1.status = STARTED
                health_fill_1.setAutoDraw(True)
            
            # if health_fill_1 is active this frame...
            if health_fill_1.status == STARTED:
                # update params
                pass
            
            # if health_fill_1 is stopping this frame...
            if health_fill_1.status == STARTED:
                if bool(fixationLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_1.tStop = t  # not accounting for scr refresh
                    health_fill_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_1.stopped')
                    # update status
                    health_fill_1.status = FINISHED
                    health_fill_1.setAutoDraw(False)
            
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
        health_fill_2.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, learn_photo_box, key_resp_learn, health_border_2, health_fill_2, learning_hint]
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
            if explorerLearn.status == NOT_STARTED and frameN >= 31:
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
            
            # if learn_photo_box is stopping this frame...
            if learn_photo_box.status == STARTED:
                if bool(len(_key_resp_learn_allKeys)):
                    # keep track of stop time/frame for later
                    learn_photo_box.tStop = t  # not accounting for scr refresh
                    learn_photo_box.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learn_photo_box.stopped')
                    # update status
                    learn_photo_box.status = FINISHED
                    learn_photo_box.setAutoDraw(False)
            
            # *key_resp_learn* updates
            waitOnFlip = False
            
            # if key_resp_learn is starting this frame...
            if key_resp_learn.status == NOT_STARTED and explorerLearn.status == STARTED:
                # keep track of start time/frame for later
                key_resp_learn.frameNStart = frameN  # exact frame index
                key_resp_learn.tStart = t  # local t and not account for scr refresh
                key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_learn.started')
                # update status
                key_resp_learn.status = STARTED
                # AllowedKeys looks like a variable named `learn_legal_keys`
                if not type(learn_legal_keys) in [list, tuple, np.ndarray]:
                    if not isinstance(learn_legal_keys, str):
                        logging.error('AllowedKeys variable `learn_legal_keys` is not string- or list-like.')
                        core.quit()
                    elif not ',' in learn_legal_keys:
                        learn_legal_keys = (learn_legal_keys,)
                    else:
                        learn_legal_keys = eval(learn_legal_keys)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_learn.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_learn.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_learn.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_learn.getKeys(keyList=list(learn_legal_keys), waitRelease=False)
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
            
            # *health_border_2* updates
            
            # if health_border_2 is starting this frame...
            if health_border_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_2.frameNStart = frameN  # exact frame index
                health_border_2.tStart = t  # local t and not account for scr refresh
                health_border_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_2.started')
                # update status
                health_border_2.status = STARTED
                health_border_2.setAutoDraw(True)
            
            # if health_border_2 is active this frame...
            if health_border_2.status == STARTED:
                # update params
                pass
            
            # *health_fill_2* updates
            
            # if health_fill_2 is starting this frame...
            if health_fill_2.status == NOT_STARTED and alienBodyLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_2.frameNStart = frameN  # exact frame index
                health_fill_2.tStart = t  # local t and not account for scr refresh
                health_fill_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_2.started')
                # update status
                health_fill_2.status = STARTED
                health_fill_2.setAutoDraw(True)
            
            # if health_fill_2 is active this frame...
            if health_fill_2.status == STARTED:
                # update params
                pass
            
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
        # store data for learning2_block_loop (TrialHandler)
        learning2_block_loop.addData('key_resp_learn.keys',key_resp_learn.keys)
        learning2_block_loop.addData('key_resp_learn.corr', key_resp_learn.corr)
        if key_resp_learn.keys != None:  # we had a response
            learning2_block_loop.addData('key_resp_learn.rt', key_resp_learn.rt)
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
          health_score = health_score - 1 #hp reduction
        
        #multiplied by the height param of the health_fill poly to represent proportional health
        health_modifier = health_score/full_health_score #proportional health based on current hp
        feedbackSoundLearn.setSound(feedback_tone, secs=.25, hamming=True)
        feedbackSoundLearn.setVolume(1.0, log=False)
        learn_trialNum_3.setText(learn_trial_nums)
        alienEyeLearn2.setOri(learn_ori_val)
        alienEyeLearn2.setSF(learn_freq_val)
        explorerLearn2.setPos((learn_explor_pos_LR, learn_explor_pos_UD))
        health_fill_3.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_feedbackComponents = [feedbackSoundLearn, learn_trialNum_3, alienBodyLearn2, alienEyeLearn2, explorerLearn2, health_border_3, health_fill_3]
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
            
            # *health_border_3* updates
            
            # if health_border_3 is starting this frame...
            if health_border_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_3.frameNStart = frameN  # exact frame index
                health_border_3.tStart = t  # local t and not account for scr refresh
                health_border_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_3.started')
                # update status
                health_border_3.status = STARTED
                health_border_3.setAutoDraw(True)
            
            # if health_border_3 is active this frame...
            if health_border_3.status == STARTED:
                # update params
                pass
            
            # if health_border_3 is stopping this frame...
            if health_border_3.status == STARTED:
                if bool(feedbackSoundLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_3.tStop = t  # not accounting for scr refresh
                    health_border_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_3.stopped')
                    # update status
                    health_border_3.status = FINISHED
                    health_border_3.setAutoDraw(False)
            
            # *health_fill_3* updates
            
            # if health_fill_3 is starting this frame...
            if health_fill_3.status == NOT_STARTED and feedbackSoundLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_3.frameNStart = frameN  # exact frame index
                health_fill_3.tStart = t  # local t and not account for scr refresh
                health_fill_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_3.started')
                # update status
                health_fill_3.status = STARTED
                health_fill_3.setAutoDraw(True)
            
            # if health_fill_3 is active this frame...
            if health_fill_3.status == STARTED:
                # update params
                pass
            
            # if health_fill_3 is stopping this frame...
            if health_fill_3.status == STARTED:
                if bool(feedbackSoundLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_3.tStop = t  # not accounting for scr refresh
                    health_fill_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_3.stopped')
                    # update status
                    health_fill_3.status = FINISHED
                    health_fill_3.setAutoDraw(False)
            
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
        if learn_stim_type == 'friendly':
            labelLearn = 'stimuli/'+friendly_label+'.wav'
        elif learn_stim_type == 'hostile':
            labelLearn = 'stimuli/'+hostile_label+'.wav'
        
        if friendly_label == 'havnori':
            if learn_stim_type == 'friendly':
                label_trig = 174
            elif learn_stim_type == 'hostile':
                label_trig = 175
        elif friendly_label == 'gowachi':
            if learn_stim_type == 'friendly':
                label_trig = 175
            elif learn_stim_type == 'hostile':
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
        health_fill_4.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_feedback_labelComponents = [trainingLabelLearn, learn_trialNum_4, alienBodyLearn3, alienEyeLearn3, explorerLearn3, health_border_4, health_fill_4]
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
            
            # *health_border_4* updates
            
            # if health_border_4 is starting this frame...
            if health_border_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
                # keep track of start time/frame for later
                health_border_4.frameNStart = frameN  # exact frame index
                health_border_4.tStart = t  # local t and not account for scr refresh
                health_border_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_4.started')
                # update status
                health_border_4.status = STARTED
                health_border_4.setAutoDraw(True)
            
            # if health_border_4 is active this frame...
            if health_border_4.status == STARTED:
                # update params
                pass
            
            # if health_border_4 is stopping this frame...
            if health_border_4.status == STARTED:
                if bool(trainingLabelLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_border_4.tStop = t  # not accounting for scr refresh
                    health_border_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_4.stopped')
                    # update status
                    health_border_4.status = FINISHED
                    health_border_4.setAutoDraw(False)
            
            # *health_fill_4* updates
            
            # if health_fill_4 is starting this frame...
            if health_fill_4.status == NOT_STARTED and trainingLabelLearn.status == STARTED:
                # keep track of start time/frame for later
                health_fill_4.frameNStart = frameN  # exact frame index
                health_fill_4.tStart = t  # local t and not account for scr refresh
                health_fill_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_4.started')
                # update status
                health_fill_4.status = STARTED
                health_fill_4.setAutoDraw(True)
            
            # if health_fill_4 is active this frame...
            if health_fill_4.status == STARTED:
                # update params
                pass
            
            # if health_fill_4 is stopping this frame...
            if health_fill_4.status == STARTED:
                if bool(trainingLabelLearn.status == FINISHED):
                    # keep track of stop time/frame for later
                    health_fill_4.tStop = t  # not accounting for scr refresh
                    health_fill_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_4.stopped')
                    # update status
                    health_fill_4.status = FINISHED
                    health_fill_4.setAutoDraw(False)
            
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
        
        # --- Prepare to start Routine "learning_regen" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from learning_regen_code
        if health_score != 0:
            has_health = True
            continueRoutine=False
        else:
            has_health = False
            regen_timer = core.Clock()
        # keep track of which components have finished
        learning_regenComponents = [explorerLearn4, health_border_regen, health_fill_regen, learning_text_regen]
        for thisComponent in learning_regenComponents:
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
        
        # --- Run Routine "learning_regen" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 10.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from learning_regen_code
            if has_health == False:
                regen_health = regen_timer.getTime()
                health_score = round(regen_timer.getTime())
                health_modifier = health_score/full_health_score
            
            # *explorerLearn4* updates
            
            # if explorerLearn4 is starting this frame...
            if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
            
            # if explorerLearn4 is stopping this frame...
            if explorerLearn4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn4.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn4.tStop = t  # not accounting for scr refresh
                    explorerLearn4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'explorerLearn4.stopped')
                    # update status
                    explorerLearn4.status = FINISHED
                    explorerLearn4.setAutoDraw(False)
            
            # *health_border_regen* updates
            
            # if health_border_regen is starting this frame...
            if health_border_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_regen.frameNStart = frameN  # exact frame index
                health_border_regen.tStart = t  # local t and not account for scr refresh
                health_border_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_regen.started')
                # update status
                health_border_regen.status = STARTED
                health_border_regen.setAutoDraw(True)
            
            # if health_border_regen is active this frame...
            if health_border_regen.status == STARTED:
                # update params
                pass
            
            # if health_border_regen is stopping this frame...
            if health_border_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_regen.tStop = t  # not accounting for scr refresh
                    health_border_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_regen.stopped')
                    # update status
                    health_border_regen.status = FINISHED
                    health_border_regen.setAutoDraw(False)
            
            # *health_fill_regen* updates
            
            # if health_fill_regen is starting this frame...
            if health_fill_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_regen.frameNStart = frameN  # exact frame index
                health_fill_regen.tStart = t  # local t and not account for scr refresh
                health_fill_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_regen.started')
                # update status
                health_fill_regen.status = STARTED
                health_fill_regen.setAutoDraw(True)
            
            # if health_fill_regen is active this frame...
            if health_fill_regen.status == STARTED:
                # update params
                health_fill_regen.setSize((healthbarW, (healthbarH*health_modifier)), log=False)
            
            # if health_fill_regen is stopping this frame...
            if health_fill_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_regen.tStop = t  # not accounting for scr refresh
                    health_fill_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_regen.stopped')
                    # update status
                    health_fill_regen.status = FINISHED
                    health_fill_regen.setAutoDraw(False)
            
            # *learning_text_regen* updates
            
            # if learning_text_regen is starting this frame...
            if learning_text_regen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_text_regen.frameNStart = frameN  # exact frame index
                learning_text_regen.tStart = t  # local t and not account for scr refresh
                learning_text_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_text_regen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'learning_text_regen.started')
                # update status
                learning_text_regen.status = STARTED
                learning_text_regen.setAutoDraw(True)
            
            # if learning_text_regen is active this frame...
            if learning_text_regen.status == STARTED:
                # update params
                pass
            
            # if learning_text_regen is stopping this frame...
            if learning_text_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_text_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_text_regen.tStop = t  # not accounting for scr refresh
                    learning_text_regen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learning_text_regen.stopped')
                    # update status
                    learning_text_regen.status = FINISHED
                    learning_text_regen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_regenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "learning_regen" ---
        for thisComponent in learning_regenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from learning_regen_code
        if has_health == False:
            health_score = 10
            health_modifier = health_score/full_health_score
            has_health = True
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-10.000000)
        
        # --- Prepare to start Routine "learning_backmask" ---
        continueRoutine = True
        # update component parameters for each repeat
        learn_trialNum_5.setText(learn_trial_nums)
        noise_backmask.setSF(0.5)
        health_fill_5.setSize((healthbarW, (healthbarH*health_modifier)))
        # keep track of which components have finished
        learning_backmaskComponents = [learn_trialNum_5, noise_backmask, health_border_5, health_fill_5]
        for thisComponent in learning_backmaskComponents:
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
        
        # --- Run Routine "learning_backmask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from backmask_noise_code
            noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
            
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
            
            # if learn_trialNum_5 is stopping this frame...
            if learn_trialNum_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_5.tStop = t  # not accounting for scr refresh
                    learn_trialNum_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'learn_trialNum_5.stopped')
                    # update status
                    learn_trialNum_5.status = FINISHED
                    learn_trialNum_5.setAutoDraw(False)
            
            # *noise_backmask* updates
            
            # if noise_backmask is starting this frame...
            if noise_backmask.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                noise_backmask.frameNStart = frameN  # exact frame index
                noise_backmask.tStart = t  # local t and not account for scr refresh
                noise_backmask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_backmask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'noise_backmask.started')
                # update status
                noise_backmask.status = STARTED
                noise_backmask.setAutoDraw(True)
            
            # if noise_backmask is active this frame...
            if noise_backmask.status == STARTED:
                # update params
                noise_backmask.setTex(noiseTexture, log=False)
            
            # if noise_backmask is stopping this frame...
            if noise_backmask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_backmask.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_backmask.tStop = t  # not accounting for scr refresh
                    noise_backmask.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'noise_backmask.stopped')
                    # update status
                    noise_backmask.status = FINISHED
                    noise_backmask.setAutoDraw(False)
            
            # *health_border_5* updates
            
            # if health_border_5 is starting this frame...
            if health_border_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_5.frameNStart = frameN  # exact frame index
                health_border_5.tStart = t  # local t and not account for scr refresh
                health_border_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_border_5.started')
                # update status
                health_border_5.status = STARTED
                health_border_5.setAutoDraw(True)
            
            # if health_border_5 is active this frame...
            if health_border_5.status == STARTED:
                # update params
                pass
            
            # if health_border_5 is stopping this frame...
            if health_border_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_5.tStop = t  # not accounting for scr refresh
                    health_border_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_border_5.stopped')
                    # update status
                    health_border_5.status = FINISHED
                    health_border_5.setAutoDraw(False)
            
            # *health_fill_5* updates
            
            # if health_fill_5 is starting this frame...
            if health_fill_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_5.frameNStart = frameN  # exact frame index
                health_fill_5.tStart = t  # local t and not account for scr refresh
                health_fill_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'health_fill_5.started')
                # update status
                health_fill_5.status = STARTED
                health_fill_5.setAutoDraw(True)
            
            # if health_fill_5 is active this frame...
            if health_fill_5.status == STARTED:
                # update params
                pass
            
            # if health_fill_5 is stopping this frame...
            if health_fill_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_5.tStop = t  # not accounting for scr refresh
                    health_fill_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'health_fill_5.stopped')
                    # update status
                    health_fill_5.status = FINISHED
                    health_fill_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_backmaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "learning_backmask" ---
        for thisComponent in learning_backmaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.500000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'learning2_block_loop'
    
    
    # --- Prepare to start Routine "learning2_break1" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from skip_learn2_break1_code
    if learning2_oddcond_loop.nRemaining == 0:
        continueRoutine=False
    
    if (full_health_score - health_score) < 10:
        health_score = full_health_score
    else:
        health_score = health_score + 10
    
    health_modifier = health_score/full_health_score
    
    learn2_break1_trig = learning2_oddcond_loop.thisN + 20
    learn2_break1_keys.keys = []
    learn2_break1_keys.rt = []
    _learn2_break1_keys_allKeys = []
    # keep track of which components have finished
    learning2_break1Components = [learn2_break1_text, learn2_break1_keys]
    for thisComponent in learning2_break1Components:
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
    
    # --- Run Routine "learning2_break1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn2_break1_text* updates
        
        # if learn2_break1_text is starting this frame...
        if learn2_break1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn2_break1_text.frameNStart = frameN  # exact frame index
            learn2_break1_text.tStart = t  # local t and not account for scr refresh
            learn2_break1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn2_break1_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn2_break1_text.started')
            # update status
            learn2_break1_text.status = STARTED
            learn2_break1_text.setAutoDraw(True)
        
        # if learn2_break1_text is active this frame...
        if learn2_break1_text.status == STARTED:
            # update params
            pass
        
        # *learn2_break1_keys* updates
        waitOnFlip = False
        
        # if learn2_break1_keys is starting this frame...
        if learn2_break1_keys.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            learn2_break1_keys.frameNStart = frameN  # exact frame index
            learn2_break1_keys.tStart = t  # local t and not account for scr refresh
            learn2_break1_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn2_break1_keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'learn2_break1_keys.started')
            # update status
            learn2_break1_keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(learn2_break1_keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(learn2_break1_keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if learn2_break1_keys.status == STARTED and not waitOnFlip:
            theseKeys = learn2_break1_keys.getKeys(keyList=['space'], waitRelease=False)
            _learn2_break1_keys_allKeys.extend(theseKeys)
            if len(_learn2_break1_keys_allKeys):
                learn2_break1_keys.keys = _learn2_break1_keys_allKeys[-1].name  # just the last key pressed
                learn2_break1_keys.rt = _learn2_break1_keys_allKeys[-1].rt
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
        for thisComponent in learning2_break1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning2_break1" ---
    for thisComponent in learning2_break1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if learn2_break1_keys.keys in ['', [], None]:  # No response was made
        learn2_break1_keys.keys = None
    learning2_oddcond_loop.addData('learn2_break1_keys.keys',learn2_break1_keys.keys)
    if learn2_break1_keys.keys != None:  # we had a response
        learning2_oddcond_loop.addData('learn2_break1_keys.rt', learn2_break1_keys.rt)
    # the Routine "learning2_break1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'learning2_oddcond_loop'


# --- Prepare to start Routine "exit_instructions" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_exit_1.keys = []
key_resp_exit_1.rt = []
_key_resp_exit_1_allKeys = []
# keep track of which components have finished
exit_instructionsComponents = [instructionExit, key_resp_exit_1]
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
    exit_questionnaireComponents = [exitQ_number, exitQuestion, exitResponse, exitContinueText, key_resp_exit_2]
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
experiment_end_key_resp.keys = []
experiment_end_key_resp.rt = []
_experiment_end_key_resp_allKeys = []
# keep track of which components have finished
experiment_endComponents = [thank_you, experiment_end_key_resp]
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
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
    
    # *experiment_end_key_resp* updates
    waitOnFlip = False
    
    # if experiment_end_key_resp is starting this frame...
    if experiment_end_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_end_key_resp.frameNStart = frameN  # exact frame index
        experiment_end_key_resp.tStart = t  # local t and not account for scr refresh
        experiment_end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_end_key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'experiment_end_key_resp.started')
        # update status
        experiment_end_key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(experiment_end_key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(experiment_end_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if experiment_end_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = experiment_end_key_resp.getKeys(keyList=['space'], waitRelease=False)
        _experiment_end_key_resp_allKeys.extend(theseKeys)
        if len(_experiment_end_key_resp_allKeys):
            experiment_end_key_resp.keys = _experiment_end_key_resp_allKeys[-1].name  # just the last key pressed
            experiment_end_key_resp.rt = _experiment_end_key_resp_allKeys[-1].rt
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
# check responses
if experiment_end_key_resp.keys in ['', [], None]:  # No response was made
    experiment_end_key_resp.keys = None
thisExp.addData('experiment_end_key_resp.keys',experiment_end_key_resp.keys)
if experiment_end_key_resp.keys != None:  # we had a response
    thisExp.addData('experiment_end_key_resp.rt', experiment_end_key_resp.rt)
thisExp.nextEntry()
# the Routine "experiment_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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

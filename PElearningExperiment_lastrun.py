#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on April 14, 2025, at 20:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.1.2')


from psychopy import locale_setup
from psychopy import prefs
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'CP6bp'  # from the Builder filename that created this script
expInfo = {'participant (experimenter use only)': '', 'LC (experimenter use only)': ['GH', 'HH', 'NL'], 'LS (experimenter use only)': ['HL', 'LH'], 'Age': '', 'Gender': ['Female','Male','Trans male/Trans man','Trans female/Trans woman','Non-binary','Non-conforming','Prefer not to answer','Other; specify below'], 'Specify here if you selected "Other" for gender above:': '', 'Race/Ethnicity': ['American Indian or Alaska Native','Asian','Black or African American','Hispanic or Latino','Native Hawaiian or Pacific Islander','White','Prefer not to answer','Multiple/Other; specify below'], 'Specify here if you selected "Other" for race/ethnicity above:': ''}
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

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='ptb')

# Initialize components for Routine "learning_instructions0"
learning_instructions0Clock = core.Clock()
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

# Initialize components for Routine "learning_instructions1"
learning_instructions1Clock = core.Clock()
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

# Initialize components for Routine "learning_instructions2"
learning_instructions2Clock = core.Clock()
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

# Initialize components for Routine "learning_instructions3"
learning_instructions3Clock = core.Clock()
instructionLearn_3 = visual.TextStim(win=win, name='instructionLearn_3',
    text='We will provide you with feedback during this training so you can learn which aliens are friendly and which are hostile. When you answer correctly, you will hear a ‘boop’ sound. Press the ‘c’ key to hear it now.',
    font='Open Sans',
    pos=(0, .2), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_3 = keyboard.Keyboard()

# Initialize components for Routine "learning_instructions4"
learning_instructions4Clock = core.Clock()
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

# Initialize components for Routine "learning_instructions5"
learning_instructions5Clock = core.Clock()
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

# Initialize components for Routine "learning_healthbar_instructions1"
learning_healthbar_instructions1Clock = core.Clock()
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

# Initialize components for Routine "learning_healthbar_instructions2"
learning_healthbar_instructions2Clock = core.Clock()
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

# Initialize components for Routine "learning_label_instructions"
learning_label_instructionsClock = core.Clock()
learning_label_instruction_text = visual.TextStim(win=win, name='learning_label_instruction_text',
    text='Previous explorers have given names to the two species: Gowachi and Havnori. You will hear the name of the species of each alien you view in addition to the feedback sounds. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
label_instructions_key_resp = keyboard.Keyboard()

# Initialize components for Routine "learning_instructions6"
learning_instructions6Clock = core.Clock()
instructionLearn6 = visual.TextStim(win=win, name='instructionLearn6',
    text='You are now ready to begin training! This task is divided into 10 sections after each of which you will be given a choice to take a short break. The counter at the top will indicate your progress in the current section. Try to respond as quickly and accurately as possible. Press the spacebar when you are prepared to start.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_learn_6 = keyboard.Keyboard()

# Initialize components for Routine "learning_fixation"
learning_fixationClock = core.Clock()
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

# Initialize components for Routine "learning_presentation"
learning_presentationClock = core.Clock()
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
key_resp_learn = keyboard.Keyboard()
health_border_2 = visual.Rect(
    win=win, name='health_border_2',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-5.0, interpolate=True)
health_fill_2 = visual.Rect(
    win=win, name='health_fill_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-6.0, interpolate=True)
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    pos=(0, -.35), height=textH, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "learning_feedback"
learning_feedbackClock = core.Clock()
health_modifier = 1 #starting modifier (full health)
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

# Initialize components for Routine "learning_feedback_label"
learning_feedback_labelClock = core.Clock()
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

# Initialize components for Routine "learning_regen"
learning_regenClock = core.Clock()
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

# Initialize components for Routine "learning_backmask"
learning_backmaskClock = core.Clock()
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

# Initialize components for Routine "learning1_break1"
learning1_break1Clock = core.Clock()
learn1_break1_text = visual.TextStim(win=win, name='learn1_break1_text',
    text='Would you like to take a break before proceeding? If so, stay on this screen. \n\nWhen you would like to proceed, press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
learn1_break1_keys = keyboard.Keyboard()

# Initialize components for Routine "learning2_instructions"
learning2_instructionsClock = core.Clock()
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

# Initialize components for Routine "learning_fixation"
learning_fixationClock = core.Clock()
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

# Initialize components for Routine "learning_presentation"
learning_presentationClock = core.Clock()
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
key_resp_learn = keyboard.Keyboard()
health_border_2 = visual.Rect(
    win=win, name='health_border_2',
    width=(healthbarW, healthbarH)[0], height=(healthbarW, healthbarH)[1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=4.0,     colorSpace='rgb',  lineColor=[0.3961, -0.7333, -0.7333], fillColor=[0.0000, 0.0000, 0.0000],
    opacity=None, depth=-5.0, interpolate=True)
health_fill_2 = visual.Rect(
    win=win, name='health_fill_2',
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0.0, pos=(healthbarPosH, healthbarPosV), anchor='bottom-left',
    lineWidth=0.0,     colorSpace='rgb',  lineColor=[0.0000, 0.0000, 0.0000], fillColor=[0.3961, -0.7333, -0.7333],
    opacity=None, depth=-6.0, interpolate=True)
learning_hint = visual.TextStim(win=win, name='learning_hint',
    text='Reminder: use the arrow keys to move the space explorer towards friendly aliens and away from hostile ones',
    font='Open Sans',
    pos=(0, -.35), height=textH, wrapWidth=1.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "learning_feedback"
learning_feedbackClock = core.Clock()
health_modifier = 1 #starting modifier (full health)
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

# Initialize components for Routine "learning_feedback_label"
learning_feedback_labelClock = core.Clock()
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

# Initialize components for Routine "learning_regen"
learning_regenClock = core.Clock()
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

# Initialize components for Routine "learning_backmask"
learning_backmaskClock = core.Clock()
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

# Initialize components for Routine "learning2_break1"
learning2_break1Clock = core.Clock()
learn2_break1_text = visual.TextStim(win=win, name='learn2_break1_text',
    text='Would you like to take a break before proceeding? If so, stay on this screen. \n\nWhen you would like to proceed, press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
learn2_break1_keys = keyboard.Keyboard()

# Initialize components for Routine "exit_instructions"
exit_instructionsClock = core.Clock()
instructionExit = visual.TextStim(win=win, name='instructionExit',
    text='That concludes the experiment! Thank you so much for your hard work today. In the next and final section, questions about your experience today will appear at the top of the screen on each page. Please type your answer to each question and press the Enter (or Return) key to go to the next page. There are a total of 5 questions to answer. Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_exit_1 = keyboard.Keyboard()

# Initialize components for Routine "exit_questionnaire"
exit_questionnaireClock = core.Clock()
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
     win, text=None, font='Open Sans',
     pos=(0, 0),     letterHeight=textH,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0, alignment='center',
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False, languageStyle='LTR',
     editable=True,
     name='exitResponse',
     autoLog=True,
)
exitContinueText = visual.TextStim(win=win, name='exitContinueText',
    text='Press the Enter key to continue',
    font='Open Sans',
    pos=(0, -.4), height=textH, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
key_resp_exit_2 = keyboard.Keyboard()

# Initialize components for Routine "experiment_end"
experiment_endClock = core.Clock()
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
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "learning_instructions0"-------
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
learning_instructions0Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions0"-------
while continueRoutine:
    # get current time
    t = learning_instructions0Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions0Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn0* updates
    if instructionLearn0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn0.frameNStart = frameN  # exact frame index
        instructionLearn0.tStart = t  # local t and not account for scr refresh
        instructionLearn0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn0, 'tStartRefresh')  # time at next scr refresh
        instructionLearn0.setAutoDraw(True)
    
    # *alienBodyDemoLL* updates
    if alienBodyDemoLL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoLL.frameNStart = frameN  # exact frame index
        alienBodyDemoLL.tStart = t  # local t and not account for scr refresh
        alienBodyDemoLL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoLL, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemoLL.setAutoDraw(True)
    
    # *alienEyeDemoLL* updates
    if alienEyeDemoLL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoLL.frameNStart = frameN  # exact frame index
        alienEyeDemoLL.tStart = t  # local t and not account for scr refresh
        alienEyeDemoLL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoLL, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemoLL.setAutoDraw(True)
    
    # *alienBodyDemoL* updates
    if alienBodyDemoL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoL.frameNStart = frameN  # exact frame index
        alienBodyDemoL.tStart = t  # local t and not account for scr refresh
        alienBodyDemoL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoL, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemoL.setAutoDraw(True)
    
    # *alienEyeDemoL* updates
    if alienEyeDemoL.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoL.frameNStart = frameN  # exact frame index
        alienEyeDemoL.tStart = t  # local t and not account for scr refresh
        alienEyeDemoL.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoL, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemoL.setAutoDraw(True)
    
    # *alienBodyDemoR* updates
    if alienBodyDemoR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoR.frameNStart = frameN  # exact frame index
        alienBodyDemoR.tStart = t  # local t and not account for scr refresh
        alienBodyDemoR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoR, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemoR.setAutoDraw(True)
    
    # *alienEyeDemoR* updates
    if alienEyeDemoR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoR.frameNStart = frameN  # exact frame index
        alienEyeDemoR.tStart = t  # local t and not account for scr refresh
        alienEyeDemoR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoR, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemoR.setAutoDraw(True)
    
    # *alienBodyDemoRR* updates
    if alienBodyDemoRR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemoRR.frameNStart = frameN  # exact frame index
        alienBodyDemoRR.tStart = t  # local t and not account for scr refresh
        alienBodyDemoRR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemoRR, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemoRR.setAutoDraw(True)
    
    # *alienEyeDemoRR* updates
    if alienEyeDemoRR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemoRR.frameNStart = frameN  # exact frame index
        alienEyeDemoRR.tStart = t  # local t and not account for scr refresh
        alienEyeDemoRR.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemoRR, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemoRR.setAutoDraw(True)
    
    # *key_resp_learn_0* updates
    waitOnFlip = False
    if key_resp_learn_0.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_0.frameNStart = frameN  # exact frame index
        key_resp_learn_0.tStart = t  # local t and not account for scr refresh
        key_resp_learn_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_0, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions0"-------
for thisComponent in learning_instructions0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionLearn0.started', instructionLearn0.tStartRefresh)
thisExp.addData('instructionLearn0.stopped', instructionLearn0.tStopRefresh)
thisExp.addData('alienBodyDemoLL.started', alienBodyDemoLL.tStartRefresh)
thisExp.addData('alienBodyDemoLL.stopped', alienBodyDemoLL.tStopRefresh)
thisExp.addData('alienEyeDemoLL.started', alienEyeDemoLL.tStartRefresh)
thisExp.addData('alienEyeDemoLL.stopped', alienEyeDemoLL.tStopRefresh)
thisExp.addData('alienBodyDemoL.started', alienBodyDemoL.tStartRefresh)
thisExp.addData('alienBodyDemoL.stopped', alienBodyDemoL.tStopRefresh)
thisExp.addData('alienEyeDemoL.started', alienEyeDemoL.tStartRefresh)
thisExp.addData('alienEyeDemoL.stopped', alienEyeDemoL.tStopRefresh)
thisExp.addData('alienBodyDemoR.started', alienBodyDemoR.tStartRefresh)
thisExp.addData('alienBodyDemoR.stopped', alienBodyDemoR.tStopRefresh)
thisExp.addData('alienEyeDemoR.started', alienEyeDemoR.tStartRefresh)
thisExp.addData('alienEyeDemoR.stopped', alienEyeDemoR.tStopRefresh)
thisExp.addData('alienBodyDemoRR.started', alienBodyDemoRR.tStartRefresh)
thisExp.addData('alienBodyDemoRR.stopped', alienBodyDemoRR.tStopRefresh)
thisExp.addData('alienEyeDemoRR.started', alienEyeDemoRR.tStartRefresh)
thisExp.addData('alienEyeDemoRR.stopped', alienEyeDemoRR.tStopRefresh)
# check responses
if key_resp_learn_0.keys in ['', [], None]:  # No response was made
    key_resp_learn_0.keys = None
thisExp.addData('key_resp_learn_0.keys',key_resp_learn_0.keys)
if key_resp_learn_0.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_0.rt', key_resp_learn_0.rt)
thisExp.addData('key_resp_learn_0.started', key_resp_learn_0.tStartRefresh)
thisExp.addData('key_resp_learn_0.stopped', key_resp_learn_0.tStopRefresh)
thisExp.nextEntry()
# the Routine "learning_instructions0" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions1"-------
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
learning_instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions1"-------
while continueRoutine:
    # get current time
    t = learning_instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo1* updates
    if alienBodyDemo1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo1.frameNStart = frameN  # exact frame index
        alienBodyDemo1.tStart = t  # local t and not account for scr refresh
        alienBodyDemo1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo1, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemo1.setAutoDraw(True)
    
    # *alienEyeDemo1* updates
    if alienEyeDemo1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo1.frameNStart = frameN  # exact frame index
        alienEyeDemo1.tStart = t  # local t and not account for scr refresh
        alienEyeDemo1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo1, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemo1.setAutoDraw(True)
    
    # *explorerDemo1_L* updates
    if explorerDemo1_L.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo1_L.frameNStart = frameN  # exact frame index
        explorerDemo1_L.tStart = t  # local t and not account for scr refresh
        explorerDemo1_L.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo1_L, 'tStartRefresh')  # time at next scr refresh
        explorerDemo1_L.setAutoDraw(True)
    
    # *instructionLearn1* updates
    if instructionLearn1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn1.frameNStart = frameN  # exact frame index
        instructionLearn1.tStart = t  # local t and not account for scr refresh
        instructionLearn1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn1, 'tStartRefresh')  # time at next scr refresh
        instructionLearn1.setAutoDraw(True)
    
    # *key_resp_learn_1* updates
    waitOnFlip = False
    if key_resp_learn_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_1.frameNStart = frameN  # exact frame index
        key_resp_learn_1.tStart = t  # local t and not account for scr refresh
        key_resp_learn_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_1, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions1"-------
for thisComponent in learning_instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('alienBodyDemo1.started', alienBodyDemo1.tStartRefresh)
thisExp.addData('alienBodyDemo1.stopped', alienBodyDemo1.tStopRefresh)
thisExp.addData('alienEyeDemo1.started', alienEyeDemo1.tStartRefresh)
thisExp.addData('alienEyeDemo1.stopped', alienEyeDemo1.tStopRefresh)
thisExp.addData('explorerDemo1_L.started', explorerDemo1_L.tStartRefresh)
thisExp.addData('explorerDemo1_L.stopped', explorerDemo1_L.tStopRefresh)
thisExp.addData('instructionLearn1.started', instructionLearn1.tStartRefresh)
thisExp.addData('instructionLearn1.stopped', instructionLearn1.tStopRefresh)
# the Routine "learning_instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions2"-------
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
learning_instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions2"-------
while continueRoutine:
    # get current time
    t = learning_instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo1_2* updates
    if alienBodyDemo1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo1_2.frameNStart = frameN  # exact frame index
        alienBodyDemo1_2.tStart = t  # local t and not account for scr refresh
        alienBodyDemo1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo1_2, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemo1_2.setAutoDraw(True)
    
    # *alienEyeDemo1_2* updates
    if alienEyeDemo1_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo1_2.frameNStart = frameN  # exact frame index
        alienEyeDemo1_2.tStart = t  # local t and not account for scr refresh
        alienEyeDemo1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo1_2, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemo1_2.setAutoDraw(True)
    
    # *explorerDemo1_2_U* updates
    if explorerDemo1_2_U.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo1_2_U.frameNStart = frameN  # exact frame index
        explorerDemo1_2_U.tStart = t  # local t and not account for scr refresh
        explorerDemo1_2_U.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo1_2_U, 'tStartRefresh')  # time at next scr refresh
        explorerDemo1_2_U.setAutoDraw(True)
    
    # *instructionLearn_2* updates
    if instructionLearn_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn_2.frameNStart = frameN  # exact frame index
        instructionLearn_2.tStart = t  # local t and not account for scr refresh
        instructionLearn_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn_2, 'tStartRefresh')  # time at next scr refresh
        instructionLearn_2.setAutoDraw(True)
    
    # *key_resp_learn_2* updates
    waitOnFlip = False
    if key_resp_learn_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_2.frameNStart = frameN  # exact frame index
        key_resp_learn_2.tStart = t  # local t and not account for scr refresh
        key_resp_learn_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_2, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions2"-------
for thisComponent in learning_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('alienBodyDemo1_2.started', alienBodyDemo1_2.tStartRefresh)
thisExp.addData('alienBodyDemo1_2.stopped', alienBodyDemo1_2.tStopRefresh)
thisExp.addData('alienEyeDemo1_2.started', alienEyeDemo1_2.tStartRefresh)
thisExp.addData('alienEyeDemo1_2.stopped', alienEyeDemo1_2.tStopRefresh)
thisExp.addData('explorerDemo1_2_U.started', explorerDemo1_2_U.tStartRefresh)
thisExp.addData('explorerDemo1_2_U.stopped', explorerDemo1_2_U.tStopRefresh)
thisExp.addData('instructionLearn_2.started', instructionLearn_2.tStartRefresh)
thisExp.addData('instructionLearn_2.stopped', instructionLearn_2.tStopRefresh)
# the Routine "learning_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions3"-------
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
learning_instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions3"-------
while continueRoutine:
    # get current time
    t = learning_instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn_3* updates
    if instructionLearn_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn_3.frameNStart = frameN  # exact frame index
        instructionLearn_3.tStart = t  # local t and not account for scr refresh
        instructionLearn_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn_3, 'tStartRefresh')  # time at next scr refresh
        instructionLearn_3.setAutoDraw(True)
    
    # *key_resp_learn_3* updates
    if key_resp_learn_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_3.frameNStart = frameN  # exact frame index
        key_resp_learn_3.tStart = t  # local t and not account for scr refresh
        key_resp_learn_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_3, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions3"-------
for thisComponent in learning_instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionLearn_3.started', instructionLearn_3.tStartRefresh)
thisExp.addData('instructionLearn_3.stopped', instructionLearn_3.tStopRefresh)
# check responses
if key_resp_learn_3.keys in ['', [], None]:  # No response was made
    key_resp_learn_3.keys = None
thisExp.addData('key_resp_learn_3.keys',key_resp_learn_3.keys)
if key_resp_learn_3.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_3.rt', key_resp_learn_3.rt)
thisExp.nextEntry()
# the Routine "learning_instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions4"-------
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
learning_instructions4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions4"-------
while continueRoutine:
    # get current time
    t = learning_instructions4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop correct_tone_instructions
    if correct_tone_instructions.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
        # keep track of start time/frame for later
        correct_tone_instructions.frameNStart = frameN  # exact frame index
        correct_tone_instructions.tStart = t  # local t and not account for scr refresh
        correct_tone_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        correct_tone_instructions.play(when=win)  # sync with win flip
    if correct_tone_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > correct_tone_instructions.tStartRefresh + .25-frameTolerance:
            # keep track of stop time/frame for later
            correct_tone_instructions.tStop = t  # not accounting for scr refresh
            correct_tone_instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(correct_tone_instructions, 'tStopRefresh')  # time at next scr refresh
            correct_tone_instructions.stop()
    
    # *instructionLearn4a* updates
    if instructionLearn4a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn4a.frameNStart = frameN  # exact frame index
        instructionLearn4a.tStart = t  # local t and not account for scr refresh
        instructionLearn4a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn4a, 'tStartRefresh')  # time at next scr refresh
        instructionLearn4a.setAutoDraw(True)
    
    # *instructionLearn4b* updates
    if instructionLearn4b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn4b.frameNStart = frameN  # exact frame index
        instructionLearn4b.tStart = t  # local t and not account for scr refresh
        instructionLearn4b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn4b, 'tStartRefresh')  # time at next scr refresh
        instructionLearn4b.setAutoDraw(True)
    
    # *key_resp_learn_4* updates
    waitOnFlip = False
    if key_resp_learn_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_4.frameNStart = frameN  # exact frame index
        key_resp_learn_4.tStart = t  # local t and not account for scr refresh
        key_resp_learn_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_4, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions4"-------
for thisComponent in learning_instructions4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
correct_tone_instructions.stop()  # ensure sound has stopped at end of routine
thisExp.addData('correct_tone_instructions.started', correct_tone_instructions.tStartRefresh)
thisExp.addData('correct_tone_instructions.stopped', correct_tone_instructions.tStopRefresh)
thisExp.addData('instructionLearn4a.started', instructionLearn4a.tStartRefresh)
thisExp.addData('instructionLearn4a.stopped', instructionLearn4a.tStopRefresh)
thisExp.addData('instructionLearn4b.started', instructionLearn4b.tStartRefresh)
thisExp.addData('instructionLearn4b.stopped', instructionLearn4b.tStopRefresh)
# check responses
if key_resp_learn_4.keys in ['', [], None]:  # No response was made
    key_resp_learn_4.keys = None
thisExp.addData('key_resp_learn_4.keys',key_resp_learn_4.keys)
if key_resp_learn_4.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_4.rt', key_resp_learn_4.rt)
thisExp.addData('key_resp_learn_4.started', key_resp_learn_4.tStartRefresh)
thisExp.addData('key_resp_learn_4.stopped', key_resp_learn_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "learning_instructions4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions5"-------
continueRoutine = True
routineTimer.add(1.000000)
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
learning_instructions5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learning_instructions5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # start/stop incorrect_tone_instructions
    if incorrect_tone_instructions.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
        # keep track of start time/frame for later
        incorrect_tone_instructions.frameNStart = frameN  # exact frame index
        incorrect_tone_instructions.tStart = t  # local t and not account for scr refresh
        incorrect_tone_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        incorrect_tone_instructions.play(when=win)  # sync with win flip
    if incorrect_tone_instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > incorrect_tone_instructions.tStartRefresh + .25-frameTolerance:
            # keep track of stop time/frame for later
            incorrect_tone_instructions.tStop = t  # not accounting for scr refresh
            incorrect_tone_instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(incorrect_tone_instructions, 'tStopRefresh')  # time at next scr refresh
            incorrect_tone_instructions.stop()
    
    # *instructionLearn5a* updates
    if instructionLearn5a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn5a.frameNStart = frameN  # exact frame index
        instructionLearn5a.tStart = t  # local t and not account for scr refresh
        instructionLearn5a.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn5a, 'tStartRefresh')  # time at next scr refresh
        instructionLearn5a.setAutoDraw(True)
    if instructionLearn5a.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructionLearn5a.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            instructionLearn5a.tStop = t  # not accounting for scr refresh
            instructionLearn5a.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructionLearn5a, 'tStopRefresh')  # time at next scr refresh
            instructionLearn5a.setAutoDraw(False)
    
    # *instructionLearn5b* updates
    if instructionLearn5b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn5b.frameNStart = frameN  # exact frame index
        instructionLearn5b.tStart = t  # local t and not account for scr refresh
        instructionLearn5b.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn5b, 'tStartRefresh')  # time at next scr refresh
        instructionLearn5b.setAutoDraw(True)
    if instructionLearn5b.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructionLearn5b.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            instructionLearn5b.tStop = t  # not accounting for scr refresh
            instructionLearn5b.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructionLearn5b, 'tStopRefresh')  # time at next scr refresh
            instructionLearn5b.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions5"-------
for thisComponent in learning_instructions5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
incorrect_tone_instructions.stop()  # ensure sound has stopped at end of routine
thisExp.addData('incorrect_tone_instructions.started', incorrect_tone_instructions.tStartRefresh)
thisExp.addData('incorrect_tone_instructions.stopped', incorrect_tone_instructions.tStopRefresh)
thisExp.addData('instructionLearn5a.started', instructionLearn5a.tStartRefresh)
thisExp.addData('instructionLearn5a.stopped', instructionLearn5a.tStopRefresh)
thisExp.addData('instructionLearn5b.started', instructionLearn5b.tStartRefresh)
thisExp.addData('instructionLearn5b.stopped', instructionLearn5b.tStopRefresh)

# ------Prepare to start Routine "learning_healthbar_instructions1"-------
continueRoutine = True
# update component parameters for each repeat
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
learning_healthbar_instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_healthbar_instructions1"-------
while continueRoutine:
    # get current time
    t = learning_healthbar_instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_healthbar_instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    curr_health_inst_time = round(health_inst_timer.getTime())
    health_score_inst = 19 + (curr_health_inst_time % 2) #alternates between 1 and 0 based on timer in 1 sec increments
    health_modifier_inst = health_score_inst/full_health_score
    
    # *health_border_instructions_1* updates
    if health_border_instructions_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_border_instructions_1.frameNStart = frameN  # exact frame index
        health_border_instructions_1.tStart = t  # local t and not account for scr refresh
        health_border_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_border_instructions_1, 'tStartRefresh')  # time at next scr refresh
        health_border_instructions_1.setAutoDraw(True)
    
    # *health_fill_instructions_1* updates
    if health_fill_instructions_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_fill_instructions_1.frameNStart = frameN  # exact frame index
        health_fill_instructions_1.tStart = t  # local t and not account for scr refresh
        health_fill_instructions_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_fill_instructions_1, 'tStartRefresh')  # time at next scr refresh
        health_fill_instructions_1.setAutoDraw(True)
    if health_fill_instructions_1.status == STARTED:  # only update if drawing
        health_fill_instructions_1.setSize((healthbarW, (healthbarH*health_modifier_inst)), log=False)
    
    # *health_instructions_explorer_1* updates
    if health_instructions_explorer_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_explorer_1.frameNStart = frameN  # exact frame index
        health_instructions_explorer_1.tStart = t  # local t and not account for scr refresh
        health_instructions_explorer_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_explorer_1, 'tStartRefresh')  # time at next scr refresh
        health_instructions_explorer_1.setAutoDraw(True)
    
    # *health_instructions_text_1* updates
    if health_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_text_1.frameNStart = frameN  # exact frame index
        health_instructions_text_1.tStart = t  # local t and not account for scr refresh
        health_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
        health_instructions_text_1.setAutoDraw(True)
    
    # *health_instructions_keys_1* updates
    waitOnFlip = False
    if health_instructions_keys_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_keys_1.frameNStart = frameN  # exact frame index
        health_instructions_keys_1.tStart = t  # local t and not account for scr refresh
        health_instructions_keys_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_keys_1, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_healthbar_instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_healthbar_instructions1"-------
for thisComponent in learning_healthbar_instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('health_border_instructions_1.started', health_border_instructions_1.tStartRefresh)
thisExp.addData('health_border_instructions_1.stopped', health_border_instructions_1.tStopRefresh)
thisExp.addData('health_fill_instructions_1.started', health_fill_instructions_1.tStartRefresh)
thisExp.addData('health_fill_instructions_1.stopped', health_fill_instructions_1.tStopRefresh)
thisExp.addData('health_instructions_explorer_1.started', health_instructions_explorer_1.tStartRefresh)
thisExp.addData('health_instructions_explorer_1.stopped', health_instructions_explorer_1.tStopRefresh)
thisExp.addData('health_instructions_text_1.started', health_instructions_text_1.tStartRefresh)
thisExp.addData('health_instructions_text_1.stopped', health_instructions_text_1.tStopRefresh)
# check responses
if health_instructions_keys_1.keys in ['', [], None]:  # No response was made
    health_instructions_keys_1.keys = None
thisExp.addData('health_instructions_keys_1.keys',health_instructions_keys_1.keys)
if health_instructions_keys_1.keys != None:  # we had a response
    thisExp.addData('health_instructions_keys_1.rt', health_instructions_keys_1.rt)
thisExp.addData('health_instructions_keys_1.started', health_instructions_keys_1.tStartRefresh)
thisExp.addData('health_instructions_keys_1.stopped', health_instructions_keys_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "learning_healthbar_instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_healthbar_instructions2"-------
continueRoutine = True
# update component parameters for each repeat
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
learning_healthbar_instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_healthbar_instructions2"-------
while continueRoutine:
    # get current time
    t = learning_healthbar_instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_healthbar_instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    if round(health_inst_timer.getTime()) >= 11:
        health_inst_timer.reset()
    
    health_score_inst = round(health_inst_timer.getTime())
    health_modifier_inst = health_score_inst/full_health_score
    
    # *health_border_instructions_2* updates
    if health_border_instructions_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_border_instructions_2.frameNStart = frameN  # exact frame index
        health_border_instructions_2.tStart = t  # local t and not account for scr refresh
        health_border_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_border_instructions_2, 'tStartRefresh')  # time at next scr refresh
        health_border_instructions_2.setAutoDraw(True)
    
    # *health_fill_instructions_2* updates
    if health_fill_instructions_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_fill_instructions_2.frameNStart = frameN  # exact frame index
        health_fill_instructions_2.tStart = t  # local t and not account for scr refresh
        health_fill_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_fill_instructions_2, 'tStartRefresh')  # time at next scr refresh
        health_fill_instructions_2.setAutoDraw(True)
    if health_fill_instructions_2.status == STARTED:  # only update if drawing
        health_fill_instructions_2.setSize((healthbarW, (healthbarH*health_modifier_inst)), log=False)
    
    # *health_instructions_explorer_2* updates
    if health_instructions_explorer_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_explorer_2.frameNStart = frameN  # exact frame index
        health_instructions_explorer_2.tStart = t  # local t and not account for scr refresh
        health_instructions_explorer_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_explorer_2, 'tStartRefresh')  # time at next scr refresh
        health_instructions_explorer_2.setAutoDraw(True)
    
    # *health_instructions_text_2* updates
    if health_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_text_2.frameNStart = frameN  # exact frame index
        health_instructions_text_2.tStart = t  # local t and not account for scr refresh
        health_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
        health_instructions_text_2.setAutoDraw(True)
    
    # *health_instructions_keys_2* updates
    waitOnFlip = False
    if health_instructions_keys_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        health_instructions_keys_2.frameNStart = frameN  # exact frame index
        health_instructions_keys_2.tStart = t  # local t and not account for scr refresh
        health_instructions_keys_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(health_instructions_keys_2, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_healthbar_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_healthbar_instructions2"-------
for thisComponent in learning_healthbar_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('health_border_instructions_2.started', health_border_instructions_2.tStartRefresh)
thisExp.addData('health_border_instructions_2.stopped', health_border_instructions_2.tStopRefresh)
thisExp.addData('health_fill_instructions_2.started', health_fill_instructions_2.tStartRefresh)
thisExp.addData('health_fill_instructions_2.stopped', health_fill_instructions_2.tStopRefresh)
thisExp.addData('health_instructions_explorer_2.started', health_instructions_explorer_2.tStartRefresh)
thisExp.addData('health_instructions_explorer_2.stopped', health_instructions_explorer_2.tStopRefresh)
thisExp.addData('health_instructions_text_2.started', health_instructions_text_2.tStartRefresh)
thisExp.addData('health_instructions_text_2.stopped', health_instructions_text_2.tStopRefresh)
# check responses
if health_instructions_keys_2.keys in ['', [], None]:  # No response was made
    health_instructions_keys_2.keys = None
thisExp.addData('health_instructions_keys_2.keys',health_instructions_keys_2.keys)
if health_instructions_keys_2.keys != None:  # we had a response
    thisExp.addData('health_instructions_keys_2.rt', health_instructions_keys_2.rt)
thisExp.addData('health_instructions_keys_2.started', health_instructions_keys_2.tStartRefresh)
thisExp.addData('health_instructions_keys_2.stopped', health_instructions_keys_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "learning_healthbar_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_label_instructions"-------
continueRoutine = True
# update component parameters for each repeat
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
learning_label_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_label_instructions"-------
while continueRoutine:
    # get current time
    t = learning_label_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_label_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *learning_label_instruction_text* updates
    if learning_label_instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        learning_label_instruction_text.frameNStart = frameN  # exact frame index
        learning_label_instruction_text.tStart = t  # local t and not account for scr refresh
        learning_label_instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning_label_instruction_text, 'tStartRefresh')  # time at next scr refresh
        learning_label_instruction_text.setAutoDraw(True)
    
    # *label_instructions_key_resp* updates
    waitOnFlip = False
    if label_instructions_key_resp.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        label_instructions_key_resp.frameNStart = frameN  # exact frame index
        label_instructions_key_resp.tStart = t  # local t and not account for scr refresh
        label_instructions_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(label_instructions_key_resp, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_label_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_label_instructions"-------
for thisComponent in learning_label_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('learning_label_instruction_text.started', learning_label_instruction_text.tStartRefresh)
thisExp.addData('learning_label_instruction_text.stopped', learning_label_instruction_text.tStopRefresh)
# the Routine "learning_label_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learning_instructions6"-------
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
learning_instructions6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning_instructions6"-------
while continueRoutine:
    # get current time
    t = learning_instructions6Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning_instructions6Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionLearn6* updates
    if instructionLearn6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn6.frameNStart = frameN  # exact frame index
        instructionLearn6.tStart = t  # local t and not account for scr refresh
        instructionLearn6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn6, 'tStartRefresh')  # time at next scr refresh
        instructionLearn6.setAutoDraw(True)
    
    # *key_resp_learn_6* updates
    waitOnFlip = False
    if key_resp_learn_6.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_learn_6.frameNStart = frameN  # exact frame index
        key_resp_learn_6.tStart = t  # local t and not account for scr refresh
        key_resp_learn_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_learn_6, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning_instructions6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning_instructions6"-------
for thisComponent in learning_instructions6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionLearn6.started', instructionLearn6.tStartRefresh)
thisExp.addData('instructionLearn6.stopped', instructionLearn6.tStopRefresh)
# check responses
if key_resp_learn_6.keys in ['', [], None]:  # No response was made
    key_resp_learn_6.keys = None
thisExp.addData('key_resp_learn_6.keys',key_resp_learn_6.keys)
if key_resp_learn_6.keys != None:  # we had a response
    thisExp.addData('key_resp_learn_6.rt', key_resp_learn_6.rt)
thisExp.addData('key_resp_learn_6.started', key_resp_learn_6.tStartRefresh)
thisExp.addData('key_resp_learn_6.stopped', key_resp_learn_6.tStopRefresh)
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
        
        # ------Prepare to start Routine "learning_fixation"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
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
        learning_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *learn_trialNum_1* updates
            if learn_trialNum_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_1.frameNStart = frameN  # exact frame index
                learn_trialNum_1.tStart = t  # local t and not account for scr refresh
                learn_trialNum_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_1, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_1.setAutoDraw(True)
            if learn_trialNum_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_1.tStop = t  # not accounting for scr refresh
                    learn_trialNum_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_1, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_1.setAutoDraw(False)
            
            # *fixationLearn* updates
            if fixationLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixationLearn.frameNStart = frameN  # exact frame index
                fixationLearn.tStart = t  # local t and not account for scr refresh
                fixationLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationLearn, 'tStartRefresh')  # time at next scr refresh
                fixationLearn.setAutoDraw(True)
            if fixationLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationLearn.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationLearn.tStop = t  # not accounting for scr refresh
                    fixationLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixationLearn, 'tStopRefresh')  # time at next scr refresh
                    fixationLearn.setAutoDraw(False)
            
            # *health_border_1* updates
            if health_border_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_1.frameNStart = frameN  # exact frame index
                health_border_1.tStart = t  # local t and not account for scr refresh
                health_border_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_1, 'tStartRefresh')  # time at next scr refresh
                health_border_1.setAutoDraw(True)
            if health_border_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_1.tStop = t  # not accounting for scr refresh
                    health_border_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_1, 'tStopRefresh')  # time at next scr refresh
                    health_border_1.setAutoDraw(False)
            
            # *health_fill_1* updates
            if health_fill_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_1.frameNStart = frameN  # exact frame index
                health_fill_1.tStart = t  # local t and not account for scr refresh
                health_fill_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_1, 'tStartRefresh')  # time at next scr refresh
                health_fill_1.setAutoDraw(True)
            if health_fill_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_1.tStop = t  # not accounting for scr refresh
                    health_fill_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_1, 'tStopRefresh')  # time at next scr refresh
                    health_fill_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_fixation"-------
        for thisComponent in learning_fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning1_block_loop.addData('learn_trialNum_1.started', learn_trialNum_1.tStartRefresh)
        learning1_block_loop.addData('learn_trialNum_1.stopped', learn_trialNum_1.tStopRefresh)
        learning1_block_loop.addData('fixationLearn.started', fixationLearn.tStartRefresh)
        learning1_block_loop.addData('fixationLearn.stopped', fixationLearn.tStopRefresh)
        learning1_block_loop.addData('health_border_1.started', health_border_1.tStartRefresh)
        learning1_block_loop.addData('health_border_1.stopped', health_border_1.tStopRefresh)
        learning1_block_loop.addData('health_fill_1.started', health_fill_1.tStartRefresh)
        learning1_block_loop.addData('health_fill_1.stopped', health_fill_1.tStopRefresh)
        
        # ------Prepare to start Routine "learning_presentation"-------
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
        learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, key_resp_learn, health_border_2, health_fill_2, learning_hint]
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
        learning_presentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_presentation"-------
        while continueRoutine:
            # get current time
            t = learning_presentationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_presentationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *learn_trialNum_2* updates
            if learn_trialNum_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_2.frameNStart = frameN  # exact frame index
                learn_trialNum_2.tStart = t  # local t and not account for scr refresh
                learn_trialNum_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_2, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_2.setAutoDraw(True)
            
            # *alienBodyLearn* updates
            if alienBodyLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn.frameNStart = frameN  # exact frame index
                alienBodyLearn.tStart = t  # local t and not account for scr refresh
                alienBodyLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn.setAutoDraw(True)
            
            # *alienEyeLearn* updates
            if alienEyeLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn.frameNStart = frameN  # exact frame index
                alienEyeLearn.tStart = t  # local t and not account for scr refresh
                alienEyeLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn.setAutoDraw(True)
            
            # *explorerLearn* updates
            if explorerLearn.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn.frameNStart = frameN  # exact frame index
                explorerLearn.tStart = t  # local t and not account for scr refresh
                explorerLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn, 'tStartRefresh')  # time at next scr refresh
                explorerLearn.setAutoDraw(True)
            
            # *key_resp_learn* updates
            waitOnFlip = False
            if key_resp_learn.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_learn.frameNStart = frameN  # exact frame index
                key_resp_learn.tStart = t  # local t and not account for scr refresh
                key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
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
            if health_border_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_2.frameNStart = frameN  # exact frame index
                health_border_2.tStart = t  # local t and not account for scr refresh
                health_border_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_2, 'tStartRefresh')  # time at next scr refresh
                health_border_2.setAutoDraw(True)
            
            # *health_fill_2* updates
            if health_fill_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_2.frameNStart = frameN  # exact frame index
                health_fill_2.tStart = t  # local t and not account for scr refresh
                health_fill_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_2, 'tStartRefresh')  # time at next scr refresh
                health_fill_2.setAutoDraw(True)
            
            # *learning_hint* updates
            if learning_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                learning_hint.frameNStart = frameN  # exact frame index
                learning_hint.tStart = t  # local t and not account for scr refresh
                learning_hint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_hint, 'tStartRefresh')  # time at next scr refresh
                learning_hint.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_presentation"-------
        for thisComponent in learning_presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning1_block_loop.addData('learn_trialNum_2.started', learn_trialNum_2.tStartRefresh)
        learning1_block_loop.addData('learn_trialNum_2.stopped', learn_trialNum_2.tStopRefresh)
        learning1_block_loop.addData('alienBodyLearn.started', alienBodyLearn.tStartRefresh)
        learning1_block_loop.addData('alienBodyLearn.stopped', alienBodyLearn.tStopRefresh)
        learning1_block_loop.addData('alienEyeLearn.started', alienEyeLearn.tStartRefresh)
        learning1_block_loop.addData('alienEyeLearn.stopped', alienEyeLearn.tStopRefresh)
        learning1_block_loop.addData('explorerLearn.started', explorerLearn.tStartRefresh)
        learning1_block_loop.addData('explorerLearn.stopped', explorerLearn.tStopRefresh)
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
        learning1_block_loop.addData('key_resp_learn.started', key_resp_learn.tStartRefresh)
        learning1_block_loop.addData('key_resp_learn.stopped', key_resp_learn.tStopRefresh)
        learning1_block_loop.addData('health_border_2.started', health_border_2.tStartRefresh)
        learning1_block_loop.addData('health_border_2.stopped', health_border_2.tStopRefresh)
        learning1_block_loop.addData('health_fill_2.started', health_fill_2.tStartRefresh)
        learning1_block_loop.addData('health_fill_2.stopped', health_fill_2.tStopRefresh)
        learning1_block_loop.addData('learning_hint.started', learning_hint.tStartRefresh)
        learning1_block_loop.addData('learning_hint.stopped', learning_hint.tStopRefresh)
        # the Routine "learning_presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "learning_feedback"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
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
        learning_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop feedbackSoundLearn
            if feedbackSoundLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSoundLearn.frameNStart = frameN  # exact frame index
                feedbackSoundLearn.tStart = t  # local t and not account for scr refresh
                feedbackSoundLearn.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackSoundLearn.play(when=win)  # sync with win flip
            if feedbackSoundLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSoundLearn.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSoundLearn.tStop = t  # not accounting for scr refresh
                    feedbackSoundLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSoundLearn, 'tStopRefresh')  # time at next scr refresh
                    feedbackSoundLearn.stop()
            
            # *learn_trialNum_3* updates
            if learn_trialNum_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_3.frameNStart = frameN  # exact frame index
                learn_trialNum_3.tStart = t  # local t and not account for scr refresh
                learn_trialNum_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_3, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_3.setAutoDraw(True)
            if learn_trialNum_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_3.tStop = t  # not accounting for scr refresh
                    learn_trialNum_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_3, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_3.setAutoDraw(False)
            
            # *alienBodyLearn2* updates
            if alienBodyLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn2.frameNStart = frameN  # exact frame index
                alienBodyLearn2.tStart = t  # local t and not account for scr refresh
                alienBodyLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn2, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn2.setAutoDraw(True)
            if alienBodyLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienBodyLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    alienBodyLearn2.tStop = t  # not accounting for scr refresh
                    alienBodyLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienBodyLearn2, 'tStopRefresh')  # time at next scr refresh
                    alienBodyLearn2.setAutoDraw(False)
            
            # *alienEyeLearn2* updates
            if alienEyeLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn2.frameNStart = frameN  # exact frame index
                alienEyeLearn2.tStart = t  # local t and not account for scr refresh
                alienEyeLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn2, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn2.setAutoDraw(True)
            if alienEyeLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienEyeLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    alienEyeLearn2.tStop = t  # not accounting for scr refresh
                    alienEyeLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienEyeLearn2, 'tStopRefresh')  # time at next scr refresh
                    alienEyeLearn2.setAutoDraw(False)
            
            # *explorerLearn2* updates
            if explorerLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn2.frameNStart = frameN  # exact frame index
                explorerLearn2.tStart = t  # local t and not account for scr refresh
                explorerLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn2, 'tStartRefresh')  # time at next scr refresh
                explorerLearn2.setAutoDraw(True)
            if explorerLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn2.tStop = t  # not accounting for scr refresh
                    explorerLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn2, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn2.setAutoDraw(False)
            
            # *health_border_3* updates
            if health_border_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_3.frameNStart = frameN  # exact frame index
                health_border_3.tStart = t  # local t and not account for scr refresh
                health_border_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_3, 'tStartRefresh')  # time at next scr refresh
                health_border_3.setAutoDraw(True)
            if health_border_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_3.tStop = t  # not accounting for scr refresh
                    health_border_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_3, 'tStopRefresh')  # time at next scr refresh
                    health_border_3.setAutoDraw(False)
            
            # *health_fill_3* updates
            if health_fill_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_3.frameNStart = frameN  # exact frame index
                health_fill_3.tStart = t  # local t and not account for scr refresh
                health_fill_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_3, 'tStartRefresh')  # time at next scr refresh
                health_fill_3.setAutoDraw(True)
            if health_fill_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_3.tStop = t  # not accounting for scr refresh
                    health_fill_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_3, 'tStopRefresh')  # time at next scr refresh
                    health_fill_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_feedback"-------
        for thisComponent in learning_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedbackSoundLearn.stop()  # ensure sound has stopped at end of routine
        learning1_block_loop.addData('feedbackSoundLearn.started', feedbackSoundLearn.tStartRefresh)
        learning1_block_loop.addData('feedbackSoundLearn.stopped', feedbackSoundLearn.tStopRefresh)
        learning1_block_loop.addData('learn_trialNum_3.started', learn_trialNum_3.tStartRefresh)
        learning1_block_loop.addData('learn_trialNum_3.stopped', learn_trialNum_3.tStopRefresh)
        learning1_block_loop.addData('alienBodyLearn2.started', alienBodyLearn2.tStartRefresh)
        learning1_block_loop.addData('alienBodyLearn2.stopped', alienBodyLearn2.tStopRefresh)
        learning1_block_loop.addData('alienEyeLearn2.started', alienEyeLearn2.tStartRefresh)
        learning1_block_loop.addData('alienEyeLearn2.stopped', alienEyeLearn2.tStopRefresh)
        learning1_block_loop.addData('explorerLearn2.started', explorerLearn2.tStartRefresh)
        learning1_block_loop.addData('explorerLearn2.stopped', explorerLearn2.tStopRefresh)
        learning1_block_loop.addData('health_border_3.started', health_border_3.tStartRefresh)
        learning1_block_loop.addData('health_border_3.stopped', health_border_3.tStopRefresh)
        learning1_block_loop.addData('health_fill_3.started', health_fill_3.tStartRefresh)
        learning1_block_loop.addData('health_fill_3.stopped', health_fill_3.tStopRefresh)
        
        # ------Prepare to start Routine "learning_feedback_label"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
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
        learning_feedback_labelClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_feedback_label"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_feedback_labelClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_feedback_labelClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop trainingLabelLearn
            if trainingLabelLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                trainingLabelLearn.frameNStart = frameN  # exact frame index
                trainingLabelLearn.tStart = t  # local t and not account for scr refresh
                trainingLabelLearn.tStartRefresh = tThisFlipGlobal  # on global time
                trainingLabelLearn.play(when=win)  # sync with win flip
            if trainingLabelLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trainingLabelLearn.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    trainingLabelLearn.tStop = t  # not accounting for scr refresh
                    trainingLabelLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trainingLabelLearn, 'tStopRefresh')  # time at next scr refresh
                    trainingLabelLearn.stop()
            
            # *learn_trialNum_4* updates
            if learn_trialNum_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_4.frameNStart = frameN  # exact frame index
                learn_trialNum_4.tStart = t  # local t and not account for scr refresh
                learn_trialNum_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_4, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_4.setAutoDraw(True)
            if learn_trialNum_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_4.tStop = t  # not accounting for scr refresh
                    learn_trialNum_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_4, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_4.setAutoDraw(False)
            
            # *alienBodyLearn3* updates
            if alienBodyLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn3.frameNStart = frameN  # exact frame index
                alienBodyLearn3.tStart = t  # local t and not account for scr refresh
                alienBodyLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn3, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn3.setAutoDraw(True)
            if alienBodyLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienBodyLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    alienBodyLearn3.tStop = t  # not accounting for scr refresh
                    alienBodyLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienBodyLearn3, 'tStopRefresh')  # time at next scr refresh
                    alienBodyLearn3.setAutoDraw(False)
            
            # *alienEyeLearn3* updates
            if alienEyeLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn3.frameNStart = frameN  # exact frame index
                alienEyeLearn3.tStart = t  # local t and not account for scr refresh
                alienEyeLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn3, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn3.setAutoDraw(True)
            if alienEyeLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienEyeLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    alienEyeLearn3.tStop = t  # not accounting for scr refresh
                    alienEyeLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienEyeLearn3, 'tStopRefresh')  # time at next scr refresh
                    alienEyeLearn3.setAutoDraw(False)
            
            # *explorerLearn3* updates
            if explorerLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn3.frameNStart = frameN  # exact frame index
                explorerLearn3.tStart = t  # local t and not account for scr refresh
                explorerLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn3, 'tStartRefresh')  # time at next scr refresh
                explorerLearn3.setAutoDraw(True)
            if explorerLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn3.tStop = t  # not accounting for scr refresh
                    explorerLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn3, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn3.setAutoDraw(False)
            
            # *health_border_4* updates
            if health_border_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_4.frameNStart = frameN  # exact frame index
                health_border_4.tStart = t  # local t and not account for scr refresh
                health_border_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_4, 'tStartRefresh')  # time at next scr refresh
                health_border_4.setAutoDraw(True)
            if health_border_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_4.tStop = t  # not accounting for scr refresh
                    health_border_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_4, 'tStopRefresh')  # time at next scr refresh
                    health_border_4.setAutoDraw(False)
            
            # *health_fill_4* updates
            if health_fill_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_4.frameNStart = frameN  # exact frame index
                health_fill_4.tStart = t  # local t and not account for scr refresh
                health_fill_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_4, 'tStartRefresh')  # time at next scr refresh
                health_fill_4.setAutoDraw(True)
            if health_fill_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_4.tStop = t  # not accounting for scr refresh
                    health_fill_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_4, 'tStopRefresh')  # time at next scr refresh
                    health_fill_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_feedback_labelComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_feedback_label"-------
        for thisComponent in learning_feedback_labelComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trainingLabelLearn.stop()  # ensure sound has stopped at end of routine
        learning1_block_loop.addData('learn_trialNum_4.started', learn_trialNum_4.tStartRefresh)
        learning1_block_loop.addData('learn_trialNum_4.stopped', learn_trialNum_4.tStopRefresh)
        learning1_block_loop.addData('alienBodyLearn3.started', alienBodyLearn3.tStartRefresh)
        learning1_block_loop.addData('alienBodyLearn3.stopped', alienBodyLearn3.tStopRefresh)
        learning1_block_loop.addData('alienEyeLearn3.started', alienEyeLearn3.tStartRefresh)
        learning1_block_loop.addData('alienEyeLearn3.stopped', alienEyeLearn3.tStopRefresh)
        learning1_block_loop.addData('explorerLearn3.started', explorerLearn3.tStartRefresh)
        learning1_block_loop.addData('explorerLearn3.stopped', explorerLearn3.tStopRefresh)
        learning1_block_loop.addData('health_border_4.started', health_border_4.tStartRefresh)
        learning1_block_loop.addData('health_border_4.stopped', health_border_4.tStopRefresh)
        learning1_block_loop.addData('health_fill_4.started', health_fill_4.tStartRefresh)
        learning1_block_loop.addData('health_fill_4.stopped', health_fill_4.tStopRefresh)
        
        # ------Prepare to start Routine "learning_regen"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
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
        learning_regenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_regen"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_regenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_regenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if has_health == False:
                regen_health = regen_timer.getTime()
                health_score = round(regen_timer.getTime())
                health_modifier = health_score/full_health_score
            
            # *explorerLearn4* updates
            if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn4.frameNStart = frameN  # exact frame index
                explorerLearn4.tStart = t  # local t and not account for scr refresh
                explorerLearn4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn4, 'tStartRefresh')  # time at next scr refresh
                explorerLearn4.setAutoDraw(True)
            if explorerLearn4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn4.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn4.tStop = t  # not accounting for scr refresh
                    explorerLearn4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn4, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn4.setAutoDraw(False)
            
            # *health_border_regen* updates
            if health_border_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_regen.frameNStart = frameN  # exact frame index
                health_border_regen.tStart = t  # local t and not account for scr refresh
                health_border_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_regen, 'tStartRefresh')  # time at next scr refresh
                health_border_regen.setAutoDraw(True)
            if health_border_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_regen.tStop = t  # not accounting for scr refresh
                    health_border_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_regen, 'tStopRefresh')  # time at next scr refresh
                    health_border_regen.setAutoDraw(False)
            
            # *health_fill_regen* updates
            if health_fill_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_regen.frameNStart = frameN  # exact frame index
                health_fill_regen.tStart = t  # local t and not account for scr refresh
                health_fill_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_regen, 'tStartRefresh')  # time at next scr refresh
                health_fill_regen.setAutoDraw(True)
            if health_fill_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_regen.tStop = t  # not accounting for scr refresh
                    health_fill_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_regen, 'tStopRefresh')  # time at next scr refresh
                    health_fill_regen.setAutoDraw(False)
            if health_fill_regen.status == STARTED:  # only update if drawing
                health_fill_regen.setSize((healthbarW, (healthbarH*health_modifier)), log=False)
            
            # *learning_text_regen* updates
            if learning_text_regen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_text_regen.frameNStart = frameN  # exact frame index
                learning_text_regen.tStart = t  # local t and not account for scr refresh
                learning_text_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_text_regen, 'tStartRefresh')  # time at next scr refresh
                learning_text_regen.setAutoDraw(True)
            if learning_text_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_text_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_text_regen.tStop = t  # not accounting for scr refresh
                    learning_text_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learning_text_regen, 'tStopRefresh')  # time at next scr refresh
                    learning_text_regen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_regenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_regen"-------
        for thisComponent in learning_regenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if has_health == False:
            health_score = 10
            health_modifier = health_score/full_health_score
            has_health = True
        learning1_block_loop.addData('explorerLearn4.started', explorerLearn4.tStartRefresh)
        learning1_block_loop.addData('explorerLearn4.stopped', explorerLearn4.tStopRefresh)
        learning1_block_loop.addData('health_border_regen.started', health_border_regen.tStartRefresh)
        learning1_block_loop.addData('health_border_regen.stopped', health_border_regen.tStopRefresh)
        learning1_block_loop.addData('health_fill_regen.started', health_fill_regen.tStartRefresh)
        learning1_block_loop.addData('health_fill_regen.stopped', health_fill_regen.tStopRefresh)
        learning1_block_loop.addData('learning_text_regen.started', learning_text_regen.tStartRefresh)
        learning1_block_loop.addData('learning_text_regen.stopped', learning_text_regen.tStopRefresh)
        
        # ------Prepare to start Routine "learning_backmask"-------
        continueRoutine = True
        routineTimer.add(0.500000)
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
        learning_backmaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_backmask"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_backmaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_backmaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
            
            # *learn_trialNum_5* updates
            if learn_trialNum_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_5.frameNStart = frameN  # exact frame index
                learn_trialNum_5.tStart = t  # local t and not account for scr refresh
                learn_trialNum_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_5, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_5.setAutoDraw(True)
            if learn_trialNum_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_5.tStop = t  # not accounting for scr refresh
                    learn_trialNum_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_5, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_5.setAutoDraw(False)
            
            # *noise_backmask* updates
            if noise_backmask.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                noise_backmask.frameNStart = frameN  # exact frame index
                noise_backmask.tStart = t  # local t and not account for scr refresh
                noise_backmask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_backmask, 'tStartRefresh')  # time at next scr refresh
                noise_backmask.setAutoDraw(True)
            if noise_backmask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_backmask.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_backmask.tStop = t  # not accounting for scr refresh
                    noise_backmask.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_backmask, 'tStopRefresh')  # time at next scr refresh
                    noise_backmask.setAutoDraw(False)
            if noise_backmask.status == STARTED:  # only update if drawing
                noise_backmask.setTex(noiseTexture, log=False)
            
            # *health_border_5* updates
            if health_border_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_5.frameNStart = frameN  # exact frame index
                health_border_5.tStart = t  # local t and not account for scr refresh
                health_border_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_5, 'tStartRefresh')  # time at next scr refresh
                health_border_5.setAutoDraw(True)
            if health_border_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_5.tStop = t  # not accounting for scr refresh
                    health_border_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_5, 'tStopRefresh')  # time at next scr refresh
                    health_border_5.setAutoDraw(False)
            
            # *health_fill_5* updates
            if health_fill_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_5.frameNStart = frameN  # exact frame index
                health_fill_5.tStart = t  # local t and not account for scr refresh
                health_fill_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_5, 'tStartRefresh')  # time at next scr refresh
                health_fill_5.setAutoDraw(True)
            if health_fill_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_5.tStop = t  # not accounting for scr refresh
                    health_fill_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_5, 'tStopRefresh')  # time at next scr refresh
                    health_fill_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_backmaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_backmask"-------
        for thisComponent in learning_backmaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning1_block_loop.addData('learn_trialNum_5.started', learn_trialNum_5.tStartRefresh)
        learning1_block_loop.addData('learn_trialNum_5.stopped', learn_trialNum_5.tStopRefresh)
        learning1_block_loop.addData('noise_backmask.started', noise_backmask.tStartRefresh)
        learning1_block_loop.addData('noise_backmask.stopped', noise_backmask.tStopRefresh)
        learning1_block_loop.addData('health_border_5.started', health_border_5.tStartRefresh)
        learning1_block_loop.addData('health_border_5.stopped', health_border_5.tStopRefresh)
        learning1_block_loop.addData('health_fill_5.started', health_fill_5.tStartRefresh)
        learning1_block_loop.addData('health_fill_5.stopped', health_fill_5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'learning1_block_loop'
    
    
    # ------Prepare to start Routine "learning1_break1"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    learning1_break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learning1_break1"-------
    while continueRoutine:
        # get current time
        t = learning1_break1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learning1_break1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn1_break1_text* updates
        if learn1_break1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn1_break1_text.frameNStart = frameN  # exact frame index
            learn1_break1_text.tStart = t  # local t and not account for scr refresh
            learn1_break1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn1_break1_text, 'tStartRefresh')  # time at next scr refresh
            learn1_break1_text.setAutoDraw(True)
        
        # *learn1_break1_keys* updates
        waitOnFlip = False
        if learn1_break1_keys.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            learn1_break1_keys.frameNStart = frameN  # exact frame index
            learn1_break1_keys.tStart = t  # local t and not account for scr refresh
            learn1_break1_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn1_break1_keys, 'tStartRefresh')  # time at next scr refresh
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
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning1_break1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learning1_break1"-------
    for thisComponent in learning1_break1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning1_oddcond_loop.addData('learn1_break1_text.started', learn1_break1_text.tStartRefresh)
    learning1_oddcond_loop.addData('learn1_break1_text.stopped', learn1_break1_text.tStopRefresh)
    # check responses
    if learn1_break1_keys.keys in ['', [], None]:  # No response was made
        learn1_break1_keys.keys = None
    learning1_oddcond_loop.addData('learn1_break1_keys.keys',learn1_break1_keys.keys)
    if learn1_break1_keys.keys != None:  # we had a response
        learning1_oddcond_loop.addData('learn1_break1_keys.rt', learn1_break1_keys.rt)
    learning1_oddcond_loop.addData('learn1_break1_keys.started', learn1_break1_keys.tStartRefresh)
    learning1_oddcond_loop.addData('learn1_break1_keys.stopped', learn1_break1_keys.tStopRefresh)
    # the Routine "learning1_break1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'learning1_oddcond_loop'


# ------Prepare to start Routine "learning2_instructions"-------
continueRoutine = True
# update component parameters for each repeat
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
learning2_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learning2_instructions"-------
while continueRoutine:
    # get current time
    t = learning2_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learning2_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *alienBodyDemo2* updates
    if alienBodyDemo2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienBodyDemo2.frameNStart = frameN  # exact frame index
        alienBodyDemo2.tStart = t  # local t and not account for scr refresh
        alienBodyDemo2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienBodyDemo2, 'tStartRefresh')  # time at next scr refresh
        alienBodyDemo2.setAutoDraw(True)
    
    # *alienEyeDemo2* updates
    if alienEyeDemo2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        alienEyeDemo2.frameNStart = frameN  # exact frame index
        alienEyeDemo2.tStart = t  # local t and not account for scr refresh
        alienEyeDemo2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(alienEyeDemo2, 'tStartRefresh')  # time at next scr refresh
        alienEyeDemo2.setAutoDraw(True)
    
    # *explorerDemo2_U* updates
    if explorerDemo2_U.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        explorerDemo2_U.frameNStart = frameN  # exact frame index
        explorerDemo2_U.tStart = t  # local t and not account for scr refresh
        explorerDemo2_U.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(explorerDemo2_U, 'tStartRefresh')  # time at next scr refresh
        explorerDemo2_U.setAutoDraw(True)
    
    # *instructionLearn2* updates
    if instructionLearn2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionLearn2.frameNStart = frameN  # exact frame index
        instructionLearn2.tStart = t  # local t and not account for scr refresh
        instructionLearn2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionLearn2, 'tStartRefresh')  # time at next scr refresh
        instructionLearn2.setAutoDraw(True)
    
    # *learning2_keyboard* updates
    waitOnFlip = False
    if learning2_keyboard.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        learning2_keyboard.frameNStart = frameN  # exact frame index
        learning2_keyboard.tStart = t  # local t and not account for scr refresh
        learning2_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(learning2_keyboard, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learning2_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learning2_instructions"-------
for thisComponent in learning2_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('alienBodyDemo2.started', alienBodyDemo2.tStartRefresh)
thisExp.addData('alienBodyDemo2.stopped', alienBodyDemo2.tStopRefresh)
thisExp.addData('alienEyeDemo2.started', alienEyeDemo2.tStartRefresh)
thisExp.addData('alienEyeDemo2.stopped', alienEyeDemo2.tStopRefresh)
thisExp.addData('explorerDemo2_U.started', explorerDemo2_U.tStartRefresh)
thisExp.addData('explorerDemo2_U.stopped', explorerDemo2_U.tStopRefresh)
thisExp.addData('instructionLearn2.started', instructionLearn2.tStartRefresh)
thisExp.addData('instructionLearn2.stopped', instructionLearn2.tStopRefresh)
# check responses
if learning2_keyboard.keys in ['', [], None]:  # No response was made
    learning2_keyboard.keys = None
thisExp.addData('learning2_keyboard.keys',learning2_keyboard.keys)
if learning2_keyboard.keys != None:  # we had a response
    thisExp.addData('learning2_keyboard.rt', learning2_keyboard.rt)
thisExp.addData('learning2_keyboard.started', learning2_keyboard.tStartRefresh)
thisExp.addData('learning2_keyboard.stopped', learning2_keyboard.tStopRefresh)
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
        
        # ------Prepare to start Routine "learning_fixation"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
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
        learning_fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_fixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_fixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *learn_trialNum_1* updates
            if learn_trialNum_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_1.frameNStart = frameN  # exact frame index
                learn_trialNum_1.tStart = t  # local t and not account for scr refresh
                learn_trialNum_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_1, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_1.setAutoDraw(True)
            if learn_trialNum_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_1.tStop = t  # not accounting for scr refresh
                    learn_trialNum_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_1, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_1.setAutoDraw(False)
            
            # *fixationLearn* updates
            if fixationLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fixationLearn.frameNStart = frameN  # exact frame index
                fixationLearn.tStart = t  # local t and not account for scr refresh
                fixationLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixationLearn, 'tStartRefresh')  # time at next scr refresh
                fixationLearn.setAutoDraw(True)
            if fixationLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixationLearn.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    fixationLearn.tStop = t  # not accounting for scr refresh
                    fixationLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixationLearn, 'tStopRefresh')  # time at next scr refresh
                    fixationLearn.setAutoDraw(False)
            
            # *health_border_1* updates
            if health_border_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_1.frameNStart = frameN  # exact frame index
                health_border_1.tStart = t  # local t and not account for scr refresh
                health_border_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_1, 'tStartRefresh')  # time at next scr refresh
                health_border_1.setAutoDraw(True)
            if health_border_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_1.tStop = t  # not accounting for scr refresh
                    health_border_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_1, 'tStopRefresh')  # time at next scr refresh
                    health_border_1.setAutoDraw(False)
            
            # *health_fill_1* updates
            if health_fill_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_1.frameNStart = frameN  # exact frame index
                health_fill_1.tStart = t  # local t and not account for scr refresh
                health_fill_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_1, 'tStartRefresh')  # time at next scr refresh
                health_fill_1.setAutoDraw(True)
            if health_fill_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_1.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_1.tStop = t  # not accounting for scr refresh
                    health_fill_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_1, 'tStopRefresh')  # time at next scr refresh
                    health_fill_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_fixation"-------
        for thisComponent in learning_fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning2_block_loop.addData('learn_trialNum_1.started', learn_trialNum_1.tStartRefresh)
        learning2_block_loop.addData('learn_trialNum_1.stopped', learn_trialNum_1.tStopRefresh)
        learning2_block_loop.addData('fixationLearn.started', fixationLearn.tStartRefresh)
        learning2_block_loop.addData('fixationLearn.stopped', fixationLearn.tStopRefresh)
        learning2_block_loop.addData('health_border_1.started', health_border_1.tStartRefresh)
        learning2_block_loop.addData('health_border_1.stopped', health_border_1.tStopRefresh)
        learning2_block_loop.addData('health_fill_1.started', health_fill_1.tStartRefresh)
        learning2_block_loop.addData('health_fill_1.stopped', health_fill_1.tStopRefresh)
        
        # ------Prepare to start Routine "learning_presentation"-------
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
        learning_presentationComponents = [learn_trialNum_2, alienBodyLearn, alienEyeLearn, explorerLearn, key_resp_learn, health_border_2, health_fill_2, learning_hint]
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
        learning_presentationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_presentation"-------
        while continueRoutine:
            # get current time
            t = learning_presentationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_presentationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *learn_trialNum_2* updates
            if learn_trialNum_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_2.frameNStart = frameN  # exact frame index
                learn_trialNum_2.tStart = t  # local t and not account for scr refresh
                learn_trialNum_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_2, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_2.setAutoDraw(True)
            
            # *alienBodyLearn* updates
            if alienBodyLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn.frameNStart = frameN  # exact frame index
                alienBodyLearn.tStart = t  # local t and not account for scr refresh
                alienBodyLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn.setAutoDraw(True)
            
            # *alienEyeLearn* updates
            if alienEyeLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn.frameNStart = frameN  # exact frame index
                alienEyeLearn.tStart = t  # local t and not account for scr refresh
                alienEyeLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn.setAutoDraw(True)
            
            # *explorerLearn* updates
            if explorerLearn.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn.frameNStart = frameN  # exact frame index
                explorerLearn.tStart = t  # local t and not account for scr refresh
                explorerLearn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn, 'tStartRefresh')  # time at next scr refresh
                explorerLearn.setAutoDraw(True)
            
            # *key_resp_learn* updates
            waitOnFlip = False
            if key_resp_learn.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_learn.frameNStart = frameN  # exact frame index
                key_resp_learn.tStart = t  # local t and not account for scr refresh
                key_resp_learn.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_learn, 'tStartRefresh')  # time at next scr refresh
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
            if health_border_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_2.frameNStart = frameN  # exact frame index
                health_border_2.tStart = t  # local t and not account for scr refresh
                health_border_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_2, 'tStartRefresh')  # time at next scr refresh
                health_border_2.setAutoDraw(True)
            
            # *health_fill_2* updates
            if health_fill_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_2.frameNStart = frameN  # exact frame index
                health_fill_2.tStart = t  # local t and not account for scr refresh
                health_fill_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_2, 'tStartRefresh')  # time at next scr refresh
                health_fill_2.setAutoDraw(True)
            
            # *learning_hint* updates
            if learning_hint.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                learning_hint.frameNStart = frameN  # exact frame index
                learning_hint.tStart = t  # local t and not account for scr refresh
                learning_hint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_hint, 'tStartRefresh')  # time at next scr refresh
                learning_hint.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_presentationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_presentation"-------
        for thisComponent in learning_presentationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning2_block_loop.addData('learn_trialNum_2.started', learn_trialNum_2.tStartRefresh)
        learning2_block_loop.addData('learn_trialNum_2.stopped', learn_trialNum_2.tStopRefresh)
        learning2_block_loop.addData('alienBodyLearn.started', alienBodyLearn.tStartRefresh)
        learning2_block_loop.addData('alienBodyLearn.stopped', alienBodyLearn.tStopRefresh)
        learning2_block_loop.addData('alienEyeLearn.started', alienEyeLearn.tStartRefresh)
        learning2_block_loop.addData('alienEyeLearn.stopped', alienEyeLearn.tStopRefresh)
        learning2_block_loop.addData('explorerLearn.started', explorerLearn.tStartRefresh)
        learning2_block_loop.addData('explorerLearn.stopped', explorerLearn.tStopRefresh)
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
        learning2_block_loop.addData('key_resp_learn.started', key_resp_learn.tStartRefresh)
        learning2_block_loop.addData('key_resp_learn.stopped', key_resp_learn.tStopRefresh)
        learning2_block_loop.addData('health_border_2.started', health_border_2.tStartRefresh)
        learning2_block_loop.addData('health_border_2.stopped', health_border_2.tStopRefresh)
        learning2_block_loop.addData('health_fill_2.started', health_fill_2.tStartRefresh)
        learning2_block_loop.addData('health_fill_2.stopped', health_fill_2.tStopRefresh)
        learning2_block_loop.addData('learning_hint.started', learning_hint.tStartRefresh)
        learning2_block_loop.addData('learning_hint.stopped', learning_hint.tStopRefresh)
        # the Routine "learning_presentation" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "learning_feedback"-------
        continueRoutine = True
        routineTimer.add(0.250000)
        # update component parameters for each repeat
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
        learning_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_feedback"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_feedbackClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_feedbackClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop feedbackSoundLearn
            if feedbackSoundLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedbackSoundLearn.frameNStart = frameN  # exact frame index
                feedbackSoundLearn.tStart = t  # local t and not account for scr refresh
                feedbackSoundLearn.tStartRefresh = tThisFlipGlobal  # on global time
                feedbackSoundLearn.play(when=win)  # sync with win flip
            if feedbackSoundLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedbackSoundLearn.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    feedbackSoundLearn.tStop = t  # not accounting for scr refresh
                    feedbackSoundLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(feedbackSoundLearn, 'tStopRefresh')  # time at next scr refresh
                    feedbackSoundLearn.stop()
            
            # *learn_trialNum_3* updates
            if learn_trialNum_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_3.frameNStart = frameN  # exact frame index
                learn_trialNum_3.tStart = t  # local t and not account for scr refresh
                learn_trialNum_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_3, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_3.setAutoDraw(True)
            if learn_trialNum_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_3.tStop = t  # not accounting for scr refresh
                    learn_trialNum_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_3, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_3.setAutoDraw(False)
            
            # *alienBodyLearn2* updates
            if alienBodyLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn2.frameNStart = frameN  # exact frame index
                alienBodyLearn2.tStart = t  # local t and not account for scr refresh
                alienBodyLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn2, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn2.setAutoDraw(True)
            if alienBodyLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienBodyLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    alienBodyLearn2.tStop = t  # not accounting for scr refresh
                    alienBodyLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienBodyLearn2, 'tStopRefresh')  # time at next scr refresh
                    alienBodyLearn2.setAutoDraw(False)
            
            # *alienEyeLearn2* updates
            if alienEyeLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn2.frameNStart = frameN  # exact frame index
                alienEyeLearn2.tStart = t  # local t and not account for scr refresh
                alienEyeLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn2, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn2.setAutoDraw(True)
            if alienEyeLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienEyeLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    alienEyeLearn2.tStop = t  # not accounting for scr refresh
                    alienEyeLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienEyeLearn2, 'tStopRefresh')  # time at next scr refresh
                    alienEyeLearn2.setAutoDraw(False)
            
            # *explorerLearn2* updates
            if explorerLearn2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn2.frameNStart = frameN  # exact frame index
                explorerLearn2.tStart = t  # local t and not account for scr refresh
                explorerLearn2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn2, 'tStartRefresh')  # time at next scr refresh
                explorerLearn2.setAutoDraw(True)
            if explorerLearn2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn2.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn2.tStop = t  # not accounting for scr refresh
                    explorerLearn2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn2, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn2.setAutoDraw(False)
            
            # *health_border_3* updates
            if health_border_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_3.frameNStart = frameN  # exact frame index
                health_border_3.tStart = t  # local t and not account for scr refresh
                health_border_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_3, 'tStartRefresh')  # time at next scr refresh
                health_border_3.setAutoDraw(True)
            if health_border_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_3.tStop = t  # not accounting for scr refresh
                    health_border_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_3, 'tStopRefresh')  # time at next scr refresh
                    health_border_3.setAutoDraw(False)
            
            # *health_fill_3* updates
            if health_fill_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_3.frameNStart = frameN  # exact frame index
                health_fill_3.tStart = t  # local t and not account for scr refresh
                health_fill_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_3, 'tStartRefresh')  # time at next scr refresh
                health_fill_3.setAutoDraw(True)
            if health_fill_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_3.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_3.tStop = t  # not accounting for scr refresh
                    health_fill_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_3, 'tStopRefresh')  # time at next scr refresh
                    health_fill_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_feedback"-------
        for thisComponent in learning_feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        feedbackSoundLearn.stop()  # ensure sound has stopped at end of routine
        learning2_block_loop.addData('feedbackSoundLearn.started', feedbackSoundLearn.tStartRefresh)
        learning2_block_loop.addData('feedbackSoundLearn.stopped', feedbackSoundLearn.tStopRefresh)
        learning2_block_loop.addData('learn_trialNum_3.started', learn_trialNum_3.tStartRefresh)
        learning2_block_loop.addData('learn_trialNum_3.stopped', learn_trialNum_3.tStopRefresh)
        learning2_block_loop.addData('alienBodyLearn2.started', alienBodyLearn2.tStartRefresh)
        learning2_block_loop.addData('alienBodyLearn2.stopped', alienBodyLearn2.tStopRefresh)
        learning2_block_loop.addData('alienEyeLearn2.started', alienEyeLearn2.tStartRefresh)
        learning2_block_loop.addData('alienEyeLearn2.stopped', alienEyeLearn2.tStopRefresh)
        learning2_block_loop.addData('explorerLearn2.started', explorerLearn2.tStartRefresh)
        learning2_block_loop.addData('explorerLearn2.stopped', explorerLearn2.tStopRefresh)
        learning2_block_loop.addData('health_border_3.started', health_border_3.tStartRefresh)
        learning2_block_loop.addData('health_border_3.stopped', health_border_3.tStopRefresh)
        learning2_block_loop.addData('health_fill_3.started', health_fill_3.tStartRefresh)
        learning2_block_loop.addData('health_fill_3.stopped', health_fill_3.tStopRefresh)
        
        # ------Prepare to start Routine "learning_feedback_label"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
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
        learning_feedback_labelClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_feedback_label"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_feedback_labelClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_feedback_labelClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # start/stop trainingLabelLearn
            if trainingLabelLearn.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                trainingLabelLearn.frameNStart = frameN  # exact frame index
                trainingLabelLearn.tStart = t  # local t and not account for scr refresh
                trainingLabelLearn.tStartRefresh = tThisFlipGlobal  # on global time
                trainingLabelLearn.play(when=win)  # sync with win flip
            if trainingLabelLearn.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > trainingLabelLearn.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    trainingLabelLearn.tStop = t  # not accounting for scr refresh
                    trainingLabelLearn.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(trainingLabelLearn, 'tStopRefresh')  # time at next scr refresh
                    trainingLabelLearn.stop()
            
            # *learn_trialNum_4* updates
            if learn_trialNum_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_4.frameNStart = frameN  # exact frame index
                learn_trialNum_4.tStart = t  # local t and not account for scr refresh
                learn_trialNum_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_4, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_4.setAutoDraw(True)
            if learn_trialNum_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_4.tStop = t  # not accounting for scr refresh
                    learn_trialNum_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_4, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_4.setAutoDraw(False)
            
            # *alienBodyLearn3* updates
            if alienBodyLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienBodyLearn3.frameNStart = frameN  # exact frame index
                alienBodyLearn3.tStart = t  # local t and not account for scr refresh
                alienBodyLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienBodyLearn3, 'tStartRefresh')  # time at next scr refresh
                alienBodyLearn3.setAutoDraw(True)
            if alienBodyLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienBodyLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    alienBodyLearn3.tStop = t  # not accounting for scr refresh
                    alienBodyLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienBodyLearn3, 'tStopRefresh')  # time at next scr refresh
                    alienBodyLearn3.setAutoDraw(False)
            
            # *alienEyeLearn3* updates
            if alienEyeLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                alienEyeLearn3.frameNStart = frameN  # exact frame index
                alienEyeLearn3.tStart = t  # local t and not account for scr refresh
                alienEyeLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(alienEyeLearn3, 'tStartRefresh')  # time at next scr refresh
                alienEyeLearn3.setAutoDraw(True)
            if alienEyeLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > alienEyeLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    alienEyeLearn3.tStop = t  # not accounting for scr refresh
                    alienEyeLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(alienEyeLearn3, 'tStopRefresh')  # time at next scr refresh
                    alienEyeLearn3.setAutoDraw(False)
            
            # *explorerLearn3* updates
            if explorerLearn3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn3.frameNStart = frameN  # exact frame index
                explorerLearn3.tStart = t  # local t and not account for scr refresh
                explorerLearn3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn3, 'tStartRefresh')  # time at next scr refresh
                explorerLearn3.setAutoDraw(True)
            if explorerLearn3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn3.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn3.tStop = t  # not accounting for scr refresh
                    explorerLearn3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn3, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn3.setAutoDraw(False)
            
            # *health_border_4* updates
            if health_border_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_4.frameNStart = frameN  # exact frame index
                health_border_4.tStart = t  # local t and not account for scr refresh
                health_border_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_4, 'tStartRefresh')  # time at next scr refresh
                health_border_4.setAutoDraw(True)
            if health_border_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_4.tStop = t  # not accounting for scr refresh
                    health_border_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_4, 'tStopRefresh')  # time at next scr refresh
                    health_border_4.setAutoDraw(False)
            
            # *health_fill_4* updates
            if health_fill_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_4.frameNStart = frameN  # exact frame index
                health_fill_4.tStart = t  # local t and not account for scr refresh
                health_fill_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_4, 'tStartRefresh')  # time at next scr refresh
                health_fill_4.setAutoDraw(True)
            if health_fill_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_4.tStartRefresh + .8-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_4.tStop = t  # not accounting for scr refresh
                    health_fill_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_4, 'tStopRefresh')  # time at next scr refresh
                    health_fill_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_feedback_labelComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_feedback_label"-------
        for thisComponent in learning_feedback_labelComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trainingLabelLearn.stop()  # ensure sound has stopped at end of routine
        learning2_block_loop.addData('learn_trialNum_4.started', learn_trialNum_4.tStartRefresh)
        learning2_block_loop.addData('learn_trialNum_4.stopped', learn_trialNum_4.tStopRefresh)
        learning2_block_loop.addData('alienBodyLearn3.started', alienBodyLearn3.tStartRefresh)
        learning2_block_loop.addData('alienBodyLearn3.stopped', alienBodyLearn3.tStopRefresh)
        learning2_block_loop.addData('alienEyeLearn3.started', alienEyeLearn3.tStartRefresh)
        learning2_block_loop.addData('alienEyeLearn3.stopped', alienEyeLearn3.tStopRefresh)
        learning2_block_loop.addData('explorerLearn3.started', explorerLearn3.tStartRefresh)
        learning2_block_loop.addData('explorerLearn3.stopped', explorerLearn3.tStopRefresh)
        learning2_block_loop.addData('health_border_4.started', health_border_4.tStartRefresh)
        learning2_block_loop.addData('health_border_4.stopped', health_border_4.tStopRefresh)
        learning2_block_loop.addData('health_fill_4.started', health_fill_4.tStartRefresh)
        learning2_block_loop.addData('health_fill_4.stopped', health_fill_4.tStopRefresh)
        
        # ------Prepare to start Routine "learning_regen"-------
        continueRoutine = True
        routineTimer.add(10.000000)
        # update component parameters for each repeat
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
        learning_regenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_regen"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_regenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_regenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if has_health == False:
                regen_health = regen_timer.getTime()
                health_score = round(regen_timer.getTime())
                health_modifier = health_score/full_health_score
            
            # *explorerLearn4* updates
            if explorerLearn4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                explorerLearn4.frameNStart = frameN  # exact frame index
                explorerLearn4.tStart = t  # local t and not account for scr refresh
                explorerLearn4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(explorerLearn4, 'tStartRefresh')  # time at next scr refresh
                explorerLearn4.setAutoDraw(True)
            if explorerLearn4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > explorerLearn4.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    explorerLearn4.tStop = t  # not accounting for scr refresh
                    explorerLearn4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(explorerLearn4, 'tStopRefresh')  # time at next scr refresh
                    explorerLearn4.setAutoDraw(False)
            
            # *health_border_regen* updates
            if health_border_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_regen.frameNStart = frameN  # exact frame index
                health_border_regen.tStart = t  # local t and not account for scr refresh
                health_border_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_regen, 'tStartRefresh')  # time at next scr refresh
                health_border_regen.setAutoDraw(True)
            if health_border_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_regen.tStop = t  # not accounting for scr refresh
                    health_border_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_regen, 'tStopRefresh')  # time at next scr refresh
                    health_border_regen.setAutoDraw(False)
            
            # *health_fill_regen* updates
            if health_fill_regen.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_regen.frameNStart = frameN  # exact frame index
                health_fill_regen.tStart = t  # local t and not account for scr refresh
                health_fill_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_regen, 'tStartRefresh')  # time at next scr refresh
                health_fill_regen.setAutoDraw(True)
            if health_fill_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_regen.tStop = t  # not accounting for scr refresh
                    health_fill_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_regen, 'tStopRefresh')  # time at next scr refresh
                    health_fill_regen.setAutoDraw(False)
            if health_fill_regen.status == STARTED:  # only update if drawing
                health_fill_regen.setSize((healthbarW, (healthbarH*health_modifier)), log=False)
            
            # *learning_text_regen* updates
            if learning_text_regen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learning_text_regen.frameNStart = frameN  # exact frame index
                learning_text_regen.tStart = t  # local t and not account for scr refresh
                learning_text_regen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learning_text_regen, 'tStartRefresh')  # time at next scr refresh
                learning_text_regen.setAutoDraw(True)
            if learning_text_regen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learning_text_regen.tStartRefresh + 10-frameTolerance:
                    # keep track of stop time/frame for later
                    learning_text_regen.tStop = t  # not accounting for scr refresh
                    learning_text_regen.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learning_text_regen, 'tStopRefresh')  # time at next scr refresh
                    learning_text_regen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_regenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_regen"-------
        for thisComponent in learning_regenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if has_health == False:
            health_score = 10
            health_modifier = health_score/full_health_score
            has_health = True
        learning2_block_loop.addData('explorerLearn4.started', explorerLearn4.tStartRefresh)
        learning2_block_loop.addData('explorerLearn4.stopped', explorerLearn4.tStopRefresh)
        learning2_block_loop.addData('health_border_regen.started', health_border_regen.tStartRefresh)
        learning2_block_loop.addData('health_border_regen.stopped', health_border_regen.tStopRefresh)
        learning2_block_loop.addData('health_fill_regen.started', health_fill_regen.tStartRefresh)
        learning2_block_loop.addData('health_fill_regen.stopped', health_fill_regen.tStopRefresh)
        learning2_block_loop.addData('learning_text_regen.started', learning_text_regen.tStartRefresh)
        learning2_block_loop.addData('learning_text_regen.stopped', learning_text_regen.tStopRefresh)
        
        # ------Prepare to start Routine "learning_backmask"-------
        continueRoutine = True
        routineTimer.add(0.500000)
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
        learning_backmaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "learning_backmask"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = learning_backmaskClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=learning_backmaskClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            noiseTexture = np.random.rand(128, 128) * 2.0 - 1.0
            
            # *learn_trialNum_5* updates
            if learn_trialNum_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                learn_trialNum_5.frameNStart = frameN  # exact frame index
                learn_trialNum_5.tStart = t  # local t and not account for scr refresh
                learn_trialNum_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(learn_trialNum_5, 'tStartRefresh')  # time at next scr refresh
                learn_trialNum_5.setAutoDraw(True)
            if learn_trialNum_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > learn_trialNum_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    learn_trialNum_5.tStop = t  # not accounting for scr refresh
                    learn_trialNum_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(learn_trialNum_5, 'tStopRefresh')  # time at next scr refresh
                    learn_trialNum_5.setAutoDraw(False)
            
            # *noise_backmask* updates
            if noise_backmask.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                noise_backmask.frameNStart = frameN  # exact frame index
                noise_backmask.tStart = t  # local t and not account for scr refresh
                noise_backmask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise_backmask, 'tStartRefresh')  # time at next scr refresh
                noise_backmask.setAutoDraw(True)
            if noise_backmask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > noise_backmask.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    noise_backmask.tStop = t  # not accounting for scr refresh
                    noise_backmask.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise_backmask, 'tStopRefresh')  # time at next scr refresh
                    noise_backmask.setAutoDraw(False)
            if noise_backmask.status == STARTED:  # only update if drawing
                noise_backmask.setTex(noiseTexture, log=False)
            
            # *health_border_5* updates
            if health_border_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_border_5.frameNStart = frameN  # exact frame index
                health_border_5.tStart = t  # local t and not account for scr refresh
                health_border_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_border_5, 'tStartRefresh')  # time at next scr refresh
                health_border_5.setAutoDraw(True)
            if health_border_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_border_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_border_5.tStop = t  # not accounting for scr refresh
                    health_border_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_border_5, 'tStopRefresh')  # time at next scr refresh
                    health_border_5.setAutoDraw(False)
            
            # *health_fill_5* updates
            if health_fill_5.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                health_fill_5.frameNStart = frameN  # exact frame index
                health_fill_5.tStart = t  # local t and not account for scr refresh
                health_fill_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(health_fill_5, 'tStartRefresh')  # time at next scr refresh
                health_fill_5.setAutoDraw(True)
            if health_fill_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > health_fill_5.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    health_fill_5.tStop = t  # not accounting for scr refresh
                    health_fill_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(health_fill_5, 'tStopRefresh')  # time at next scr refresh
                    health_fill_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in learning_backmaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "learning_backmask"-------
        for thisComponent in learning_backmaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        learning2_block_loop.addData('learn_trialNum_5.started', learn_trialNum_5.tStartRefresh)
        learning2_block_loop.addData('learn_trialNum_5.stopped', learn_trialNum_5.tStopRefresh)
        learning2_block_loop.addData('noise_backmask.started', noise_backmask.tStartRefresh)
        learning2_block_loop.addData('noise_backmask.stopped', noise_backmask.tStopRefresh)
        learning2_block_loop.addData('health_border_5.started', health_border_5.tStartRefresh)
        learning2_block_loop.addData('health_border_5.stopped', health_border_5.tStopRefresh)
        learning2_block_loop.addData('health_fill_5.started', health_fill_5.tStartRefresh)
        learning2_block_loop.addData('health_fill_5.stopped', health_fill_5.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'learning2_block_loop'
    
    
    # ------Prepare to start Routine "learning2_break1"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    learning2_break1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learning2_break1"-------
    while continueRoutine:
        # get current time
        t = learning2_break1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learning2_break1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *learn2_break1_text* updates
        if learn2_break1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learn2_break1_text.frameNStart = frameN  # exact frame index
            learn2_break1_text.tStart = t  # local t and not account for scr refresh
            learn2_break1_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn2_break1_text, 'tStartRefresh')  # time at next scr refresh
            learn2_break1_text.setAutoDraw(True)
        
        # *learn2_break1_keys* updates
        waitOnFlip = False
        if learn2_break1_keys.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            learn2_break1_keys.frameNStart = frameN  # exact frame index
            learn2_break1_keys.tStart = t  # local t and not account for scr refresh
            learn2_break1_keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learn2_break1_keys, 'tStartRefresh')  # time at next scr refresh
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
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning2_break1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learning2_break1"-------
    for thisComponent in learning2_break1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learning2_oddcond_loop.addData('learn2_break1_text.started', learn2_break1_text.tStartRefresh)
    learning2_oddcond_loop.addData('learn2_break1_text.stopped', learn2_break1_text.tStopRefresh)
    # check responses
    if learn2_break1_keys.keys in ['', [], None]:  # No response was made
        learn2_break1_keys.keys = None
    learning2_oddcond_loop.addData('learn2_break1_keys.keys',learn2_break1_keys.keys)
    if learn2_break1_keys.keys != None:  # we had a response
        learning2_oddcond_loop.addData('learn2_break1_keys.rt', learn2_break1_keys.rt)
    learning2_oddcond_loop.addData('learn2_break1_keys.started', learn2_break1_keys.tStartRefresh)
    learning2_oddcond_loop.addData('learn2_break1_keys.stopped', learn2_break1_keys.tStopRefresh)
    # the Routine "learning2_break1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'learning2_oddcond_loop'


# ------Prepare to start Routine "exit_instructions"-------
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
exit_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "exit_instructions"-------
while continueRoutine:
    # get current time
    t = exit_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=exit_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructionExit* updates
    if instructionExit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructionExit.frameNStart = frameN  # exact frame index
        instructionExit.tStart = t  # local t and not account for scr refresh
        instructionExit.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructionExit, 'tStartRefresh')  # time at next scr refresh
        instructionExit.setAutoDraw(True)
    
    # *key_resp_exit_1* updates
    waitOnFlip = False
    if key_resp_exit_1.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_exit_1.frameNStart = frameN  # exact frame index
        key_resp_exit_1.tStart = t  # local t and not account for scr refresh
        key_resp_exit_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_exit_1, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in exit_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "exit_instructions"-------
for thisComponent in exit_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructionExit.started', instructionExit.tStartRefresh)
thisExp.addData('instructionExit.stopped', instructionExit.tStopRefresh)
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
    
    # ------Prepare to start Routine "exit_questionnaire"-------
    continueRoutine = True
    # update component parameters for each repeat
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
    exit_questionnaireClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "exit_questionnaire"-------
    while continueRoutine:
        # get current time
        t = exit_questionnaireClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=exit_questionnaireClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *exitQ_number* updates
        if exitQ_number.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitQ_number.frameNStart = frameN  # exact frame index
            exitQ_number.tStart = t  # local t and not account for scr refresh
            exitQ_number.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitQ_number, 'tStartRefresh')  # time at next scr refresh
            exitQ_number.setAutoDraw(True)
        
        # *exitQuestion* updates
        if exitQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitQuestion.frameNStart = frameN  # exact frame index
            exitQuestion.tStart = t  # local t and not account for scr refresh
            exitQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitQuestion, 'tStartRefresh')  # time at next scr refresh
            exitQuestion.setAutoDraw(True)
        
        # *exitResponse* updates
        if exitResponse.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            exitResponse.frameNStart = frameN  # exact frame index
            exitResponse.tStart = t  # local t and not account for scr refresh
            exitResponse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitResponse, 'tStartRefresh')  # time at next scr refresh
            exitResponse.setAutoDraw(True)
        
        # *exitContinueText* updates
        if exitContinueText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exitContinueText.frameNStart = frameN  # exact frame index
            exitContinueText.tStart = t  # local t and not account for scr refresh
            exitContinueText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exitContinueText, 'tStartRefresh')  # time at next scr refresh
            exitContinueText.setAutoDraw(True)
        
        # *key_resp_exit_2* updates
        waitOnFlip = False
        if key_resp_exit_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_exit_2.frameNStart = frameN  # exact frame index
            key_resp_exit_2.tStart = t  # local t and not account for scr refresh
            key_resp_exit_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_exit_2, 'tStartRefresh')  # time at next scr refresh
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
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exit_questionnaireComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exit_questionnaire"-------
    for thisComponent in exit_questionnaireComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    exitQ_loop.addData('exitQ_number.started', exitQ_number.tStartRefresh)
    exitQ_loop.addData('exitQ_number.stopped', exitQ_number.tStopRefresh)
    exitQ_loop.addData('exitQuestion.started', exitQuestion.tStartRefresh)
    exitQ_loop.addData('exitQuestion.stopped', exitQuestion.tStopRefresh)
    exitQ_loop.addData('exitResponse.text',exitResponse.text)
    exitQ_loop.addData('exitResponse.started', exitResponse.tStartRefresh)
    exitQ_loop.addData('exitResponse.stopped', exitResponse.tStopRefresh)
    exitQ_loop.addData('exitContinueText.started', exitContinueText.tStartRefresh)
    exitQ_loop.addData('exitContinueText.stopped', exitContinueText.tStopRefresh)
    # the Routine "exit_questionnaire" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'exitQ_loop'


# ------Prepare to start Routine "experiment_end"-------
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
experiment_endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "experiment_end"-------
while continueRoutine:
    # get current time
    t = experiment_endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=experiment_endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    
    # *experiment_end_key_resp* updates
    waitOnFlip = False
    if experiment_end_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        experiment_end_key_resp.frameNStart = frameN  # exact frame index
        experiment_end_key_resp.tStart = t  # local t and not account for scr refresh
        experiment_end_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(experiment_end_key_resp, 'tStartRefresh')  # time at next scr refresh
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
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in experiment_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "experiment_end"-------
for thisComponent in experiment_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thank_you.started', thank_you.tStartRefresh)
thisExp.addData('thank_you.stopped', thank_you.tStopRefresh)
# check responses
if experiment_end_key_resp.keys in ['', [], None]:  # No response was made
    experiment_end_key_resp.keys = None
thisExp.addData('experiment_end_key_resp.keys',experiment_end_key_resp.keys)
if experiment_end_key_resp.keys != None:  # we had a response
    thisExp.addData('experiment_end_key_resp.rt', experiment_end_key_resp.rt)
thisExp.addData('experiment_end_key_resp.started', experiment_end_key_resp.tStartRefresh)
thisExp.addData('experiment_end_key_resp.stopped', experiment_end_key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "experiment_end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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

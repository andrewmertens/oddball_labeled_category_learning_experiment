# Oddball Labeled Category Learning Experiment

This is a visual oddball experiment implemented in Psychopy (Builder). The task consists of 800 trials, in each of which the participant views and classifies individual Gabor patch stimuli that vary on dimensions of orientation and spatial frequency, with eight values on each dimension, resulting in 64 unique stimuli. Participants are tasked with learning, with feedback, to classify each stimulus into one of two categories based on the orientation of Gabor patch stimuli. The primary experimental manipulation in this design is the inclusion of a labeling condition, in which participants receive redundant, verbal category labels as part of their training feedback.

The oddball paradigm employs a 3:1 standard-to-deviant ratio, the configuration of which switches halfway through the task (i.e., previously deviant orientations of stimuli become standard and vice versa). Trials are balanced such that each standard stimuli is encountered three times and each deviant is experienced once per sequence of 16 trials. Trial balancing also ensures that encounters of each unique combination of orientation and spatial frequency are roughly evenly distributed. The R script used to create trial sequences can be found in the "supplemental_materials" folder.

The experiment includes EEG triggers configured to be transmitted through serial port COM4. The coding scheme for these triggers can be found in the "supplemental_materials" folder. The experiment also includes presentation of white space to be picked up by photometer for the option of latency correction.

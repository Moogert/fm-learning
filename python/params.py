# get parameters!!!
# this is a test script which we'll use to
# render some presets
import random
import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import os
from scipy.spatial.distance import euclidean
from os import listdir
from os.path import isfile, join, basename, splitext
import os

## todo - put these settings in an ini file
#CONST_DX_PARAM_COUNT = 147
CONST_DX_PARAM_COUNT = 15
CONST_DIR = "../"
CONST_DX_VST = CONST_DIR + "Dexed.vst" # we're using dexed
#CONST_DX_VST = CONST_DIR + "mda DX10.vst"
CONST_MIDI_FILE = CONST_DIR + "midi_export.mid"
CONST_MRS_WATSON = "\"" +  CONST_DIR + "MrsWatson-0.9.8/Mac OS X/mrswatson" + "\""
#CONST_OUT_FILE = CONST_DIR + "output.wav"
CONST_OUT_FILE = "./output.wav"


def get_mrs_watson_preset_command(mrswatson, vsti, midifile, preset_index, outfile):
	cmd = mrswatson + " --channels 1 --quiet --plugin \""  + vsti + ","+str(preset_index)+"\""
	cmd = cmd + " --midi-file "+midifile
	cmd = cmd + " --output \"" + outfile + "\""
	return cmd

	# get a command that will render the sent synth's output
def get_mrs_watson_command(mrswatson, vsti, midifile, params, outfile):
	cmd = mrswatson + " --channels 1 --quiet --plugin \""  + vsti + "\""
	cmd = cmd + " --midi-file "+midifile
	cmd = cmd + params
	cmd = cmd + " --output \"" + outfile + "\""
	return cmd


def render_preset(synth, index, filename):
	cmd = get_mrs_watson_preset_command(CONST_MRS_WATSON, synth, CONST_MIDI_FILE, index, filename)
#	print cmd
	os.system(cmd) # ok so this should print

def render_random_dx_sound(outfile):
	params = get_random_params(CONST_DX_PARAM_COUNT) # ok so small # of params
	param_string = get_mrs_watson_param_string(params) #
	cmd = get_mrs_watson_command(CONST_MRS_WATSON, CONST_DX_VST, CONST_MIDI_FILE, param_string, outfile)
	os.system(cmd)
	return params

# get a parameter argument string for mrswatson for the sent params
# e.g. --parameter 1,0.3 --parameter 0,0.75
def get_mrs_watson_param_string(params):
	inds = [i for i in range(0, len(params))]
	p_and_is = []
	for i in range(0, len(params)):
		p_and_is.append([inds[i], params[i]])
	ps = "".join([" --parameter "+str(p[0])+","+str(p[1]) for p in p_and_is])
	return ps

def get_random_params(length): # returns a random # of parameters??
	params = np.random.rand(length)
	return params

def render_population(pop, synth, output_folder):
	files = []
	for i in range(0, len(pop)):
		#print "Rendering "+str(i)
		filename = output_folder + "output_"+str(i)+".wav"
		param_string = get_mrs_watson_param_string(pop[i])
		cmd = get_mrs_watson_command(CONST_MRS_WATSON, synth, CONST_MIDI_FILE, param_string, filename)
		os.system(cmd)
		files.append(filename)
	return files

def get_population(size, param_count):
	pop = []
	for i in range(0, size):
		pop.append(get_random_params(param_count))
	return pop

## ok so this is where the party starts
pop = get_population(3, CONST_DX_PARAM_COUNT) # OK great so far
files = render_population(pop, synth, CONST_DIR)



"""
TODO:
* diff between synth and vst?

"""

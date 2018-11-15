# FM learning - use machine learning to make DX7 parameters 

This will render the presets from a synth and then try to find settings that make sounds like those presets:
```
cd python
python ga_find_test_set.py
```

You might need a couple of python packages:

```
pip install scipy
pip install scikits.talkbox
```

## External projects we're lowkey ripping off: 

* DX7 emulator: https://github.com/asb2m10/dexed
* Command line VST runner: https://github.com/teragonaudio/MrsWatson
* Other free VST plugins for testing: http://mda.smartelectronix.com
* yeeking's dx7 programmer

## things you will need to do upon downloading: 
Go into the project/dx7-programmer/python/ga direcctory, open 'workOrElse.py' and change your path
(under the CONST_MRS_WATSON variable). Then you should be able to run 'workOrElse.py' (python2 please) 
to get some random sounds. 

## TODO: 
* find out the relationship between the parameters (list of floats) [passed from get_random_params()]
to mrswatson. The docs at https://github.com/asb2m10/dexed/blob/master/Documentation/sysex-format.txt 
may be the trick, not sure yet. (Big if yes.) 
* get machine learning stuff running
* load in a .wav file for machine learning
* automate sound generation based on relevant parameters. random noises ain't the thing 


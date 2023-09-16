import numpy
import pandas
import cohere

#input_comm = input('Hi! Start your conversation here')


comm_bool = False
rizz_bool = True

##Communication 
pre_prommpt_c = "give me honest feedback on my communication skills"

##Rizz
input_rizz = 'hi' #input('Type your pickup line here: ')
pre_prompt_r = 'give honest and kinda mean feedback on this pickup line' + input_rizz

if rizz_bool == True:
    co = cohere.Client('Lx3HxSuVigT0CNAqmdlZfUwKTeC4WUj1YfYaDWga') # This is your trial API key
    response = co.generate(
    model='command',
    prompt=pre_prompt_r,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))
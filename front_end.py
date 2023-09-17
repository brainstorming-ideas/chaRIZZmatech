import time
import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        print("Speak now:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


import taipy
from taipy import Gui
import cohere

text = "Speak!"
roast = ""
content = r'C:\Users\varsh\Documents\GitHub\taipy-website\charizzmatech.png'

page = """
<|layout|columns=1 1|

# ChaRIZZmatech

<|{content}|image|>


|>

*Your Opener:* <|{text}|>

*What I Think:* <|{roast}|>


<|Record|button|on_action=on_button_action|>

"""
def on_button_action(state):
    state.text = 'Listening...'
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    guess = recognize_speech_from_mic(recognizer, microphone)
    input_rizz = " {}".format(guess["transcription"])
    state.text = input_rizz

    pre_prompt_r = 'tell me if my pick up line peoople is good or bad and be very mean about it. if its good say "w rizz" and if its bad be very mean and make fun of me in a funny way:' + input_rizz
    co = cohere.Client('Lx3HxSuVigT0CNAqmdlZfUwKTeC4WUj1YfYaDWga') # This is your trial API key
    response = co.generate(
        model='command',
        prompt=pre_prompt_r,
        max_tokens=200,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    roast = ' {}'.format(response.generations[0].text)
    state.roast = roast


def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return



# stylekit = {
#   "color_primary": "#6a329f",
#   "color_secondary": "#d5a6bd",
# }

pages = {
    "/"
}

Gui(page).run(host = "0.0.0.0", port = 5000)
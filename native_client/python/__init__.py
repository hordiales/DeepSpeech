import deepspeech

# rename for backwards compatibility
from deepspeech._impl import AudioToInputVector as audioToInputVector
from deepspeech._impl import PrintVersions as printVersions


class Model(object):
    def __init__(self, *args, **kwargs):
        # make sure the attribute is there if CreateModel fails
        self._impl = None

        status, impl = deepspeech._impl.CreateModel(*args, **kwargs)
        if status != 0:
            raise RuntimeError("CreateModel failed with error code {}".format(status))
        self._impl = impl

    def __del__(self):
        if self._impl:
            deepspeech._impl.DestroyModel(self._impl)
            self._impl = None

    def enableDecoderWithLM(self, *args, **kwargs):
        deepspeech._impl.EnableDecoderWithLM(self._impl, *args, **kwargs)

    def stt(self, *args, **kwargs):
        return deepspeech._impl.SpeechToText(self._impl, *args, **kwargs)

    def setupStream(self, *args, **kwargs):
        status, ctx = deepspeech._impl.SetupStream(self._impl, *args, **kwargs)
        if status != 0:
            raise RuntimeError("SetupStream failed with error code {}".format(status))
        return ctx

    def feedAudioContent(self, *args, **kwargs):
        deepspeech._impl.FeedAudioContent(*args, **kwargs)

    def finishStream(self, *args, **kwargs):
        return deepspeech._impl.FinishStream(*args, **kwargs)

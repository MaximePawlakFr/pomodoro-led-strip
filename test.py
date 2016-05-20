

class Strip(object):
    class __OnlyOne:
        def __init__(self):
            self.val = 'PPPP'
        def __str__(self):
            return `self` + self.val
        def coucu(self):
            print 'coutou'
        def init(self):
            print 'init'
        def test():
            print 'test'
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Strip.instance:
            Strip.instance = Strip.__OnlyOne()
            # Create NeoPixel object with appropriate configuration.
            Strip.instance.neopixel = "NEOPIXEL"
        	# Intialize the library (must be called once before other functions).
            # Strip.neopixel.begin()
        return Strip.instance
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)

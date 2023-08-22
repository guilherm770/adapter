class Octopus:

	"""Class for Octopus"""

	def __init__(self):
		self.name = "Octopus"

	def EightLimbed(self):
		return "Eight-Limbed Mollusc"


class Squid:

	"""Class for Squid"""

	def __init__(self):
		self.name = "Squid"

	def TenLimbed(self):
		return "Ten-Limbed Mollusc"

class Adapter:
	"""
	Adapts an object by replacing methods.
	Usage:
	squid = Squid()
	squid = Adapter(Squid, Limbs = Squid.TenLimbed)
	"""

	def __init__(self, obj, **adapted_methods):
		"""We set the adapted methods in the object's dict"""
		self.obj = obj
		self.__dict__.update(adapted_methods)

	def __getattr__(self, attr):
		"""All non-adapted calls are passed to the object"""
		return getattr(self.obj, attr)

	def original_dict(self):
		"""Print original object dict"""
		return self.obj.__dict__

if __name__ == "__main__":

    """list to store objects"""
    objects = []

    octupus = Octopus()
    objects.append(Adapter(octupus, limbs = octupus.EightLimbed))

    squid = Squid()
    objects.append(Adapter(squid, limbs = squid.TenLimbed))
    
    for obj in objects:
        print("A {0} is a {1}".format(obj.name, obj.limbs()))
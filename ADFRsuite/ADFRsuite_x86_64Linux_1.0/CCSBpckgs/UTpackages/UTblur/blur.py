# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_blur', [dirname(__file__)])
        except ImportError:
            import _blur
            return _blur
        if fp is not None:
            try:
                _mod = imp.load_module('_blur', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _blur = swig_import_helper()
    del swig_import_helper
else:
    import _blur
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def generateBlurmap(coords, radii, dens, blobbyness, weights=0, gridMove=0, padding=0.0):
    return _blur.generateBlurmap(coords, radii, dens, blobbyness, weights, gridMove, padding)
generateBlurmap = _blur.generateBlurmap

def getBoundingBox(coords, radii, blobbyness, padding=0.0):
    return _blur.getBoundingBox(coords, radii, blobbyness, padding)
getBoundingBox = _blur.getBoundingBox
elementTable = {
    "N:GLY"   : (1.625, 0.0, 0.0, 1.0,  1, 10 ),
     "CA:GLY" : (1.750, 0.3, 0.3, 0.3, -1, 10 ),
     "C:GLY"  : (1.875, 0.3, 0.3, 0.3,  1, 10 ),
     "O:GLY"  :  (1.480, 1.0, 0.0, 0.0,  1, 10 ),
     "N:ALA"  : (1.625, 0.0, 0.0, 1.0,  1,  1 ),
     "CA:ALA" : (1.750, 0.3, 0.3, 0.3, -1,  1 ),
     "C:ALA"  : (1.875, 0.3, 0.3, 0.3,  1,  1 ),
     "O:ALA"  : (1.480, 1.0, 0.0, 0.0,  1,  1 ),
     "CB:ALA" : (1.750, 0.3, 0.3, 0.3, -1,  1 ),
     "N:VAL"  : (1.625, 0.0, 0.0, 1.0,  1, 23 ),
     "CA:VAL" : (1.750, 0.3, 0.3, 0.3, -1, 23 ),
     "C:VAL"  : (1.875, 0.3, 0.3, 0.3,  1, 23 ),
     "O:VAL"  : (1.480, 1.0, 0.0, 0.0,  1, 23 ),
     "CB:VAL" : (1.750, 0.3, 0.3, 0.3, -1, 23 ),
     "CG1:VAL": (1.750, 0.3, 0.3, 0.3, -1, 23 ),
     "CG2:VAL": (1.750, 0.3, 0.3, 0.3, -1, 23 ),
     "N:LEU"  : (1.625, 0.0, 0.0, 1.0,  1, 13 ),
     "CA:LEU" : (1.750, 0.3, 0.3, 0.3, -1, 13 ),
     "C:LEU"  : (1.875, 0.3, 0.3, 0.3,  1, 13 ),
     "O:LEU"  : (1.480, 1.0, 0.0, 0.0,  1, 13 ),
     "CB:LEU" : (1.750, 0.3, 0.3, 0.3, -1, 13 ),
     "CG:LEU" : (1.750, 0.3, 0.3, 0.3, -1, 13 ),
     "CD1:LEU": (1.750, 0.3, 0.3, 0.3, -1, 13 ),
     "CD2:LEU": (1.750, 0.3, 0.3, 0.3, -1, 13 ),
     "N:ILE"  : (1.625, 0.0, 0.0, 1.0,  1, 12 ),
     "CA:ILE" : (1.750, 0.3, 0.3, 0.3, -1, 12 ),
     "C:ILE"  : (1.875, 0.3, 0.3, 0.3,  1, 12 ),
     "O:ILE"  : (1.480, 1.0, 0.0, 0.0,  1, 12 ),
     "CB:ILE" : (1.750, 0.3, 0.3, 0.3, -1, 12 ),
     "CG1:ILE": (1.750, 0.3, 0.3, 0.3, -1, 12 ),
     "CG2:ILE": (1.750, 0.3, 0.3, 0.3, -1, 12 ),
     "CD1:ILE": (1.750, 0.3, 0.3, 0.3, -1, 12 ),
     "N:MET"  : (1.625, 0.0, 0.0, 1.0,  1, 15 ),
     "CA:MET" : (1.750, 0.3, 0.3, 0.3, -1, 15 ),
     "C:MET"  : (1.875, 0.3, 0.3, 0.3,  1, 15 ),
     "O:MET"  : (1.480, 1.0, 0.0, 0.0,  1, 15 ),
     "CB:MET" : (1.750, 0.3, 0.3, 0.3, -1, 15 ),
     "CG:MET" : (1.750, 0.3, 0.3, 0.3, -1, 15 ),
     "SD:MET" : (1.775, 1.0, 1.0, 0.0,  1, 15 ),
     "CE:MET" : (1.750, 0.3, 0.3, 0.3, -1, 15 ),
     "N:PRO"  : (1.625, 0.0, 0.0, 1.0, -1, 17 ),
     "CA:PRO" : (1.750, 0.3, 0.3, 0.3, -1, 17 ),
     "C:PRO"  : (1.875, 0.3, 0.3, 0.3,  1, 17 ),
     "O:PRO"  : (1.480, 1.0, 0.0, 0.0,  1, 17 ),
     "CB:PRO" : (1.750, 0.3, 0.3, 0.3, -1, 17 ),
     "CG:PRO" : (1.750, 0.3, 0.3, 0.3, -1, 17 ),
     "CD:PRO" : (1.750, 0.3, 0.3, 0.3, -1, 17 ),
     "N:PHE"  : (1.625, 0.0, 0.0, 1.0,  1, 16 ),
     "CA:PHE" : (1.750, 0.3, 0.3, 0.3, -1, 16 ),
     "C:PHE"  : (1.875, 0.3, 0.3, 0.3,  1, 16 ),
     "O:PHE"  : (1.480, 1.0, 0.0, 0.0,  1, 16 ),
     "CB:PHE" : (1.750, 0.3, 0.3, 0.3, -1, 16 ),
     "CG:PHE" : (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "CD1:PHE": (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "CD2:PHE": (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "CE1:PHE": (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "CE2:PHE": (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "CZ:PHE" : (1.775, 0.3, 0.3, 0.3, -1, 16 ),
     "N:TRP"  : (1.625, 0.0, 0.0, 1.0,  1, 20 ),
     "CA:TRP" : (1.750, 0.3, 0.3, 0.3, -1, 20 ),
     "C:TRP"  : (1.875, 0.3, 0.3, 0.3,  1, 20 ),
     "O:TRP"  : (1.480, 1.0, 0.0, 0.0,  1, 20 ),
     "CB:TRP" : (1.750, 0.3, 0.3, 0.3, -1, 20 ),
     "CG:TRP" : (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CD1:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CD2:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "NE1:TRP": (1.625, 0.2, 0.2, 1.0,  1, 20 ),
     "CE2:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CE3:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CZ2:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CZ3:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "CH2:TRP": (1.775, 0.3, 0.3, 0.3, -1, 20 ),
     "N:SER"  : (1.625, 0.0, 0.0, 1.0,  1, 18 ),
     "CA:SER" : (1.750, 0.3, 0.3, 0.3, -1, 18 ),
     "C:SER"  : (1.875, 0.3, 0.3, 0.3,  1, 18 ),
     "O:SER"  : (1.480, 1.0, 0.0, 0.0,  1, 18 ),
     "CB:SER" : (1.750, 0.3, 0.3, 0.3, -1, 18 ),
     "OG:SER" : (1.560, 1.0, 0.0, 0.0,  1, 18 ),
     "N:THR"  : (1.625, 0.0, 0.0, 1.0,  1, 19 ),
     "CA:THR" : (1.750, 0.3, 0.3, 0.3, -1, 19 ),
     "C:THR"  : (1.875, 0.3, 0.3, 0.3,  1, 19 ),
     "O:THR"  : (1.480, 1.0, 0.0, 0.0,  1, 19 ),
     "CB:THR" : (1.750, 0.3, 0.3, 0.3, -1, 19 ),
     "OG1:THR": (1.560, 1.0, 0.0, 0.0,  1, 19 ),
     "CG2:THR": (1.750, 0.3, 0.3, 0.3, -1, 19 ),
     "N:ASN"  : (1.625, 0.0, 0.0, 1.0,  1,  3 ),
     "CA:ASN" : (1.750, 0.3, 0.3, 0.3, -1,  3 ),
     "C:ASN"  : (1.875, 0.3, 0.3, 0.3,  1,  3 ),
     "O:ASN"  : (1.480, 1.0, 0.0, 0.0,  1,  3 ),
     "CB:ASN" : (1.750, 0.3, 0.3, 0.3, -1,  3 ),
     "CG:ASN" : (1.875, 0.3, 0.3, 0.3,  1,  3 ),
     "OD1:ASN": (1.480, 1.0, 0.0, 0.0,  1,  3 ),
     "ND2:ASN": (1.625, 0.2, 0.2, 1.0,  1,  3 ),
     "N:GLN"  : (1.625, 0.0, 0.0, 1.0,  1,  7 ),
     "CA:GLN" : (1.750, 0.3, 0.3, 0.3, -1,  7 ),
     "C:GLN"  : (1.875, 0.3, 0.3, 0.3,  1,  7 ),
     "O:GLN"  : (1.480, 1.0, 0.0, 0.0,  1,  7 ),
     "CB:GLN" : (1.750, 0.3, 0.3, 0.3, -1,  7 ),
     "CG:GLN" : (1.750, 0.3, 0.3, 0.3, -1,  7 ),
     "CD:GLN" : (1.875, 0.3, 0.3, 0.3,  1,  7 ),
     "OE1:GLN": (1.480, 1.0, 0.0, 0.0,  1,  7 ),
     "NE2:GLN": (1.625, 0.2, 0.2, 1.0,  1,  7 ),
     "N:TYR"  : (1.625, 0.0, 0.0, 1.0,  1, 21 ),
     "CA:TYR" : (1.750, 0.3, 0.3, 0.3, -1, 21 ),
     "C:TYR"  : (1.875, 0.3, 0.3, 0.3,  1, 21 ),
     "O:TYR"  : (1.480, 1.0, 0.0, 0.0,  1, 21 ),
     "CB:TYR" : (1.750, 0.3, 0.3, 0.3, -1, 21 ),
     "CG:TYR" : (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "CD1:TYR": (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "CD2:TYR": (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "CE1:TYR": (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "CE2:TYR": (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "CZ:TYR" : (1.775, 0.3, 0.3, 0.3, -1, 21 ),
     "OH:TYR" : (1.535, 1.0, 0.0, 0.0,  1, 21 ),
     "N:CYS"  : (1.625, 0.0, 0.0, 1.0,  1,  6 ),
     "CA:CYS" : (1.750, 0.3, 0.3, 0.3, -1,  6 ),
     "C:CYS"  : (1.875, 0.3, 0.3, 0.3,  1,  6 ),
     "O:CYS"  : (1.480, 1.0, 0.0, 0.0,  1,  6 ),
     "CB:CYS" : (1.750, 0.3, 0.3, 0.3, -1,  6 ),
     "SG:CYS" : (1.775, 1.0, 1.0, 0.0,  1,  6 ),
     "N:LYS"  : (1.625, 0.0, 0.0, 1.0,  1, 14 ),
     "CA:LYS" : (1.750, 0.3, 0.3, 0.3, -1, 14 ),
     "C:LYS"  : (1.875, 0.3, 0.3, 0.3,  1, 14 ),
     "O:LYS"  : (1.480, 1.0, 0.0, 0.0,  1, 14 ),
     "CB:LYS" : (1.750, 0.3, 0.3, 0.3, -1, 14 ),
     "CG:LYS" : (1.750, 0.3, 0.3, 0.3, -1, 14 ),
     "CD:LYS" : (1.750, 0.3, 0.3, 0.3, -1, 14 ),
     "CE:LYS" : (1.750, 0.3, 0.3, 0.3, -1, 14 ),
     "NZ:LYS" : (1.625, 0.2, 0.2, 1.0,  1, 14 ),
     "N:ARG"  : (1.625, 0.0, 0.0, 1.0,  1,  2 ),
     "CA:ARG" : (1.750, 0.3, 0.3, 0.3, -1,  2 ),
     "C:ARG"  : (1.875, 0.3, 0.3, 0.3,  1,  2 ),
     "O:ARG"  : (1.480, 1.0, 0.0, 0.0,  1,  2 ),
     "CB:ARG" : (1.750, 0.3, 0.3, 0.3, -1,  2 ),
     "CG:ARG" : (1.750, 0.3, 0.3, 0.3, -1,  2 ),
     "CD:ARG" : (1.750, 0.3, 0.3, 0.3, -1,  2 ),
     "NE:ARG" : (1.625, 0.2, 0.2, 1.0,  1,  2 ),
     "CZ:ARG" : (1.125, 0.3, 0.3, 0.3,  1,  2 ),
     "NH1:ARG": (1.625, 0.2, 0.2, 1.0,  1,  2 ),
     "NH2:ARG": (1.625, 0.2, 0.2, 1.0,  1,  2 ),
     "N:HIS"  : (1.625, 0.0, 0.0, 1.0,  1, 11 ),
     "CA:HIS" : (1.750, 0.3, 0.3, 0.3, -1, 11 ),
     "C:HIS"  : (1.875, 0.3, 0.3, 0.3,  1, 11 ),
     "O:HIS"  : (1.480, 1.0, 0.0, 0.0,  1, 11 ),
     "CB:HIS" : (1.750, 0.3, 0.3, 0.3, -1, 11 ),
     "CG:HIS" : (1.775, 0.3, 0.3, 0.3, -1, 11 ),
     "ND1:HIS": (1.625, 0.2, 0.2, 1.0,  1, 11 ),
     "CD2:HIS": (1.775, 0.3, 0.3, 0.3, -1, 11 ),
     "CE1:HIS": (1.775, 0.3, 0.3, 0.3,  1, 11 ),
     "NE2:HIS": (1.625, 0.2, 0.2, 1.0,  1, 11 ),
     "N:ASP"  : (1.625, 0.0, 0.0, 1.0,  1,  4 ),
     "CA:ASP" : (1.750, 0.3, 0.3, 0.3, -1,  4 ),
     "C:ASP"  : (1.875, 0.3, 0.3, 0.3,  1,  4 ),
     "O:ASP"  : (1.480, 1.0, 0.0, 0.0,  1,  4 ),
     "CB:ASP" : (1.750, 0.3, 0.3, 0.3, -1,  4 ),
     "CG:ASP" : (1.875, 0.3, 0.3, 0.3,  1,  4 ),
     "OD1:ASP": (1.480, 1.0, 1.0, 1.0,  1,  4 ),
     "OD2:ASP": (1.480, 1.0, 0.0, 0.0,  1,  4 ),
     "N:GLU"  : (1.625, 0.0, 0.0, 1.0,  1,  8 ),
     "CA:GLU" : (1.750, 0.3, 0.3, 0.3, -1,  8 ),
     "C:GLU"  : (1.875, 0.3, 0.3, 0.3,  1,  8 ),
     "O:GLU"  : (1.480, 1.0, 0.0, 0.0,  1,  8 ),
     "CB:GLU" : (1.750, 0.3, 0.3, 0.3, -1,  8 ),
     "CG:GLU" : (1.750, 0.3, 0.3, 0.3, -1,  8 ),
     "CD:GLU" : (1.875, 0.3, 0.3, 0.3,  1,  8 ),
     "OE1:GLU": (1.480, 1.0, 0.0, 0.0,  1,  8 ),
     "OE2:GLU": (1.480, 1.0, 0.0, 0.0,  1,  8 )
}


def getRadii(names):
    radii = []
    for n in names:
	if elementTable.has_key(n):
            radii.append(elementTable[n][0])
	else:
            radii.append(1.0)
    return radii


# This file is compatible with both classic and new-style classes.



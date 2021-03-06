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
            fp, pathname, description = imp.find_module('_coda_types', [dirname(__file__)])
        except ImportError:
            import _coda_types
            return _coda_types
        if fp is not None:
            try:
                _mod = imp.load_module('_coda_types', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _coda_types = swig_import_helper()
    del swig_import_helper
else:
    import _coda_types
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


class SwigPyIterator(_object):
    """Proxy of C++ swig::SwigPyIterator class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_types.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        """value(SwigPyIterator self) -> PyObject *"""
        return _coda_types.SwigPyIterator_value(self)


    def incr(self, n=1):
        """
        incr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        incr(SwigPyIterator self) -> SwigPyIterator
        """
        return _coda_types.SwigPyIterator_incr(self, n)


    def decr(self, n=1):
        """
        decr(SwigPyIterator self, size_t n=1) -> SwigPyIterator
        decr(SwigPyIterator self) -> SwigPyIterator
        """
        return _coda_types.SwigPyIterator_decr(self, n)


    def distance(self, x):
        """distance(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t"""
        return _coda_types.SwigPyIterator_distance(self, x)


    def equal(self, x):
        """equal(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _coda_types.SwigPyIterator_equal(self, x)


    def copy(self):
        """copy(SwigPyIterator self) -> SwigPyIterator"""
        return _coda_types.SwigPyIterator_copy(self)


    def next(self):
        """next(SwigPyIterator self) -> PyObject *"""
        return _coda_types.SwigPyIterator_next(self)


    def __next__(self):
        """__next__(SwigPyIterator self) -> PyObject *"""
        return _coda_types.SwigPyIterator___next__(self)


    def previous(self):
        """previous(SwigPyIterator self) -> PyObject *"""
        return _coda_types.SwigPyIterator_previous(self)


    def advance(self, n):
        """advance(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _coda_types.SwigPyIterator_advance(self, n)


    def __eq__(self, x):
        """__eq__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _coda_types.SwigPyIterator___eq__(self, x)


    def __ne__(self, x):
        """__ne__(SwigPyIterator self, SwigPyIterator x) -> bool"""
        return _coda_types.SwigPyIterator___ne__(self, x)


    def __iadd__(self, n):
        """__iadd__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _coda_types.SwigPyIterator___iadd__(self, n)


    def __isub__(self, n):
        """__isub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _coda_types.SwigPyIterator___isub__(self, n)


    def __add__(self, n):
        """__add__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator"""
        return _coda_types.SwigPyIterator___add__(self, n)


    def __sub__(self, *args):
        """
        __sub__(SwigPyIterator self, ptrdiff_t n) -> SwigPyIterator
        __sub__(SwigPyIterator self, SwigPyIterator x) -> ptrdiff_t
        """
        return _coda_types.SwigPyIterator___sub__(self, *args)

    def __iter__(self):
        return self
SwigPyIterator_swigregister = _coda_types.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import coda.coda_sys
class RowColDouble(_object):
    """Proxy of C++ types::RowCol<(double)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RowColDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RowColDouble, name)
    __repr__ = _swig_repr
    __swig_setmethods__["row"] = _coda_types.RowColDouble_row_set
    __swig_getmethods__["row"] = _coda_types.RowColDouble_row_get
    if _newclass:
        row = _swig_property(_coda_types.RowColDouble_row_get, _coda_types.RowColDouble_row_set)
    __swig_setmethods__["col"] = _coda_types.RowColDouble_col_set
    __swig_getmethods__["col"] = _coda_types.RowColDouble_col_get
    if _newclass:
        col = _swig_property(_coda_types.RowColDouble_col_get, _coda_types.RowColDouble_col_set)

    def __init__(self, *args):
        """
        __init__(types::RowCol<(double)> self) -> RowColDouble
        __init__(types::RowCol<(double)> self, double r, double c) -> RowColDouble
        __init__(types::RowCol<(double)> self, std::pair< double,double > const & p) -> RowColDouble
        """
        this = _coda_types.new_RowColDouble(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iadd__(self, scalar):
        """__iadd__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___iadd__(self, scalar)


    def __add__(self, scalar):
        """__add__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___add__(self, scalar)


    def __isub__(self, scalar):
        """__isub__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___isub__(self, scalar)


    def __sub__(self, scalar):
        """__sub__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___sub__(self, scalar)


    def __imul__(self, scalar):
        """__imul__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___imul__(self, scalar)


    def __mul__(self, scalar):
        """__mul__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___mul__(self, scalar)


    def __idiv__(self, scalar):
        """__idiv__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___idiv__(self, scalar)


    def __div__(self, scalar):
        """__div__(RowColDouble self, double scalar) -> RowColDouble"""
        return _coda_types.RowColDouble___div__(self, scalar)


    def __eq__(self, p):
        """__eq__(RowColDouble self, RowColDouble p) -> bool"""
        return _coda_types.RowColDouble___eq__(self, p)


    def __ne__(self, p):
        """__ne__(RowColDouble self, RowColDouble p) -> bool"""
        return _coda_types.RowColDouble___ne__(self, p)


    def normL1(self):
        """normL1(RowColDouble self) -> double"""
        return _coda_types.RowColDouble_normL1(self)


    def normL2(self):
        """normL2(RowColDouble self) -> double"""
        return _coda_types.RowColDouble_normL2(self)

    __swig_destroy__ = _coda_types.delete_RowColDouble
    __del__ = lambda self: None
RowColDouble_swigregister = _coda_types.RowColDouble_swigregister
RowColDouble_swigregister(RowColDouble)

class RowColInt(_object):
    """Proxy of C++ types::RowCol<(sys::SSize_T)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RowColInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RowColInt, name)
    __repr__ = _swig_repr
    __swig_setmethods__["row"] = _coda_types.RowColInt_row_set
    __swig_getmethods__["row"] = _coda_types.RowColInt_row_get
    if _newclass:
        row = _swig_property(_coda_types.RowColInt_row_get, _coda_types.RowColInt_row_set)
    __swig_setmethods__["col"] = _coda_types.RowColInt_col_set
    __swig_getmethods__["col"] = _coda_types.RowColInt_col_get
    if _newclass:
        col = _swig_property(_coda_types.RowColInt_col_get, _coda_types.RowColInt_col_set)

    def __init__(self, *args):
        """
        __init__(types::RowCol<(sys::SSize_T)> self) -> RowColInt
        __init__(types::RowCol<(sys::SSize_T)> self, ssize_t r, ssize_t c) -> RowColInt
        __init__(types::RowCol<(sys::SSize_T)> self, std::pair< ssize_t,ssize_t > const & p) -> RowColInt
        """
        this = _coda_types.new_RowColInt(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iadd__(self, scalar):
        """__iadd__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___iadd__(self, scalar)


    def __add__(self, scalar):
        """__add__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___add__(self, scalar)


    def __isub__(self, scalar):
        """__isub__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___isub__(self, scalar)


    def __sub__(self, scalar):
        """__sub__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___sub__(self, scalar)


    def __imul__(self, scalar):
        """__imul__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___imul__(self, scalar)


    def __mul__(self, scalar):
        """__mul__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___mul__(self, scalar)


    def __idiv__(self, scalar):
        """__idiv__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___idiv__(self, scalar)


    def __div__(self, scalar):
        """__div__(RowColInt self, ssize_t scalar) -> RowColInt"""
        return _coda_types.RowColInt___div__(self, scalar)


    def __eq__(self, p):
        """__eq__(RowColInt self, RowColInt p) -> bool"""
        return _coda_types.RowColInt___eq__(self, p)


    def __ne__(self, p):
        """__ne__(RowColInt self, RowColInt p) -> bool"""
        return _coda_types.RowColInt___ne__(self, p)


    def normL1(self):
        """normL1(RowColInt self) -> ssize_t"""
        return _coda_types.RowColInt_normL1(self)


    def normL2(self):
        """normL2(RowColInt self) -> ssize_t"""
        return _coda_types.RowColInt_normL2(self)

    __swig_destroy__ = _coda_types.delete_RowColInt
    __del__ = lambda self: None
RowColInt_swigregister = _coda_types.RowColInt_swigregister
RowColInt_swigregister(RowColInt)

class RowColSizeT(_object):
    """Proxy of C++ types::RowCol<(size_t)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RowColSizeT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RowColSizeT, name)
    __repr__ = _swig_repr
    __swig_setmethods__["row"] = _coda_types.RowColSizeT_row_set
    __swig_getmethods__["row"] = _coda_types.RowColSizeT_row_get
    if _newclass:
        row = _swig_property(_coda_types.RowColSizeT_row_get, _coda_types.RowColSizeT_row_set)
    __swig_setmethods__["col"] = _coda_types.RowColSizeT_col_set
    __swig_getmethods__["col"] = _coda_types.RowColSizeT_col_get
    if _newclass:
        col = _swig_property(_coda_types.RowColSizeT_col_get, _coda_types.RowColSizeT_col_set)

    def __init__(self, *args):
        """
        __init__(types::RowCol<(size_t)> self) -> RowColSizeT
        __init__(types::RowCol<(size_t)> self, size_t r, size_t c) -> RowColSizeT
        __init__(types::RowCol<(size_t)> self, std::pair< size_t,size_t > const & p) -> RowColSizeT
        """
        this = _coda_types.new_RowColSizeT(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iadd__(self, scalar):
        """__iadd__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___iadd__(self, scalar)


    def __add__(self, scalar):
        """__add__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___add__(self, scalar)


    def __isub__(self, scalar):
        """__isub__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___isub__(self, scalar)


    def __sub__(self, scalar):
        """__sub__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___sub__(self, scalar)


    def __imul__(self, scalar):
        """__imul__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___imul__(self, scalar)


    def __mul__(self, scalar):
        """__mul__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___mul__(self, scalar)


    def __idiv__(self, scalar):
        """__idiv__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___idiv__(self, scalar)


    def __div__(self, scalar):
        """__div__(RowColSizeT self, size_t scalar) -> RowColSizeT"""
        return _coda_types.RowColSizeT___div__(self, scalar)


    def __eq__(self, p):
        """__eq__(RowColSizeT self, RowColSizeT p) -> bool"""
        return _coda_types.RowColSizeT___eq__(self, p)


    def __ne__(self, p):
        """__ne__(RowColSizeT self, RowColSizeT p) -> bool"""
        return _coda_types.RowColSizeT___ne__(self, p)


    def normL1(self):
        """normL1(RowColSizeT self) -> size_t"""
        return _coda_types.RowColSizeT_normL1(self)


    def normL2(self):
        """normL2(RowColSizeT self) -> size_t"""
        return _coda_types.RowColSizeT_normL2(self)

    __swig_destroy__ = _coda_types.delete_RowColSizeT
    __del__ = lambda self: None
RowColSizeT_swigregister = _coda_types.RowColSizeT_swigregister
RowColSizeT_swigregister(RowColSizeT)

class RgAzDouble(_object):
    """Proxy of C++ types::RgAz<(double)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RgAzDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RgAzDouble, name)
    __repr__ = _swig_repr
    __swig_setmethods__["rg"] = _coda_types.RgAzDouble_rg_set
    __swig_getmethods__["rg"] = _coda_types.RgAzDouble_rg_get
    if _newclass:
        rg = _swig_property(_coda_types.RgAzDouble_rg_get, _coda_types.RgAzDouble_rg_set)
    __swig_setmethods__["az"] = _coda_types.RgAzDouble_az_set
    __swig_getmethods__["az"] = _coda_types.RgAzDouble_az_get
    if _newclass:
        az = _swig_property(_coda_types.RgAzDouble_az_get, _coda_types.RgAzDouble_az_set)

    def __init__(self, *args):
        """
        __init__(types::RgAz<(double)> self) -> RgAzDouble
        __init__(types::RgAz<(double)> self, double r, double c) -> RgAzDouble
        __init__(types::RgAz<(double)> self, std::pair< double,double > const & p) -> RgAzDouble
        """
        this = _coda_types.new_RgAzDouble(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def __iadd__(self, scalar):
        """__iadd__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___iadd__(self, scalar)


    def __add__(self, scalar):
        """__add__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___add__(self, scalar)


    def __isub__(self, scalar):
        """__isub__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___isub__(self, scalar)


    def __sub__(self, scalar):
        """__sub__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___sub__(self, scalar)


    def __imul__(self, scalar):
        """__imul__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___imul__(self, scalar)


    def __mul__(self, scalar):
        """__mul__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___mul__(self, scalar)


    def __idiv__(self, scalar):
        """__idiv__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___idiv__(self, scalar)


    def __div__(self, scalar):
        """__div__(RgAzDouble self, double scalar) -> RgAzDouble"""
        return _coda_types.RgAzDouble___div__(self, scalar)


    def __eq__(self, p):
        """__eq__(RgAzDouble self, RgAzDouble p) -> bool"""
        return _coda_types.RgAzDouble___eq__(self, p)


    def __ne__(self, p):
        """__ne__(RgAzDouble self, RgAzDouble p) -> bool"""
        return _coda_types.RgAzDouble___ne__(self, p)

    __swig_destroy__ = _coda_types.delete_RgAzDouble
    __del__ = lambda self: None
RgAzDouble_swigregister = _coda_types.RgAzDouble_swigregister
RgAzDouble_swigregister(RgAzDouble)

class VectorRowColInt(_object):
    """Proxy of C++ std::vector<(types::RowCol<(sys::SSize_T)>)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorRowColInt, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorRowColInt, name)
    __repr__ = _swig_repr

    def iterator(self):
        """iterator(VectorRowColInt self) -> SwigPyIterator"""
        return _coda_types.VectorRowColInt_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        """__nonzero__(VectorRowColInt self) -> bool"""
        return _coda_types.VectorRowColInt___nonzero__(self)


    def __bool__(self):
        """__bool__(VectorRowColInt self) -> bool"""
        return _coda_types.VectorRowColInt___bool__(self)


    def __len__(self):
        """__len__(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::size_type"""
        return _coda_types.VectorRowColInt___len__(self)


    def pop(self):
        """pop(VectorRowColInt self) -> RowColInt"""
        return _coda_types.VectorRowColInt_pop(self)


    def __getslice__(self, i, j):
        """__getslice__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i, std::vector< types::RowCol< ssize_t > >::difference_type j) -> VectorRowColInt"""
        return _coda_types.VectorRowColInt___getslice__(self, i, j)


    def __setslice__(self, *args):
        """
        __setslice__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i, std::vector< types::RowCol< ssize_t > >::difference_type j, VectorRowColInt v)
        __setslice__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i, std::vector< types::RowCol< ssize_t > >::difference_type j)
        """
        return _coda_types.VectorRowColInt___setslice__(self, *args)


    def __delslice__(self, i, j):
        """__delslice__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i, std::vector< types::RowCol< ssize_t > >::difference_type j)"""
        return _coda_types.VectorRowColInt___delslice__(self, i, j)


    def __delitem__(self, *args):
        """
        __delitem__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i)
        __delitem__(VectorRowColInt self, PySliceObject * slice)
        """
        return _coda_types.VectorRowColInt___delitem__(self, *args)


    def __getitem__(self, *args):
        """
        __getitem__(VectorRowColInt self, PySliceObject * slice) -> VectorRowColInt
        __getitem__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i) -> RowColInt
        """
        return _coda_types.VectorRowColInt___getitem__(self, *args)


    def __setitem__(self, *args):
        """
        __setitem__(VectorRowColInt self, PySliceObject * slice, VectorRowColInt v)
        __setitem__(VectorRowColInt self, PySliceObject * slice)
        __setitem__(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::difference_type i, RowColInt x)
        """
        return _coda_types.VectorRowColInt___setitem__(self, *args)


    def append(self, x):
        """append(VectorRowColInt self, RowColInt x)"""
        return _coda_types.VectorRowColInt_append(self, x)


    def empty(self):
        """empty(VectorRowColInt self) -> bool"""
        return _coda_types.VectorRowColInt_empty(self)


    def size(self):
        """size(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::size_type"""
        return _coda_types.VectorRowColInt_size(self)


    def clear(self):
        """clear(VectorRowColInt self)"""
        return _coda_types.VectorRowColInt_clear(self)


    def swap(self, v):
        """swap(VectorRowColInt self, VectorRowColInt v)"""
        return _coda_types.VectorRowColInt_swap(self, v)


    def get_allocator(self):
        """get_allocator(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::allocator_type"""
        return _coda_types.VectorRowColInt_get_allocator(self)


    def begin(self):
        """begin(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::iterator"""
        return _coda_types.VectorRowColInt_begin(self)


    def end(self):
        """end(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::iterator"""
        return _coda_types.VectorRowColInt_end(self)


    def rbegin(self):
        """rbegin(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::reverse_iterator"""
        return _coda_types.VectorRowColInt_rbegin(self)


    def rend(self):
        """rend(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::reverse_iterator"""
        return _coda_types.VectorRowColInt_rend(self)


    def pop_back(self):
        """pop_back(VectorRowColInt self)"""
        return _coda_types.VectorRowColInt_pop_back(self)


    def erase(self, *args):
        """
        erase(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::iterator pos) -> std::vector< types::RowCol< ssize_t > >::iterator
        erase(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::iterator first, std::vector< types::RowCol< ssize_t > >::iterator last) -> std::vector< types::RowCol< ssize_t > >::iterator
        """
        return _coda_types.VectorRowColInt_erase(self, *args)


    def __init__(self, *args):
        """
        __init__(std::vector<(types::RowCol<(sys::SSize_T)>)> self) -> VectorRowColInt
        __init__(std::vector<(types::RowCol<(sys::SSize_T)>)> self, VectorRowColInt arg2) -> VectorRowColInt
        __init__(std::vector<(types::RowCol<(sys::SSize_T)>)> self, std::vector< types::RowCol< ssize_t > >::size_type size) -> VectorRowColInt
        __init__(std::vector<(types::RowCol<(sys::SSize_T)>)> self, std::vector< types::RowCol< ssize_t > >::size_type size, RowColInt value) -> VectorRowColInt
        """
        this = _coda_types.new_VectorRowColInt(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        """push_back(VectorRowColInt self, RowColInt x)"""
        return _coda_types.VectorRowColInt_push_back(self, x)


    def front(self):
        """front(VectorRowColInt self) -> RowColInt"""
        return _coda_types.VectorRowColInt_front(self)


    def back(self):
        """back(VectorRowColInt self) -> RowColInt"""
        return _coda_types.VectorRowColInt_back(self)


    def assign(self, n, x):
        """assign(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::size_type n, RowColInt x)"""
        return _coda_types.VectorRowColInt_assign(self, n, x)


    def resize(self, *args):
        """
        resize(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::size_type new_size)
        resize(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::size_type new_size, RowColInt x)
        """
        return _coda_types.VectorRowColInt_resize(self, *args)


    def insert(self, *args):
        """
        insert(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::iterator pos, RowColInt x) -> std::vector< types::RowCol< ssize_t > >::iterator
        insert(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::iterator pos, std::vector< types::RowCol< ssize_t > >::size_type n, RowColInt x)
        """
        return _coda_types.VectorRowColInt_insert(self, *args)


    def reserve(self, n):
        """reserve(VectorRowColInt self, std::vector< types::RowCol< ssize_t > >::size_type n)"""
        return _coda_types.VectorRowColInt_reserve(self, n)


    def capacity(self):
        """capacity(VectorRowColInt self) -> std::vector< types::RowCol< ssize_t > >::size_type"""
        return _coda_types.VectorRowColInt_capacity(self)

    __swig_destroy__ = _coda_types.delete_VectorRowColInt
    __del__ = lambda self: None
VectorRowColInt_swigregister = _coda_types.VectorRowColInt_swigregister
VectorRowColInt_swigregister(VectorRowColInt)

class VectorSizeT(_object):
    """Proxy of C++ std::vector<(size_t)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorSizeT, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorSizeT, name)
    __repr__ = _swig_repr

    def iterator(self):
        """iterator(VectorSizeT self) -> SwigPyIterator"""
        return _coda_types.VectorSizeT_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        """__nonzero__(VectorSizeT self) -> bool"""
        return _coda_types.VectorSizeT___nonzero__(self)


    def __bool__(self):
        """__bool__(VectorSizeT self) -> bool"""
        return _coda_types.VectorSizeT___bool__(self)


    def __len__(self):
        """__len__(VectorSizeT self) -> std::vector< size_t >::size_type"""
        return _coda_types.VectorSizeT___len__(self)


    def pop(self):
        """pop(VectorSizeT self) -> std::vector< size_t >::value_type"""
        return _coda_types.VectorSizeT_pop(self)


    def __getslice__(self, i, j):
        """__getslice__(VectorSizeT self, std::vector< size_t >::difference_type i, std::vector< size_t >::difference_type j) -> VectorSizeT"""
        return _coda_types.VectorSizeT___getslice__(self, i, j)


    def __setslice__(self, *args):
        """
        __setslice__(VectorSizeT self, std::vector< size_t >::difference_type i, std::vector< size_t >::difference_type j, VectorSizeT v)
        __setslice__(VectorSizeT self, std::vector< size_t >::difference_type i, std::vector< size_t >::difference_type j)
        """
        return _coda_types.VectorSizeT___setslice__(self, *args)


    def __delslice__(self, i, j):
        """__delslice__(VectorSizeT self, std::vector< size_t >::difference_type i, std::vector< size_t >::difference_type j)"""
        return _coda_types.VectorSizeT___delslice__(self, i, j)


    def __delitem__(self, *args):
        """
        __delitem__(VectorSizeT self, std::vector< size_t >::difference_type i)
        __delitem__(VectorSizeT self, PySliceObject * slice)
        """
        return _coda_types.VectorSizeT___delitem__(self, *args)


    def __getitem__(self, *args):
        """
        __getitem__(VectorSizeT self, PySliceObject * slice) -> VectorSizeT
        __getitem__(VectorSizeT self, std::vector< size_t >::difference_type i) -> std::vector< size_t >::value_type const &
        """
        return _coda_types.VectorSizeT___getitem__(self, *args)


    def __setitem__(self, *args):
        """
        __setitem__(VectorSizeT self, PySliceObject * slice, VectorSizeT v)
        __setitem__(VectorSizeT self, PySliceObject * slice)
        __setitem__(VectorSizeT self, std::vector< size_t >::difference_type i, std::vector< size_t >::value_type const & x)
        """
        return _coda_types.VectorSizeT___setitem__(self, *args)


    def append(self, x):
        """append(VectorSizeT self, std::vector< size_t >::value_type const & x)"""
        return _coda_types.VectorSizeT_append(self, x)


    def empty(self):
        """empty(VectorSizeT self) -> bool"""
        return _coda_types.VectorSizeT_empty(self)


    def size(self):
        """size(VectorSizeT self) -> std::vector< size_t >::size_type"""
        return _coda_types.VectorSizeT_size(self)


    def clear(self):
        """clear(VectorSizeT self)"""
        return _coda_types.VectorSizeT_clear(self)


    def swap(self, v):
        """swap(VectorSizeT self, VectorSizeT v)"""
        return _coda_types.VectorSizeT_swap(self, v)


    def get_allocator(self):
        """get_allocator(VectorSizeT self) -> std::vector< size_t >::allocator_type"""
        return _coda_types.VectorSizeT_get_allocator(self)


    def begin(self):
        """begin(VectorSizeT self) -> std::vector< size_t >::iterator"""
        return _coda_types.VectorSizeT_begin(self)


    def end(self):
        """end(VectorSizeT self) -> std::vector< size_t >::iterator"""
        return _coda_types.VectorSizeT_end(self)


    def rbegin(self):
        """rbegin(VectorSizeT self) -> std::vector< size_t >::reverse_iterator"""
        return _coda_types.VectorSizeT_rbegin(self)


    def rend(self):
        """rend(VectorSizeT self) -> std::vector< size_t >::reverse_iterator"""
        return _coda_types.VectorSizeT_rend(self)


    def pop_back(self):
        """pop_back(VectorSizeT self)"""
        return _coda_types.VectorSizeT_pop_back(self)


    def erase(self, *args):
        """
        erase(VectorSizeT self, std::vector< size_t >::iterator pos) -> std::vector< size_t >::iterator
        erase(VectorSizeT self, std::vector< size_t >::iterator first, std::vector< size_t >::iterator last) -> std::vector< size_t >::iterator
        """
        return _coda_types.VectorSizeT_erase(self, *args)


    def __init__(self, *args):
        """
        __init__(std::vector<(size_t)> self) -> VectorSizeT
        __init__(std::vector<(size_t)> self, VectorSizeT arg2) -> VectorSizeT
        __init__(std::vector<(size_t)> self, std::vector< size_t >::size_type size) -> VectorSizeT
        __init__(std::vector<(size_t)> self, std::vector< size_t >::size_type size, std::vector< size_t >::value_type const & value) -> VectorSizeT
        """
        this = _coda_types.new_VectorSizeT(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        """push_back(VectorSizeT self, std::vector< size_t >::value_type const & x)"""
        return _coda_types.VectorSizeT_push_back(self, x)


    def front(self):
        """front(VectorSizeT self) -> std::vector< size_t >::value_type const &"""
        return _coda_types.VectorSizeT_front(self)


    def back(self):
        """back(VectorSizeT self) -> std::vector< size_t >::value_type const &"""
        return _coda_types.VectorSizeT_back(self)


    def assign(self, n, x):
        """assign(VectorSizeT self, std::vector< size_t >::size_type n, std::vector< size_t >::value_type const & x)"""
        return _coda_types.VectorSizeT_assign(self, n, x)


    def resize(self, *args):
        """
        resize(VectorSizeT self, std::vector< size_t >::size_type new_size)
        resize(VectorSizeT self, std::vector< size_t >::size_type new_size, std::vector< size_t >::value_type const & x)
        """
        return _coda_types.VectorSizeT_resize(self, *args)


    def insert(self, *args):
        """
        insert(VectorSizeT self, std::vector< size_t >::iterator pos, std::vector< size_t >::value_type const & x) -> std::vector< size_t >::iterator
        insert(VectorSizeT self, std::vector< size_t >::iterator pos, std::vector< size_t >::size_type n, std::vector< size_t >::value_type const & x)
        """
        return _coda_types.VectorSizeT_insert(self, *args)


    def reserve(self, n):
        """reserve(VectorSizeT self, std::vector< size_t >::size_type n)"""
        return _coda_types.VectorSizeT_reserve(self, n)


    def capacity(self):
        """capacity(VectorSizeT self) -> std::vector< size_t >::size_type"""
        return _coda_types.VectorSizeT_capacity(self)

    __swig_destroy__ = _coda_types.delete_VectorSizeT
    __del__ = lambda self: None
VectorSizeT_swigregister = _coda_types.VectorSizeT_swigregister
VectorSizeT_swigregister(VectorSizeT)

# This file is compatible with both classic and new-style classes.



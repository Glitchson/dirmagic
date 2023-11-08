"""
This is a simple """
from errno import ENOTEMPTY
from os import (
    chdir,
    environ, 
    getcwd, 
    listdir, 
    mkdir, 
    remove, 
    rmdir
)
from os.path import (
    abspath, 
    dirname, 
    exists, 
    getsize, 
    isdir, 
    isfile, 
    join
)
from platform import system
class cls:
    def __init__(self,kwargs) -> None:
        self.__dict__={**kwargs}
def _init(_p):
    if _p==Ellipsis:
        _p=getcwd()
    cd= getcwd()
    try:
        _p=abspath(_p)
    except:
        _p=join(cd,_p)
    return cls({
        "path":_p,
        "isfolder":isdir(_p),
        "isfile":isfile(_p),
        "exists":exists(_p),
        "folder":dirname(_p) if isfile(_p) else _p,
        "cd":cd,
        "isin":False,
        "index":0,
        "iter":[] if not exists(_p) or isfile(_p) else listdir(_p)
    })
def _home():
    sys=system()
    if sys=="Windows":
        return environ["USERPROFILE"]
    return environ["HOME"]
def _pdel(_p):
    if not exists(_p):
        return
    if isfile(_p):
        remove(_p)
        return
    rmdir(_p)
def mkfile(_p):
    if exists(_p):
        return
    elif _p.endswith("/"):
        mkdir(_p)
        return
    with open(_p,"w") as f:
        f.write("")
    return
def _check_exists(_dict):
    if _dict.exists:
            return
    raise FileNotFoundError("The path doesn't exist. Use `.create` to create the file / folder")
def _create(_dict,isdir):
    if not _dict.exists:
        if isdir:
            mkdir(_dict.path)
            _dict.isfolder=False
            _dict.isfolder=True
        else:
            mkfile(_dict.path)
            _dict.isfolder=False
            _dict.isfolder=True
        _dict.exists=True
def _rm(_dict):
    if _dict.isfile:
            remove(_dict.path)
            return
    try:
        rmdir(_dict.path)
        return
    except Exception as e:
        if e==OSError and e.errno==ENOTEMPTY:
            raise OSError(f"The folder {_dict.path}, use the del function to delete the folder and the instance")
        raise e
def _join(_dict,v):
    if isinstance(v,str):
        return join(_dict.folder,v)
    elif v==Ellipsis:
        return dirname(_dict.folder)
def _inv_chdir(_dict):
    if not _dict.isin:
        chdir(_dict.folder)
        _dict.isin=True
        return
    chdir(_dict.cd)
    _dict.isin=False
def _sub(_dict,v):
    if isinstance(v,str):
        _pdel(join(_dict.folder,v))
        return
    elif isinstance(v,(tuple,list)):
        [_pdel(join(_dict.folder,i)) for i in v]
        return
def _add(_dict,v):
    if isinstance(v,str):
        p=join(_dict.folder,v)
        mkfile(p)
        return
    elif isinstance(v,(tuple,list)):
        [mkfile(join(_dict.folder,i)) for i in v]
        return
class Path:
    """"""
    @staticmethod
    def home()->str:
        return _home()
    def __init__(self,path:str):
        self.cls=_init(path)
    def exists(self)->bool:
        """Checks whether the path exists"""
        return self.cls.exists
    def parent(self):
        """Returns the a `Path` instance parent folder of the file or folder refrenced in the class"""
        _check_exists(self.cls)
        return Path(dirname(self.cls.path))
    def create(self,isdir:bool=True):
        """Create the the path if it doesn't exist. If the path is a file, `isdir=False` else a folder is created"""
        _create(self.cls,isdir)
    def remove(self):
        """Removes the file or folder refrenced in this path"""
        _check_exists(self.cls)
        _rm(self.cls)
    def __str__(self) -> str:
        return self.cls.path
    def __truediv__(self,v:str):
        """Joins a string into a path"""
        _check_exists(self.cls)
        return Path(_join(self.cls,v))
    def __invert__(self):
        """Entering and Leaving a directory"""
        _inv_chdir(self.cls)
        return
    def __bool__(self)->bool:
        """Returns true if the folder """
        return self.cls.exists
    def __sub__(self,v:object):
        """Removes files or folders"""
        _check_exists(self.cls)
        _sub(self.cls,v)
    def __add__(self,v:object):
        """Adds files or folders to the directory"""
        _check_exists(self.cls)
        _add(self.cls,v)
    def __iter__(self)->list|tuple:
        """Returns a list of the files and folders in the folder"""
        _check_exists(self.cls)
        if self.cls.isfile:
            raise ValueError("Path is a file not a directory")
        return iter([join(self.cls.folder,i) for i in self.cls.iter])
    def __next__(self):
        if self.cls.index>len(list(self)):
            raise StopIteration
        self.cls.index+=1
        return self.cls.iter[self.cls.index-1]
    def __len__(self)->int:
        """Returns the size """
        _check_exists(self.cls)
        return getsize(self.cls.path)
    def __enter__(self):
        """Changes the directory into the folder"""
        _check_exists(self.cls)
        self.cls.cd=getcwd()
        chdir(self.cls.folder)
        return self
    def __exit__(self, exc_type, exc_value, traceback)->None:
        """Returns to the directory"""
        if exc_type:
            raise exc_type
        chdir(self.cls.cd)
        return 
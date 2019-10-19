import pkg_resources
from subprocess import call


packages = [dist.project_name for dist in pkg_resources.working_set]

array = ["zict", "XlsxWriter", "wurlitzer", "wrapt", "pyzmq", "traitlets", "jupyter-core", "tornado", "jupyter-client",
         "setuptools", "prompt-toolkit", "parso", "jedi", "ipython", "ipykernel", "entrypoints", "Jinja2", "nbconvert",
         "prometheus-client", "terminado", "notebook", "widgetsnbextension", "wheel", "Werkzeug", "urllib3", "typing",
         "attrs", "Twisted", "tqdm", "numpy", "torch", "Pillow", "torchvision", "toolz", "srsly", "plac", "preshed", "blis", "thinc",
         "tf-estimator-nightly", "gast", "grpcio", "protobuf", "absl-py", "tensorboard", "opt-einsum", "tensorflow-estimator",
         "google-pasta", "tensorflow", "mpmath", "sympy", "scipy", "pytz", "pandas", "statsmodels", "SQLAlchemy", "qtconsole",
         "lazy-object-proxy", "astroid", "isort", "pylint", "pyparsing", "packaging", "snowballstemmer", "docutils", "Sphinx",
         "cloudpickle", "spyder-kernels", "QtPy", "QtAwesome", "PyQt5-sip", "PyQt5", "PyQtWebEngine", "keyring", "psutil", "spyder",
         "spacy", "soupsieve", "joblib", "scikit-learn", "ruamel.yaml.clib", "ruamel-yaml", "PyYAML", "importlib-metadata", "pluggy",
         "pytest", "pytest-remotedata", "pytest-openfiles", "pytest-doctestplus", "PySocks", "pyrsistent", "pyodbc", "pycurl", "pyasn1",
         "pyasn1-modules", "pathlib2", "partd", "llvmlite", "numba", "pynndescent", "openTSNE", "commonmark", "msgpack", "lockfile",
         "cachecontrol", "orange-canvas-core", "matplotlib", "orange-widget-base", "Orange3", "openpyxl", "olefile", "numexpr", "nltk",
         "lxml", "h5py", "Keras", "json5", "jsonschema", "jupyterlab-server", "jupyterlab", "jeepney", "ipywidgets", "imageio", "idna","glob2",
         "gensim", "funcy", "Flask", "Flask-Cors", "filelock", "dask", "distributed", "cytoolz","Cython", "contextlib2", "certifi", "botocore",
         "boto3", "bokeh", "bitarray", "beautifulsoup4", "astropy","asn1crypto", "intel-numpy"]


for a in array:
    try:
        print("pip install " + a + " --upgrade ")
        call("pip install " + a + " --upgrade ", shell=True)
    except:
        call("pip install " + a, shell=True)

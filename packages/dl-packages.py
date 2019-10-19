from subprocess import call

lib = ["numpy", "scipy", "pandas", "matplotlib", "seaborn", "bokeh", "plotly"
    ,"scikit-learn","keras", "nltk", "gensim", "scrapy", "tensorflow-gpu",
       "torch", "statsmodels", "spyder", "spacy", "imgaug", "opencv-python"
       , "Pillow", "jupyter", "pylint"]


# call("sudo apt install python3-pip")

for l in lib:
    try:
        call("pip3 install " + l + " --upgrade --user", shell=True)
    except:
        call("pip3 install " + l + " --user", shell=True)

call("sudo apt-get purge nvidia*", shell=True)
call("sudo apt install ubuntu-drivers-common", shell=True)
call("sudo apt install jupyter", shell=True)
call("sudo apt-get install nvidia-375", shell=True)

# cases
python = "vignesh"
print(python.upper())
python = "VIGNESH"
print(python.lower())

#
python = "vignesh"
print(python.replace("gnesh","ntage"))

python ="python programm"
print(python.index("python"))

python ="python programm"
print(python.find("programm"))

#
python = "vignesh"
print(python.startswith("v"))

python = "vignesh"
print(python.endswith("h"))

# strips
python = "vignesh"
print(len(python))

python = "  vignesh   "
print(python.strip())

python = "  vignesh   "
print(python.rstrip())

python = "  vignesh   "
print(python.lstrip())

# prefix and suffix
python = "python programm"
print(python.removeprefix("python"))

python = "python programm"
print(python.removesuffix("programm"))
#
python = "python programm"
print(python.count("p"))
#
python = "python programm"
print(python.split())

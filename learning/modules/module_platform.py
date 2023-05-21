import platform

line = "-" * 80

print(line, "| 01 dir", line, sep="\n")
print(dir(platform))

print(line, "| 02 platform", line, sep="\n")
print(platform.platform())

print(line, "| 03 version", line, sep="\n")
print(platform.version())

print(line, "| 04 architecture", line, sep="\n")
print(platform.architecture())

print(line, "| 05 machine", line, sep="\n")
print(platform.machine())

print(line, "| 06 processor", line, sep="\n")
print(platform.processor())

print(line, "| 06 system", line, sep="\n")
print(platform.system())

print(platform.python_version())
print(platform.python_implementation())
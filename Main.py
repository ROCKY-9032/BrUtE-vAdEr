import subprocess

req = int(input("[+] Enter 0 for requirements > "))

if req == 0:
    subprocess.call("pip install pyfiglet", shell=True)
    subprocess.call("pip install pyzipper", shell=True)
else:
    print("-------Proceed-------")

print("=========================================================")

print("Requirements installed successfully")

print("Running The BrUtE-vAdEr:")

subprocess.call("python BruTe-vAdEr.py")
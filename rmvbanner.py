import plistlib
import glob
import os

parentFolder = input("Enter the path to the folder that contains all the .webclip folders:\n")

try:
    subfolderList = [f.path for f in os.scandir(parentFolder) if f.is_dir()]
except FileNotFoundError:
    print("Error: Invalid path.")
    exit()

i = 1
for subfolder in subfolderList:
    print(f"Processing folder {i}: {os.path.basename(subfolder)}")

    plistFiles = glob.glob(subfolder + '/*.plist')

    for plistFile in plistFiles:

        try:
            with open(plistFile, 'rb') as f:
                plist = plistlib.load(f)
        except FileNotFoundError:
            print(f"Error: Unable to open {os.path.basename(plistFile)}")
            continue

        if 'ShortcutIdentifier' in plist:
            del plist['ShortcutIdentifier']
            with open(plistFile, 'wb') as f:
                plistlib.dump(plist, f)
            print(f"Successfully removed ShortcutIdentifier from {os.path.basename(plistFile)}")
        else:
            print(f"{os.path.basename(plistFile)} does not contain ShortcutIdentifier.")
            shutil.rmtree(subfolder)

    i += 1

print("\n\nsuccessfully removed all the ShortcutIdentifiers from all the .plists in all the folders.\nYou can restore the folders now and enjoy your icons without anoying banners :)")

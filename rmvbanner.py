import plistlib
import glob
import os

# enter folder path
parent_folder = input("Enter path to parent folder: \n\n")

try:
    subfolder_list = [f.path for f in os.scandir(parent_folder) if f.is_dir()]
except FileNotFoundError:
    print("Error: Invalid path.")
    exit()

i = 1
for subfolder in subfolder_list:
    print(f"Processing folder {i}: {os.path.basename(subfolder)}")

    plist_files = glob.glob(subfolder + '/*.plist')

    for plist_file in plist_files:

        try:
            with open(plist_file, 'rb') as f:
                plist = plistlib.load(f)
        except FileNotFoundError:
            print(f"Error: Unable to open {os.path.basename(plist_file)}")
            continue

        if 'ShortcutIdentifier' in plist:
            del plist['ShortcutIdentifier']
            with open(plist_file, 'wb') as f:
                plistlib.dump(plist, f)
            print(f"Successfully removed ShortcutIdentifier from {os.path.basename(plist_file)}")
        else:
            print(f"{os.path.basename(plist_file)} does not contain ShortcutIdentifier.")
            os.system("rm -rf '{}'".format(subfolder))

    i += 1

print("\n\n successfully removed all the ShortcutIdentifiers from all the .plists in all the folders.\n You can restore the folders now and enjoy your icons without anoying banners :)")

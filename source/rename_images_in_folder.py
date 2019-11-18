import sys
import os

def rename_images(name_string, extension, zero_padding):
	path = os.path.dirname(os.path.realpath(__file__))
	files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	for i in range(0, len(files)):
		if not files[i].endswith(extension):
			continue
		new_name = "%s.%s" % (name_string % str(i).zfill(zero_padding), extension)
		print files[i], "=>", new_name
		os.rename(os.path.join(path, files[i]), os.path.join(path, new_name))

def main():
	if len(sys.argv) < 4:
		print "Missing Arguments."
		print "Example:"
		print "    python rename_images_in_folder.py image_%s png 4"
		return
	rename_images(str(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]))

main()

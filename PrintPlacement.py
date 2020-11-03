from PIL import Image
import os

def name_sort(name):
	if name.endswith('.png'):
		return 2*int(name.split('_')[0]) + ('[back]' in name)
	return 0

im_list = []
for file_name in sorted(os.listdir('input'), key=name_sort):
	print(file_name)
	if file_name.endswith('.png'):
		 im_list.append(Image.open('./input/'+file_name).convert('RGB'))

im_list[0].save("./output/cards.pdf","PDF", resolution=100.0, save_all=True, append_images=im_list[1:])

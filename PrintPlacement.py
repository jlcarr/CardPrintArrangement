from PIL import Image, ImageDraw
import os
import json
import math

def name_sort(name):
	if name.endswith('.png'):
		return 2*int(name.split('_')[0]) + ('[back]' in name)
	return 0


def load_files(input_dir):
	im_list = []
	for file_name in sorted(os.listdir(input_dir), key=name_sort):
		if file_name.endswith('.png'):
			full_path = os.path.join(os.getcwd(), input_dir, file_name)
			print(f"Reading: {full_path}")
			im_list.append(Image.open(full_path))
	
	return im_list


def create_layouts(im_list, config):
	layout_list = []

	printsheet_height_inches = config["printsheet-height-inches"]
	printsheet_width_inches = config["printsheet-width-inches"]
	printsheet_ppi = config["printsheet-ppi"]
	printsheet_height_px = int(printsheet_height_inches * printsheet_ppi)
	printsheet_width_px = int(printsheet_width_inches * printsheet_ppi)

	card_height_inches = config["card-height-inches"]
	card_width_inches = config["card-width-inches"]
	card_bleed_inches = config["card-bleed-inches"]
	card_height_px = card_height_inches * printsheet_ppi
	card_width_px = card_width_inches * printsheet_ppi
	total_card_height_px = (card_height_inches + 2*card_bleed_inches) * printsheet_ppi
	total_card_width_px = (card_width_inches + 2*card_bleed_inches) * printsheet_ppi

	n_vertical = int(printsheet_height_px / total_card_height_px)
	n_horizontal = int(printsheet_width_px / total_card_width_px)
	n_sheets = math.ceil(len(im_list) / 2 / n_vertical / n_horizontal)
	print(f"{n_sheets} sheets (front and back) of {n_vertical}x{n_horizontal} cards")
	
	line_width = int(printsheet_ppi/16)

	for i_sheet in range(n_sheets):
		# Prepare the front
		front = Image.new('RGB', (printsheet_width_px, printsheet_height_px), (255,255,255))
		front_draw = ImageDraw.Draw(front)
		back = Image.new('RGB', (printsheet_width_px, printsheet_height_px), (255,255,255))
		back_draw = ImageDraw.Draw(back)
		# draw the cutting guides
		for i_guide in range(n_vertical):
			y_pos = (1/2+i_guide) * printsheet_height_px / n_vertical - card_height_px /2
			front_draw.line([(0,y_pos), (printsheet_width_px, y_pos)], fill=(255,0,0), width=line_width)
			back_draw.line([(0,y_pos), (printsheet_width_px, y_pos)], fill=(255,0,0), width=line_width)
			y_pos = (1/2+i_guide) * printsheet_height_px / n_vertical + card_height_px /2
			front_draw.line([(0,y_pos), (printsheet_width_px, y_pos)], fill=(255,0,0), width=line_width)
			back_draw.line([(0,y_pos), (printsheet_width_px, y_pos)], fill=(255,0,0), width=line_width)
		for i_guide in range(n_horizontal):
			x_pos = (1/2+i_guide) * printsheet_width_px / n_horizontal - card_width_px /2
			front_draw.line([(x_pos,0), (x_pos, printsheet_height_px)], fill=(255,0,0), width=line_width)
			back_draw.line([(x_pos,0), (x_pos, printsheet_height_px)], fill=(255,0,0), width=line_width)
			x_pos = (1/2+i_guide) * printsheet_width_px / n_horizontal + card_width_px /2
			front_draw.line([(x_pos,0), (x_pos, printsheet_height_px)], fill=(255,0,0), width=line_width)
			back_draw.line([(x_pos,0), (x_pos, printsheet_height_px)], fill=(255,0,0), width=line_width)

		for i_horizontal in range(n_horizontal):
			for i_vertical in range(n_vertical):
				if(not im_list):
					break
				x_pos = int((1/2+i_horizontal) * printsheet_width_px / n_horizontal - total_card_width_px /2)
				y_pos = int((1/2+i_vertical) * printsheet_height_px / n_vertical - total_card_height_px /2)
				front.paste(im_list.pop(), (x_pos,y_pos))
				x_pos = int((n_horizontal - 1/2 - i_horizontal) * printsheet_width_px / n_horizontal - total_card_width_px /2)
				back.paste(im_list.pop(), (x_pos,y_pos))
		layout_list.append(front.convert('RGB'))
		layout_list.append(back.convert('RGB'))
	return layout_list



if __name__ == "__main__":
	with open('config.json','r') as config_file:
		config = json.load(config_file)

	im_list = load_files('input')
	layout_list = create_layouts(im_list, config)	
	layout_list[0].save("./output/cards.pdf","PDF", resolution=100.0, save_all=True, append_images=layout_list[1:])

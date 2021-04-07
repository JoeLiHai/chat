
# 讀取檔案，把對話存成清單
def read_file(input_name):
	dialogues = []	
	with open(input_name, 'r', encoding='utf-8-sig') as file:
		for dialogue in file:
			dialogues.append(dialogue.strip())
	return dialogues

# 轉換格式
def convert(dialogues):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	for dialogue in dialogues:
		s = dialogue.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			else:
				for msg in s[2:]:
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			else:
				for msg in s[2:]:
					viki_word_count += len(msg)
	print(f'Allen說了{allen_word_count}個字，傳了{allen_sticker_count}個貼圖')
	print(f'Viki說了:{viki_word_count}個字，傳了{viki_sticker_count}個貼圖')
		#print(s)

# 儲存檔案
def write_file(output_name, news):
	with open(output_name, 'w', encoding='utf-8-sig') as file:
		for new in news:
			file.write(new + '\n')

# 主程式
def main(input_name, output_name):
	dialogues = read_file(input_name)
	news = convert(dialogues)
	#write_file(output_name, news)

main('LINE-Viki.txt', 'output.txt')
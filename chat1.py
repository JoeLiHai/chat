
# 讀取檔案，把對話存成清單
def read_file(input_name):
	dialogues = []	
	with open(input_name, 'r', encoding='utf-8-sig') as file:
		for dialogue in file:
			dialogues.append(dialogue.strip())
	return dialogues

# 轉換格式
def convert(dialogues):
	news = []
	person = None
	for dialogue in dialogues:
		if dialogue == 'Allen':
			person = 'Allen'
			continue
		elif dialogue == 'Tom':
			person = 'Tom'
			continue
		if person:
			news.append(person + ': ' + dialogue)
	return(news)

# 儲存檔案
def write_file(output_name, news):
	with open(output_name, 'w', encoding='utf-8-sig') as file:
		for new in news:
			file.write(new + '\n')

# 主程式
def main(input_name, output_name):
	dialogues = read_file(input_name)
	news = convert(dialogues)
	write_file(output_name, news)

main('input.txt', 'output.txt')
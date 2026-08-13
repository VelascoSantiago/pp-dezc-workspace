from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f'Files in {current_dir}:')

for filepath in current_dir.iterdir():
	if '.txt' not in filepath.name:
		continue

	print(f' - {filepath.name}')

	if filepath.is_file():
		content = filepath.read_text(encoding='utf-8')
		if not len(content):
			filepath.write_text(f"Hi! My name is {filepath.name}")
		print(f'{filepath.name} now has available content!')



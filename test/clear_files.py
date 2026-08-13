from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f'Files in {current_dir}:')

for filepath in current_dir.iterdir():
	if filepath.suffix != '.txt':
		continue

	print(f' - {filepath.name}')

	if filepath.is_file():
		filepath.write_text(f"")
		print(f'{filepath.name} has been cleared!')

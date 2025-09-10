# coding=utf-8
import os
import shutil
import json

commands_file = 'commands.txt'
suffix_name = '.json'
git_commands = [
	'git clone ',
	'git checkout ',
	'git pull',
	'git push origin HEAD:refs/for/',
	'git reset --hard HEAD~'
]

def parse_json(json_str):
	try:
		cmds = json.loads(json_str)
		labels = []
		commands = []
		for i in range(0, len(cmds['customer'])):
			labels.append(cmds['customer'][i]['name'])
			commands.append(cmds['customer'][i]['branch'])
		return labels, commands
	except json.JSONDecodeError:
		print('invalid json strings :\n%s' % json_str)

def main():
	base_path = os.getcwd()
	labels = []
	branchs = []
	for item in os.listdir(base_path):
		if item.endswith(suffix_name):
			with open(os.path.join(base_path, item), "r", encoding='utf-8') as customer_file:
				json_str = customer_file.read()
				labels, branchs = parse_json(json_str)
				print(labels, branchs)

	lines = []
	if os.path.exists(commands_file):
		with open(os.path.join(base_path, commands_file), "r", encoding='utf-8') as cmds_file:
			cmds_lines = cmds_file.readlines()
			for line in cmds_lines:
				line = line.strip()
				if len(lines) == 0:
					git_repo_path = line.split(' ')[2]
					git_repo_name = git_repo_path.split('/')[-1]
					if not os.path.exists(git_repo_name):
						print('it is not exist!')
						os.system(git_commands[0] + git_repo_path)
				lines.append(line)

		os.chdir(os.path.join(base_path, git_repo_name))
		for i in range(0, len(branchs)):
			os.system(git_commands[1] + branchs[i])
			os.system(git_commands[2])
			for line in lines:
				os.system(line)
			os.system(git_commands[3] + branchs[i])
			os.system(git_commands[4] + str(len(lines)))
			print('\033[1;31;47----- ' + labels[i] + ' done! -----\033[0m')
		print('\033[1;31;47m----- all done! -----\033[0m')
	else:
		pass

if __name__ == '__main__':
	main()

run: leetcode.py
	sed -i 's/List\[/list\[/g' main.py && python leetcode.py < input

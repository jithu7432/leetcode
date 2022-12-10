run: leetcode.py
	sed -i 's/List\[/list\[/g' template.py && python leetcode.py < input

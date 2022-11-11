run: leetcode.py
	sed -i 's/List\[/list\[/g' leetcode.py && python leetcode.py < input

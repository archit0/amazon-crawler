from crawler.amazon import amazon

keyword = '<INSERT YOUR KEYWORD>'

product_data = amazon.get_data(keyword)

file_name = "{}.json".format(keyword.replace(' ', '_').lower().strip())

import json
f = open(file_name, "w+")
f.write(json.dumps(product_data))
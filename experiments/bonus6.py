contents = ["Hello my name is Jair",
            "I am 25 years old",
            'When I was child I dream to become '
            'soccer player']
filenames = ['doc.txt','report.txt','presentation.txt']

for content, filename in zip(contents,filenames):
    file = open(f"../files/bonus6/{filename}",'w')
    file.write(content)
    file.close()

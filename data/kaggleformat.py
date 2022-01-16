import json
import csv
import sys
csv.field_size_limit(sys.maxsize)
labels = {'0': 'yes', '1': 'no'}
with open('RawKaggleData.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     rowcount = 0
     wordcount = 0
     with open('KaggleDataforGPT3-V1.json', 'w') as f:
        for row in reader:
            if rowcount > 17000:
                break
            if row['title'] != "":
                prompt = row['title'].split("-")[0]
                if prompt[-1] == " ":
                    prompt = prompt[:-1]
                print([prompt, labels[row['label']]])
                f.write(json.dumps({'prompt': prompt + "\nReliable: ", 'completion': labels[row['label']]}) + "\n")
                wordcount += len(row['title']) + len(row['label'])
                rowcount += 1
            
     with open('ValidateKaggleDataforGPT3-V1.json', 'w') as f:
        for row in reader:
            if rowcount < 17000:
                pass
            elif rowcount > 20000:
                break
            elif row['title'] != "":
                prompt = row['title'].split("-")[0]
                if prompt[-1] == " ":
                    prompt = prompt[:-1]
                print([prompt, labels[row['label']]])
                f.write(json.dumps({'prompt': prompt + "\nReliable: ", 'completion': labels[row['label']]}) + "\n")
                wordcount += len(row['title']) + len(row['label'])
                rowcount += 1
            
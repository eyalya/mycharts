from os import listdir, system, rename

# load all dashboard file
onlyfiles = listdir("charts/configmap/")

def EditName(filename):
    return filename.lower().replace("_","-").replace(" ", "").replace("(","").replace(")","") 

for filename in onlyfiles:
  if("json" in filename):
      oldName = "charts/configmap/" + filename
      newName = "charts/configmap/" + EditName(filename)
      rename(oldName, newName)


#config file structure
configFile = """apiVersion: v1
kind: ConfigMap
metadata:
  name: {{{{ .Release.Name }}}}-{0}
data:
  {1}: |-
{{{{ .Files.Get \"{1}\" | indent 4}}}}"""

def RemoveFileEnding(filename):
    return filename.split(sep=".")[0]

# create config maps files 
for filename in onlyfiles:
        if("json" in filename):
            path = "charts/configmap/templates/" + filename.split(sep=".")[0] + ".yaml"
            with open(path, 'w') as f:
                f.write(configFile.format(RemoveFileEnding(filename), filename))


#adding the files to value.yaml
valueFile = """
  - configMapName: grafana-{0}
    fileName: {1}"""

with open('values.yaml', 'r') as f:
    content = f.read()
    phrase = '#\ndashboardsConfigMaps'
    strlen = len(phrase)
    pos = content.index(phrase)
    pos += 2 + strlen
    
for filename in onlyfiles:
    if("json" in filename):
        value = valueFile.format(RemoveFileEnding(filename), filename)
        valueLen = len(value)
        content = content[:pos] + value + content[pos:]
        pos += valueLen

with open('values.yaml', 'w') as f:
        f.write(content)
    
    
                    

from lida.components import Manager
from llmx import TextGenerationConfig, llm
import pybase64
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from dotenv import load_dotenv

load_dotenv()

# Configuring LLM 
lida = Manager(text_gen=llm("openai", api_key='OPEN_API'))

#Summary generation
num_goals = 4
textgen_config = TextGenerationConfig(n=1, temperature=0.5, use_cache=True)
summary = lida.summarize("dataset.1.json", summary_method="default", textgen_config=textgen_config)

print(summary)

goals = lida.goals(summary, n=num_goals, textgen_config=textgen_config)
print(len(goals))
for goal in goals:
    print(goal)

library="plotly"
textgen_config = TextGenerationConfig(n=num_goals, temperature=0.2, use_cache=True)
print(".............................................\n")

for ch in range(0,num_goals):
    charts, chart = lida.visualize(summary=summary, goal=goals[ch], textgen_config=textgen_config, library=library)
    # print("chhhhhhh",type(chart))
    print("Visualized.................................\n")
    img_base64_string = charts[ch].raster
    #decode base64 string data
    decoded_data=pybase64.b64decode((img_base64_string))
    #write the decoded data back to original format in file
    im = 'image'+str(ch)+'.jpeg'
    img_file = open(im, 'wb')
    img_file.write(decoded_data)
    img_file.close()


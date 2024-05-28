# enhancer.py

import contextlib
 
import gradio as gr
from modules import scripts

from PIL import Image, ImageEnhance

def enhance_image(input_image_path, output_image_path, enhancement_factor):
    image = Image.open(input_image_path)
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(enhancement_factor)
    enhanced_image.save(output_image_path)

def send_text_to_prompt(new_text,old_text):
   
    if old_text =="":
         return new_text
    
    print(old_text+","+new_text)
    return old_text+","+new_text

class reminderPlugin(scripts.Script):
    def __init__(self) -> None:
        super().__init__()
 
    def title(self):
        return "test-project"
 
    def show(self,is_img2img):
        return scripts.AlwaysVisible
 
    def ui(self,is_img2img):
        with gr.Group():
            with gr.Accordion("测试插件",open=False):
                send_text_button = gr.Button(value="发送文本",variant='primary')
                text_to_be_sent = gr.Textbox(label="文本内容")
                types_to_sent = gr.Dropdown(["cat", "dog", "bird"], label="Animal", info="Will add more animals later!")
 
        with contextlib.suppress(AttributeError):
            if is_img2img:
                #根据当前的Tab来设置点击后数据输出的组件
                send_text_button.click(fn=send_text_to_prompt,inputs=[text_to_be_sent,send_text_button])
            else:
                #根据当前的Tab来设置点击后数据输出的组件
                send_text_button.click(fn=send_text_to_prompt,inputs=[text_to_be_sent,send_text_button])
        return [text_to_be_sent,send_text_button,types_to_sent]
 
 
def after_component(self,component,**kwargs):
    if kwargs.get("elem_id")=="txt2img_prompt":
        self.boxx = component
    if kwargs.get("elem_id")=="img2img_prompt":
        self.boxxIMG = component
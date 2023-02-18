
import pandas as pd
import ast
import os
import gradio as gr


class airpods(object):
  
def __init__(
    self, master, input_model, input_charging_case_serial, input_box_serial_number,
    input_leftbud_model, input_rightbud_model, input_leftbud_serial, input_rightbud_serial, input_firmware
):
    '''
    '''
    self.master = master
    self.input_model = input_model
    self.input_charging_case_serial = input_charging_case_serial
    self.input_box_serial_number = input_box_serial_number
    self.input_leftbud_model = input_leftbud_model
    self.input_rightbud_model = input_rightbud_model
    self.input_leftbud_serial = input_leftbud_serial
    self.input_rightbud_serial = input_rightbud_serial
    self.input_firmware = input_firmware


def Iterative_Serial_Check(self):
    '''
    Function checks if the airbuds serial numbers are iterative
    '''
    string =  self.input_leftbud_serial[-1] + self.input_rightbud_serial[-1] + self.input_charging_case_serial[-1]
    string = string.lower()
    return not any(m > n for m, n in zip(string, string[1:]))

def check_latest_firmware(self):
    '''
    Function to check if the airbuds are on the latest firmware
    '''
    return self.master[self.input_model]['firmware'] == self.input_firmware

def check_matching_serial(self):
    '''
    Function to check if the airbuds are having the
    same serial number as that of the case
    '''
    return self.input_charging_case_serial == self.input_box_serial_number


def check_model_number(self):
    '''
    Function to check if the airbuds are having the
    same serial number as that of the case
    '''
    return (
        self.input_leftbud_model in self.master[self.input_model]['Model_number']
        and self.input_rightbud_model in self.master[self.input_model]['Model_number']
    )

def final_check(self):

    if self.Iterative_Serial_Check() and self.check_latest_firmware() and self.check_matching_serial() and self.check_model_number():
        return 'Congratulations, Your Earpods/ Headphones are Genuine'
    elif self.check_latest_firmware() and self.check_matching_serial() and self.check_model_number():
        return 'Looks like Earpods/ Headphones are mostly Genuine, but Case has been swapped'
    else:
        return 'Extremely sorry, Your Earpods/ Headphones are Probably Knock off'


def app_check(input_model,input_charging_case_serial,input_box_serial_number,input_leftbud_model,input_rightbud_model,input_leftbud_serial,input_rightbud_serial,input_firmware):
  input_dict = master#ast.literal_eval(os.environ.get('master'))
  

  if  (all(i >= 10 for i in valu) and any(i < 15 for i in valu))  :
    airpod = airpods(input_dict,input_model,input_charging_case_serial,input_box_serial_number,input_leftbud_model,input_rightbud_model,input_leftbud_serial,input_rightbud_serial,input_firmware)
    return airpod.final_check()
  else:
    return 'the serial numbers are not correct, please check and re enter'

gr.Interface(fn=app_check, 
             inputs=[
        gr.inputs.Dropdown(['AirPods_Pro2', 'AirPods_3', 'AirPods_Max', 'AirPods_Pro', 'AirPods_2', 'AirPods_1']),
        gr.inputs.Textbox(
                placeholder="Please enter the CharginCase serial number", label="CharginCase serial number", lines=1,), 
        gr.inputs.Textbox(
                placeholder="Please enter the Box serial number", label="Box serial number", lines=1),
        gr.inputs.Textbox(
                placeholder="Please enter the left bud model number A2083", label="Left bud model number", lines=1),
        gr.inputs.Textbox(
                placeholder="Please enter the right bud number A2083", label="Right bud number", lines=1),
        gr.inputs.Textbox(
                placeholder="Please enter the left bud serial number", label="Left bud serial number", lines=1),
                
        gr.inputs.Textbox(
                placeholder="Please enter the right bud number", label="Right bud number", lines=1),
        gr.inputs.Textbox(
                placeholder="Please enter the Firmware", label="Firmware", lines=1)
                ],
             outputs= [gr.outputs.Textbox(label="Output Box")],
             examples=[]).launch(debug= True)





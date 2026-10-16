# Normal Distribution Calculator
# Copyright (c) 2026 Saran Kumar
# Licensed under the MIT License. See LICENSE file in the project root.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg 
import matplotlib.ticker as ticker
import matplotlib.patheffects as pe
import tkinter as tk
from tkinter import (messagebox,ttk,Button)
from scipy.stats import norm

def nd():
    mean = 0
    sd= 1
    x=np.linspace(mean-4.5*sd,mean+4.5*sd,1000)
    y=0.01 + norm(loc=mean,scale=sd).pdf(x)
    ztext_objects = []
    zline_object = None
    ztext_objects2 = []
    zline_object2 = None
    x_Ztext_objects = []
    x_Xtext_objects = []
    Xtext_objects = []
    Xline_object = None
    Xtext_objects2 = []
    Xline_object2 = None


    app = tk.Tk()
    app.title('NORMAL DISTRIBUTION')
    app.geometry("1000x1000")

    fig, ax = plt.subplots()

    option=["P(Z>a)","P(|Z|>a)","P(Z<a)","P(|Z|<a)","P(a<Z<b)","P(X>a)","P(|X|>a)","P(X<a)","P(|X|<a)","P(a<X<b)"]

    menu_label=tk.Label(app,text='Choose Format')
    menu_label.pack(anchor=tk.CENTER,padx=0)
    menu = tk.StringVar(app) 
    drop_menu = tk.OptionMenu(app, menu, *option) 
    drop_menu.pack(anchor="center",padx=0) 
    menu.set("Format")

    info = tk.Frame(app)
    info.pack(anchor=tk.CENTER)
    frame = tk.Frame(app)
    frame.pack(anchor=tk.CENTER)
    answer_label = tk.Label(app, text="")
    answer_label.pack(anchor=tk.CENTER, padx=10) 

    def input():
        nonlocal x_Ztext_objects,x_Xtext_objects, zline_object, zline_object2, ztext_objects, ztext_objects2, Xline_object, Xline_object2, Xtext_objects, Xtext_objects2
        for widget in frame.winfo_children(): 
            widget.pack_forget()
        for widget in info.winfo_children(): 
            widget.pack_forget()
        for widget in plot.winfo_children(): 
            widget.pack_forget()  
        graph()
        for text_object in ztext_objects:
                text_object.remove()
        ztext_objects.clear()
        for ztext_object2 in ztext_objects2:
                ztext_object2.remove()
        ztext_objects2.clear()
        if zline_object is not None:
                zline_object.remove()
        zline_object = None
        if zline_object2 is not None:
                zline_object2.remove()
        zline_object2 = None 
        for Xtext_object in Xtext_objects:
            Xtext_object.remove()
        Xtext_objects.clear()
        if Xline_object is not None:
            Xline_object.remove()
        Xline_object = None
        for Xtext_object2 in Xtext_objects2:
            Xtext_object2.remove()
        Xtext_objects2.clear()
        if Xline_object2 is not None:
            Xline_object2.remove()
        Xline_object2 = None
        for x_Ztext_object in x_Ztext_objects:
            x_Ztext_object.remove()
        x_Ztext_objects.clear()
        for x_Xtext_object in x_Xtext_objects:
            x_Xtext_object.remove()
        x_Xtext_objects.clear()   
        plt.fill_between(x,y, color ="white")
        if "X" in menu.get():
            ax.set(xlabel='X',title='Normal Distribution Graph')
            mean_label = tk.Label(info, text="What is the Mean")
            mean_label.pack(anchor=tk.CENTER, padx=55)
            mean_in = tk.Entry(info)
            mean_in.pack(anchor=tk.CENTER, padx=10)
            sd_label = tk.Label(info, text="What is the Standard Deviatian ")
            sd_label.pack(anchor=tk.CENTER, padx=55)
            sd_in = tk.Entry(info)
            sd_in.pack(anchor=tk.CENTER, padx=10)
            x_text = ax.text(0, -0.01, "",horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
        else :
            mean = 0
            sd = 1
            ax.set(xlabel='Z',title='Standard Normal Distribution Graph')
            x_text = ax.text(mean, -0.015, mean,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
        x_Ztext_objects.append(x_text)
        a_label = tk.Label(frame, text='Enter "a" value for ' + menu.get())
        a_label.pack(anchor=tk.CENTER, padx=55)
        a = tk.Entry(frame)
        a.pack(anchor=tk.CENTER, padx=10)
        if "b" in menu.get():
            b_label = tk.Label(frame, text='Enter "b" value for ' + menu.get())
            b_label.pack(anchor=tk.CENTER, padx=55)
            b = tk.Entry(frame)
            b.pack(anchor=tk.CENTER, padx=10)
        fig.canvas.draw()
        def solve():
            a_value = float(a.get())
            nonlocal x_Ztext_objects,x_Xtext_objects, zline_object, zline_object2, ztext_objects, ztext_objects2, Xline_object, Xline_object2, Xtext_objects, Xtext_objects2
            plt.fill_between(x,y, color ="white")
            chosen_option = menu.get()
            if "Z" in chosen_option:
                for text_object in ztext_objects:
                    text_object.remove()
                ztext_objects.clear()
                for ztext_object2 in ztext_objects2:
                    ztext_object2.remove()
                ztext_objects2.clear()
                if zline_object is not None:
                    zline_object.remove()
                zline_object = None
                if zline_object2 is not None:
                    zline_object2.remove()
                zline_object2 = None
                if chosen_option == "P(Z>a)":
                    try:
                        if a_value >= 0: 
                            answer = 1 - norm.cdf(a_value)  
                            answer_text = f"P(Z>{a_value}) = {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text) 
                        else:
                            answer = 1 - norm.cdf(a_value)  
                            answer_text = f" P(Z>{a_value}) \n= P(Z<{-a_value}) \n= 1 - P(Z>{-a_value})\n= 1 - {(norm.cdf(a_value)):.4f} \n= {answer:.4f}" 
                            answer_label.config(justify="left" , text=answer_text)
                        plt.fill_between(x,y,where= x>=a_value, color ="c")
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(|Z|>a)":
                    try:
                        if a_value >= 0: 
                            answer = 2*(1-norm.cdf(a_value))  
                            answer_text = f"P(|Z|>{a_value}) \n= P(Z>{a_value}) + P(Z<{-a_value}) \n= 2P(Z>{a_value})\n= 2({((1-norm.cdf(a_value))):.4f})\n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= (x>=a_value), color ="c") 
                            plt.fill_between(x,y,where= (x<=-a_value), color ="c")   
                        else:
                            answer = 1- 2*(norm.cdf(a_value))  
                            answer_text = f"P(|Z|>{a_value}) \n= P(|Z|<{-a_value}) \n= P({a_value}<Z<{-a_value}) \n= 1 - 2P(Z>{-a_value}) \n= 1 - 2({(norm.cdf(a_value)):.4f}) \n= 1-{(2*norm.cdf(a_value)):.4f} \n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= ((x>=a_value) & (x<=-a_value )), color ="c")
                        zline_object2 = ax.axvline(-a_value, ls="--", c="g")
                        new_text2 = ax.text(-a_value, 0.055, -a_value,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        ztext_objects2.append(new_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(Z<a)":
                    try:
                        if a_value >= 0:  
                            answer = norm.cdf(a_value)  
                            answer_text = f"P(Z<{a_value}) \n= 1 - P(Z>{a_value}) \n= 1 - {1-answer:.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text)   
                        else:
                            answer = norm.cdf(a_value)  
                            answer_text = f"P(Z<{a_value}) \n= P(Z>{-a_value}) \n= {answer:.4f}" 
                            answer_label.config(justify="left" , text=answer_text)
                        plt.fill_between(x,y,where= (x<=a_value), color ="c") 
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(|Z|<a)":
                    try:
                        if a_value >= 0: 
                            answer = 1- 2*(1-norm.cdf(a_value))  
                            answer_text = f"P(|Z|<{a_value})\n= P({-a_value}<Z<{a_value}) \n= 1 - 2P(Z>{a_value}) \n= 1 - 2({(1-norm.cdf(a_value)):.4f}) \n= 1 - {(2*(1-norm.cdf(a_value))):.4f} \n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= ((x<=a_value) & (x>=-a_value )), color ="c") 
                        else:
                            answer = 2*(norm.cdf(a_value))  
                            answer_text = f"P(|Z|<{a_value}) \n= P(|Z|>{-a_value}) \n= P(Z>{-a_value}) + P(Z<{a_value}) \n= 2P(Z>{-a_value})\n= 2({((1-norm.cdf(-a_value))):.4f})\n= {answer:.4f}"
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= (x<=a_value), color ="c")
                            plt.fill_between(x,y,where= (x>=-a_value), color ="c")
                        zline_object2 = ax.axvline(-a_value, ls="--", c="g")
                        new_text2 = ax.text(-a_value, 0.055, -a_value,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        ztext_objects2.append(new_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(a<Z<b)":
                    try:
                        b_value = float(b.get())
                        if a_value >= 0 and b_value >=0 :  
                            answer = (1- norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_value}<Z<{b_value}) \n= P(Z>{a_value}) - P(Z>{b_value}) \n= {(1- norm.cdf(a_value)):.4f} - {(1-norm.cdf(b_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text) 
                        elif a_value <=0 and b_value <= 0 :
                            answer = (1- norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_value}<Z<{b_value}) \n= P({-b_value}<Z<{-a_value}) \n= P(Z>{-b_value}) - P(Z>{-a_value}) \n= {(1- norm.cdf(-b_value)):.4f} - {(1-norm.cdf(-a_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text)
                        else :  
                            answer = 1 - (norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_value}<Z<{b_value}) \n= 1 - P(Z<{a_value}) - P(Z>{b_value}) \n= 1 - P(Z>{-1*a_value}) - P(Z>{b_value}) \n= 1 - {( norm.cdf(a_value)):.4f} - {(1-norm.cdf(b_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text) 
                        plt.fill_between(x,y,where= ((x<=b_value) & (x>=a_value )), color ="c") 
                        zline_object2 = ax.axvline(b_value, ls="--", c="g")    
                        new_text2 = ax.text(b_value, 0.055, b_value,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        ztext_objects2.append(new_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for")
                zline_object = ax.axvline(a_value, ls="--", c="g")
                new_text = ax.text(a_value, 0.03, a_value,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                ztext_objects.append(new_text)
            if "X" in chosen_option:
                for Xtext_object in Xtext_objects:
                    Xtext_object.remove()
                Xtext_objects.clear()
                if Xline_object is not None:
                    Xline_object.remove()
                Xline_object = None
                for Xtext_object2 in Xtext_objects2:
                    Xtext_object2.remove()
                Xtext_objects2.clear()
                if Xline_object2 is not None:
                    Xline_object2.remove()
                Xline_object2 = None
                for x_Xtext_object in x_Xtext_objects:
                    x_Xtext_object.remove()
                x_Xtext_objects.clear()
                a_ori = a_value
                try:
                    mean_value = float(mean_in.get())  
                    sd_value = float(sd_in.get())      
                    mean = mean_value 
                    sd = sd_value 
                except ValueError:
                    answer_label.config(text="Error: Invalid input for 'mean' or 'sd'")
                a_value =round((a_value-mean)/sd,2) 
                if chosen_option == "P(X>a)":
                    try:
                        if a_value >= 0: 
                            answer = 1 - norm.cdf(a_value)  
                            answer_text = f"P(X>{a_ori}) \n= P(Z>(({a_ori}-{mean})/{sd})) \n= P(Z>{a_value}) \n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text) 
                        else:
                            answer = 1 - norm.cdf(a_value)  
                            answer_text = f"P(X>{a_ori}) \n= P(Z>(({a_ori}-{mean})/{sd})) \n=P(Z>{a_value}) \n= P(Z<{-a_value}) \n= 1 - P(Z>{-a_value})\n= 1 - {(norm.cdf(a_value)):.4f} \n= {answer:.4f}" 
                            answer_label.config(justify="left" , text=answer_text)
                        plt.fill_between(x,y,where= x>=(a_value), color ="c")
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(|X|>a)":
                    try:
                        if a_value >= 0: 
                            answer = 2*(1-norm.cdf(a_value))  
                            answer_text = f"P(|X|>{a_ori}) \n= P(|Z|>(({a_ori}-{mean})/{sd})) \n= P(|Z|>{a_value}) \n= P(Z>{a_value}) + P(Z<{-a_value}) \n= 2P(Z>{a_value})\n= 2({((1-norm.cdf(a_value))):.4f})\n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= (x>=a_value), color ="c") 
                            plt.fill_between(x,y,where= (x<=-a_value), color ="c")   
                        else:
                            answer = 1- 2*(norm.cdf(a_value))  
                            answer_text = f"P(|X|>{a_ori}) \n= P(|Z|>(({a_ori}-{mean})/{sd})) \n= P(|Z|>{a_value}) \n= P(|Z|<{-a_value}) \n= P({a_value}<Z<{-a_value}) \n= 1 - 2P(Z>{-a_value}) \n= 1 - 2({(norm.cdf(a_value)):.4f}) \n= 1-{(2*norm.cdf(a_value)):.4f} \n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= ((x>=a_value) & (x<=-a_value )), color ="c")
                        Xline_object2 = ax.axvline(-a_value, ls="--", c="g")
                        Xnew_text2 = ax.text(-a_value, 0.08, -a_ori,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        Xtext_objects2.append(Xnew_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(X<a)":
                    try:
                        if a_value >= 0:  
                            answer = norm.cdf(a_value)  
                            answer_text = f"P(X<{a_ori}) \n= P(Z<(({a_ori}-{mean})/{sd}))\n= P(Z<{a_value})\n= 1 - P(Z>{a_value}) \n= 1 - {1-answer:.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text)   
                        else:
                            answer = norm.cdf(a_value)  
                            answer_text = f"P(X<{a_ori}) \n= P(Z<(({a_ori}-{mean})/{sd})) \n= P(Z<{a_value}) \n= P(Z>{-a_value}) \n= {answer:.4f}" 
                            answer_label.config(justify="left" , text=answer_text)
                        plt.fill_between(x,y,where= (x<=a_value), color ="c") 
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(|X|<a)":
                    try:
                        if a_value >= 0: 
                            answer = 1- 2*(1-norm.cdf(a_value))  
                            answer_text = f"P(|X|<{a_ori}) \n= P(|Z|<(({a_ori}-{mean})/{sd})) \n= P(|Z|<{a_value})\n= P({-a_value}<Z<{a_value}) \n= 1 - 2P(Z>{a_value}) \n= 1 - 2({(1-norm.cdf(a_value)):.4f}) \n= 1 - {(2*(1-norm.cdf(a_value))):.4f} \n= {answer:.4f}"  
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= ((x<=a_value) & (x>=-a_value )), color ="c") 
                        else:
                            answer = 2*(norm.cdf(a_value))  
                            answer_text = f"P|(X|<{a_ori}) \n= P(|Z|<(({a_ori}-{mean})/{sd})) \n= P(|Z|<{a_value}) \n= P(|Z|>{-a_value}) \n= P(Z>{-a_value}) + P(Z<{a_value}) \n= 2P(Z>{-a_value})\n= 2({((1-norm.cdf(-a_value))):.4f})\n= {answer:.4f}"
                            answer_label.config(justify="left",text=answer_text)
                            plt.fill_between(x,y,where= (x<=a_value), color ="c")
                            plt.fill_between(x,y,where= (x>=-a_value), color ="c")
                        Xline_object2 = ax.axvline(-a_value, ls="--", c="g")
                        Xnew_text2 = ax.text(-a_value, 0.08, -a_ori,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        Xtext_objects2.append(Xnew_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for 'a'")
                elif chosen_option == "P(a<X<b)":
                    try:
                        b_value = float(b.get())
                        b_ori = b_value
                        b_value = round((b_value-mean)/sd,2)
                        if a_value >= 0 and b_value >=0 :  
                            answer = (1- norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_ori}<X<{b_ori})\n= P((({a_ori}-{mean})/{sd})<Z<(({b_ori}-{mean}))/{sd}) \n= P({a_value}<Z<{b_value}) \n= P(Z>{a_value}) - P(Z>{b_value}) \n= {(1- norm.cdf(a_value)):.4f} - {(1-norm.cdf(b_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text) 
                        elif a_value <=0 and b_value <= 0 :
                            answer = (1- norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_ori}<X<{b_ori})\n= P((({a_ori}-{mean})/{sd})<Z<(({b_ori}-{mean})/{sd})) \n= P({a_value}<Z<{b_value}) \n= P({-b_value}<Z<{-a_value}) \n= P(Z>{-b_value}) - P(Z>{-a_value}) \n= {(1- norm.cdf(-b_value)):.4f} - {(1-norm.cdf(-a_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text)
                        else :  
                            answer = 1 - (norm.cdf(a_value))-(1 - norm.cdf(b_value)) 
                            answer_text = f"P({a_ori}<X<{b_ori})\n= P((({a_ori}-{mean})/{sd})<Z<(({b_ori}-{mean}))/{sd}) \n= P({a_value}<Z<{b_value}) \n= 1 - P(Z<{a_value}) - P(Z>{b_value}) \n= 1 - P(Z>{-1*a_value}) - P(Z>{b_value}) \n= 1 - {( norm.cdf(a_value)):.4f} - {(1-norm.cdf(b_value)):.4f}\n= {answer:.4f}"  
                            answer_label.config(justify="left", text=answer_text)
                        plt.fill_between(x,y,where= ((x<=b_value) & (x>=a_value )), color ="c") 
                        Xline_object2 = ax.axvline(b_value, ls="--", c="g")    
                        Xnew_text2 = ax.text(b_value, 0.08, b_ori,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                        Xtext_objects2.append(Xnew_text2)
                    except ValueError:  
                        answer_label.config(text="Error: Invalid input for")
                x_Xtext = ax.text(0, -0.015, mean ,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                x_Xtext_objects.append(x_Xtext)
                Xline_object = ax.axvline(a_value, ls="--", c="g")
                Xnew_text = ax.text(a_value , 0.035, a_ori ,horizontalalignment='center',verticalalignment='top',path_effects=[pe.withStroke(linewidth=2, foreground="white")])
                Xtext_objects.append(Xnew_text)
            fig.canvas.draw() 
        
        solve_button = Button(frame, text="Solve", command=solve).pack()
    confirm_button = Button(app, text="Confirm Format", command=input).pack(anchor="center")

    plot = tk.Frame(app)
    plot.pack(anchor=tk.CENTER)

    def graph():  
        ax.xaxis.set_major_locator(ticker.NullLocator())
        ax.yaxis.set_major_locator(ticker.NullLocator())
        ax.plot(x, y, c="blue")
        ax.xaxis.set_label_coords(mean,-0.07)
        ax.axvline(mean, ls="-", c="black")
        ax.axhline(0, ls="-", c="black")
        canvas = FigureCanvasTkAgg(fig, master=plot)
        canvas.get_tk_widget().pack(padx=10,pady=10,side=tk.TOP, fill=tk.BOTH, expand=True)
        canvas.draw() 
    graph()
    app.mainloop()
    
nd()
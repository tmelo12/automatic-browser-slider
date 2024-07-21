import time
import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import messagebox

class BrowserAutomator:
    def __init__(self, urls):
        self.urls = urls
        self.driver = None

    def start_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(options=chrome_options)
        
        self.driver.get(self.urls[0]['url'])
        
        for url in self.urls[1:]:
            # self.driver.execute_script("window.open('{}');".format(url))
            self.driver.execute_script("window.open('{}');".format(url['url']))
            
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.cycle_tabs()

    def cycle_tabs(self):
        while True:
            for data, handle in zip(self.urls, self.driver.window_handles):
                self.driver.switch_to.window(handle)
                if data['login']:
                    self.perform_login(data['url'], data['params_login'])
                time.sleep(data['time'])
                
    def perform_login(self, url, login_data):
        if 'google' in url:
            self.login_google(login_data)
            
    def login_google(self, login_data):
        email_field = self.driver.find_element_by_id("identifierId")
        email_field.send_keys('')
        email_field.send_keys(login_data['username'])
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys('')
        password_field.send_keys(login_data['password'])
        password_field.send_keys(Keys.RETURN)
        time.sleep(2)
        
    

class Application(tk.Tk):
    def __init__(self, automator):
        super().__init__()
        self.automator = automator
        self.title("Navegador Automático")
        self.geometry("400x300")

        self.url_label = tk.Label(self, text="Nova URL:")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(self)
        self.url_entry.pack(pady=5)

        self.time_label = tk.Label(self, text="Tempo de espera (segundos):")
        self.time_label.pack(pady=5)

        self.time_entry = tk.Entry(self)
        self.time_entry.pack(pady=5)

        self.login_label = tk.Label(self, text="Login (username:password):")
        self.login_label.pack(pady=5)

        self.login_entry = tk.Entry(self)
        self.login_entry.pack(pady=5)

        self.add_url_button = tk.Button(self, text="Adicionar URL", command=self.add_url)
        self.add_url_button.pack(pady=5)

        self.start_button = tk.Button(self, text="Iniciar", command=self.start_automation)
        self.start_button.pack(pady=20)

    def add_url(self):
        new_url = self.url_entry.get()
        new_time = int(self.time_entry.get())
        new_login = self.login_entry.get()
        if new_url and new_time:
            login_data = None
            if new_login:
                username, password = new_login.split(':')
                login_data = {'username': username, 'password': password}
            self.automator.url_data.append({'url': new_url, 'time': new_time, 'login': login_data})
            self.url_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.login_entry.delete(0, tk.END)
            messagebox.showinfo("Info", f"URL adicionada: {new_url}")

    def start_automation(self):
        self.destroy()
        threading.Thread(target=self.automator.start_browser).start()

if __name__ == "__main__":
    urls_padrao = [
        {'url': "http://www.google.com", 'time': 15, 'login': False, 'params_login': {'login': '', 'password': ''}},
        {'url': "http://www.facebook.com", 'time': 15, 'login': False, 'params_login': {'login': '', 'password': ''}},
        {'url': "http://www.instagram.com", 'time': 15, 'login': False, 'params_login': {'login': '', 'password': ''}}
    ]
    automator = BrowserAutomator(urls_padrao)
    app = Application(automator)
    app.mainloop()
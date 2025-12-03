import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import subprocess
import time
import threading
import psutil
import sys
import winreg as reg
import locale

class AutoStartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Start Scheduler")
        self.root.geometry("900x650")
        self.root.minsize(900, 650)
        self.root.resizable(True, True)
        self.config_file = "config.json"
        self.apps = []
        self.is_running = False
        self.startup_mode = "--startup" in sys.argv
        self.detect_language()
        self.load_translations()
        self.load_config()
        self.create_gui()
        if self.startup_mode:
            self.root.after(1000, self.start_autostart)
    
    def detect_language(self):
        try:
            try:
                system_locale = locale.getlocale()[0]
            except:
                system_locale = locale.getdefaultlocale()[0]
            
            if system_locale and system_locale.startswith('id'):
                self.language = 'id'
            else:
                self.language = 'en'
        except:
            self.language = 'en'
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    saved_lang = config.get('language')
                    if saved_lang in ['en', 'id']:
                        self.language = saved_lang
            except:
                pass
    
    def load_translations(self):
        self.translations = {
            'en': {
                'title': 'Start Scheduler',
                'add_app': '➕ Add Application',
                'delete': '🗑️ Delete',
                'move_up': '⬆️ Up',
                'move_down': '⬇️ Down',
                'settings': 'Settings',
                'delay_label': 'Delay between apps (seconds):',
                'check_label': 'App check interval (seconds):',
                'save_settings': '💾 Save Settings',
                'app_list': 'Application List (Execution Order)',
                'col_no': 'No',
                'col_name': 'Name',
                'col_path': 'Path',
                'col_status': 'Status',
                'start_autostart': '▶️ Start AutoStart',
                'register_startup': '⚙️ Register to Windows Startup',
                'unregister_startup': '❌ Remove from Windows Startup',
                'ready': 'Ready',
                'warning': 'Warning',
                'select_app_delete': 'Select an application to delete',
                'select_app_move': 'Select an application to move',
                'info': 'Info',
                'settings_saved': 'Settings saved successfully!',
                'already_running': 'AutoStart is already running!',
                'no_apps': 'No applications to run!',
                'starting': 'Starting AutoStart...',
                'running_app': 'Running: ',
                'app_running': ' is running',
                'waiting': 'Waiting {} seconds...',
                'completed': 'AutoStart completed - All applications have been launched',
                'error_running': 'Error running ',
                'added': 'Added: ',
                'deleted': 'Deleted: ',
                'status_waiting': 'Waiting',
                'status_running': 'Running...',
                'status_started': 'Started ✓',
                'status_error': 'Error ✗',
                'status_done': 'Running ✓',
                'select_exe': 'Select Executable File',
                'success': 'Success',
                'register_success': 'Application successfully registered to Windows Startup!',
                'registered': 'Registered to Windows Startup',
                'unregister_success': 'Application successfully removed from Windows Startup!',
                'unregistered': 'Removed from Windows Startup',
                'not_registered': 'Application is not registered in Windows Startup',
                'error': 'Error',
                'register_failed': 'Failed to register to startup: ',
                'unregister_failed': 'Failed to remove from startup: ',
                'settings_saved_status': 'Settings saved',
                'language': 'Language:',
                'english': 'English',
                'indonesian': 'Indonesian'
            },
            'id': {
                'title': 'Start Scheduler',
                'add_app': '➕ Tambah Aplikasi',
                'delete': '🗑️ Hapus',
                'move_up': '⬆️ Naik',
                'move_down': '⬇️ Turun',
                'settings': 'Pengaturan',
                'delay_label': 'Delay antar aplikasi (detik):',
                'check_label': 'Interval cek aplikasi (detik):',
                'save_settings': '💾 Simpan Pengaturan',
                'app_list': 'Daftar Aplikasi (Urutan Eksekusi)',
                'col_no': 'No',
                'col_name': 'Nama',
                'col_path': 'Path',
                'col_status': 'Status',
                'start_autostart': '▶️ Mulai AutoStart',
                'register_startup': '⚙️ Daftarkan ke Windows Startup',
                'unregister_startup': '❌ Hapus dari Windows Startup',
                'ready': 'Siap',
                'warning': 'Peringatan',
                'select_app_delete': 'Pilih aplikasi yang ingin dihapus',
                'select_app_move': 'Pilih aplikasi yang ingin dipindahkan',
                'info': 'Info',
                'settings_saved': 'Pengaturan berhasil disimpan!',
                'already_running': 'AutoStart sudah berjalan!',
                'no_apps': 'Tidak ada aplikasi yang akan dijalankan!',
                'starting': 'Memulai AutoStart...',
                'running_app': 'Menjalankan: ',
                'app_running': ' telah berjalan',
                'waiting': 'Menunggu {} detik...',
                'completed': 'AutoStart selesai - Semua aplikasi telah dijalankan',
                'error_running': 'Error menjalankan ',
                'added': 'Ditambahkan: ',
                'deleted': 'Dihapus: ',
                'status_waiting': 'Menunggu',
                'status_running': 'Menjalankan...',
                'status_started': 'Dimulai ✓',
                'status_error': 'Error ✗',
                'status_done': 'Berjalan ✓',
                'select_exe': 'Pilih File Executable',
                'success': 'Sukses',
                'register_success': 'Aplikasi berhasil didaftarkan ke Windows Startup!',
                'registered': 'Terdaftar di Windows Startup',
                'unregister_success': 'Aplikasi berhasil dihapus dari Windows Startup!',
                'unregistered': 'Dihapus dari Windows Startup',
                'not_registered': 'Aplikasi tidak terdaftar di Windows Startup',
                'error': 'Error',
                'register_failed': 'Gagal mendaftarkan ke startup: ',
                'unregister_failed': 'Gagal menghapus dari startup: ',
                'settings_saved_status': 'Pengaturan disimpan',
                'language': 'Bahasa:',
                'english': 'English',
                'indonesian': 'Bahasa Indonesia'
            }
        }
    
    def t(self, key):
        return self.translations[self.language].get(key, key)
    
    def change_language(self, lang):
        self.language = lang
        config = {
            'apps': self.apps,
            'delay_between_apps': self.delay_between_apps,
            'check_interval': self.check_interval,
            'language': self.language
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)

        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_gui()
    
    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.apps = config.get('apps', [])
                self.delay_between_apps = config.get('delay_between_apps', 3)
                self.check_interval = config.get('check_interval', 2)
        else:
            self.apps = []
            self.delay_between_apps = 3
            self.check_interval = 2
    
    def save_config(self):
        config = {
            'apps': self.apps,
            'delay_between_apps': self.delay_between_apps,
            'check_interval': self.check_interval,
            'language': self.language
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
    
    def create_gui(self):
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        ttk.Label(top_frame, text=self.t('title'), font=("Arial", 16, "bold")).pack()

        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text=self.t('add_app'), command=self.add_app).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.t('delete'), command=self.remove_app).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.t('move_up'), command=self.move_up).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text=self.t('move_down'), command=self.move_down).pack(side=tk.LEFT, padx=5)

        settings_frame = ttk.LabelFrame(self.root, text=self.t('settings'), padding="10")
        settings_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(settings_frame, text=self.t('delay_label')).grid(row=0, column=0, sticky=tk.W)
        self.delay_var = tk.IntVar(value=self.delay_between_apps)
        ttk.Spinbox(settings_frame, from_=0, to=60, textvariable=self.delay_var, width=10).grid(row=0, column=1, padx=5)
        
        ttk.Label(settings_frame, text=self.t('check_label')).grid(row=0, column=2, sticky=tk.W, padx=(20,0))
        self.check_var = tk.IntVar(value=self.check_interval)
        ttk.Spinbox(settings_frame, from_=1, to=30, textvariable=self.check_var, width=10).grid(row=0, column=3, padx=5)

        ttk.Label(settings_frame, text=self.t('language')).grid(row=0, column=4, sticky=tk.W, padx=(20,0))
        self.lang_var = tk.StringVar(value=self.language)
        lang_combo = ttk.Combobox(settings_frame, textvariable=self.lang_var, width=12, state='readonly')
        lang_combo['values'] = (self.t('english'), self.t('indonesian'))
        lang_combo.current(0 if self.language == 'en' else 1)
        lang_combo.bind('<<ComboboxSelected>>', lambda e: self.change_language('en' if self.lang_var.get() == self.t('english') else 'id'))
        lang_combo.grid(row=0, column=5, padx=5)
        
        ttk.Button(settings_frame, text=self.t('save_settings'), command=self.save_settings).grid(row=0, column=6, padx=20)

        list_frame = ttk.LabelFrame(self.root, text=self.t('app_list'), padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ('No', 'Nama', 'Path', 'Status')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        self.tree.heading('No', text=self.t('col_no'))
        self.tree.heading('Nama', text=self.t('col_name'))
        self.tree.heading('Path', text=self.t('col_path'))
        self.tree.heading('Status', text=self.t('col_status'))
        
        self.tree.column('No', width=50, anchor=tk.CENTER)
        self.tree.column('Nama', width=180)
        self.tree.column('Path', width=480)
        self.tree.column('Status', width=120, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        bottom_frame = ttk.Frame(self.root, padding="10")
        bottom_frame.pack(fill=tk.X)
        
        self.start_button = ttk.Button(bottom_frame, text=self.t('start_autostart'), command=self.start_autostart)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(bottom_frame, text=self.t('register_startup'), command=self.register_to_startup).pack(side=tk.LEFT, padx=5)
        ttk.Button(bottom_frame, text=self.t('unregister_startup'), command=self.unregister_from_startup).pack(side=tk.LEFT, padx=5)

        self.status_label = ttk.Label(self.root, text=self.t('ready'), relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.refresh_list()
    
    def refresh_list(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, app in enumerate(self.apps):
            self.tree.insert('', tk.END, values=(
                i + 1,
                app.get('name', 'Unknown'),
                app.get('path', ''),
                app.get('status', self.t('status_waiting'))
            ))
    
    def add_app(self):
        file_path = filedialog.askopenfilename(
            title=self.t('select_exe'),
            filetypes=[("Executable Files", "*.exe"), ("All Files", "*.*")]
        )
        
        if file_path:
            app_name = os.path.splitext(os.path.basename(file_path))[0]
            self.apps.append({
                'name': app_name,
                'path': file_path,
                'status': self.t('status_waiting')
            })
            self.save_config()
            self.refresh_list()
            self.update_status(self.t('added') + app_name)
    
    def remove_app(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.t('warning'), self.t('select_app_delete'))
            return
        
        item = self.tree.item(selected[0])
        index = int(item['values'][0]) - 1
        
        app_name = self.apps[index]['name']
        del self.apps[index]
        self.save_config()
        self.refresh_list()
        self.update_status(self.t('deleted') + app_name)
    
    def move_up(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.t('warning'), self.t('select_app_move'))
            return
        
        item = self.tree.item(selected[0])
        index = int(item['values'][0]) - 1
        
        if index > 0:
            self.apps[index], self.apps[index - 1] = self.apps[index - 1], self.apps[index]
            self.save_config()
            self.refresh_list()
            new_item = self.tree.get_children()[index - 1]
            self.tree.selection_set(new_item)
            self.tree.see(new_item)
    
    def move_down(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning(self.t('warning'), self.t('select_app_move'))
            return
        
        item = self.tree.item(selected[0])
        index = int(item['values'][0]) - 1
        
        if index < len(self.apps) - 1:
            self.apps[index], self.apps[index + 1] = self.apps[index + 1], self.apps[index]
            self.save_config()
            self.refresh_list()
            new_item = self.tree.get_children()[index + 1]
            self.tree.selection_set(new_item)
            self.tree.see(new_item)
    
    def save_settings(self):
        self.delay_between_apps = self.delay_var.get()
        self.check_interval = self.check_var.get()
        self.save_config()
        self.update_status(self.t('settings_saved_status'))
        messagebox.showinfo(self.t('info'), self.t('settings_saved'))
    
    def update_status(self, message):
        self.status_label.config(text=message)
    
    def is_process_running(self, exe_name):
        exe_name = os.path.basename(exe_name).lower()
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'].lower() == exe_name:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
    
    def start_autostart(self):
        if self.is_running:
            messagebox.showwarning(self.t('warning'), self.t('already_running'))
            return
        
        if not self.apps:
            messagebox.showwarning(self.t('warning'), self.t('no_apps'))
            return
        
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)

        thread = threading.Thread(target=self.run_autostart, daemon=True)
        thread.start()
    
    def run_autostart(self):
        self.update_status(self.t('starting'))
        
        for i, app in enumerate(self.apps):
            app_name = app['name']
            app_path = app['path']
            exe_name = os.path.basename(app_path)
            
            self.update_app_status(i, self.t('status_running'))
            self.update_status(self.t('running_app') + app_name)
            
            try:
                subprocess.Popen([app_path])
                max_wait = 30 
                wait_count = 0
                
                while wait_count < max_wait:
                    if self.is_process_running(exe_name):
                        self.update_app_status(i, self.t('status_done'))
                        self.update_status(app_name + self.t('app_running'))
                        break
                    time.sleep(self.check_interval)
                    wait_count += self.check_interval
                else:
                    self.update_app_status(i, self.t('status_started'))

                if i < len(self.apps) - 1:
                    self.update_status(self.t('waiting').format(self.delay_between_apps))
                    time.sleep(self.delay_between_apps)
                    
            except Exception as e:
                self.update_app_status(i, self.t('status_error'))
                self.update_status(self.t('error_running') + app_name + ": " + str(e))
        
        self.update_status(self.t('completed'))
        self.is_running = False

        if self.startup_mode:
            time.sleep(3)
            self.root.quit()
        else:
            self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
    
    def update_app_status(self, index, status):
        def update():
            items = self.tree.get_children()
            if index < len(items):
                item = items[index]
                values = list(self.tree.item(item)['values'])
                values[3] = status
                self.tree.item(item, values=values)
        
        self.root.after(0, update)
    
    def register_to_startup(self):
        try:
            if getattr(sys, 'frozen', False):
                app_path = sys.executable
            else:
                app_path = f'"{sys.executable}" "{os.path.abspath(__file__)}"'

            startup_command = f'{app_path} --startup'
            key = reg.HKEY_CURRENT_USER
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            reg_key = reg.OpenKey(key, key_path, 0, reg.KEY_WRITE)
            reg.SetValueEx(reg_key, "StartScheduler", 0, reg.REG_SZ, startup_command)
            reg.CloseKey(reg_key)
            messagebox.showinfo(self.t('success'), self.t('register_success'))
            self.update_status(self.t('registered'))
            
        except Exception as e:
            messagebox.showerror(self.t('error'), self.t('register_failed') + str(e))
    
    def unregister_from_startup(self):
        try:
            key = reg.HKEY_CURRENT_USER
            key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
            
            reg_key = reg.OpenKey(key, key_path, 0, reg.KEY_WRITE)
            reg.DeleteValue(reg_key, "StartScheduler")
            reg.CloseKey(reg_key)
            
            messagebox.showinfo(self.t('success'), self.t('unregister_success'))
            self.update_status(self.t('unregistered'))
            
        except FileNotFoundError:
            messagebox.showinfo(self.t('info'), self.t('not_registered'))
        except Exception as e:
            messagebox.showerror(self.t('error'), self.t('unregister_failed') + str(e))

def main():
    root = tk.Tk()
    app = AutoStartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

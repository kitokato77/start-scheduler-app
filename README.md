# Start Scheduler

**English** | [Bahasa Indonesia](README-ID.md)

A Python application to manage and automatically run applications at Windows startup with a queue system.

## Features

- 🚀 **Autostart with Queue System**: Run applications sequentially, waiting for each app to start before launching the next
- 🎨 **User-Friendly GUI**: Easy-to-use graphical interface built with tkinter
- ⚙️ **Flexible Configuration**: Configure delay between apps and check intervals
- 📝 **Application Management**: Add, remove, and reorder applications easily
- 🔄 **Drag & Drop Order**: Move applications up or down to set priority
- 💾 **Auto-Save**: Configuration automatically saved to JSON file
- 🪟 **Windows Startup Integration**: Register to Windows startup with one click
- ✅ **Status Monitoring**: Monitor status of each application (Waiting, Running, Error)
- 🌐 **Multi-Language**: Supports English and Indonesian (automatic detection)

## How It Works

1. Application reads the list of executables from `config.json`
2. At startup, the application launches the first program in the queue
3. Waits until the program is actually running (process detected)
4. After the specified delay, launches the next application
5. Process continues until all applications in the list have been launched
6. The manager application automatically closes after completion (if run from startup)

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Application

```bash
python autostart_manager.py
```

## Usage Guide

### Adding Applications

1. Click the **"➕ Add Application"** button
2. Select the executable file (.exe) to run at startup
3. The application will be added to the list

### Reordering Applications

1. Select an application in the list
2. Click **"⬆️ Up"** to move up (higher priority)
3. Click **"⬇️ Down"** to move down

**Note**: The topmost application will be launched first

### Removing Applications

1. Select the application you want to remove
2. Click the **"🗑️ Delete"** button

### Settings

- **Delay between apps**: Wait time (seconds) after an app starts before launching the next one
- **App check interval**: How often (seconds) to check if an application is running
- **Language**: Choose interface language (English or Bahasa Indonesia)
- Click **"💾 Save Settings"** after changing values

### Testing AutoStart

Click **"▶️ Start AutoStart"** to test running all applications in the list without having to restart your computer.

### Register to Windows Startup

1. Click **"⚙️ Register to Windows Startup"**
2. The application will automatically run every time Windows starts
3. To remove from startup, click **"❌ Remove from Windows Startup"**

## File Structure

```
autostart-app/
├── autostart_manager.py   # Main application file
├── config.json             # Application list configuration
├── requirements.txt        # Python dependencies
├── README.md              # Documentation (English)
└── README-ID.md           # Documentation (Bahasa Indonesia)
```

## config.json Format

```json
{
  "apps": [
    {
      "name": "Application1",
      "path": "C:\\Path\\To\\App1.exe",
      "status": "Waiting"
    },
    {
      "name": "Application2",
      "path": "C:\\Path\\To\\App2.exe",
      "status": "Waiting"
    }
  ],
  "delay_between_apps": 3,
  "check_interval": 2,
  "language": "en"
}
```

## Compile to EXE

To convert the Python application into a standalone EXE file:

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Compile

```bash
pyinstaller --onefile --windowed --icon=app.ico --name="StartScheduler" autostart_manager.py
```

**Parameters:**
- `--onefile`: Creates a single EXE file
- `--windowed`: No console window (GUI only)
- `--icon`: Add icon (optional)
- `--name`: EXE file name

### 3. Result

The EXE file will be available in the `dist/StartScheduler.exe` folder

**Note**: Make sure the `config.json` file is in the same folder as the EXE

## Troubleshooting

### Application not detected as running

- Increase the **"App check interval"** value
- Some applications take longer to start

### Application doesn't run automatically

- Make sure you clicked **"Register to Windows Startup"**
- Check Task Manager → Startup to verify
- Run the application as Administrator if needed

### "Access Denied" Error

- Run the application as Administrator
- Some applications require elevated privileges

### Language not matching

- The application will automatically detect Windows language
- You can change it manually in the Settings section
- Language preference will be saved for next sessions

## Requirements

- Windows 10/11
- Python 3.7+
- tkinter (usually included with Python)
- psutil

## Tips

1. **Order Matters**: Place applications that must run first at the top
2. **Adequate Delay**: Provide sufficient delay between apps (3-5 seconds recommended)
3. **Test First**: Use the "Start AutoStart" button to test before registering to startup
4. **Absolute Path**: Ensure the path to executable is correct and uses full path
5. **Choose Language**: Use the language dropdown in settings to change interface language

## License

Free to use and modify.

## Author

Created with ❤️ for better Windows startup management

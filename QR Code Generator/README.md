# QR Code Generator

A simple Python script that generates a QR code from a URL (or any text) and saves it as a PNG image.

## What It Does

This script uses the `qrcode` library to encode a string (by default, `https://www.google.com`) into a QR code image. The generated QR code is saved as `google_qr.png` in the project folder.

Key settings used:
- **Version**: 1 (controls the size/data capacity of the QR code, range 1–40)
- **Error correction**: Low (`ERROR_CORRECT_L`) — recovers if up to ~7% of the code is damaged/obscured
- **Box size**: 10 pixels per box
- **Border**: 4 boxes wide
- **Colors**: Black foreground, white background

## Requirements

- Python 3.10+ (project tested on Python 3.14)
- [`qrcode`](https://pypi.org/project/qrcode/) library with the `pil` extra (for image generation)

## Setup

It's recommended to use a virtual environment to keep this project's dependencies isolated from your system Python.

### 1. Create a virtual environment

From the project folder, run:

```bash
py -3.14 -m venv venv
```

> Replace `-3.14` with whichever Python version you have installed. Run `py -0` to list available versions.

### 2. Activate the virtual environment

**Windows (PowerShell):**
```powershell
venv\Scripts\activate
```

> If you get an error about script execution being disabled, run this once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**macOS / Linux:**
```bash
source venv/bin/activate
```

Once activated, your terminal prompt should show `(venv)` at the start of the line.

### 3. Install dependencies

```bash
pip install qrcode[pil]
```

## Usage

With the virtual environment activated, run:

```bash
python main.py
```

This will generate a file called `google_qr.png` in the project folder containing the QR code.

### Customizing the QR code

Open `main.py` and edit the `data` variable to encode a different URL or text:

```python
data = "https://your-link-here.com"
```

You can also adjust the appearance by changing the parameters in `qrcode.QRCode(...)`:

| Parameter | Description |
|---|---|
| `version` | QR code size/capacity (1–40, higher = more data) |
| `error_correction` | Error correction level (`ERROR_CORRECT_L`, `_M`, `_Q`, `_H`) |
| `box_size` | Size of each box in pixels |
| `border` | Border thickness in boxes |

And the fill/background colors in `qr.make_image(...)`:

```python
img = qr.make_image(fill_color="black", back_color="white")
```

## Deactivating the Virtual Environment

When you're done working, run:

```bash
deactivate
```

## Project Structure

```
QR Code Generator/
├── main.py          # Main script
├── README.md         # This file
├── venv/              # Virtual environment (not tracked in version control)
└── google_qr.png     # Generated QR code (created after running the script)
```
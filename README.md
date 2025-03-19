pip install fastapi uvicorn sqlalchemy psycopg2 bcrypt python-dotenv jwt redis celery stripe twilio psutil PyQt6 PyQt6-sip PyQt6-tools PyScript kivy flask requests pillow


### **🚀 Fix: "ModuleNotFoundError: No module named 'PyQt6'"**
Your error means that **PyQt6 is not installed** in the Python environment that **VS Code is using**.

---

## **🔹 Step 1: Check Python Interpreter**
Your script is running using:
```bash
C:/Users/USERAS/AppData/Local/Programs/Python/Python313/python.exe
```
But PyQt6 is likely installed in **another environment**.

### **Check if PyQt6 is installed in this Python version**
Run:
```bash
C:/Users/USERAS/AppData/Local/Programs/Python/Python313/python.exe -m pip show PyQt6
```
✅ **If you see output like this, PyQt6 is installed:**
```
Name: PyQt6
Version: 6.x.x
Location: C:/Users/USERAS/AppData/Local/Programs/Python/Python313/lib/site-packages
```

❌ **If you see nothing, it means PyQt6 is missing. Proceed to Step 2.**

---

## **🔹 Step 2: Install PyQt6 in the Correct Python Environment**
Run:
```bash
C:/Users/USERAS/AppData/Local/Programs/Python/Python313/python.exe -m pip install PyQt6
```
or if you're using **Anaconda**, install with:
```bash
conda install pyqt
```

✅ **Now, PyQt6 should be installed properly.**

---

## **🔹 Step 3: Run the Script Again**
Try running the script again:
```bash
C:/Users/USERAS/AppData/Local/Programs/Python/Python313/python.exe admin.py
```
or simply:
```bash
python admin.py
```

✅ **Now it should work without issues!** 🚀

---

## **🔹 Step 4: Ensure VS Code Uses the Correct Python Interpreter**
1. **Open VS Code Command Palette** (`Ctrl + Shift + P`)
2. Search: **"Python: Select Interpreter"**
3. Select:
   ```
   C:/Users/USERAS/AppData/Local/Programs/Python/Python313/python.exe
   ```
4. Restart VS Code and run:
```bash
python admin.py
```

✅ **Now, everything should work perfectly!** 🎯  

---

🔥 **Let me know if you need more help! 🚀**

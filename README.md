# *Crackathon* 🔥  
**A powerful file comparison tool for analyzing text differences with difficulty-based scoring.**

## **🚀 Features:**  
✅ Compare two text files and identify differences  
✅ Assign scores based on difficulty levels  
✅ Supports four difficulty levels: Easy, Medium, Hard, Insane  
✅ Simple command-line usage  

---

## **📥 Installation**  
### **Option 1: Clone via Git (Recommended)**  
```bash
git clone https://github.com/Overdog10/crackathon.git
cd crackathon
chmod +x crackathon
```

### **Option 2: Download ZIP**  
1. Go to: [GitHub Repository](https://github.com/Overdog10/crackathon)  
2. Click the **"Code"** button and select **"Download ZIP"**  
3. Extract the ZIP file  
4. Open a terminal in the extracted folder and run:  
   ```bash
   chmod +x crackathon
   ```

---

## **🛠 Usage**  
Crackathon compares two text files and assigns scores based on difficulty level:  

| Difficulty | Flag | Score per Match |
|------------|------|---------------|
| Easy       | `-e` | 0.5           |
| Medium     | `-m` | 1.0           |
| Hard       | `-h` | 1.5           |
| Insane     | `-i` | 2.0           |

### **Example Usage:**  
```bash
./crackathon -m medium1.txt hashes1_medium_with_password
```
This compares `easy.txt` and `easy_solutions.txt`, giving **0.5 points** per matching line.

---

## **🔧 Contributing**  
Want to improve **Crackathon**? Feel free to fork the repo and submit a pull request!  

---

## **📝 License**  
This project is **open-source** 


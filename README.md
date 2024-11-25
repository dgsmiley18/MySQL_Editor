
# **MySQL Editor**

A basic CRUD (Create, Read, Update, Delete) application built with Python. This project was created to test my skills with database and for my college

## **Features**
- Create new records.
- Read and display existing records.
- Update existing records.
- Delete records.
- Simple and intuitive terminal-based interface.

## **Technologies Used**
- **Programming Language**: Python (Version 3.8+ recommended)
- **Database**: MySQL
- **Libraries**:
  - `mysql.connector` for database management.

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher installed on your system.
- Basic understanding of how to run Python scripts.

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/dgsmiley18/MySQL_Editor.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MySQL_Editor
   ```
3. Install any required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```
   *(For this simple project, dependencies may not be required.)*

### **Running the Application**
Run the script directly from your terminal:
```bash
python main.py
```

### **Usage**
1. The program starts with a menu that lets you choose an action:
   - Add a new record.
   - View all records.
   - Update an existing record.
   - Delete a record.
   - Exit the application.
2. Follow the prompts to perform each operation.

### **Database**
The data is stored in a local MySQL database file (`template\backup.db`)

## **Future Improvements**
- Add a graphical user interface (GUI) using a library like Tkinter or PyQt.
- Implement user authentication for secure access.
- Add pagination for large datasets.
- Improve error handling and input validation.

## **Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and create a pull request.

## **License**
This project is licensed under the GPL3 License. See the [LICENSE](LICENSE) file for details.

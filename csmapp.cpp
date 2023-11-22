/*
copyright 2023
author: Sowrav Roy Joy
This program helps a developer to save code snippets that he use frequently with add, update, delete options.
*/


#include "include/csm.h"

//Global variables
sqlite3 *db;
sqlite3_stmt *stmt;
int result;
void connection();

void printMenu() {
    cout << "Welcome to My Code Snippet Manager " <<endl;
    cout << "Please enter your selection: "<< endl;
    cout << "\t1. Add New Code Snippet "<< endl;
    cout << "\t2. Delete An Existing One "<< endl;
    cout << "\t3. Update An Existing One "<< endl;
    cout << "\t4. Show Saved Code Snippets "<< endl;
    cout << "\t5. Exit "<< endl;
}  // prints menu when program starts



int main() {
    //call connection function
    connection();

    sqlite3_close(db);
    return(0);
}

void connection(){
    if(sqlite3_open("snippets.db", &db) == SQLITE_OK){
        result = sqlite3_prepare16_v2(db, "CREATE TABLE IF NOT EXISTS user(name varchar(50), roll INT, email varchar(80));", -1, &stmt, NULL);
        sqlite3_step(stmt);
        sqlite3_finalize(stmt);

        if(result != SQLITE_OK){
            cout << "Error: " << sqlite3_errmsg(db)<<endl;

        }else{

            cout << "Table created successfully"<<endl;
        }
    }


}